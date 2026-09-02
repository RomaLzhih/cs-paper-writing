# Pass 6 — Stance

**Ask:** For every claim in this paragraph: whose evidence is it, where does that evidence stop, and is the uncertainty sitting outside the claim rather than inside it?

**Do not touch in this pass.** Do not add a knowledge-scope wrapper to every priority claim: 5 of 6 'the first …' claims in this corpus are stated flat, and a wrapper on a question settled by citation or proof reads as evasion. Do not flag a bare 'significantly faster' — 83% of its comparative uses have no adjacent number, and the requirement is that scope and magnitude appear somewhere in the results, not in every sentence. Do not hedge a proved universal or a stated sampling frame. Do not cut 'very' or 'highly' in their descriptive senses ('very large graphs', 'highly parallel'), and do not treat 'carefully' as a competitor-only word — it usually marks the authors' own design work. And do not rewrite structure at this stage: if a stance fix wants a new sentence, note it and re-run Pass 1 on that paragraph only.

7 patterns.

---

## Scope the claim from outside or state it flat — never move the hedge into the claim

> Narrowed after corpus measurement contradicted the original claim.

**Move.** State a priority or gap claim in exactly one of two shapes: flat and fully qualified ('we give the first work-efficient algorithm for X'), or with a knowledge-scope wrapper on the outside ('to the best of our knowledge', 'we are unaware of any X that ...', 'it was not previously known whether ...') with everything inside left intact and checkable. Never relocate the uncertainty into the claim itself — 'one of the first', 'arguably novel', 'relatively little work exists'. One wrapper at most; the qualifiers that limit the claim ('first work-optimal', 'first that handles correlated shocks') do the real narrowing and belong inside.

**Why it works.** The wrapper tells the reader exactly whose search came up empty, which is the only thing the authors can actually vouch for; the claim inside stays sharp enough that a reader who knows a counterexample can produce it. Blurring the claim itself instead ("one of the first", "relatively little work") makes the sentence unfalsifiable and reads as insurance rather than caution.

**Seen in.** predictive, dp, CH, semisort, incremental, asymmetry, buildingblock, arxiv-2301.01356 (sampled from 8-10 papers for this sub-topic, not all 119)

- "Prior to our work, we are not aware of any integer sorting algorithm in the binary-forking model (formally defined in section II) that achieved optimal O(log n) span and O(n) work." — *predictive*, I.A Related Prior Work

- "More importantly, we also provide what we believe is the first parallel learning-augmented sorting algorithm." — *predictive*, I.B Our Results

- "In theory, however, there are still no known bounds for parallel Delaunay triangulation using the incremental approach, nor for many other problems." — *incremental*, Introduction

**Violation signature.** A novelty or gap sentence whose hedge has migrated into the noun phrase — 'one of the first', 'arguably novel', 'a relatively unexplored area', 'comparatively few studies' — so that no reader could produce a counterexample, because nothing precise was claimed. Second tell: two scope wrappers stacked on one claim ('to the best of our knowledge, we believe this may be the first ...'). A flat, unwrapped priority claim is NOT a tell.

**Revision.**

- Before: Ours is arguably one of the first frameworks to deal with correlated shocks in this setting, and comparatively little work exists on the problem.
- After: To the best of our knowledge, this is the first framework that handles correlated shocks without assuming a common factor structure. The three closest prior treatments [4, 9, 17] all impose that structure.

**Do not apply when.** The question is settled by a citation or a proof — state it flat and point at the source, since a knowledge-scope wrapper on a decided question reads as evasion. Do not use the wrapper on a claim you have not actually searched: the phrase asserts a search was performed. And do not add a wrapper reflexively to every priority claim; a flat claim whose qualifiers are precise is the commoner and often the better form.

<sub>Verifier: The half about blurring is confirmed: 'one of the first' 3 uses/3 papers, 'among the first' 2, 'arguably' 4 in 1.1M words. The half that says a priority claim needs a knowledge-scope wrapper is not: of 225 sentences making a 'the first ...' claim, only 38 (17%) carry any wrapper ('to the best of our knowledge' 53, 'we are unaware' 49, 'as far as we know' 22, 'to our knowledge' 13, 'we are not aware' 7). Five-sixths of priority claims in this corpus are simply stated flat, and a rule that implies a wrapper is the correct shape will make a draft more hedged than the register. Two of the offered </sub>

---

