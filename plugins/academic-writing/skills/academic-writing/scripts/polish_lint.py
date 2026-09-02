#!/usr/bin/env python3
"""Mechanical first pass over a draft, calibrated against a 119-paper corpus.

Flags only what is countable. It cannot judge whether an argument lands or whether a
hedge is honest, so it is a pre-pass for the human/model review, never a substitute:
everything it reports still needs a reader to confirm it matters in context.

Usage:
    python3 polish_lint.py draft.tex [--verbose]

Reads .tex, .md, or .txt. LaTeX commands, math, and comments are stripped before analysis.
Each finding cites the corpus rate it is measured against.

Expects a CLEAN draft. Text pasted out of a PDF is spliced by column extraction and will
produce false LONG/VERB-LATE findings from fragments no author wrote.

Calibration — findings per 1,000 words:
    0.6 - 1.5   corpus papers (the target range; some findings are expected and fine)
    ~80         a draft dense with banned constructions and uncashed magnitude words
A raw count means little without the denominator; judge the rate, and read every finding in
context before acting on it.
"""
import re, sys, os, statistics as st
from collections import Counter

# ---- corpus reference values (measured over 119 papers, 1.1M words) --------
REF = {
    'sent_median': 19, 'sent_mean': 21.1, 'sent_p90': 36,
    'short_frac': 0.23, 'long_frac': 0.12,
    'verb_pos_median': 5, 'verb_pos_p90': 15,
    'bare_subject_open': 0.464, 'connective_open': 0.064,
    'hedge_per_1k': 8.1, 'boost_per_1k': 2.6, 'we_per_1k': 15.3,
    'para_median_sents': 4,
}
# constructions effectively absent from the corpus: (regex, per-1M-word count, replacement)
BANNED = [
    (r'\bthere (?:is|are|exists?)\s+\w+\s+that\b', 1, 'make the noun the subject: "X does Y"'),
    (r'\breally\b', 1, 'delete, or name the magnitude'),
    (r'\ba lot of\b', 8, '"many", or a number'),
    (r'\bdue to the fact that\b', 11, '"because"'),
    (r'\bin spite of the fact that\b', 0, '"although"'),
    (r'\bit is (?:important|interesting|worth|necessary|possible) to (?:note|see|observe|mention)\b', 49,
     'state the point directly, or use "Note that"'),
    (r'\bobviously\b|\bof course\b', 64, 'delete; if it needs saying it is not obvious'),
    (r'\bin spite of the fact\b', 0, '"although"'),
]
# Present in the corpus but sparingly: flag only when the draft's RATE exceeds the corpus rate.
# Flagging these on presence would fault prose that matches the corpus exactly.
RATE_GATED = [
    (r'\bvery\b', 0.318, 'usually delete, or use a stronger adjective'),
    (r'\bquite\b', 0.049, 'delete'),
    (r'\bextremely\b', 0.029, 'give the number'),
    (r'\bhighly\b', 0.237, 'give the number, or delete'),
    (r'\bin order to\b', 0.078, '"to"'),
    (r'\bmake use of\b', 0.036, '"use"'),
    (r'\bis able to\b|\bare able to\b', 0.040, '"can"'),
    (r'\bperform(?:s|ed)? (?:an?|the) \w+', 0.218, 'use the verb the noun came from'),
    (r'\bprovide(?:s|d)? (?:an?|the) \w+', 0.266, 'use the verb the noun came from'),
    (r'\bconduct(?:s|ed)? (?:an?|the) \w+', 0.015, 'use the verb the noun came from'),
    (r'\bwith respect to\b', 0.113, '"for" or "on"'),
    (r'\bin terms of\b', 0.164, 'name the dimension directly'),
]
CONN_FRONTS = {'however','therefore','furthermore','moreover','in contrast','as a result','for example',
               'in particular','specifically','in addition','finally','hence','nevertheless','consequently'}
CONN_EMBEDS = {'also','first','second','then','next','while','instead','overall','that is','such as'}
HEDGE = r'\b(may|might|could|appears?|seems?|suggests?|likely|possibly|perhaps|typically|generally|often|usually|tends? to|relatively|somewhat|largely|mostly|we believe|arguably)\b'
BOOST = r'\b(clearly|obviously|significantly|substantially|dramatically|considerably|remarkably|notably|strongly|greatly|vastly|hugely)\b'
MAGNITUDE = (r'\b(significantly|substantially|dramatically|considerably|greatly|vastly|markedly)\b'
             r'|(?<!so )(?<!as )\bfar (?=more|less|better|worse|faster|slower|above|below|beyond)'
             r'|\bmuch (?=more|less|better|worse|faster|slower|larger|smaller)')

