# Corpus-wide validation of polishing claims

Each sub-topic agent read 10 papers. Claims testable by measurement were re-tested against all
119. Where a measurement sharpened a pattern, the sharper version is what belongs in the skill.

## "the former / the latter"

Three agents independently produced a pattern telling the writer to avoid it. Measured:

| | Count | Share |
|---|---|---|
| Total uses in 1.1M words | 39 (26/119 papers) | 0.035/1k |
| **Bare** ("the latter requires…") | **7** | 18% |
| Attached to a noun ("the latter *case*") | 32 | 82% |

Nouns used: case (18), two (6), dominates (2), three (2), model, part, condition, measure.

**The agents' rule is too strong and the correction matters.** The corpus does not avoid
former/latter; it avoids the BARE form — 7 uses in 1.1M words. When these authors use it, they
attach a noun that re-identifies the referent. This is the same move as "This + classifying
noun", so it belongs with the demonstrative patterns rather than as a separate prohibition.

Rewritten rule: *Do not leave "the former/the latter" bare. Attach the noun that names what it
points at, or name the item outright.*

## "such + noun"

1,635 uses across 118/119 papers (1.48/1k). Confirms the cohesion pattern that uses
"such + noun" to move from instance to kind — this is a live, heavily used device, not a
stylistic flourish.

## "respectively"

368 uses in 97/119 papers (0.334/1k). Common enough to be a normal part of the register; a
draft using it is not deviating.

## Method note

Three agents converging on the same pattern is weak evidence, not strong: they share a prior
about what good writing looks like, and can converge on a plausible rule the corpus does not
follow. Convergence marks a claim as worth measuring, never as confirmed.

## Paragraph openings — strongest confirmation in this pass

Of 7,188 paragraphs with three or more sentences, only **127 (1.8%)** open with a fronted
connective (However, Therefore, Moreover, Furthermore, In addition, In contrast, Also,
Finally, …). This confirms "open the paragraph on the noun it is about" about as strongly as
the corpus can confirm anything, and it is the single most actionable polishing finding:
a draft whose paragraphs habitually open with "However," or "Moreover," is deviating from
98% of this corpus.

Note the contrast with sentence-level use: `however` is heavily used (1,022 times, 118/119
papers) and fronts 78% of the time — but almost never at a PARAGRAPH boundary. The connective
opens sentences inside a paragraph, not the paragraph itself.

## Sentence length by position in the paragraph — confirmed but weak

| Position | Median | Mean | p25 | p75 |
|---|---|---|---|---|
| First sentence | 17 | 19.0 | 10 | 25 |
| Middle sentences | 20 | 21.6 | 14 | 27 |
| Last sentence | 18 | 20.0 | 11 | 26 |

First and last sentences are shorter than middle ones, so "keep the opener short" and "end on
a short consequence" point the right way — but the effect is 2-3 words at the median, not the
sharp contrast the patterns imply. The heavier short tail (p25 of 10 for openers versus 14 for
middles) is where the real signal is: openers are more OFTEN short, rather than uniformly
shorter. State these two patterns as tendencies, and do not flag a 24-word opening sentence as
a defect on this evidence alone.

## Enumeration and naming — confirmed

| Device | Uses | Papers | Rate |
|---|---|---|---|
| Announced count + category noun ("three challenges") | ~2,636 | 118/119 | 2.39/1k |
| Abbreviation defined as "(ABC)" | 1,357 | 118/119 | 1.23/1k |
| Colon introducing a list or explanation | 1,130 | 115/119 | 1.03/1k |
| "we call" / "we refer to" / "referred to as" | 296 | 87/119 | 0.27/1k |
| **Em-dash pair as an aside** | **25** | **14/119** | 0.023/1k |

Caveat on the first row: the regex `NUM + plural noun` also matches "Figure 3 shows" and similar,
so 2,636 is inflated — "shows" (96) and "illustrates" (33) are in the counted-noun list and are
plainly not categories. The pattern is well supported by document frequency (118/119) and by the
genuine category nouns (cases 73, steps 67, types 46, techniques 34), but do not quote the raw
count as if it were clean.

The em-dash result is the sharp one: **25 paired em-dash asides in 1.1M words, in 14 of 119
papers.** Parentheses (24.9/1k) carry essentially all of this corpus's asides. A draft leaning on
em-dashes for parenthetical remarks is doing something these authors almost never do.

## Connective placement — independently re-measured

The connectives agent reported its own counts. Re-measured over cleaned prose (52,063 sentences):

| Word | Total | Initial | Medial | Final | After "and" | Post-auxiliary |
|---|---|---|---|---|---|---|
| however | 1,022 | 795 (78%) | 214 | 13 | 1 | 1 |
| therefore | 828 | 566 (68%) | 253 | 9 | 77 | 99 |
| thus | 679 | 320 (47%) | 358 | 1 | 250 | 20 |
| hence | 468 | 301 (64%) | 167 | 0 | 122 | 4 |
| in contrast | 130 | 105 (81%) | 25 | 0 | 0 | 0 |
| instead | 455 | 112 (25%) | 334 | 9 | 14 | 3 |
| moreover | 74 | 70 (95%) | 4 | 0 | 1 | 0 |
| furthermore | 226 | 206 (91%) | 20 | 0 | 4 | 0 |

The agent's **structural** claims hold. Of "thus"'s 358 medial uses, 250 (70%) ride on a
coordinating "and"; for "hence" it is 122 of 167 (73%). "Therefore" prefers the post-auxiliary
slot ("is therefore", 99) over "and therefore" (77) when embedded. So the three cause connectives
really are three weights, not synonyms.

Its raw totals were 15-20% higher than these (it reported thus 811, hence 540, therefore 1,003).
The gap is text filtering: these figures count cleaned body prose only, while a plain grep also
picks up captions, headers and reference lines. Neither is wrong, but the skill should quote the
prose-only figures, since that is what a writer is editing.

Additions worth keeping: **"instead" is a medial connective** (25% initial, 73% medial) and
patterns should not treat it as a sentence-opener; **"moreover" (95%) and "furthermore" (91%) are
almost exclusively sentence-initial.**
