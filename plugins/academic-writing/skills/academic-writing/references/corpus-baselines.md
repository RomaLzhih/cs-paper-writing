# Corpus baselines

Measured over 119 papers (118 analysable, 52,006 sentences, 10,893 paragraphs) from Yan Gu,
Yihan Sun, and Helen Xu — SPAA, PPoPP, SIGMOD, VLDB, ESA, ALENEX and others, 2011-2026.
These are descriptive facts about a corpus of well-regarded papers, not targets to hit. Use
them to tell a reviewer whether a draft sits inside or outside the range good papers occupy,
and always prefer the reason a number matters over the number itself.

## Sentence and paragraph shape

| Measure | Corpus value |
|---|---|
| Sentence length, median | 19 words |
| Sentence length, mean | 21.1 words (sd 12.1) |
| Sentence length, p10 / p25 / p75 / p90 | 8 / 13 / 27 / 36 words |
| Share of sentences <= 12 words | 23% (median paper) |
| Share of sentences >= 35 words | 12% (median paper) |
| Paragraph length, median | 4 sentences |
| Paragraph length, p75 / p90 | 6 / 10 sentences |

The spread matters more than the average. A draft whose sentences cluster tightly around 21
words is *less* like this corpus than one that mixes 8-word verdicts with 36-word qualified
claims. Uniformity is the deviation.

## Stance and voice (per 1,000 words, median paper)

| Measure | Rate |
|---|---|
| "we" | 15.3 |
| passive-voice constructions | 10.0 |
| hedges | 8.1 |
| boosters | 2.6 |
| transitions | 13.1 |
| nominalisations | 29.2 |

Hedges outrun boosters roughly 3:1. The corpus buys emphasis with evidence, not with adverbs:
"clearly" appears in only 23/118 papers, "substantially" in 15/118, "obviously" essentially
never. Meanwhile "must", "always", "exactly" and "directly" are frequent — but read them
before counting them, because in algorithms prose they are usually technical precision
("the invariant must hold"), not rhetorical force.

## Citation

| Measure | Value |
|---|---|
| Bracket citations | 6.7 per 1,000 words |
| Integral citations ("Smith et al. [3] show") | 0.3 per 1,000 words |
| Ratio | about 22:1 in favour of bracketed |
| Citations sitting mid-sentence, attached to what they name | 68% of 6,881 citations |

Integral citation is reserved, not default. When these authors write a name into the sentence,
they are crediting an origin or attributing an opinion — not padding a list.

## Signposting

| Phrase | Papers using it |
|---|---|
| "in this paper" | 111/118 (94%) |
| "in section" | 76/118 (64%) |
| "note that" | 88/119 (74%) |
| "is organized as follows" | 15/118 (13%) |
| "the remainder of" | 11/118 (9%) |

This is the sharpest single finding in the measurements: the corpus signposts constantly and
almost never uses the boilerplate roadmap paragraph. Heavy signposting and the "organized as
follows" paragraph are opposites here, not companions.

## What is NOT measurable from this corpus

- **Section structure.** Raw PDF extraction does not isolate headings, and pseudocode
  fragments contaminate any regex (best recovery: 7/119 papers, with false positives such as
  "starts here"). No claim about section counts, ordering, or naming rests on measurement.
- **Anything about paragraph boundaries beyond a floor.** Paragraphs are recovered by a
  line-width heuristic, so counts of paragraph-initial constructions are lower bounds.
- **Limitations sections.** The lexicon is thin: "limitation" in 20/118 papers, "future work"
  in 46/118, "beyond the scope" in 3/118. Either this corpus concedes inside the technical
  prose rather than in a dedicated section, or it concedes little. Do not cite this corpus as
  a model for writing limitations until that is resolved by reading rather than counting.
