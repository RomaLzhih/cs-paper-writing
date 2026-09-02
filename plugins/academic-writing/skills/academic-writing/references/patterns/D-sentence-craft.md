# D. Sentence craft

8 patterns, ordered by how much each would improve a weak draft.

---

## Reach the main verb inside the first six words, then extend the sentence rightward

**Move.** Subject and finite verb come up front, often after a two-to-four-word adverbial frame, and every qualification, mechanism, and list is appended to the right of the verb — most often through a trailing ", which" clause — rather than wedged between subject and verb.

**Why it works.** The reader banks the proposition before the qualifications arrive, so a 35-word sentence costs no more working memory than a 15-word one; comprehension degrades only when the subject is left hanging.

**Evidence.** 6 of the 12 papers read for dimension D, but the mechanical check is corpus-wide.

**Exemplars.**

- "In this paper, we present the ParGeo library for parallel computational geometry, which includes a rich set of parallel algorithms for geometric problems and data structures" — *ParGeo*, Introduction
- "Our main observation is that the PMA is well-suited to concurrent updates despite occasionally requiring a rewrite of the entire structure" — *xu-ppcsr-alenex-21*, Abstract
- "A batch deletion in CGAL removes the points one by one, which performs well for small batches, but is very inefficient for large batches." — *kdtree*, 6 Experiments

**Violation signature.** Sentences over ~25 words in which a comma-delimited relative clause, appositive, or participial phrase sits between the subject noun and its verb ("The method, which we developed after…, produces…"). Corpus-wide this is essentially absent: of 21,722 sentences of 25+ words, 16 (0.1%) interrupt the subject-verb bond, and of 2,725 ", which" clauses in long sentences, 2,680 (98%) hang off the tail.

**Revision.**

- Before: The assay, which was developed in our laboratory over three years and validated against two independent patient cohorts collected in different countries, detects the marker at picomolar concentrations.
- After: The assay detects the marker at picomolar concentrations, a sensitivity we reached over three years of development and confirmed against two independent patient cohorts collected in different countries.

**Do not apply when.** A short non-restrictive appositive genuinely identifies the subject at first mention ("Vitamin D, a secosteroid hormone, regulates…"); a three-to-five-word gloss does not break the bond. Also inapplicable to sentences that deliberately front a long conditional, where the delay is on the adjunct, not inside the clause.

---

## Never let a sentence end on an uninterpreted number, symbol, or bound

**Move.** After stating a quantity or formal result, the meaning is appended in the same sentence — a tail ", which indicates/means/implies…" clause or an em-dash plus a full clause — rather than starting a new sentence or leaving the reader to infer it.

**Why it works.** The reader gets the datum and its significance in one intake, so the number never sits inert; and because the gloss is grammatically subordinate it cannot be mistaken for a second, independent finding.

**Evidence.** 7 of the 12 papers read for dimension D. Validated corpus-wide: 46,583/52,063 sentences (89.5%) do not end on a bare number or symbol.

**Exemplars.**

- "From Figure 11(c), we observe that B2 has vastly superior performance—it does almost no work other than tombstoning the deleted points so it is extremely efficient." — *ParGeo*, Experiments
- "For construction, the performance gain is from better cache complexity—data movement can be greatly saved by constructing multiple levels in one round." — *kdtree*, Introduction
- "This approach trades off (slower) query performance for (faster) construction and updates, which can be more pronounced in higher dimensions." — *kdtree*, 6 Experiments

**Violation signature.** Results sentences terminating in a figure, a p-value, an effect size, or a formula, with the interpretation absent or deferred. Detector: read only the last five words of every sentence in the results section; a run of numerals and units means the pattern is missing. Corpus support: 2,725 tail ", which" clauses in long sentences (914 of them ", which is"), and the mid-sentence em-dash in 86/119 papers.

**Revision.**

- Before: Mean response latency in the treatment group was 4.2 ms (SD 0.8). Latency matters for perceived responsiveness.
- After: Mean response latency in the treatment group was 4.2 ms (SD 0.8)—below the 5 ms threshold at which listeners begin to report a perceptible delay.

**Do not apply when.** A dense table-replacement paragraph or a formal derivation where each quantity's meaning is fixed by an earlier definition and glossing every line would bury the argument. Gloss the quantities the argument turns on, not the intermediate ones.

---

## Match the claim verb to the class of evidence, and adverb-mark it when the verb is ambiguous

**Move.** Three verb bands are kept separate — prove/show for a formal derivation, find/observe for something measured, believe/expect/project for an extrapolation with no evidence in the paper — and when a verb from one band is used for another kind of evidence, an adverb says so ("we show empirically").

**Why it works.** The verb alone tells the reader what kind of scrutiny the claim can survive, so no separate epistemic disclaimer is needed and no claim is silently upgraded.

**Evidence.** 8 of the 12 papers read for dimension D.

**Exemplars.**

- "For sorting, we show the surprising result that on asymmetric memories, comparison sorting is asymptotically faster than sorting networks." — *asymmetry*, Introduction
- "Yet, we show empirically in Section 5 that the dynamic programming (DP) heuristic performs very well on a wide variety of graphs—and even the greedy heuristic does well on well-structured graphs." — *RadiusStepping*, 4 Heuristics
- "Since the write costs will significantly increase for future non-volatile main memory, we project that samplesort will be more efficient in this setting" — *buildingblock*, 5 Sorting

