---
name: academic-writing
description: Review, polish, paraphrase, or suggest edits to academic prose using writing patterns extracted from a corpus of well-regarded papers. Use when polishing or tightening a draft, rewriting a passage, reviewing a paper or section, fixing wordiness, hedging, connectives, cohesion or sentence rhythm, checking whether a gap statement or contribution list lands, or judging citation and evidence-reporting choices.
---

# Academic writing

Built from 119 peer-reviewed papers (Yan Gu, Yihan Sun, Helen Xu; SPAA, PPoPP, SIGMOD, VLDB,
ESA, ALENEX; 2011-2026), read for craft rather than content, plus mechanical measurements over
all 52,006 of their sentences and 1.1M words.

Everything here describes what well-written papers **do**, not what style guides recommend.
When the two disagree, the corpus wins — but see `references/gaps.md` for where it has nothing
to say.

## Language polishing — start here

This is the deepest part of the skill: **72 patterns** across ten sub-topics, each adversarially
verified against corpus-wide counts (11 kept as written, 61 narrowed or corrected, 2 rejected).

**`references/polishing/PLAYBOOK.md`** is the main entry point. It orders every pattern into six
sequential passes, each asking one question of every sentence, each with a **do not touch** list
so a later pass cannot re-break what an earlier one settled:

| Pass | Question |
|---|---|
| 1. First position | What occupies the first position of this paragraph and this sentence — did it earn that slot? |
| 2. Names | Does every concept travel under exactly one name, introduced after the thing it names? |
| 3. Reference | Can every pronoun and demonstrative be resolved without looking back more than one sentence? |
| 4. Shape | Does the main verb arrive early, and is everything after it hung on the right hinge? |
| 5. Action and weight | Where is the action, what performs it, and does every remaining word earn its place? |
| 6. Stance | Whose evidence is it, where does it stop, and is the uncertainty outside the claim? |

Work them **in order**. Fixing word choice before sentence shape means rewriting the same words
twice. Pattern detail per pass is in `references/polishing/pass-1.md` … `pass-6.md`.

The playbook also carries a **quick checklist** (15 checks, one read of a paragraph) and a
**cut list** (16 constructions the corpus effectively bans, each with its replacement and the
measured evidence).

### Run the linter first

    python3 scripts/polish_lint.py draft.tex

It flags only what is countable — banned constructions, uncashed magnitude words, stance
imbalance, late main verbs, monotonous openings, bare demonstratives — and cites the corpus rate
for each. Calibration: **0.6-1.5 findings per 1,000 words is the corpus's own range**; a draft
dense with these problems scores around 80. Use it as a pre-pass, never a verdict: it cannot
tell whether an argument lands, and every finding needs confirming in context.

It expects a clean `.tex`/`.md` draft. Text pasted out of a PDF is spliced by column extraction
and will produce false findings from fragments no author wrote.

## The three jobs

### Polish or paraphrase

Preserve the claim and its epistemic strength exactly; change only the delivery.

- Keep hedges that mark genuinely unverified content. Removing a hedge from an extrapolation is
  a factual error, not a style improvement.
- Keep every technical term invariant. This corpus refuses elegant variation; a synonym
  introduced for rhythm reads as a second concept.
- Do not add emphasis the evidence does not carry. Hedges run 8.1 per 1,000 words against 2.6
  for boosters.
- Match sentence-length **variance**, not average. Uniform 21-word sentences are further from
  this corpus than a mix of 8-word verdicts and 36-word qualified claims.

### Review a draft

Work from violation signatures, not impressions. Every pattern carries one: the shape the prose
takes when the pattern is missing. Structural findings outrank sentence-level ones, so start at
`references/patterns/` (dimensions A and B) before the polishing passes.

Check `references/conflicts.md` before calling anything a defect — on ten contested choices the
corpus does both, and a condition rather than a preference decides which is right.

### Suggest edits

Order by leverage: thesis and gap statements, then section openings, then the six polishing
passes. Attach each suggestion to a named pattern so the author can accept or reject it on the
reasoning rather than on taste.

## Reading the evidence

Two denominators appear in this skill and they mean different things:

- **"n/119"** — measured across the whole corpus. Trustworthy as a rate.
- **"seen in N papers"** — observed in the 8-12 papers that sub-topic sampled. A local
  observation, not a corpus law.

Never justify a finding with a count without checking which kind it is. Where a sampled claim
was later tested corpus-wide, `references/polish-validation.md` records the result — including
three cases where measurement **narrowed or overturned** what the sampled reading suggested.

## References

| File | Use it for |
|---|---|
| `references/polishing/PLAYBOOK.md` | **The six revision passes, checklist, and cut list.** Start here for polishing. |
| `references/polishing/pass-N.md` | Full pattern detail for one pass. |
| `scripts/polish_lint.py` | Mechanical pre-pass over a draft. |
| `references/patterns/INDEX.md` | 59 structural patterns (macro-architecture through reader management). |
| `references/corpus-baselines.md` | Measured sentence, stance, citation, and signposting rates. |
| `references/conflicts.md` | Ten choices the corpus makes both ways, and the governing condition. |
| `references/polish-validation.md` | Where corpus-wide measurement narrowed or overturned a sampled claim. |
| `references/gaps.md` | What this skill does not cover. |
| `references/rubric.md` | The eight dimensions, for extending the library. |
| `references/pattern-format.md` | Entry format and the rules that keep the library honest. |

## Limits worth stating up front

One subfield, three research groups, one citation style. Three consequences bite often:

- **Citation patterns assume numeric brackets**, about 22:1 over integral citation. The
  bracket-placement pattern does not transfer to author-date fields at all.
- **Limitations and discussion are thin.** "Limitation" appears in 20 of 118 papers, "beyond the
  scope" in 3. CS conference papers mostly have no discussion section, so this corpus is not a
  model for writing one.
- **Uncertainty reporting is absent.** The corpus reports spread across instances but almost
  nothing on run-to-run variance, error bars, or significance.

Section structure could not be measured mechanically — raw PDF extraction does not isolate
headings — so no claim about section ordering or naming rests on counts.
