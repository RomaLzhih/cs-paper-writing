# B. Section-level rhetorical moves

9 patterns, ordered by how much each would improve a weak draft.

---

## Grant before you take

**Move.** The field's achievement goes into a subordinate clause and the gap into the main clause. Two realisations: split the literature into two camps with opposite strengths and let the empty intersection be your slot; or put the mass of prior work into a concessive clause carrying a large citation bundle ("Despite…", "Although X is widely studied [20 refs]…") and make the main clause the gap.

**Why it works.** The reader learns what the field already gets right before learning what it lacks, so the contribution reads as filling a named hole rather than as generic superiority; the bundle buys the right to say "and yet", and a gap claimed without it reads as ignorance and invites a reviewer to name a counterexample.

**Evidence.** 9 papers, union of the B and F samples (12 each).

**Exemplars.**

- "While many classic data structures, such as the link-cut tree, provide strong bounds for incremental MST, their performance is limited in practice. Meanwhile, existing practical solutions used in applications do not have any non-trivial theoretical guarantees." — *am-tree*, Abstract
- "While higher quality structures can be generated using agglomerative (bottom-up) construction schemes [Walter et al. 2008], these methods, even with recent optimizations, have not been demonstrated to be performance competitive with best practice divisive implementations." — *HPG13*, 1 Introduction
- "Although SCC is also widely studied in parallel (see the literature review in Sec. 7), most existing algorithms are" — *scc*, 1 Introduction

**Violation signature.** The gap paragraph names one deficiency of "existing work" with an evaluative adjective and no counterweight, and the gap sentence carries no citation. Detector: search the gap sentence for a paired construction ("While X…, Y…", "Despite…", "Meanwhile", "At the other extreme") and for a reference bundle or a pointer to the related-work section. If every criticism is one-sided and uncited, the pattern is absent.

**Revision.**

- Before: Existing sentiment classifiers do not work well on clinical notes, so we propose a new one.
- After: Rule-based classifiers built on clinical lexicons [3, 8, 11] are auditable by the clinicians who must sign off on them, but miss negation scope. Transformer classifiers [15, 19, 22] capture negation scope but produce decisions no clinician can inspect. No published system is both.

**Do not apply when.** The literature genuinely has one camp, or the gap really is a first move into an unstudied setting — manufacturing a second camp or a concession about work that does not bear on your problem misrepresents the field; there the honest form is a hedged absence. Also wrong when you deliver only one of the two properties you set up: the two-sided frame promises the intersection.

---

## Criticise the mechanism, measure it, and supply the replacement

**Move.** Each criticism of prior work states what the work does that produces the problem (not a verdict on its quality), carries a number the reader can check — your re-implementation, your run of the baseline, or the rival's own reported figure — and is followed in the same sentence or the next by what this paper does instead.

**Why it works.** A quantified, mechanism-level criticism is falsifiable and therefore credible, and it silently establishes that the authors understood the prior work well enough to run it; following it with your alternative teaches the design space rather than a ranking.

**Evidence.** 10 papers, union of the B and F samples.

**Exemplars.**

- "our experiences reimplementing and optimizing these techniques in C++ yield singlecore performance that is (even after non-trivial effort) about four to seven times slower than a binned SAH build (see Table 2)." — *HPG13*, 2 Background
- "These techniques greatly improve locality in computations on static graphs, but do not easily translate to graphs that evolve over time." — *xu-terrace-sigmod-21*, 1 Introduction
- "The parallel bag [66] supports similar interfaces as our hash bag, but uses a very different design." — *scc*, 7 Related Work

**Violation signature.** Two detectors. (1) The gap rests on adjectives — "prohibitively expensive", "does not scale", "naive", "ad hoc" — each with a citation but no number and no figure in this paper to check. Ask of each criticism: "what number, and where?" (2) A related-work paragraph ends on the criticism with the contrast to the present work implicit or deferred.

**Revision.**

- Before: Existing annotation pipelines are inadequate for corpora of this size.
- After: Both published pipelines re-parse the full document at every pass; over our 40M-token corpus each needed more than 30 hours per pass (Table 1), against a two-hour overnight budget. We cache the parse and re-score incrementally.