## Spend exactly one hedge word at the boundary where your evidence stops

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** When a sentence carries a finding from the cases you tested into cases you did not, split it at that boundary: the tested part stays universal and unhedged, and the extension takes exactly one frequency or probability word — likely, usually, typically, generally, often, can. One word, and only on the extension: 92% of every hedged sentence in this corpus carries exactly one hedge, and three-or-more is 1%.

**Why it works.** One word placed at the boundary tells the reader precisely how far the evidence reaches, which is more informative than a uniformly cautious sentence and more honest than a uniformly confident one. Because it is one word, the claim keeps its shape; a stacked hedge ("may possibly tend to") destroys the shape without adding information.

**Seen in.** arxiv-2301.01356, buildingblock, predictive, dp, incremental (sampled from 8-10 papers for this sub-topic, not all 119)

- "this step for GBBS is the dominating cost for large-diameter graphs, and this is likely the case for other parallel BCC algorithms using BFS-based skeletons" — *arxiv-2301.01356*, Experiments (running-time breakdown)

- "Moreover, conclusions drawn from these numbers can likely give insights into tradeoffs between reads and writes among different algorithms." — *buildingblock*, Introduction

- "The performance of algorithms with predictions is typically tied to the quality of the provided predictions." — *predictive*, Introduction

**Violation signature.** A sentence whose subject quietly widens from the objects you tested to a class — 'methods of this kind', 'such systems', 'practitioners', 'other settings' — with no hedge anywhere in it; the inverse, a hedge sitting on the clause that reports what you actually measured; or two hedges modifying one and the same claim ('may possibly tend to'). Two hedges in two independent clauses of a long sentence is normal and is not a tell.

**Revision.**

- Before: The effect is driven by liquidity constraints, so credit-constrained firms respond the same way in other industries.
- After: The effect is concentrated in credit-constrained firms in all four industries we observe. It is likely present in other industries with similar financing structures, which we do not test.

**Do not apply when.** The generalisation is your proved theorem or your stated sampling frame — a proof or a random sample licenses the universal, and hedging it understates a result you earned. Do not hedge 'for all n' when you proved it for all n. Nor does this apply to ordinary background statements about what is common practice in a field: those take a frequency adverb because they are about frequency, not because your evidence stopped.

