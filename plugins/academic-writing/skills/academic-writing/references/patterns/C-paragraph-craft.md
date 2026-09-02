# C. Paragraph craft

8 patterns, ordered by how much each would improve a weak draft.

---

## Relay the previous sentence's last noun into the next sentence's subject, in the same words

**Move.** Start a sentence with the exact noun phrase that ended the previous one, rather than a synonym, a pronoun, or a fresh subject.

**Why it works.** The reader never searches backwards for the antecedent, and because the words are identical rather than varied there is no moment of wondering whether a new concept has been introduced.

**Evidence.** 12 of the 12 papers read for dimension C. Measured: 16-32% of adjacent sentence pairs open with a content word lifted from the previous tail; 22-40% of sentences open with some explicit backward link.

**Exemplars.**

- "and supporting snapshots. Supporting snapshots is particularly useful in scenarios in which a stream of updates is being made to a collection which is concurrently being analyzed" — *PacTree*, 1 Introduction
- "The double- or triple-red issue is resolved after the rotation. The rotation, however, makes the new subtree root red, which can again violate the red rule between the root of the rotated tree and its parent." — *joinable*, 4.2 Red-Black Trees
- "Each element e in the data structure has an integer height he determined by a sequence of biased coin flips. Coin flips are implemented by hashing e" — *xu-wosl-pods-17*, 3 Randomized balancing

**Violation signature.** Consecutive sentences whose subjects are unrelated noun phrases, so each restarts the topic; a chain held together by bare "it"/"this"/"they" with more than one candidate antecedent; or elegant variation, where the same object is "the mechanism", then "the procedure", then "the pathway" in three successive sentences.

**Revision.**

- Before: Participants completed the recall task after a twenty-minute delay. This period was chosen to match the consolidation window reported in earlier work. It varied across studies, however.
- After: Participants completed the recall task after a twenty-minute delay. The twenty-minute delay was chosen to match the consolidation window reported in earlier work, though that window varies across studies.

**Do not apply when.** The relay word is the grammatical subject of four or five sentences running — the paragraph reads as a stutter; break it with a fronted adjunct once the link is secure. And do not relay across a genuine topic shift: repeating the old term at the head of a new topic sentence tells the reader the topic has not changed when it has.

---

## Front the purpose, then deliver the move: "To <do X>, we <do Y>"

**Move.** Open the sentence that introduces a new step with an infinitival purpose clause naming a goal already on the table, and put the new action in the main clause.

**Why it works.** The fronted clause carries information the reader already has, so the new mechanism lands where the reader is looking for news; nobody holds an unexplained action in mind while waiting to learn why it exists.

**Evidence.** 12 of the 12 papers read for dimension C.

**Exemplars.**

- "To address the space issue, we proposed BFS-B-Hash using blocking." — *ED*, 1 Introduction
- "To address this limitation, a significant research effort over the past decade has centered on efficient dynamic-graph containers and their corresponding systems" — *p2307-wheatman*, 1 Introduction
- "To construct a sparse partition, the sequential algorithm proceeds in rounds." — *closest*, 2.2 A Grid-Based Implementation of Sparse Partition

**Violation signature.** Mechanism sentences whose motive arrives late or not at all: "We use blocking here. This reduces the space overhead." or "We use blocking in order to reduce the space overhead." Grep symptom: sentence-initial "In order to" — across all 119 corpus papers it opens a sentence only 19 times in 11 papers, against 110 fronted "To <verb>…" openings in these 12 papers alone.

**Revision.**

- Before: We ran the models a second time with the outlier cases removed. This was done in order to check that the correlation was not driven by the three extreme observations.
- After: To check that the correlation was not driven by the three extreme observations, we ran the models a second time with the outlier cases removed.

**Do not apply when.** Three consecutive sentences would open this way — the prose becomes a chain of subordinated preambles with no independent assertions. Also drop it when the step was exploratory and the purpose is genuinely post hoc; inventing a fronted purpose misrepresents the work.

---

## Put the topic in a run-in label so sentence 1 can spend itself on the claim

**Move.** Prefix the paragraph with a bolded one-to-five-word noun-phrase label ending in a period, then make the first sentence assert a result, definition, or decision instead of announcing what the paragraph is about.