**Do not apply when.** The weakness is definitional rather than empirical — prior work does not handle a case at all, or assumes something your setting violates. There a benchmark number is theatre: name the missing case. Also when you cannot run the baseline fairly (quote its authors' figure and say you are doing so), and in a survey or background section written to inform rather than to position, where a constant "but we…" turn becomes self-promotion.

---

## Concede at the point of the claim

**Move.** The sentence conceding a limit of your own result — or the respect in which a rival beats you, or the sense in which the idea is not new — sits adjacent to the claim it qualifies, often inside it after "Although", and is immediately followed by a number showing how much of the real workload falls outside the limit, or by the ground you are actually claiming.

**Why it works.** Concession at the point of claim pre-empts the objection while the claim is still in view and lets the author, not the referee, choose the frame it is read in; the trailing measurement or retained-ground clause converts an admission into a scope statement the reader can evaluate.

**Evidence.** 10 papers, union of the B and H samples.

**Exemplars.**

- "Although the bounds (typically, O(n + m/B)) may not be optimal for low-degree graphs, many real-world graphs have average degree at least B, in which case the I/O complexity is optimal." — *ROSE*, 1 Introduction
- "We note that there exist parallel LIS algorithms [22, 54] with better worst-case span bounds than our results in theory." — *lis*, 1 Introduction, contribution summary
- "Our algorithms are not in-place, but we discuss in Section 6.1 about the extra storage needed." — *DP*, 1 Introduction, contribution list

**Violation signature.** Every comparative statement in the introduction runs the author's way; "however/although/while" appear only when the subject is prior work; the first concession is in a terminal Limitations or Future Work paragraph, unquantified ("may not scale to all settings"). Detector: for each headline claim, is its scope condition within two sentences, and does that condition carry a number or a named rival?

**Revision.**

- Before: Our parser reaches 91% attachment accuracy. (…six pages later…) A limitation is that we evaluated only on newswire.
- After: Our parser reaches 91% attachment accuracy on newswire. On the two spoken-language treebanks it falls to 74%, because disfluency repairs create arcs the training data never contains; spoken material is 8% of the corpus we target.

**Do not apply when.** The concession is large enough to change what the paper claims — then it is not a fence but a restatement of scope and belongs inside the claim. Skip when no measurement exists: an invented fence ("most real datasets resemble ours") is worse than a plain admission. And never concede to an apparent rival that solves an orthogonal problem, or concede without supplying the ground you keep.

---

## Say which way it went before you say how much

**Move.** At section scale, the first block of a large evaluation is a findings summary and the machine/compiler/dataset description follows it; at paragraph scale, the opening sentence states the direction of the finding qualitatively (faster, smaller, no different) and the following sentences carry the numbers and the explanation. The section then closes by reassembling the sub-results into the same claim.

**Why it works.** The reader gets a map before the terrain, so every table arrives with a question attached; direction is what an explanation attaches to, and a paragraph opening with a number dump makes the reader compute the claim before they can evaluate it.

**Evidence.** 8 papers, union of the B and C samples.

**Exemplars.**

- "We first summarize the high-level takeaways from our large-scale evaluation." — *p2307-wheatman*, 6 Experimental Evaluation (6.1 Summary precedes 6.2 Setup)
- "Running Time. PaC-IM is significantly faster than the baselines on almost all graphs." — *im*, 6 Experiments, opening of results paragraph
- "The lazy version always achieves much better performance than the strict version, due to two main reasons." — *am-tree*, 8.2 Update Throughput

**Violation signature.** The results section opens with hardware and compiler flags and the first number arrives a page later; nothing states in advance what the numbers will collectively show; results paragraphs open with a pointer plus figures ("Table 3 shows running times of 4.1s, 6.8s and 11.2s"). Detector: read only the first sixty words of the evaluation, and only the first sentence of each results paragraph — if you cannot say which way things went, the pattern is missing.

**Revision.**

- Before: 5 EVALUATION. All experiments were run on a 32-core machine with 256 GB of RAM. We use five-fold cross-validation… Table 4 reports accuracy for the three encoders: 0.71, 0.79, and 0.80.
- After: 5 EVALUATION. Across all six corpora the morphological features add 4-7 F1 over the lexical baseline, and the gain comes almost entirely from low-frequency lemmas. 5.1 Setup. All experiments were run on… 5.2 Results. The two neural encoders beat the bag-of-words baseline but were indistinguishable from each other (0.71 against 0.79 and 0.80, Table 4).

**Do not apply when.** One system, one baseline, one table: a findings-first block duplicates the caption, and two papers here (scc, ParChain) correctly open with Setup. The condition is size — many baselines across many datasets earn a map. Also skip when the setup contains a choice the reader must accept before any number means anything (a non-standard metric, a contested split). At paragraph scale the corpus genuinely splits: when the paragraph's whole point is a magnitude reported once and not explained, leading with the number loses nothing.

---

## Open the technical section with goal, obstacle, construct — before any notation

**Move.** A technical section's first paragraph restates what the section must deliver, names why the obvious approach fails, and only then announces the construct; definitions and symbols begin in the second paragraph.

**Why it works.** The reader holds machinery far more cheaply once she knows what it is for and what it had to defeat; without the obstacle sentence every design choice in the section looks arbitrary.

**Evidence.** 5 of the 12 papers read for dimension B.

**Exemplars.**

- "In this section, we propose the AM-tree to support incremental MST. Recall that an incremental MST needs to maintain the edges in the MST and efficiently answer PathMax queries." — *am-tree*, 3 The Anti-Monopoly tree, opening
- "In this section, we discuss the parallel cover tree algorithms. We note that the queries on cover trees are already parallel since they do not change the data structure, so multiple queries can directly be applied simultaneously." — *covertree_2*, 4 Parallel Cover Tree, opening
- "In this section, we present our framework ParChain for parallelizing the nearest-neighbor chain (NNC) algorithm, which works for all linkage criteria that satisfy the reducibility property explained in Section 2.1." — *ParChain*, 3 ParChain, opening

**Violation signature.** A section beginning "Definition 1", "Let X = …", or "Algorithm 2 shows our procedure": machinery first, unmotivated. Detector: does each body section's first sentence contain a purpose word ("to support", "needs to", "the goal is")? Is there any obstacle marker ("however", "this is not easy", "the difficulty is") in the opening paragraph?

**Revision.**

- Before: 4 METHOD. Let D = {(x_i, y_i)} be the annotated set and let phi be the feature map defined in Equation 3.
- After: 4 METHOD. This section builds the classifier that must separate scribal hands from spelling alone. Raw character n-grams fail here, because the most frequent variants are shared by every hand. We therefore weight each variant by how unevenly it is distributed across hands, which we define next.

**Do not apply when.** The section is a short formal interlude whose purpose was fully stated by the section before it; or a preliminaries section that only fixes notation, where nothing is being overcome and a manufactured obstacle sentence misleads.

---

## End every related-work group on the axis where you differ, and name which entries became baselines

**Move.** Related work is grouped by approach family; each group closes on the same comparison axis — the property this group lacks or permits that the present work does not — and says which members were actually compared against and why those.

**Why it works.** One repeated axis turns a list of names into a table the reader can hold in mind, and naming the baselines inside related work closes the usual gap where cited systems and evaluated systems are disjoint sets.

**Evidence.** 6 of the 12 papers read for dimension B.

**Exemplars.**

- "Unlike the present paper, that paper did not formalize a read-only model, did not consider block transfers, allowed more than O(n) internal memory in a key variant" — *ROSE*, 2.2 Related Work
- "For this type of approach, we compared the two newest ones with the released code: Multi-step [98] and iSpan [58]." — *scc*, 7 Related Work
- "While these algorithms are insightful, to the best of our knowledge, none of them have implementations." — *stepping*, 8 Related Work on Parallel SSSP

**Violation signature.** Consecutive sentences of the form "Smith [12] proposed X. Jones [13] proposed Y." with no "unlike", "in contrast", "however", "does not", or first-person clause anywhere in the paragraph. Second detector: the systems named in related work and the baselines in the evaluation are disjoint, and nothing explains the mismatch.

**Revision.**

- Before: Smith et al. [12] used a hidden Markov model. Jones [13] used CRFs. Patel et al. [14] applied a transformer.
- After: All three prior taggers assume the token stream is already segmented — Smith et al. [12] with an HMM, Jones [13] with CRFs, Patel et al. [14] with a transformer. Our corpus has no segmentation, which is why we compare against [13] and [14], the two with released code.

**Do not apply when.** The group is foundation rather than rival — machinery you build on. Closing "we differ in that…" on work you depend on misrepresents the debt; say what you take from it. Also inappropriate in a survey, where the taxonomy is the point.

---

## Choose one grammar for the contribution list — artifacts or claims — and hold it

**Move.** The bulleted contribution list is written entirely in one grammar: bare noun phrases naming deliverables (often with a relative clause stating the payoff), or full sentences led by "We" plus a claim verb. Papers pick one and do not mix.

**Why it works.** A single grammar makes the list skimmable — the reader parses the first bullet and reuses the frame — and forces the author to decide whether the paper hands over objects or defends propositions.

**Evidence.** 8 of the 12 papers read for dimension B; the sample splits 5 artifact-noun / 3 claim-sentence, and the split tracks whether the contribution is a thing handed over or a claim defended.

**Exemplars.**

- "The ParChain framework for parallel HAC using linear space." — *ParChain*, 1 Introduction, contribution list
- "An experimental study of PPCSR compared to Aspen, Ligra, and Ligra+ that demonstrates that PPCSR supports efficient updates and queries." — *xu-ppcsr-alenex-21*, 1.2 Contributions
- "We introduce the Read-Only Semi-External (ROSE) model for the design and analysis of large graph algorithms, motivated by real-world systems considerations." — *ROSE*, 1 Introduction, contribution list

**Violation signature.** Inside one list, "We prove a tight bound on X" sits beside "An open-source implementation" beside "Extensive experiments demonstrate effectiveness", so the reader re-parses each bullet. Second signature: a bullet that names a section rather than a contribution.

**Revision.**

- Before: • A new corpus of 4,000 annotated letters. • We show that spelling variation predicts scribal origin. • Evaluation is performed against three baselines.
- After: • A corpus of 4,000 letters annotated for scribal hand and spelling variant. • A classifier that predicts scribal origin from spelling variation alone. • An evaluation of that classifier against three published baselines on held-out letters.

**Do not apply when.** The paper has a single contribution — a one-item bullet list is weaker than one sentence of prose; or a venue's structured form mandates a grammar.

---

## Enumerate the challenges once, then answer them in the same order under the same names
> **Status:** variant

**Move.** After stating the goal, the introduction lists the obstacles as a tagged sequence, and each following paragraph opens with a clause reusing the tag and announcing which item it discharges, with the section number where the technique lives.

**Why it works.** It converts unexplained difficulty into a checklist the reader carries into the body, makes the contribution list derivable rather than asserted, and the ordering constraint forces the author to notice a challenge that received no answer.

**Evidence.** 8 papers across the A and B samples, but validated corpus-wide at only 28/119 (23.5%) — a variant, not a rule. (An over-narrow first regex scored it at 1.7%, so treat the number as a floor.)

**Exemplars.**

- "(Q1) How can we achieve a good trade-off between PIM load balance, reduced off-chip communication, and low space consumption?" — *pimzd*, 1 Introduction
- "To address (Q1), PIM-zd-tree divides the tree into three layers based on the properties of nodes, where each layer has its own strategy for data partitioning, placement and lightweight sharing (caching)." — *pimzd*, 1 Introduction
- "There are two challenges in achieving both space efficiency and high parallelism. The first challenge is to maintain all chains and merge reciprocal nearest neighbor clusters correctly and efficiently in parallel." — *ParChain*, 1 Introduction

**Violation signature.** The introduction goes from problem to solution with no sentence saying what makes the problem hard; or challenges are listed in one place and solutions in another with different names, counts, or order. Detector: number the challenges and number the answering paragraphs; if the sequences are not 1-1 and in order, or a listed challenge is never returned to, the pattern is absent.

**Revision.**

- Before: Two problems complicate longitudinal cohort analysis: attrition and measurement drift. We used inverse-probability weighting, harmonised the instruments, and imputed missing covariates.
- After: Two problems complicate longitudinal cohort analysis. (P1) Attrition is non-random… (P2) Instruments changed between waves… To address (P1), we reweight by inverse probability of retention (Section 3.2). To address (P2), we harmonise the instruments to a common scale (Section 3.3).

**Do not apply when.** There is only one challenge (the tags become noise); the obstacles are the steps of a routine pipeline, where three "challenges" any competent reader finds trivial read as inflation; or the solutions genuinely cross-cut the challenges — then say so ("these two techniques jointly address both") rather than forcing a false pairing.

---

## Convert your own residue into named open problems in the conclusion

**Move.** The closing section names the specific thing this paper did not get — the one non-optimal case, the assumption still standing, the variant not investigated — precisely enough to be attacked, rather than filing it under generic future work.

**Why it works.** A conclusion that names its own residue adds information the abstract did not contain, and a precisely stated gap reads as command of the problem rather than an omission the reader has to discover.

**Evidence.** 4 of the 12 papers read for dimension B.

**Exemplars.**

- "The only non-optimal algorithm regarding cache complexity in this paper is for the GAP recurrence. The I/O cost has an additional low-order term of O((n2 log M )/B)." — *DP*, 9 Conclusions and Future Work
- "We have not yet investigated the possibility of a “lazy” variant of an AAC build. While lack of support for lazy builds is a known drawback of previous bottom-up approaches" — *HPG13*, 5 Discussion
- "One of such examples is the metric skip lists [41], which provide similar (but randomized) query and update costs to cover trees but do not need to assume bounded aspect ratio." — *covertree_2*, 6 Conclusions

**Violation signature.** The final section restates the abstract and closes with "In future work, we plan to extend our approach to other domains." Detector: does the conclusion contain any noun that did not already appear in the abstract? If not, it adds nothing. Second detector: a generality claim with no partition into where it transfers unchanged and where it needs more work.

**Revision.**

- Before: In future work we plan to apply our method to other languages and larger datasets.
- After: Two things remain unresolved. Our aligner assumes one scribe per letter, so the 6% of letters in two hands are silently mis-attributed, and we do not know whether those errors are systematic. And the edit model is trained on the century it is tested on; whether the edits transfer across two centuries is open.

**Do not apply when.** The residue is a defect that invalidates a claim rather than bounding it — that belongs in the body beside the claim, not on the last page. Also do not manufacture open problems for the appearance of thoroughness: three vague ones are worse than one sharp one.