**Violation signature.** One verb (usually "show" or "demonstrate") doing duty for derived results, measured results, and speculation alike; or "we find" attached to something no measurement in the paper could produce. Check by verb-band count per paper: proof-heavy papers here run 6-9 "we show/prove" and near-zero "we find"; measurement-heavy ones invert it (p2307-wheatman: 11 "we find", 0 "we prove").

**Revision.**

- Before: Our simulations demonstrate that the protocol converges, our field data demonstrate that adoption is rising, and we demonstrate that the approach will scale to national deployment.
- After: We prove that the protocol converges. In the field data we observe that adoption rose in eleven of the twelve districts. We expect, though we have not tested it, that the approach scales to national deployment.

**Do not apply when.** A field where "show" is the neutral house verb for empirical results and "prove" reads as arrogance — in most of biology and the social sciences reserving "we show" for derivation would misfire. Port the three-band discipline, not this corpus's specific lexical assignment.

---

## Hedge the priority claim, state the result flat

**Move.** The knowledge hedge ("as far as we know", "to the best of our knowledge", "appears to be") attaches only to claims of being first or of an absence in the literature — claims no amount of work could fully verify — while the result itself, often in the same sentence, is asserted without hedge. A negative claim is never evidenced by citing an absence.

**Why it works.** The reader learns exactly which part of the sentence the authors could not check, and stops discounting the parts they could; and a knowledge hedge makes the scope of a negative claim checkable instead of pretending an absence can be evidenced.

**Evidence.** 10 papers across the D and F samples. Corpus-wide 37/119 papers carry "to the best of our knowledge", and it lands on a first-or-absence claim essentially every time.

**Exemplars.**

- "As far as we know, our work is the first to experimentally evaluate parallel closest pair algorithms, in both the static and the dynamic settings." — *closest*, Abstract
- "with overwhelming probability, which is asymptotically optimal and appears to be the first such bounds for the binary-forking model." — *predictive*, Abstract
- "While several graph algorithm benchmarks have been developed to date, to the best of our knowledge, BYO is the first system designed to benchmark graph containers." — *p2307-wheatman*, Abstract

**Violation signature.** Two opposite failures, both greppable. (a) A hedge sitting on a measured or derived quantity: "we believe our method reduces error by 30%", "results suggest a 2.4× speedup". (b) A bare priority claim with no hedge: "this is the first method to…" with no knowledge qualifier in the sentence.

**Revision.**

- Before: We believe our protocol reduces annotation time by roughly 30 percent, and it is possibly the first unsupervised method to do so.
- After: Our protocol reduces annotation time by 31 percent. As far as we know, it is the first unsupervised method to do so.

**Do not apply when.** The result genuinely rests on an assumption the authors cannot test — an unverified model, an extrapolation past the measured range, a claim about a population you did not sample. Then the hedge belongs on the result, and "we project"/"we expect" is the honest verb.

---

## Never write the agentless research passive; spend passive on naming and on locating evidence

**Move.** "It is observed that" / "it was found that" is refused in favour of "we observe"; passive is reserved for three narrow jobs — introducing a term ("is referred to as"), pointing to where something lives ("are presented in Appendix B"), and sentences whose topic genuinely is the object rather than any agent.

**Why it works.** Keeping the agent visible in claims makes responsibility for each assertion traceable; keeping it out of definitions and cross-references stops an irrelevant "we" from stealing the subject slot from the term being defined.

**Evidence.** 5 of the 12 papers read for dimension D; the grep below is corpus-wide.

**Exemplars.**

- "Our new parallel algorithm also uses this data structure, which is referred to as the sparse partition of an input set." — *closest*, 2 Preliminaries
- "More details are presented in Appendix B." — *closest*, 2 Preliminaries
- "Graphs with time information are referred to as temporal graphs, and efficient algorithms for temporal graphs have received immense attention recently." — *am-tree*, Introduction

**Violation signature.** Grep for `[Ii]t (is|was|has been|can be|could be) (found|observed|noted|believed|argued|concluded|shown|demonstrated) that`. Across all 119 corpus papers this returns 18 hits total, most of them "it can be shown" standing in for an omitted proof. Second detector: count first-person pronouns against be+past-participle per 1000 words — in all 12 sampled papers "we" outnumbers passive by 1.1× to 3.2×.

**Revision.**

- Before: It was observed that response rates declined after week six, and it is believed that fatigue was responsible.
- After: We observed that response rates declined after week six. We attribute the decline to fatigue, though we did not measure it directly.

**Do not apply when.** A venue or subfield mandates impersonal reporting, or the agent is a third party you are deliberately backgrounding because the point is the finding's independence from any one lab. Note also that this corpus's methods prose passivises freely when the object of study is the topic — that is the licensed use, not a violation.

---

## Keep the paper's own actions as finite verbs, not light verb plus noun