**Why it works.** The label discharges the naming duty that would otherwise eat the topic sentence, so subject and claim arrive in the same eye-span and whole paragraphs can be skipped by label alone.

**Evidence.** 11 of the 12 papers read for dimension C; the twelfth (full) runs its introduction and related work with zero run-in labels.

**Exemplars.**

- "Space Usage. For 𝐵 = 128, PaC-trees obtain a 2.48x reduction in space usage compared to using P-trees" — *PacTree*, 9 Experiments
- "Benchmark results. We perform a cross-cutting evaluation of graph containers and frameworks along several distinct axes." — *p2307-wheatman*, 1 Introduction
- "External-memory model. The external-memory or disk-access model (DAM) [2] consists of two levels of memory: a fast memory (RAM) of size M and a slow arbitrarily large external memory, such as a disk." — *xu-wosl-pods-17*, 2 Adapting to External Memory

**Violation signature.** The paragraph's first sentence contains no assertion — it only names the subject ("In this section, we discuss space usage.", "There are several considerations regarding X."). Or a run-in label is present and the first sentence restates it ("Space usage. Space usage is an important concern.").

**Revision.**

- Before: Sample preparation. In this subsection we describe how the samples were prepared. Sample preparation followed several steps, which we now explain.
- After: Sample preparation. Tissue was fixed in formalin for 24 hours, then dehydrated through a graded ethanol series before embedding. We chose 24 hours because shorter fixation left the deeper layers unstable under sectioning.

**Do not apply when.** The passage is continuous argument rather than an inventory of parts — an introduction's territory-gap-occupation sequence, or a discussion that builds across paragraphs; chopping narrative into labelled bins destroys the through-line. Also where the venue's style forbids run-in heads.

---

## Advance a design paragraph by naming the defect of the thing you just described

**Move.** After presenting a solution, spend the next sentence on that solution's specific cost, and let the cost introduce the following step — so the paragraph moves problem, fix, new problem, fix, rather than as a list.

**Why it works.** Each new component arrives already justified, so the reader never stores an unmotivated design decision; the paragraph's spine is causal, which compresses in memory far better than an enumeration of equally-weighted options.

**Evidence.** 7 of the 12 papers read for dimension C.

**Exemplars.**

- "Although suffix array is theoretically efficient with O(n) construction work, the hidden constant is large. Thus, we use hashing-based solutions to replace SA for LCP queries to improve the performance in practice." — *ED*, 1 Introduction
- "However they come at a cost of high space usage—every element requires a node in the tree. This is particularly problematic for large-scale data analysis, since in large-systems memory is often the dominating cost." — *PacTree*, 1 Introduction
- "The strict AM-tree, however, requires maintaining the child pointers in each node, which may increase performance overhead in practice." — *am-tree*, 1 Introduction

**Violation signature.** A design or methods paragraph reading as a catalogue of coordinate additions — "We also implement X. We additionally use Y. We further add Z." — with no sentence stating what was wrong with X that made Y necessary. Tell-tale connectives: "also", "additionally", "furthermore" carrying the load where "however", "thus", "to address this" should be. Second symptom: each variant's motivation is deferred to the evaluation.

**Revision.**

- Before: We first used a keyword filter to select candidate documents. We also used a topic model. We additionally applied a manual review pass.
- After: We first used a keyword filter to select candidate documents. The filter admitted many documents that merely mentioned the terms in passing, so we added a topic model to score topical centrality. The topic model still could not separate the two closest topics, and we resolved those by manual review.

**Do not apply when.** The components genuinely are independent and coordinate — four unrelated datasets, three orthogonal robustness checks. Forcing a defect chain invents a dependency and implies each check repaired the last; use the cardinal-and-frame pattern there instead.

---

## End the paragraph on the consequence, not on the last detail

**Move.** Close a body paragraph with either the general lesson the local result licenses, or the specific cost the next paragraph will fix — never with a subordinate technicality, a citation dump, or a figure pointer.

**Why it works.** The final position is what the reader carries forward, so it either banks the paragraph's payoff or hands the next paragraph its starting problem; a paragraph ending on a detail forces the reader to reconstruct why it existed.