def strip_markup(t, ext):
    if ext == '.tex':
        t = re.sub(r'(?<!\\)%.*', '', t)
        t = re.sub(r'\\begin\{(figure|table|equation|align|lstlisting|verbatim|algorithm|tabular|displaymath|proof)\*?\}.*?\\end\{\1\*?\}', ' ', t, flags=re.S)
        t = re.sub(r'\$\$.*?\$\$', ' MATH ', t, flags=re.S)
        t = re.sub(r'\$[^$]*\$', ' MATH ', t)
        t = re.sub(r'\\(cite|ref|eqref|label|autoref|cref)\w*\{[^}]*\}', ' CITE ', t)
        t = re.sub(r'\\(section|subsection|subsubsection|paragraph)\*?\{([^}]*)\}', r'\n\n\2.\n\n', t)
        t = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?', ' ', t)
        t = t.replace('{',' ').replace('}',' ').replace('~',' ').replace('\\',' ')
    elif ext == '.md':
        t = re.sub(r'```.*?```', ' ', t, flags=re.S)
        t = re.sub(r'`[^`]*`', ' ', t)
        t = re.sub(r'^\s{0,3}#+\s*', '', t, flags=re.M)
        t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    return t

ABBR = (r'(?<!\be\.g)(?<!\bi\.e)(?<!\bcf)(?<!\bvs)(?<!\bal)(?<!\bFig)(?<!\bEq)(?<!\bSec)'
        r'(?<!\bTab)(?<!\bApp)(?<!\bResp)(?<!\bapprox)(?<!\betc)(?<!\bNo)(?<!\bvol)(?<!\bpp)')
SPLIT = re.compile(ABBR + r'(?<![A-Z])[.!?]["\')\]]?\s+(?=[A-Z(])')
VERB = re.compile(r'\b(is|are|was|were|has|have|had|can|will|would|may|might|does|do|did|shows?|gives?|'
                  r'takes?|uses?|requires?|provides?|yields?|achieves?|reduces?|improves?|allows?|presents?|'
                  r'proposes?|proves?|runs?|costs?|makes?|becomes?|remains?|holds?|follows?)\b')