**Move.** Research acts are written as one verb governing an object — "we evaluate X", "we implement X" — never as a semantically empty verb carrying a nominalised action ("perform an evaluation of", "provide a comparison of").

**Why it works.** Collapsing the light verb removes two or three words and restores the agent-action-object shape the reader parses fastest; the real predicate stops hiding inside a noun.

**Evidence.** 6 of the 12 papers read for dimension D; the ratio below is corpus-wide.

**Exemplars.**

- "We measure the running time of 10 highly-optimized algorithms across over 20 different containers and 10 graphs." — *p2307-wheatman*, Abstract
- "In this section, we theoretically analyze the asymmetric I/O costs of different types of binary search trees." — *buildingblock*, 4.2.4
- "We evaluate our algorithm on both real-world and synthetic data sets." — *closest*, Introduction

**Violation signature.** Grep for `(perform|conduct|carry out|make|provide|undertake) (a|an|the) \w+(tion|sis|ment|ance|ence|ing) of`. Across all 119 corpus papers this occurs 14 times, against 503 uses of the corresponding bare verbs — a 36:1 ratio in favour of the finite verb.

**Revision.**

- Before: We performed an evaluation of the classifier and made a comparison of its output with the annotations that were produced by the human raters.
- After: We evaluated the classifier and compared its output with the human raters' annotations.

**Do not apply when.** The nominalisation names a standing object of the field rather than an action the authors took ("the construction", "the distribution" as things that exist and can be measured). This corpus is nominalisation-dense (median 29 per 1000 words) precisely because its subject matter is nouns; the rule targets the authors' verbs, not the discipline's vocabulary.

---

## Break the twenty-word rhythm with a short flat verdict

**Move.** Inside runs of 18-25-word explanatory sentences, drop a four-to-ten-word declarative stating a verdict with no hedge, no subordination and no citation, then resume normal length.

**Why it works.** The abrupt drop in length is the emphasis mechanism — the eye registers the short sentence as the paragraph's takeaway without any booster word doing the work.

**Evidence.** 5 of the 12 papers read for dimension D.

**Exemplars.**

- "The BHL-tree is competitive." — *kdtree*, 6 Experiments, range queries
- "These factors offset each other." — *buildingblock*, 5 Sorting
- "There are no dependencies among different lists." — *soda2015-final*, 3 Dependence analysis

**Violation signature.** A section in which every sentence lands between 18 and 30 words and nothing is asserted in under twelve — the prose has no place for the eye to stop. Measure it: the sampled papers run 19-33% of sentences at 10 words or fewer alongside 8-19% at 35 or more (corpus median 23% short / 12% long). A draft whose short-sentence share is under ~10% is uniformly paced.

**Revision.**

- Before: Across all four field sites condition B produced a higher score than condition A, and although the margin was small it never reversed in any site, which we take as evidence that the manipulation had a real if modest effect.
- After: Across all four field sites, condition B scored higher than condition A. The margin never reversed. It is that consistency, rather than the size of the gap, that we take as evidence of a real effect.

**Do not apply when.** Formal definitions, theorem statements, and algorithm specifications, where a clipped sentence would drop a precondition. The short verdict belongs to argument prose; it is not a licence to fragment a definition.

---

## Choose the subject of a results claim by the claim's scope
> **Status:** documented split

**Move.** Per-object comparisons make the object the grammatical subject and drop the observer entirely; aggregate results front "we find that" and prefix it with an adverbial saying over what the finding holds.

**Why it works.** An artefact-subject sentence reads as a property of the thing and needs no scope statement; a "we find" sentence advertises that a judgement was made, which is what an aggregate over many measurements requires — and the adverbial supplies the domain the average was taken over.

**Evidence.** 6 of the 12 papers read for dimension D. Comparative-verdict counts: kdtree 30 artefact-subject vs 3 we-subject; closest 6 vs 0; am-tree 7 vs 1; the benchmarking paper p2307-wheatman inverts it at 5 vs 9, with every "we find" carrying a scope frame.

**Exemplars.**

- "Pkd-trees have the best performance for all instances on all distributions." — *kdtree*, 6 Experiments, batch updates
- "On average, we find that the overall difference between the best offthe-shelf dynamic structure and the best specialized dynamic structure is within about 1.1×." — *p2307-wheatman*, Experiments
- "Finally, B1 has the worst performance, as it must fully rebuild on every insertion." — *ParGeo*, Experiments

**Violation signature.** Two mismatches. (a) A single-instance comparison wrapped in observer machinery — "we observed that Method C was faster on the German corpus" — where the observer adds nothing. (b) An aggregate stated as a bare property with no scope — "Method C is faster" — leaving the reader unable to tell over what.

**Revision.**

- Before: We observed that Method C was 1.3× faster than Method D on the German corpus, and Method C is faster overall.
- After: On the German corpus, Method C ran 1.3× faster than Method D. Averaged over all twelve corpora, we find that Method C is 1.2× faster.

**Do not apply when.** Fields where an unhedged artefact-subject verdict reads as overclaiming because the measurement is noisy — there the observer frame is doing epistemic work, not clutter, and should stay even on local comparisons. The split above is governed by results being reproducible and near-deterministic.