**Evidence.** 5 of the 12 papers read for dimension C.

**Exemplars.**

- "This experiment reaffirms the importance of work efficiency on practical performance for parallel algorithms." — *ED*, 6.2 Overall Performance on Synthetic Data
- "This speedup comes from the theoretical guarantees of the AM-tree that leads to shallower tree depths." — *am-tree*, 8.2 Update Throughput
- "While this is a seemingly natural requirement, it was not fully met in existing papers evaluating graph systems." — *p2307-wheatman*, 1 Introduction, Fairness of graph-container evaluation

**Violation signature.** Read the last sentence of each paragraph in isolation. If it is a parenthetical qualification, a bare cross-reference ("See Figure 4 for details."), a list of citations, or a detail subordinate to the sentence before it, the paragraph has no landing. In related-work paragraphs: three prior papers summarised and then a stop, with no sentence saying where the authors stand.

**Revision.**

- Before: Two earlier surveys used telephone sampling, and a third used an online panel. The panel study also reported a response rate of 43%, given in their appendix B.
- After: Two earlier surveys used telephone sampling, and a third used an online panel. All three drew from urban frames only, which is why we sample rural districts separately here.

**Do not apply when.** The paragraph is definitional or specification prose — a notation block, a list of supported operations, model parameters. Bolting an implication onto "we write A[i..j] for the i-th through j-th characters" is padding; those paragraphs may end when the specification ends.

---

## Announce the cardinality, then hold one frame per item

**Move.** State how many items there are before enumerating them, then give each in the same syntactic mould — same opening word class, same verb slot, same order of information — and reuse that mould when the items recur later in the paper. At paragraph scale the same discipline gives each item its own paragraph opening with a constant frame plus an ordinal.

**Why it works.** The count tells the reader how much stack to allocate; the repeated frame lets them diff the items instead of re-parsing each one; and the later reuse of the frame is what makes contributions and results legible as a matched pair.

**Evidence.** 9 papers across the C and D samples. Corpus-wide: 82/119 papers use an explicit "two/three <noun>:" enumeration frame — the rule. Ordinal-opened paragraph runs are far rarer (12/119, a floor because paragraph breaks are recovered heuristically) — the variant realisation.

**Exemplars.**

- "A dynamic-graph system is made up of two parts: the container and the programming framework." — *p2307-wheatman*, 1 Introduction
- "It runs in two phases: the first phase works on increase-key updates, and the second phase on decrease-key updates." — *closest*, 5 Parallel heap
- "Two major challenges exist to scale sketch-based approaches to billion-scale graphs. The first is the space." — *im*, 1 Introduction

**Violation signature.** A list whose items are grammatically heterogeneous — a noun phrase, then a full clause, then a gerund — or a list the reader must count themselves because no cardinal was announced. Also: contributions listed in one order and results reported in another or in different wording; consecutive paragraphs opening "We also evaluate…", "Another experiment examines…", so the reader cannot tell how many units remain.

**Revision.**

- Before: The pipeline cleans the transcripts, and there is also an alignment stage, after which segmentation into utterances happens. We also looked at the older cohort. Another analysis examined the younger cohort.
- After: The pipeline has three stages: the first cleans the transcripts, the second aligns them to the audio, and the third segments them into utterances. We ran it on two cohorts. We first examined the older cohort, where the effect held at full strength. We then examined the younger cohort, where it halved.

**Do not apply when.** The items are not parallel in kind — one conceptual, one methodological, one engineering — and a shared frame would make them look interchangeable; or the units are causally dependent (step two exists because step one failed), where ordinals flatten the dependency and the defect chain is right. Skip the cardinal when the list is open-ended ("among others"), and skip ordinals when n is two.

---

## Use "Note that" to fence a caveat or block a misreading — never to carry a load-bearing claim

**Move.** The marker does two jobs. Structurally, an edge case or scope limit that would break one-idea-per-paragraph is marked "Note that" and left inside the paragraph, and the main line resumes. Inferentially, directly after a definition, figure, or claim that invites a plausible over-reading, a "Note that" sentence states what does NOT follow, or which visible object is decoration.