def main(path, verbose=False):
    ext = os.path.splitext(path)[1].lower()
    raw = open(path, encoding='utf-8', errors='ignore').read()
    text = strip_markup(raw, ext)
    paras = [re.sub(r'\s+',' ',p).strip() for p in re.split(r'\n\s*\n', text)]
    paras = [p for p in paras if len(p.split()) >= 15]
    def is_prose(x):
        if len(x.split()) < 4: return False
        letters = sum(c.isalpha() or c.isspace() for c in x)
        if letters < len(x) * 0.75: return False          # notation / table row
        if sum(c in '=+∑∈≤≥→←⌈⌉⌊⌋∪∩⊆·×√≠≈|' for c in x) > 2: return False
        if re.match(r'^\s*(Table|Figure|Algorithm|Lemma|Theorem|Proof|Definition|Corollary)\b', x): return False
        return True
    sents = [s.strip() for p in paras for s in SPLIT.split(p) if is_prose(s.strip())]
    if not sents:
        print('No prose found. If this is LaTeX, check that the body is not all inside environments.')
        return 1
    words = len(re.findall(r"[A-Za-z][A-Za-z'-]*", ' '.join(paras)))
    low = ' '.join(paras).lower()
    print(f"{os.path.basename(path)}: {len(paras)} paragraphs, {len(sents)} sentences, {words} words\n")
    findings = []

    # 1. banned constructions
    for rx, corpus_n, fix in BANNED:
        hits = [m.group(0) for m in re.finditer(rx, low)]
        if hits:
            rate = 1_000_000 * corpus_n / 1_102_126
            findings.append(('CUT', f'"{hits[0]}" x{len(hits)}',
                             f'corpus uses this {corpus_n}x in 1.1M words ({rate:.1f}/M). Replace with: {fix}'))
    for rx, corpus_rate, fix in RATE_GATED:
        n = len(re.findall(rx, low))
        if not n: continue
        rate = 1000 * n / max(1, words)
        if rate > max(corpus_rate * 2.5, corpus_rate + 0.35):
            findings.append(('OVERUSED', f'"{re.findall(rx, low)[0]}" x{n} ({rate:.2f}/1k words)',
                             f'corpus rate is {corpus_rate}/1k. Replace with: {fix}'))

    # 2. sentence length
    sl = [len(s.split()) for s in sents]
    med = st.median(sl)
    longs = [s for s in sents if len(s.split()) >= 50]
    if med > 26:
        findings.append(('RHYTHM', f'median sentence {med:.0f} words',
                         f'corpus median is {REF["sent_median"]}. Long-sentence habit; split the qualified ones.'))
    shortf = sum(1 for x in sl if x <= 12)/len(sl)
    if shortf < 0.10:
        findings.append(('RHYTHM', f'only {100*shortf:.0f}% of sentences are <=12 words',
                         f'corpus runs {100*REF["short_frac"]:.0f}%. Uniform length reads as monotone; land verdicts in short sentences.'))
    for s in longs[:5]:
        findings.append(('LONG', f'{len(s.split())} words', s[:120] + '...'))
    # 3. subject-verb distance
    far = []
    for s in sents:
        m = VERB.search(s)
        if m:
            d = len(s[:m.start()].split())
            if d >= 12: far.append((d, s))
    if far:
        far.sort(reverse=True)
        findings.append(('VERB-LATE', f'{len(far)} sentences delay the main verb past 12 words',
                         f'corpus median is {REF["verb_pos_median"]}. Worst: "{far[0][1][:100]}..."'))
    # 4. sentence openings
    opens = Counter()
    for s in sents:
        w1 = re.match(r'^\s*([A-Za-z]+)', s)
        opens[w1.group(1).lower() if w1 else '?'] += 1
    # The corpus itself opens 13.8% of sentences with a prepositional frame, so a common
    # frame-starter at 12% is normal. Only a genuinely dominant single opener is a finding.
    for w, c in opens.most_common(4):
        share = c / len(sents)
        if c >= 5 and share >= 0.18:
            findings.append(('OPENING', f'{c} sentences ({100*share:.0f}%) open with "{w}"',
                             'corpus spreads openings: 46% bare-subject, 14% prepositional frame, '
                             '6.4% connective. One word dominating the entry point flattens rhythm.'))
    # 5. connective placement
    for c in CONN_EMBEDS:
        n = len(re.findall(r'(?:^|\.\s+)' + re.escape(c).capitalize() + r'\s*,', ' '.join(sents)))
        if n:
            findings.append(('CONNECTIVE', f'"{c.capitalize()}," opens a sentence {n}x',
                             f'corpus fronts "{c}" in under 25% of its uses; embed it after the subject instead.'))
    # 6. bare demonstratives
    bare = len(re.findall(r'(?:^|[.;]\s+)(This|These|That|Those)\s+(?:is|are|was|were|means|implies|allows|gives|shows|can|will|would|may|has|have)\b', ' '.join(sents)))
    withn = len(re.findall(r'\b(?:This|These|That|Those)\s+[a-z]+\b', ' '.join(sents)))
    if bare and bare > withn * 0.6:
        findings.append(('COHESION', f'{bare} bare "This/These" subjects vs {withn} carrying a noun',
                         'corpus attaches a noun about two-thirds of the time; name what "this" refers to.'))
    # 7. stance calibration
    h = len(re.findall(HEDGE, low)); b = len(re.findall(BOOST, low))
    hr, br = 1000*h/max(1,words), 1000*b/max(1,words)
    if br > REF['boost_per_1k'] * 2:
        findings.append(('STANCE', f'boosters {br:.1f}/1k words',
                         f'corpus runs {REF["boost_per_1k"]}. Emphasis is bought with evidence, not adverbs.'))
    if h and b and hr < br:
        findings.append(('STANCE', f'boosters ({br:.1f}) outnumber hedges ({hr:.1f}) per 1k',
                         'corpus runs hedges 3:1 over boosters. Check that strength tracks evidence.'))
    # 8. uncashed magnitude words
    for m in re.finditer(MAGNITUDE, low):
        seg = low[m.start():m.start()+220]
        if not re.search(r'\d', seg):
            findings.append(('UNCASHED', f'"{m.group(0)}" with no number nearby',
                             '...' + low[max(0,m.start()-45):m.start()+90].strip() + '...'))
    # 9. paragraph length
    pl = [len(SPLIT.split(p)) for p in paras]
    if pl and st.median(pl) > 9:
        findings.append(('PARAGRAPH', f'median paragraph {st.median(pl):.0f} sentences',
                         f'corpus median is {REF["para_median_sents"]}; long paragraphs usually hold two claims.'))

    order = {'CUT':0,'UNCASHED':1,'STANCE':2,'COHESION':3,'CONNECTIVE':4,'VERB-LATE':5,
             'OPENING':6,'RHYTHM':7,'PARAGRAPH':8,'LONG':9}
    findings.sort(key=lambda f: order.get(f[0], 99))
    if not findings:
        print("No mechanical findings. This checks only countable things — the argument still needs a reader.")
        return 0
    shown = Counter()
    for kind, what, why in findings:
        shown[kind] += 1
        if not verbose and shown[kind] > 4:
            continue
        print(f"[{kind}] {what}\n    {why}\n")
    extra = {k: v-4 for k, v in shown.items() if v > 4}
    if extra and not verbose:
        print("(" + ", ".join(f"{v} more {k}" for k, v in extra.items()) + " — rerun with --verbose)")
    print(f"\n{len(findings)} findings. These are countable signals only; confirm each in context "
          f"before acting, and see references/patterns/ for the reasoning behind them.")
    return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1], '--verbose' in sys.argv))