<sub>Verifier: The quantitative core is the best-supported claim in this topic: of 2,800 sentences containing at least one hedge, 92% carry exactly one, 7% carry two (almost always in two independent clauses), and 1% carry three or more; the stacked forms the pattern warns about are effectively absent ('may possibly/potentially' 5, 'might possibly' 1). But two of the four exemplars do not show the move. Exemplar 3 ('The performance of algorithms with predictions is typically tied to the quality of the provided predictions') and exemplar 4 ('Due to simplicity, this algorithm is usually the choice of implement</sub>

---

## Aim quality intensifiers at the competitor, and back each one with a fact

> Narrowed after corpus measurement contradicted the original claim.

**Move.** When you name a baseline you beat, put the intensifier on ITS quality — 'highly-optimized', 'extremely well-optimized', 'the fastest X we are aware of' — and place a checkable fact beside it ('over 15,000 lines of code', the library's name, a citation). The same move covers the difficulty of your own analysis ('the correctness analysis is highly non-trivial'). What you should not do is use an evaluative intensifier as a stand-in for the SIZE of your own advantage; that slot takes a number or a scope.

**Why it works.** An intensifier aimed at the baseline raises the bar the paper then clears, so it argues for the authors while costing them nothing in credibility; an intensifier aimed at their own margin occupies the slot the reader is scanning for a number and reads as substitution for one. The added fact ("over 15,000 lines of code") converts an adjective into evidence.

**Seen in.** semisort, dp, arxiv-2301.01356, buildingblock, predictive, incremental (sampled from 8-10 papers for this sub-topic, not all 119)

- "We also looked at the highly-optimized radix sort of [15], which is the fastest radix sort that we are aware of." — *semisort*, Experiments (comparison with other implementations)

- "Their code is highly-optimized with over 15,000 lines of code." — *semisort*, Experiments (comparison with other implementations)

- "sequential algorithms are extremely well-optimized" — *dp*, Introduction

**Violation signature.** Every evaluative intensifier in the paper points inward at your own contribution and none at anything a reader can check, while prior work gets only dismissive adjectives ('the standard approach', 'a naive baseline', 'a rather crude method'). Word-level tells are the near-absent boosters: 'dramatically' (8 uses in 1.1M words), 'remarkably' (4), 'substantially' (18). Test: delete every intensifier attached to your own result; if the sentence now looks empty, the intensifier was standing in for a number.

**Revision.**

- Before: Our estimator dramatically outperforms the standard approach, which is a fairly crude benchmark.
- After: The standard approach is a carefully tuned estimator that has been the field's default for two decades; ours reduces mean squared error against it by 34% across all six samples.

**Do not apply when.** 'Very' and 'highly' in their plain descriptive senses — 'very large graphs', 'very similar', 'highly parallel' — are scale words, not stance, and are among the commonest words in this register (411 and 320 uses); nothing here asks you to cut them. 'Carefully' is likewise not a competitor-only word: it marks deliberate design and is normally applied to the authors' own work. And where the paper's contribution is precisely that the incumbent is weak, show that with evidence instead of praising it.

<sub>Verifier: The competitor half holds: 'highly-optimized' 51 uses in 32/119 papers, and a sample of them points almost exclusively outward, at ParallelSTL, PBBS, a cited radix sort, a sequential baseline — usually with a checkable fact attached. The word list around it does not. 'Very' (411 uses, 100/119 papers) overwhelmingly modifies neutral scale words — large 68, similar 45, simple 31, small 25 — not competitor quality. 'Carefully' (81 uses, 45 papers) is aimed at the authors' OWN engineering in most of its uses ('we carefully redesigned join and expose', 'we carefully benchmarked our new implementati</sub>

---

## Carry a superiority claim on scope, number, and a named exception

> Narrowed after corpus measurement contradicted the original claim.

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** Give a superiority claim three checkable parts somewhere in the results: the set you tested ('on 27 graphs', 'on all graphs', 'consistently'), the magnitude as a number with its aggregation named ('3.1x faster on average, geometric mean'), and the case where it fails ('except for small omega on social networks'). The universal over a tested set is verifiable from your own table, so it commits you to more than an adverb does and therefore carries more force; the named exception is what makes the unqualified remainder believable. Keep or cut 'significantly' as you like — just never let it be the only thing carrying the claim.

**Why it works.** The universal quantifier over the tested set ("on all graphs", "consistently", "regardless of k") is verifiable from the table, so it carries more force than "significantly" while committing to more; and the named exception is what makes the unqualified remainder believable. This is how the corpus reconciles a 3:1 hedge-to-booster ratio with claims that still land hard.

**Seen in.** arxiv-2301.01356, buildingblock, semisort, dp, incremental (sampled from 8-10 papers for this sub-topic, not all 119)

- "We tested them on a 96-core machine on 27 graphs with varying edge distributions. FAST-BCC is the fastest on all graphs." — *arxiv-2301.01356*, Abstract

- "FAST-BCC is the fastest on all graphs. On average (geometric means), FAST-BCC is 3.1× faster than the best existing baseline on each graph." — *arxiv-2301.01356*, Abstract

- "The experimental results show that phased Dijkstra consistently outperforms the binary-heap version on I/O cost except for the combination of small ω (= 10), small cache size, and on social networks." — *buildingblock*, 6.2.4 Conclusions

**Violation signature.** A results section in which no sentence names a tested set, a magnitude, or an exception — no 'on all', no 'except', no figure or table reference — so every comparative verb floats free. Word-level tells are the boosters this register almost never uses: 'dramatically', 'remarkably', 'substantially'. 'Significantly faster' is not a tell on its own.

**Revision.**

- Before: Our method substantially outperforms existing approaches across a wide range of settings.
- After: Across the 14 country-year panels we assemble, our method has lower out-of-sample error than both baselines in 13; the median reduction is 22%. It loses to the ridge baseline on the one panel with fewer than 200 observations.

**Do not apply when.** Theoretical claims, where the bound statement itself carries the force; and where there is genuinely no exception, do not manufacture one — write the universal and let the table be checked. Do not flag a bare 'significantly faster' in an abstract: 83% of this corpus's comparative uses of 'significantly' have no adjacent number, and the requirement is that the paper supply scope and magnitude somewhere in the results, not in every sentence.

<sub>Verifier: The constructive half is well supported: 'on all graphs/inputs/instances' 70 uses in 23 papers, 'consistently' 74 in 41, 'except' 227 in 86, 'in most cases' 39 in 26. The prohibitive half fails at 119 papers. 'Significantly' is 281 uses in 92/119 papers, 166 of them directly on a comparative (faster 28, more 25, better 16, improves 13, outperforms 19, reduce 10); a random sample shows only 17% have any number within 160 characters either side, and abstracts routinely read 'our algorithms are highly parallelized and significantly outperform their sequential counterparts' with no number in sight</sub>

---

## Let a definition or a proof step license must, always and exactly — and treat clearly as deletable outside a derivation

> Narrowed after corpus measurement contradicted the original claim.

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** Treat must / always / never / exactly as pointers to a licence the reader can follow: a definition that forces the count, a theorem that forces the necessity, a step they can complete in one line. Delete any instance whose licence you cannot name. These are the register's ordinary precision markers, not emphasis (must 700 uses in 107/119 papers, always 478, exactly 246). 'Clearly' and 'obviously' are not in that class — 77 uses in 1.1M words, nearly all inside proofs — so outside a derivation, where you could not immediately write the step the word stands for, cut them rather than looking for a licence.

**Why it works.** In this register these are precision markers, not emphasis: "exactly two" is a fact about a definition, "must" is the conclusion of a proof step. Keeping them tied to a licence means the reader never has to decide whether a given "always" is a proof or a boast. Note the measurement caveat: the digest's 2.6 boosters per 1,000 words is inflated by exactly these technical uses — in the ten papers read here almost every must/always/never/exactly is licensed, so the real rhetorical-booster rate sits far below the 8.1 hedge rate, making the asymmetry stronger than the count suggests.

**Seen in.** CH, dp, incremental, asymmetry, xu-wosl-pods-17 (sampled from 8-10 papers for this sub-topic, not all 119)

- "A ridge is incident on exactly two facets of the same orientation." — *CH*, 5 Convex hull (configuration space)

- "Note that any longer path must have a length l path as a prefix, so we need not consider the longer paths." — *CH*, proof

- "Clearly, their DP values cannot be relaxed by other states and they will be identified as ready in our algorithm." — *dp*, proof of correctness

**Violation signature.** must / always / never / exactly attached to a claim about value, novelty, difficulty or measurement rather than to a deduction: 'this always improves performance', 'our formulation exactly captures the intuition', 'researchers must consider'. For clearly/obviously, the test is stricter: for each instance, write out the one-line step it stands for; if you cannot ('clearly, this is an important problem', 'clearly this issue is solvable'), the word is doing the work of an argument you did not write.

**Revision.**

- Before: Clearly, wealthier households must respond more strongly, and this is always true in our data.
- After: Wealthier households respond more strongly in every decile we observe (Table 3). The model in Section 2 implies this ordering whenever risk aversion is decreasing in wealth.

**Do not apply when.** 'Must' stating a precondition or specification ('the sample must be balanced before the second stage') is a requirement, not a boost, and needs no theorem. And where you cannot complete the step behind a 'clearly', the fix is to write the step or drop the word — not to hedge it.

<sub>Verifier: The licence test is right, but the rule groups two classes that behave nothing alike. 'Must' is 700 uses in 107/119 papers, 'always' 478 in 101, 'exactly' 246 in 83 — ubiquitous precision markers, and 'keep them licensed' is the right instruction. 'Clearly' (63, 26 papers) and 'obviously' (14, 6 papers) are among the constructions the digest lists as effectively avoided, at 0.039 and 0.009 per 1k; a full read of all 77 uses shows nearly every one inside a proof on a step the reader finishes in a line ('Clearly, lambda* <= lambda0', 'Clearly, the preprocessing takes O(n log n) time'). Presentin</sub>

---

## Locate an unproved negative in your proof or your knowledge, not in the world

**Move.** When something did not work and you have not proved it impossible, attach the negation to the artefact that actually failed — the theorem, the search, the field's current knowledge — using "does not obviously generalize", "it seems difficult to prove", "we cannot find", "it is not known whether".

**Why it works.** It distinguishes a limit you established from a limit you merely hit, which is the difference between a result and a confession, and it converts a dead end into an open problem a later reader can take up. A bare impossibility claim invites exactly one response: a counterexample.

**Seen in.** xu-wosl-pods-17, incremental, asymmetry, arxiv-2301.01356, semisort, predictive (sampled from 8-10 papers for this sub-topic, not all 119)

- "Unfortunately, Theorem 10 does not obviously generalize to give matching high probability bounds on the amortized insertion cost." — *xu-wosl-pods-17*, Analysis of insertions

- "Unfortunately it seems difficult to prove a logarithmic bound on dependence depth for such an approach." — *incremental*, Delaunay triangulation

- "It is not known whether this is optimal." — *asymmetry*, Upper bounds (edit distance / Kleene)

**Violation signature.** A bare impossibility or non-existence with no proof and no citation: "this cannot be extended to the multivariate case", "no method exists for X", "the approach fails under heteroskedasticity" — where the paper's only evidence is that the authors tried and stopped. Also detectable as a missing agent: ask whose failure the sentence is reporting; if the sentence hides that it is yours, rewrite it.

**Revision.**

- Before: The identification argument cannot be extended to panels with attrition.
- After: The identification argument does not obviously extend to panels with attrition; we do not know whether the exclusion restriction can be weakened enough to cover that case.

**Do not apply when.** You have a proof or a citation for the impossibility. A proved lower bound is stated flat and pointed at ("we show a lower bound of ..., which indicates that no asymptotic improvement is achievable"); hedging a negative you established throws away the result.

<sub>Verifier: Attested as a family across the corpus even though each individual template is rare: 'we cannot / could not / were unable to / do not know' 104 uses in 56/119 papers, 'it is/seems difficult/hard/unclear/not clear' 40 in 28, 'open problem/question' 59 in 25, 'remains open' 16 in 14, 'does not obviously/directly generalize or extend' 6 in 4, 'seems difficult/hard' 8 in 7. All four exemplars illustrate the move exactly — each attaches the negation to a bounded artefact (Theorem 10, a proof attempt, the field's knowledge, the authors' search) rather than to the world. The violation signature is ch</sub>

---

## Facts about a cited work flat; their motives and unstated limits hedged and licensed

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** Anything about a cited work that a reader can derive from its own published description — its cost, its assumptions, its stated scope, its reported speed — is written flat and cited. Anything you infer about the authors' reasons, intentions, or unstated design limits takes 'we believe', 'probably', or 'appears to', and is followed immediately by the fact that licenses the guess ('We believe the reason is the space-inefficiency (it uses O(m) extra space)').

**Why it works.** The hedge marks the line between reading someone's paper and reading their mind, which is the line a wronged author will contest. Stating the derivable fact flat is also more damaging to a weak baseline than an insinuation would be, because the reader can confirm it; and the licensing fact placed just after the belief lets them judge the guess.

**Seen in.** arxiv-2301.01356, semisort, predictive, CH, dp, incremental (sampled from 8-10 papers for this sub-topic, not all 119)

- "However, Tarjan-Vishkin is not widely used in practice. We believe the reason is the spaceinefficiency" — *arxiv-2301.01356*, Introduction

- "We believe that their code is designed to only handle well-balanced distributions, and so it is not surprising that it outperforms our code." — *semisort*, Experiments (comparison with other implementations)

- "their methods all appear to be inherently sequential; hence, trying to convert these algorithms into efficient parallel methods does not appear to be a productive approach" — *predictive*, I.A Related Prior Work

**Violation signature.** A flat assertion about a cited author's motive, intent, or unstated limitation — 'they used aggregate data because household panels were unavailable', 'their method was never intended for skewed inputs', 'prior work overlooks X' — with no page reference where they say it and no experiment showing it. The inverse tell: a hedge draped over something the cited paper states plainly ('their algorithm may require quadratic memory'), which reads as insinuation rather than caution.

**Revision.**

- Before: Earlier studies rely on aggregate data because household panels were unavailable to them, so their elasticities are biased upward.
- After: Earlier studies rely on aggregate data [4, 9]; we believe the reason is that household panels for that period were not released until 2011. Their specification omits within-household variation, which raises the estimated elasticity by 0.3 in our replication.

**Do not apply when.** The property is stated or proved in the cited work, or you measured it yourself — cite or measure and write it flat. An unfavourable comparison against your own method is likewise reported flat; the hedge belongs on the explanation that follows, not on the number that hurts. And this is not a rule about 'we believe' generally: in this register it marks any judgment the authors cannot prove, including their own priority claims and design preferences. The constraint is one-directional — a derivable fact about someone's paper must not be hedged, and a motive must not be stated flat.

<sub>Verifier: The move is attested — 'we believe' 196 uses in 70/119 papers, 'appears/appear to' 17 in 13, and the specific attribution formula 'we believe the (main) reason' 7 uses across 6 papers, every one of them an unmeasured guess about a cited system rather than a fact from its paper. Two repairs. First, exemplar 4 does not illustrate the move: 'We use the definition of configuration space from Mulmuley since we believe it is simpler and more general than Clarkson and Shor's original presentation' hedges the authors' own preference between two formulations, not an inference about another author's rea</sub>