**Why it works.** The marker tells the reader in advance that the sentence is parenthetical, so the caveat is registered without being mistaken for the thesis and without the topic change a new paragraph signals; and a misreading is corrected before it hardens, at the cost of one sentence, rather than being found by a referee three pages later.

**Evidence.** 13 papers, union of the C and H samples. Validated corpus-wide: "note that" fences a caveat in 88/119 papers (74%).

**Exemplars.**

- "Note that this is an upper bound—if the LCP length L is small, the cost can be significantly smaller" — *ED*, 3.3 BFS-B-Hash
- "Note that this sequence pre𝑖 is not maintained in our algorithm but is just used for illustration." — *lis*, 3 Longest Increasing Subsequence, discussion of Fig. 3
- "We note that our definition of the k-d grid cannot abstract all possible recurrences and computations, but it is sufficient to analyze the DP recurrences and algorithms shown in Section 7, 8 and appendices." — *DP*, 3 The k-d Grid Computation Structure

**Violation signature.** Three shapes. (a) Every caveat gets its own paragraph, so the argument is interrupted every three sentences. (b) Caveats are folded in unmarked, so the exception reads as the point. (c) The draft contains no sentence of the shape "X does not imply Y", "this is only used for illustration", "our definition does not cover Z" — and the reviewer's margin notes are all "does this mean that…?". Also watch for the marker wrapped around the paper's actual contribution, which reads as evasion.

**Revision.**

- Before: The effect was stable across all four sites. One site used a different assay lot, which we could not control for. The pooled estimate is therefore 0.34. Figure 2 shows the corpus with the confidence column alongside each label.
- After: The effect was stable across all four sites, giving a pooled estimate of 0.34. Note that one site used a different assay lot, which we could not control for. Figure 2 shows the corpus with the confidence column alongside each label. Note that the confidence column is shown only for illustration; the second pass never reads it.

**Do not apply when.** The caveat is a limitation of the contribution itself, or the sentence carries a step the argument depends on — demoting either to a marked aside hides what the reader most needs, and it belongs in an owned, unhedged sentence beside the claim. Also: more than about one marked aside per paragraph turns the prose into a hedge thicket, and the device keeps its force only while it reliably signals "here is a trap".

---

## Break the four-sentence norm on purpose with a one-or-two-sentence orienting paragraph

**Move.** Where a subsection or a run of dense paragraphs begins, stand a single sentence alone as its own paragraph, saying what the passage will do or what property is about to be unpacked.

**Why it works.** Against a median of four sentences per paragraph, a one-sentence paragraph is a marked event; the white space makes it a landmark the eye finds when scanning, without the weight of another numbered heading.

**Evidence.** 5 of the 12 papers read for dimension C. Corpus baseline: mean 4.77 sentences per paragraph, median 4, p90 10, across 10,893 paragraphs.

**Exemplars.**

- "We now describe the geometric graph construction algorithms that are currently provided by GeoGraph." — *geograph*, 2.1 Geometric Graph Construction
- "We now describe Golin et al.’s implementation of the sparse partition." — *closest*, 2.2 A Grid-Based Implementation of Sparse Partition
- "Algorithm Overview. We first present the high-level idea of our sketch compression algorithm." — *im*, 3 Sketch Compression

**Violation signature.** Uniform paragraph length throughout — every paragraph four to six sentences — so dense technical prose arrives with no visual entry point. The converse anti-pattern: short paragraphs everywhere, which spends the emphasis and leaves nothing marked.

**Revision.**

- Before: The interview protocol had three phases, which we describe here along with the coding scheme and the reliability checks. In the first phase, participants were asked to recall the incident in their own words for up to ten minutes.
- After: We now describe the three phases of the interview protocol.\n\nIn the first phase, participants were asked to recall the incident in their own words, without interruption, for up to ten minutes.

**Do not apply when.** The orienting sentence would only restate the heading directly above it ("3.2 Coding Scheme" followed by "We now describe the coding scheme."). It earns its place by adding scope, provenance, or a promise the heading does not carry. Do not scatter these: more than one per subsection and the marking stops meaning anything.
