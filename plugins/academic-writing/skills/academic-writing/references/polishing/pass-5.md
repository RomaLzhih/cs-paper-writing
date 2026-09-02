# Pass 5 — Action and weight

**Ask:** Where is the action in this sentence, what is performing it, and does every remaining word earn its place?

**Do not touch in this pass.** The subject slot is Pass 1's decision. When un-nominalising would change which noun is the subject ('Improvement of forecast accuracy was achieved through the aggregation of the panels' → 'Aggregating the panels improved forecast accuracy'), check that the new subject is still traceable to the previous sentence's tail; if it is not, keep the subject and change only the verb. Do not cut 'due to' before a noun (734 uses) — only the 'the fact that' wrapper. Do not cut nominalisations wholesale: the register runs 28.8 per 1,000 words and its commonest content nouns are nominalisations. Do not touch stance words here — hedges and intensifiers are Pass 6, and cutting them mid-compression produces flat over-claims.

20 patterns.

---

## Report the observation flat and hedge only the mechanism you infer for it

**Move.** Write the measurement or observed fact with no hedge at all, then hedge the explanation offered for it — and decide which by a single test: an explanation that follows deductively from the design of the thing being explained takes a flat "This is because...", while an explanation appealing to something the study did not measure takes "likely due to", "we believe the reason is", or "probably because".

**Why it works.** It separates what the paper establishes from what the paper guesses at exactly the seam where a sceptical reader draws that line, so the numbers keep their full weight while the story around them stays revisable. The inverted arrangement — soft numbers, hard causes — is the signature of a paper defending a result rather than reporting one.

**Seen in.** semisort, buildingblock, arxiv-2301.01356 (sampled from 8-10 papers for this sub-topic, not all 119)

- "The lower speedup for smaller input sizes is likely due to overhead of parallelism on smaller data." — *semisort*, Experiments

- "We believe the reason to be that, samplesort does not explicitly utilize L1 and L2 caches (the binary search, offset transpose, etc.) so most small-memory accesses are toward L3 cache." — *buildingblock*, Sorting experiments

- "This is because the radix sort is designed for sorting keys from a small range, and the 64-bit keys used in our experiments require too many rounds to sort." — *semisort*, Experiments

**Violation signature.** The hedges sit on the numbers and the causes are flat: "our method appears to be somewhat faster on most inputs, which is because the baseline wastes bandwidth." Concretely, look for (a) any "This is because" introducing a mechanism nothing in the paper observed or derived, and (b) any "seems/appears/somewhat/tends to" modifying a quantity the paper actually measured.

**Revision.**

- Before: Treatment households appear to save somewhat more on average, which is because the reminder raises the salience of the deadline.
- After: Treatment households save 4.2% more than controls (s.e. 1.1). We believe the reason is increased salience of the deadline, though the design does not separate salience from the information the reminder carries.

**Do not apply when.** The study was built to isolate the mechanism — an ablation, a manipulation check, a placebo arm — in which case the mechanism is itself a result and takes the same flat verb as the number. Equally, do not hedge an explanation that follows from the design of the object being explained (why a range-limited method loses on wide keys is not a conjecture).

<sub>Verifier: Survives measurement at 119 papers even though it was drawn from three. Flat 'This is because' 181 uses in 65/119 papers; a 12-sentence random sample of it introduces mechanisms deducible from the design of the object ('This is because the other three balancing schemes also need to store an extra field'), never an unmeasured guess. The hedged side is separately attested: 'likely due to/because' 22 uses in 17 papers, 'we believe' 196 in 70. Hedges on measured quantities are correspondingly rare ('somewhat' 18 uses/14 papers, mostly on 'somewhat surprisingly' and on proofs, not on numbers). All </sub>

---

## Use "however" to name the cost of what you just described; use "in contrast" only when a second, named subject is measured on the same stated dimension

**Move.** "However" continues on the same referent: the previous sentence describes a method, result, or property, and the "however" sentence names what it fails at — its subject is that same thing or an aspect of it, and it needs no second item. Use "in contrast" when you set a second side beside the first and restate the same property for it, so the reader can lay the pair down side by side; that second side may be a named alternative, a different condition, or a different regime. Before writing "in contrast", check that the reader can point at both sides and at the one property on which they differ; if there is no second side, the word is "however".

**Why it works.** The cheaper word is the far more frequent one: "however" runs to 1,022 uses across 118 of 119 papers, while "in contrast" appears 106 times. That ratio is the point. "However" makes no promise beyond a turn; "in contrast" promises a comparison, and an unpaid promise sends the reader back up the page hunting for a comparand that was never named. Conversely, using "however" where two rivals are genuinely being ranked reads as a change of topic rather than a comparison, and the reader loses the axis.

**Seen in.** psi, p2307-wheatman, kcore, am-tree, lis, xu-ppcsr-alenex-21 (sampled from 8-10 papers for this sub-topic, not all 119)

- "Almost all existing Orth-trees [17, 39, 40, 50, 65] use spacefilling curves (SFCs) to accelerate construction and updates. However, simply computing and sorting the SFC codes of the points already requires several passes of reading and moving all data, which is time-consuming." — *psi*, Introduction

- "The original GBBS specification required the datastructure developer to implement several neighborhood operators. In contrast, BYO requires them to implement only one." — *p2307-wheatman*, Sec. 4.4, Connecting BYO to GBBS

- "The bottleneck is that a PaC-tree enforces a total order on points according to an SFC, which is overly costly. In contrast, P-Orth trees and Pkd-trees leave points in the leaves unsorted." — *psi*, Sec. 4, SPaC-tree design

**Violation signature.** An "In contrast" sentence whose subject is the same entity as the previous sentence's, or one where the contrasted property is stated for only one of the two sides so the reader must supply the missing half. The reverse tell: "However" introducing a rival's different behaviour, where the reader was braced for the limitation of the thing just described.

**Revision.**

- Before: Cohort studies track exposure prospectively and avoid recall bias. In contrast, they are expensive and slow to yield endpoints.
- After: Cohort studies track exposure prospectively and avoid recall bias. However, they are expensive and slow to yield endpoints. Case-control designs, in contrast, reach endpoints immediately but must reconstruct exposure from recall.

**Do not apply when.** When the second sentence supplies a replacement for a rejected option rather than a limitation or a comparison — that is "instead", and neither word here fits. When a genuine two-item taxonomy is already written in matched grammatical shapes, the parallelism carries the contrast and "in contrast" claims credit for work the syntax did. And a second item does not compel "in contrast": if you deliver it as a fronted frame, medial however does the same job ("In the placebo group, however, titres stayed at baseline") — reserve "in contrast" for when you want the two sides read as a matched pair.

<sub>Verifier: The core is confirmed by direct sampling, not just frequency. Eighteen random "However," sentences with their predecessors: the subject continues the same referent and the sentence names its cost ("the fetch-and-add based implementation performs poorly", "the hidden terms in the bounds are large", "Fw-Bw does not provide sufficient parallelism"). Twelve random "In contrast," sentences: a second side is named and the same property restated. Frequency ratio holds (however 1,022 in 118/119 papers; in contrast 130 in 53 — the pattern's 106 is a slight undercount, immaterial). All three exemplars g</sub>

---

## Fold the rejected option into the sentence as "instead of X"; save a stand-alone "Instead," for a rejection you have already stated outright

**Move.** When you replace one option with another, put the rejected option in a prepositional phrase inside the sentence that states your choice — "Instead of maintaining the full mapping, we keep …" — so the main clause is entirely about what you did and the negative never occupies a sentence of its own. Reserve the sentence connective "Instead," for the case where the previous sentence has said in so many words that the alternative is unsatisfactory; "Instead," then points back at that rejection and supplies the substitute.

**Why it works.** Of 491 uses of "instead", 311 are the preposition ("instead of", plus fronted "Instead of") and only 62 are the sentence connective "Instead,". The preposition costs the reader nothing and gets the decision into the main clause; the connective form spends one sentence on what you did not do and a second on what you did. And the corpus's connective uses come attached to an explicit prior rejection, which is what gives "Instead," an antecedent to point at — without one, the reader has to reconstruct which alternative is being replaced.

**Seen in.** psi, ch, PacTree, kcore, xu-ppcsr-alenex-21 (sampled from 8-10 papers for this sub-topic, not all 119)

- "First, instead of pre-calculating SFC values before sorting, we compute them when the points are first touched in sorting, which saves one round of reads and writes to associated arrays." — *psi*, Sec. 3, construction

- "Instead of adding them directly to the CSR of the overlay graph, we first use E+ to buffer them." — *ch*, Sec. 4, shortcut insertion

- "Although one could deal with in-place and functional updates separately, this is not attractive. Instead, we designed a simple approach to handle both cases using the same code" — *PacTree*, Sec. 7, Implementation

**Violation signature.** A sentence opening "Instead," whose predecessor only describes the alternative neutrally and never says it was rejected, so the reader must guess what is being replaced. Also a two-sentence pair in which the first sentence exists solely to state a negative that could have been a four-word phrase.

**Revision.**

- Before: Prior surveys ask respondents to recall spending over the past year. Instead, we use transaction records.
- After: Instead of asking respondents to recall spending over the past year, we use transaction records.

**Do not apply when.** When the rejected option needs its own explanation — a clause or two on why it fails — folding it in pushes the main verb far to the right, and this register reaches the subject-verb bond fast (median five words before the main verb, p75 of nine). Then state the rejection in its own sentence and let "Instead," open the next one.

<sub>Verifier: Every number checks out and the hard part of the claim survives a direct test. Measured: 455 uses of "instead", of which 306 are prepositional (265 mid-sentence "instead of" plus 41 fronted "Instead of") and 60 are the sentence connective "Instead," — against the pattern's 311 and 62. The non-obvious half is the antecedent condition, and I sampled fourteen random "Instead," sentences with their predecessors: all fourteen predecessors state an explicit rejection or impossibility ("we cannot afford to keep all unfinished iterations active", "it would require significant work to re-implement them</sub>

---

## Put the acting noun in the subject slot; keep "there is/are" only for claims about existence itself.

> Narrowed after corpus measurement contradicted the original claim.

**Move.** When the real content is that some things have a property or do something, promote those things to grammatical subject and drop the existential frame together with its relative pronoun. Keep "there is/are/exist(s)" when the sentence asserts existence, non-existence, or a count -- including the theorem form ("There is an algorithm that computes...") and the survey form ("There are several methods that take linear time [refs]"), both of which this corpus writes. When existence is the point and the noun is yours to place, the corpus will also postpose the verb: "faster algorithms exist for certain special cases".

**Why it works.** The expletive spends the sentence's first three words on a dummy subject and parks the acting noun behind "that", so the reader reaches the verb late; the corpus's median is 5 words before the main verb. The digest counts "there is/are X that" once in 1.1M words — the strictest near-absence it records.

**Seen in.** scc, RadiusStepping, joinable, ParGeo (sampled from 8-10 papers for this sub-topic, not all 119)

- "Many other fundamental problems in CS use SCC as an important primitive, such as graph matching [42], topological sort [26, 87], graph contraction [31], and code analysis [86]." — *scc*, Introduction

- "This is the best theoretical running time for general nonnegative edge weights although faster algorithms exist for certain special cases." — *RadiusStepping*, Introduction

- "many balancing schemes for binary trees have been widely studied and are widely used, such as AVL trees [4], red-black trees [10], weight-balanced trees [52], splay trees [57], treaps [56], and many others." — *joinable*, Introduction

**Violation signature.** "There is / There are / There exist(s)" + noun phrase + "that/which" + content verb, in a sentence that is not asserting existence, non-existence, or a count. Two-step test: (1) delete the frame and the relative pronoun; (2) ask whether the remainder still claims the same thing. "There are several surveys that report a decline" -> "Several surveys report a decline" survives both steps, so cut. "There is an estimator that attains the bound" -> "An estimator attains the bound" survives step 1 but fails step 2, because it turns an existence claim into a generic one; keep the frame.

**Revision.**

- Before: There are several household surveys in the literature that report a decline in precautionary saving after 2008.
- After: Several household surveys report a decline in precautionary saving after 2008.

**Do not apply when.** Existence, non-existence, or a count is itself the claim -- the corpus writes "there is/are/exist no|not" 184 times in 77/119 papers and "There are two/three/several/many..." 94 times in 55 papers, and keeps the expletive in concessive frames (ParGeo: "While there exist numerous libraries for computational geometry, most of them are not designed for parallel processing") and with mass nouns and no relative clause. Correct the digest's figure when you cite it: its count of 1 comes from a one-word window; measured over all 119 papers with a 1-6 word window, "there is/are/exist(s) X that/which" appears 108 times in 58 papers, and 27 of those are sentence-initial, in 21 papers. The frame is rationed, not unattested -- do not tell a writer the construction is absent from the register.

<sub>Verifier: Direction is right but the evidence is overstated at its core. The digest's "there is/are X that = 1 use" is a one-word-window artifact: my regex `there (is|are) \w+ that` reproduces it (2 hits), but allowing 1-6 words between verb and relative gives 108 hits in 58/119 papers, and sentence-initial `There is/are/exist(s) X ... that/which` gives 27 hits in 21/119 papers. So the pattern's own honest correction (~35) is itself an undercount, and calling this "the strictest near-absence the digest records" is false. Worse, the delete-test misfires on the corpus's dominant surviving use: "There is a</sub>

---

## Explain with "This is because" plus a finite clause; delete every "the fact that" and "the reason ... is" wrapper.

**Move.** State the result, stop the sentence, then open a new short sentence with a bare pointer subject and "is because", followed by a full clause with its own subject and verb. The explanation gets its own sentence rather than a nominal bolt-on.

**Why it works.** "due to the fact that" appears 11 times in 1.1M words and "The reason for this is" zero times, while "This is because" appears 181 times and occurs in every one of the eight papers I read. The wrapper costs four to six words announcing that a cause is coming; "This is because" costs three and lands on the cause.

**Seen in.** RadiusStepping, joinable, PIP, kdtree, ParGeo, scc, full, soda2015-final (sampled from 8-10 papers for this sub-topic, not all 119)

- "Evidently, both heuristics achieve similar results on the road map and 2D grid. This is because road maps and grids are relatively regular, in fact almost planar." — *RadiusStepping*, Experimental Analysis

- "Generally speaking, WB trees have the best performance among the four tested balancing schemes. This is because the other three balancing schemes also need to store an extra field as the balancing information (e.g., the height for AVL trees)." — *joinable*, Experiments

- "This is because even if we have an infinite number of processors, no more than S of them can do useful work simultaneously." — *PIP*, Preliminaries (parallel in-place models)

**Violation signature.** The words "fact" or "reason" appearing with no informational job beyond announcing that a cause follows: "due to the fact that", "owing to the fact that", "The reason for this is that", "This is attributable to the fact that", "on account of the fact that".

**Revision.**

- Before: Uptake was lower in the treated cohort, due to the fact that the receptor is downregulated within hours of the first dose.
- After: Uptake was lower in the treated cohort. This is because the receptor is downregulated within hours of the first dose.

**Do not apply when.** "Due to" followed by a noun is normal and frequent (734 uses: "due to the overhead of", "due to the use of"); cut only the "the fact that" wrapper, not the preposition. And when the cause compresses to a short noun phrase, an appended "because of X" or "due to X" beats a new sentence — the fresh-sentence form earns its place when the cause needs its own subject and verb. "The reason is that" itself survives 26 times, so it is a weak preference, not a ban; "The reason for this is that" is the padded form that is absent.

<sub>Verifier: Every number I could re-derive over all 119 papers holds: "due to the fact that" 11 uses in 9 papers (matches the digest row exactly), "owing to the fact that" 0, "The reason for this is" 0, "This is because" 165 in 62/119 papers (pattern says 181; within tokenisation noise), "The reason is that" 21 (pattern says 26), "due to" 764 in 109/119 papers (pattern says 734), "because of" 143. The do-not-apply carve-out is the important part and it is accurate: "due to" + noun is one of the most frequent constructions in the corpus, so the rule genuinely targets the six-word wrapper and not the prepos</sub>

---

## Give every observation an owner — "Note that", "We note that", "Table 3 shows" — never an agentless "It is / It can be" frame.

> Narrowed after corpus measurement contradicted the original claim.

**Move.** When directing attention, name the agent doing the directing (you) or the thing doing the showing (the figure, the table, the result), then go straight into the that-clause. Delete "It is/can be" + adjective or participle + "that", and delete a bare "Clearly," or "Obviously," outright.

**Why it works.** "Note that" (545) and "We note that" (404) and "Figure/Table N shows/reports/presents" (333) dominate; against them, "It should be noted that" appears 0 times in 1.1M words, "It can be seen" 6, "It is clear that" 1, "It is obvious that" 1. The expletive frame adds four words and removes the one piece of information — who noticed — that the reader can act on.

**Seen in.** scc, kdtree, joinable, soda2015-final, ParGeo, PIP (sampled from 8-10 papers for this sub-topic, not all 119)

- "Fig. 1 shows that existing SCC algorithms work well for certain social networks but perform badly on other graphs." — *scc*, Introduction

- "We note that the major technical difficulty in VGC and local search is to handle the nondeterminism in generating the next frontier" — *scc*, Introduction

- "Our results show that the theoretical guarantee for Pkd-trees (Thm. 3.3 and 4.1) indeed allows for better cache-efficiency and leads to good performance in practice." — *kdtree*, Experiments

**Violation signature.** A sentence opening "It should be noted that", "It can be seen that", "It is worth mentioning that", "It is clear/obvious/evident that", or a sentence-initial "Clearly," / "Obviously," attached to a claim for which no reason has yet been given.

**Revision.**

- Before: It should be noted that it is clear from Table 2 that the effect is confined to the youngest quartile.
- After: Table 2 shows that the effect is confined to the youngest quartile.

**Do not apply when.** "It" is a genuine placeholder for an infinitive that carries content: "it is easy/possible/hard/difficult/important/sufficient to" appears 136 times in 66/119 papers, and "It is easy to see that" 30 times -- always where a short derivation follows, never as a claim of self-evidence. "It is worth noting/mentioning that" survives 13 times in 13 papers: rationed, not forbidden. And correct the usual defence of "Clearly": it is not normally paired with a stated reason -- of 44 sentence-initial uses, only 7 carry a "since"/"because" in the same sentence -- but about 40 of the 44 sit inside a proof or derivation, where the surrounding argument is the reason. So the test is context, not company: inside a derivation the word is normal; outside one, asserting self-evidence with no reason anywhere nearby is the defect.

<sub>Verifier: The core is one of the strongest results in this topic and survives at 119 papers: "Note that" 545 (92/119), "We note that" 347 (73/119), "(Figure|Fig.|Table|Tab.) N shows/reports/presents/illustrates" 295 (83/119), "We observe/see/find/show/note/remark" 700 (103/119) -- against "It should be noted that" 0, "It is clear that" 1, "It is obvious that" 1, "it can be seen" ~0 ("it can be shown/verified/observed" 9). One factual claim inside do_not_apply_when is wrong and has to go: it says clearly/obviously is "almost entirely inside proofs and paired with an explicit since/because in the same sen</sub>

---

## On a magnitude claim of your own, put the measured number in the sentence

> Narrowed after corpus measurement contradicted the original claim.

**Move.** When a sentence claims a magnitude your own work measured, put the quantity -- with its range -- into that sentence. The degree adverb may stay or go; what must not stay is a headline magnitude claim with no number in or beside it. The corpus frequently writes both together ("very good speedups on most datasets, achieving speedups of 5-33x"), so the number is the addition, not a swap.

**Why it works.** "extremely" appears 32 times in 1.1M words, "a lot of" 8, "really" 1, "very fast/efficient/effective" 11 — while "N× faster/slower/better" appears 787 times and "up to N×" 223. The number is usually no longer than the intensifier plus the hedge it invites, and unlike the intensifier it can be checked.

**Seen in.** kdtree, scc, ParGeo, joinable (sampled from 8-10 papers for this sub-topic, not all 119)

- "For construction, the Pkd-tree is the fastest in all tests, which is 8.26–12.5× faster than Log-trees, 8.20–11.1× faster than BHL-trees, and 39.1–363× faster than CGAL." — *kdtree*, Experiments

- "For example, on the Hyperlink12 [75] graph with billions of edges, Tarjan’s SCC algorithm takes more than half an hour (see Tab. 3) to finish." — *scc*, Introduction

- "On 36 cores with two-way hyper-threading, our fastest convex hull algorithm achieves up to 44.7x self-relative parallel speedup and up to 559x speedup against the best existing sequential implementation." — *ParGeo*, Abstract

**Violation signature.** "extremely", "really", "a lot of", "hugely", "dramatically", or an unquantified superlative, carrying a claim about your own result for which a number exists elsewhere in your paper but nowhere in or beside that sentence.

**Revision.**

- Before: Adoption in the treated villages was extremely high relative to the control villages.
- After: Adoption reached 64% in the treated villages, against 19% in controls.

**Do not apply when.** No number exists, or the magnitude is incidental to the point. Do not extend the rule to "very": 411 uses in 100/119 papers (very similar, very large, very simple, very small) make it ordinary register, not a defect. The same goes for hedged comparatives -- "significantly/substantially/much/considerably + comparative" appears 530 times in 104/119 papers -- which are fine wherever the exact size is not the point, including about a baseline's already-cited defect (kdtree: "making it much slower than other implementations"). The rule targets an unquantified magnitude claim about your own contribution, not degree words as a class, and it does not license a results paragraph stuffed with numbers the reader cannot hold.

<sub>Verifier: Half the violation signature is contradicted by the corpus. It flags "'very' + evaluative adjective", but "very" appears 411 times in 100/119 papers and "very + adjective" from the common list 201 times in 80/119 papers (very similar 45, very large 41, very simple 31, very small 25) -- it is ordinary register here, not a defect, and a rule that flags it would fire on 84% of these papers. The corpus also refutes the "delete the degree adverb and put the quantity in its place" mechanic: it routinely writes both at once -- DBSCAN, "Our implementations obtain very good speedups on most datasets, a</sub>

---

## Open a purpose clause with bare "To …", never "In order to …".

**Move.** Front the purpose as a bare infinitive phrase, comma, then a main clause with a real subject. The same cut applies to "for the purpose of" and "with the aim of".

**Why it works.** Sentence-initial "In order to" appears 19 times in 1.1M words against 1,168 sentence-initial "To + verb" openers — roughly 60:1. Six of the eight papers I read use "in order to" zero times in any position. "For the purpose of" appears 11 times. "In order" is two words that change nothing about meaning.

**Seen in.** ParGeo, scc, kdtree, joinable, PIP, soda2015-final, RadiusStepping, full (sampled from 8-10 papers for this sub-topic, not all 119)

- "To demonstrate the efficiency of our proposed algorithms and library, we perform a comprehensive set of experiments on synthetic and real-world geometric data sets" — *ParGeo*, Introduction

- "To do this, we propose a novel idea referred to as the vertical granularity control (VGC) optimization." — *scc*, Introduction

- "To tackle this challenge, we propose an efficient parallel SCC implementation using a new parallel reachability approach." — *scc*, Abstract

**Violation signature.** A sentence beginning "In order to", "In order for X to", "For the purpose of", or "With the aim of".

**Revision.**

- Before: In order to isolate the demand channel, we instrument local prices with the 2013 tariff schedule.
- After: To isolate the demand channel, we instrument local prices with the 2013 tariff schedule.

**Do not apply when.** Mid-sentence, where "in order to" occasionally separates a purpose from a preceding infinitive that would otherwise read as coordinate — the corpus keeps about 95 mid-sentence uses. And do not convert every sentence into this shape: purpose-infinitive openings account for only 2.2% of sentences, against 46.4% bare-subject openings, so the frame is for the sentence that genuinely answers "why".

<sub>Verifier: Re-measured over all 119 papers and the ratio holds: sentence-initial "In order to" 23 uses in 12/119 papers, against 1,185 sentence-initial "To + verb" openers in 117/119 papers -- roughly 50:1, and only a tenth of the papers ever open a sentence this way. Total "in order to" is 114 in 47/119 papers, so mid-sentence use is about 91, which matches the pattern's stated ~95 and is exactly what its do_not_apply_when protects; "for the purpose of" 11 in 6 papers, "with the aim of" 0, "so as to" 6 -- all confirmed rare. The carve-out is the part that keeps this honest twice over: it protects mid-se</sub>

---

## Write the action as an -ing form, not as a noun followed by "of"

**Move.** When a process has to occupy a noun slot — subject, object, or object of a preposition — spell it as VERB-ing plus that verb's own object ("by applying both techniques", "Finding n objects ... requires"), not as "the DEVERBAL-NOUN of" plus that object ("by the application of both techniques", "The finding of n objects ... requires"). The action stays a verb form even when it is doing a noun's job.

**Why it works.** The gerund keeps the verb's arguments welded to the verb, so the reader receives the action and the thing acted on as one unit; the deverbal noun forces an article and an "of", pushes the object one link further away, and leaves a slot for a second "of" behind it. Measured over the full 1.1M words: after by/for/after/before/without, gerund forms outnumber "the NOUN of" roughly 1,936 to 15. Pair by pair: "by using" 175 vs "by the use of" 0; "for computing" 136 vs "for the computation of" 0; "by applying" 64 vs "by the application of" 0; "by sorting" 8 vs "by the sorting of" 0. In subject position the same asymmetry holds: sentence-initial VERB-ing subjects 1,491 vs "The <nominalisation> of ..." subjects 34.

**Seen in.** geometry, parlayann, pbtree, im, ROSE, pimtree (sampled from 8-10 papers for this sub-topic, not all 119)

- "We can obtain parallel write-efficient randomized incremental algorithms by applying both techniques together." — *geometry*, Section 1, Introduction

- "Finding n objects in a configuration of size n requires O(n log n) reads but only O(n) writes." — *geometry*, Section 1, Introduction

- "We provide new general techniques for building ANNS graphs in parallel, such as prefix doubling and batch updates." — *parlayann*, Section 1, Introduction

**Violation signature.** A preposition (by / for / after / before / without / through) followed by "the" + a noun ending in -tion, -ment, -ance, -sion or -al + "of". Or a sentence whose subject is "The <-tion noun> of X" where the same clause could have begun "<Verb>ing X". Read the sentence aloud: if the first verb you meet is "is", "was" or "requires" and the real action is sitting in front of it as a noun, the pattern is violated.

**Revision.**

- Before: Improvement of forecast accuracy was achieved through the aggregation of the regional panels.
- After: Aggregating the regional panels improved forecast accuracy.

**Do not apply when.** The event itself needs a predicate of its own — "After the computation of both subtasks is finished, ..." — because a gerund cannot take "is finished"; the noun is an established term of art rather than a paraphrase of a verb; or the event needs a determiner or quantifier ("each removal", "the first insertion"). Headings and cited titles conventionally use the noun style. Also keep the gerund phrase short: in the corpus's 1,090 gerund-subject sentences the main verb still arrives by word 6 at the median (p75 10), matching the corpus-wide median of 5, so a gerund subject that runs ten-plus words before its verb trades a nominalisation fault for a delayed-verb fault — demote it to a "by"/"when" clause instead.

<sub>Verifier: Direction confirmed emphatically at 119 papers, but the quoted figures do not reproduce and one guardrail is missing. My counts: prep+VERB-ing 3,619 vs prep+the+NOM+of 68 (pattern claims 1,936 vs 15); by using 162 / by the use of 0; for computing 120 / for the computation of 0; by applying 61 / by the application of 0; by sorting 7 / by the sorting of 0. The 68-item residue is mostly non-action nouns (by the definition of 13, for the performance of 4, for the existence of 1), so the real action-nominalisation residue is a handful. I also confirmed the object slot, which the pattern asserts but</sub>

---

## Keep the paper's own moves as single finite verbs

**Move.** Write the acts the authors perform — presenting, showing, comparing, assuming, defining, evaluating — as one finite verb with "we" or a section as subject. Reach for a light verb plus a nominalisation of that same act ("we perform a comparison of", "an evaluation was carried out") only when the noun carries something the verb cannot; in this corpus the periphrasis runs at roughly one use per sixty of the plain verb, so treat it as a last resort rather than an equal option.

**Why it works.** The move-verb inventory in this corpus is small, plain and monotransitive: use (1,368), show (583), assume (466), note (406), present (372), consider (236), define (229), call (220), compare (208), describe (180), propose (179), discuss (169), provide (158), introduce (158), prove (108), observe (102), evaluate (97), study (96), denote (91), analyze (88), omit (78). The periphrastic alternatives are absent: "we make a comparison" 0, "conduct an analysis" 0, "perform an analysis" 0, "carry out" 0, "make a decision" 0, "give a description" 0, "provide a description" 0, "with the aim of" 0, "plays an important role" 0. Honest qualification: the corpus does not ban the form outright — "make/makes/making use of" survives at 52 uses — but "use" itself appears about 3,000 times, so the periphrasis runs at roughly 1 in 60. Treat it as a last resort, not as forbidden.

**Seen in.** hdbscan, im, pimtree, xu-alignment-ipdps-25, parlayann (sampled from 8-10 papers for this sub-topic, not all 119)

- "We introduce a new notion of well-separation to reduce the work and space of our algorithm for HDBSCAN" — *hdbscan*, Abstract

- "We compare PaC-IM with state-of-the-art parallel IM systems on a 96-core machine with 1.5TB memory." — *im*, Abstract

- "Section 3 presents our parallel well-separated pair decomposition approach and uses it to obtain parallel algorithms for the two problems." — *hdbscan*, Section 1, Introduction (roadmap)

**Violation signature.** A verb of doing (perform, conduct, carry out, undertake, make, provide, give) whose object is an abstract noun naming the very act — analysis, comparison, evaluation, examination, investigation, description, assessment — usually followed by "of". Test: can the noun be turned back into the sentence's main verb without losing anything? If yes, the light verb is padding.

**Revision.**

- Before: In this section we carry out a comparison of the two estimators and provide a description of their finite-sample behaviour.
- After: In this section we compare the two estimators and describe their finite-sample behaviour.

**Do not apply when.** The noun names the deliverable rather than the act. "We provide a proof", "we give a bound", "we present an implementation" hand the reader an object that outlives the sentence; the noun is the thing, not a disguised verb, which is why "provide a/an/the NOUN" survives ~300 times with objects like an algorithm, an interface, a toolkit. Leave it too when the noun carries a modifier the verb cannot ("a comprehensive set of experiments"), and do not flag a light verb whose object is a real thing rather than a copy of the verb — the corpus's eight uses of "carry out" are all of that kind ("a parallel search is carried out on the CPU"), as are its sixty uses of "we perform" (experiments, queries, a parameter sweep).

<sub>Verifier: Well supported, but the move says "Never" while the pattern's own why says the corpus does not ban the form — an internal contradiction that also mildly overstates the measurement. Re-measured: make a comparison 0, conduct an analysis/study/comparison/evaluation 2, perform an analysis/comparison/evaluation 1, make a decision 0, give/provide a description 0, with the aim of 0 — all confirmed near-zero. Three small errors: "carry out" is 8 (6 papers), not 0; "plays an important role" is 1, not 0; "make/makes/making use of" is 46, not 52. Crucially, all 8 "carried out" uses take a real object ("a</sub>

---

## Give a consequence a transitive verb, not "leads to a <nominalisation>"

**Move.** When one fact causes another, use a transitive verb whose object is the affected thing: reduces, saves, improves, limits, avoids, guarantees, ensures, yields, means. Do not route the consequence through "leads to a reduction in X" or "results in an improvement of X".

**Why it works.** In 1.1M words the periphrastic forms are at zero: "leads to a reduction" 0, "results in a reduction" 0, "leads to an improvement" 0, "results in an improvement" 0, "gives an improvement" 0, "achieves a reduction" 0. "leads to" (208) and "results in" (242) are themselves common, but their objects are genuine result-objects — a contradiction (10), the following theorem (8), a shallower tree, a query cost — never a nominalised copy of the verb the writer wanted. The same preference shows in what a bare "This" subject takes: means 134, gives 106, indicates 62, leads 51, allows 34, implies 26, guarantees 16, makes 15, avoids 13, ensures 12, reduces 8. The transitive verb also carries the number with it, which the nominal form buries in a prepositional phrase.

**Seen in.** hdbscan, parlayann, pimtree, im, ROSE (sampled from 8-10 papers for this sub-topic, not all 119)

- "This optimization reduces the total number of BCCP calls." — *hdbscan*, Section 3, EMST algorithm

- "This optimization significantly saved space and in turn improved parallelism with no drop in QPS for a given recall." — *parlayann*, Section 4, algorithm-specific optimizations

- "This approach limits the contention on each node, avoiding load imbalance." — *pimtree*, Section 2, background on prior solutions

**Violation signature.** "leads to", "results in", "gives rise to", "brings about" or "achieves" followed by a/an/the plus a noun that names a change — reduction, improvement, increase, decrease, degradation, speedup — with the magnitude, if any, hanging off it in an "of" or "in" phrase. The test is that the noun is a copy of the verb the sentence wanted: "leads to a reduction in X" where "reduces X" was available. Not a hit when the object is a genuine result-object (a contradiction, a theorem, a running time, a data structure).

**Revision.**

- Before: The new subsidy leads to a reduction in the drop-out rate of roughly four percentage points.
- After: The new subsidy cuts the drop-out rate by roughly four percentage points.

**Do not apply when.** The consequence really is an object rather than a process — a contradiction, a theorem, a data structure, a named condition — in which case "leads to" is the right verb; that is how all 17 of the corpus's near-miss uses work. Keep the nominal form when the change itself must be quantified as a thing and then predicated ("the four-point reduction is concentrated in urban districts"). And do not apply this to reporting an observation rather than asserting a cause: the corpus writes "we see a steady increase in the running time" and "we observe a small decrease in running time", where the noun names what was seen and no causal verb is being replaced.

<sub>Verifier: The core is the strongest evidence in this topic and reproduces exactly: leads to a reduction 0, results in a reduction 0, leads to an improvement 0, results in an improvement 0, gives an improvement 0, achieves a reduction 0, results in a/an X increase|decrease|reduction|improvement|degradation|speedup 0 — across 1.1M words. Meanwhile leads to 386 and results in 357 are common, and I inspected every one of the 17 hits of "leads to / results in + a/an + -tion|-ment|-ance|-ing": all take genuine result-objects (a contradiction ×13, a situation, a running time, an approximation), never a nominal</sub>

---

## Re-open on a category noun, not on a nominalisation of the verb you just used

> Narrowed after corpus measurement contradicted the original claim.

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** To make the previous sentence's action the subject of the next one, label it with a generic category noun — This step, This approach, This process, This optimization, This idea, This technique, This observation — rather than nominalising the specific verb you just wrote ("This computation of ...", "This partitioning ..."). The category noun classifies the previous move as well as pointing at it. What the new subject then does is free: in the corpus these openers take "is" as often as any content verb.

**Why it works.** This is the corpus's actual answer to "turn a process into a noun so it can be the next subject": it nominalises the KIND, not the verb. Counts: This step 52, This approach 50, This process 33, This optimization 21, This idea 14, This technique 11, This observation 6 — 187 in all — against This construction 3, This decomposition 2, This computation 1, This traversal 1, This transformation 1, This insertion 0, This partitioning 0 — 8 in all. The category noun does two jobs the nominalisation cannot: it classifies the previous move, telling the reader whether it was a mere step, a real optimisation, or only an observation; and because it does not repeat the verb, it leaves the verb slot free for the consequence. Corpus-wide, "This/These + noun" runs 1,799 against 915 bare demonstrative subjects, so carrying a noun is the default.

**Seen in.** hdbscan, parlayann, geometry, pimtree, im (sampled from 8-10 papers for this sub-topic, not all 119)

- "Our implementation only computes the BCCP between a pair if their points are not yet connected in the spanning forest generated so far." — *hdbscan*, Section 3, EMST algorithm (sentence preceding "This optimization reduces ...")

- "This optimization reduces the total number of BCCP calls." — *hdbscan*, Section 3, EMST algorithm

- "This approach requires linear writes, O(n log n) reads and polylogarithmic depth." — *geometry*, Section 5, k-d tree construction

**Violation signature.** Two consecutive sentences where the second opens "This/The <noun formed from the verb of the first sentence>" — "We re-weighted ... This re-weighting ...", "We partition ... This partitioning ...". The giveaway is the same verb appearing twice, once as a verb and once as a noun. Do not use the following verb as evidence: a copula after the demonstrative is normal here ("is" is the commonest verb in this slot in the corpus).

**Revision.**

- Before: We then re-weighted the sample by inverse propensity. This re-weighting of the sample is what removes the selection bias.
- After: We then re-weighted the sample by inverse propensity. This step removes the selection bias.

**Do not apply when.** The previous sentence introduced a named operation you will refer to again by that name — then use the name, not a category label. Do not reach for a demonstrative at all when nothing needs carrying forward: 46.4% of sentences open on a bare subject and only 6.5% on a demonstrative, so a run of "This step ... This approach ... This process ..." is its own defect. And do not treat a copula in the new sentence as a symptom needing repair.

<sub>Verifier: The noun half of this pattern is the best-evidenced finding in the topic, and I confirmed it is not a base-rate artifact — the decisive test the pattern did not run. Controlling for how common each word is: construction occurs 813 times but "This construction" only 3 (0.37%); computation 880 / "This computation" 1 (0.11%); insertion 638 / "This insertion" 0; partitioning 245 / 0; traversal 224 / 1 (0.45%). Against category nouns: step 1395 / "This step" 50 (3.58%); approach 905 / 49 (5.41%); optimization 385 / 19 (4.94%); observation 120 / 6 (5.00%). A ten-fold difference in demonstrative-subj</sub>

---

## Keep the nominalisations you can count or name; cut the ones that duplicate the clause's verb

**Move.** Deverbal nouns are the register's normal vocabulary — 28.8 per 1,000 words, and the commonest content nouns in this corpus are nominalisations — so do not strip them on sight. Keep one when the paper would genuinely count or index those events ("each non-self-edge removal", "the first insertion", "three passes") or when the noun is a defined term you will use again by name. Cut it when un-nominalising leaves the clause a perfectly good verb and loses nothing: "performs the initialization of the array" becomes "initializes the array".

**Why it works.** The register is emphatically not nominalisation-free — 28.8 per 1,000 words, and the commonest content nouns in the corpus are nominalisations (implementation 1,404, operations 1,230, computation 880, construction 813, insertion 639). So the editorial rule cannot be "use fewer". What separates the working ones is that they denote discrete, enumerable events or defined terms, which is exactly what lets them take determiners, be counted, be plural, and become the subject of a real verb. The failing ones sit as the object of a weak verb and add an article and an "of" to a clause that already had a perfectly good verb: "has the ability to" 0, "provides support for" 0, "is capable of" 1 across 1.1M words.

**Seen in.** hdbscan, xu-alignment-ipdps-25, parlayann, im, pimtree (sampled from 8-10 papers for this sub-topic, not all 119)

- "Each non-self-edge removal splits a cluster into two, which become the two children of the cluster in the dendrogram." — *hdbscan*, Section 2, Preliminaries

- "The edge labeled on an internal node is the edge whose removal splits a cluster into the two clusters represented by its children." — *hdbscan*, Section 4, dendrogram construction

- "The process of computing the updated cost using values from the current row and incorporating insertions is called insertion propagation." — *xu-alignment-ipdps-25*, Section II.C, Dynamic-Programming Approach

**Violation signature.** A deverbal noun sitting as the object of a weak verb — is, has, provides, performs, undergoes, experiences — usually with "of" behind it, in a clause whose real verb is inside that noun. Two tests, and it must fail both to be a defect: (1) would this paper ever write "each X" or "the second X" about these events, or define X as a term? (2) does un-nominalising lose anything? Grammatical countability alone does not save it — "undergoes a transformation" takes "a" and is still the fault.

**Revision.**

- Before: The panel undergoes a transformation before the estimation of the coefficients is performed.
- After: We transform the panel, then estimate the coefficients.

**Do not apply when.** The nominalisation heads a defined technical term or a named quantity, where it is a label and countability is beside the point. Do not force a count noun onto a genuinely mass process — evidence, compliance, uncertainty — to satisfy the test; the fix there is a different verb, not a pluralised abstraction. And do not run this rule as a global sweep: a draft in this register is expected to carry roughly 29 nominalisations per 1,000 words.

<sub>Verifier: Keep it, but the stated test misfires on the pattern's own example. The test as written is grammatical countability ("can it take each, a, the first, or a number"), and the revision_before sentence — "The panel undergoes a transformation before the estimation of the coefficients is performed" — contains "a transformation", which passes that test while being exactly the fault. Almost any deverbal noun can take "a", so as literally stated the test does not discriminate; the discriminating content is in the signature (weak verb + "of") and in whether the paper would ever enumerate these events. I</sub>

---

## Put the argument in front of the nominalisation instead of behind an "of"

**Move.** When the noun is the right call, compress "the construction of the tree" into "tree construction" and "the selection of seeds" into "seed selection". The premodifier absorbs the article and the "of", and blocks a second "of" from ever attaching.

**Why it works.** The corpus overwhelmingly prefers the compound: "tree construction" 93 vs "the construction of the tree" 1. The same shape recurs across the register — tree contraction 222, list contraction 167, seed selection 83, batch insertion 76, core decomposition 69 — while "the <nominalisation> of the <noun>" is a scattering of one-offs. This is why the measured of-chains are so rare: "the X of the Y of" appears 87 times in 1.1M words and chains of two or more "of the" only 80 times. The mechanism matters: every "of" you leave open is a socket another "of" can plug into, and a premodifier removes the socket.

**Seen in.** geometry, im, hdbscan, parlayann (sampled from 8-10 papers for this sub-topic, not all 119)

- "The first technique is to decouple the tree construction from sorting" — *geometry*, Section 1, Introduction

- "The second technique includes new data structures for parallel seed selection." — *im*, Abstract

- "Thus, the seed selection time is dominated by constructing the data structures" — *im*, Experiments

**Violation signature.** A noun phrase with two or more "of" links — "the reduction of the variance of the estimator" — or a single "the <action nominalisation> of the <short noun>" where the short noun is a plain one- or two-word category that could move in front. Count the "of"s in each noun phrase: two is a rewrite, three is a rebuild. The nominalisation must name an action (construction, selection, insertion, reduction); a state or property noun is not this fault.

**Revision.**

- Before: We report the improvement of the accuracy of the classifier under each sampling regime.
- After: We report the classifier's accuracy improvement under each sampling regime.

**Do not apply when.** The noun names a state or property rather than an action — the corpus's surviving "the X of the Y" phrases are mostly these (the performance of the classifier, the position of the sensor, the distance of the closest pair, the definition of the step) — leave them. Leave the "of" too when the argument is long, heavily modified, or possessive, since a four-word noun pile is worse, and stop at two nouns: stacking three or more premodifiers relocates the ambiguity rather than removing it. Do not coin a compound the field does not already use; an unfamiliar noun-noun pair reads as a term of art and sends the reader hunting for a definition that does not exist.

<sub>Verifier: Measurements reproduce almost exactly: tree construction 90 vs "the construction of the tree" 1; seed selection 69 vs "the selection of seeds" 0; tree contraction 210; list contraction 159; batch insertion 72; core decomposition 64. All four exemplars illustrate the compound. The narrowing needed is on the signature, which flags any "the <nominalisation> of the <short noun>". I pulled every instance of that shape in the corpus (201 hits) and the survivors are dominated by state and property nouns, not action nouns: the position of the sensor, the performance of the classic sequential..., the d</sub>

---

## Let the object of study act: inanimate subjects take ordinary transitive verbs

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Models, methods, structures and mechanisms are given plain transitive verbs — measures, captures, reflects, maintains, takes, requires, returns, computes, supports, proceeds, outperforms — rather than a copula plus a nominalised action ("is responsible for the allocation of", "has the ability to identify", "provides support for the handling of").

**Why it works.** Restricted to subjects of the form the/our/this + algorithm, approach, model, structure, method, technique, implementation or framework, the corpus verb inventory is: is 683, has 105, uses 70, takes 46, requires 43, runs 30, processes 25, achieves 25, allows 24, maintains 23, proceeds 21, starts 18, applies 17, combines 13, computes 12, outperforms 11, terminates 10, returns 10, supports 10, partitions 10. The evasive alternatives are effectively absent: "has the ability to" 0, "provides support for" 0, "is capable of" 1, "plays an important role" 0. This matters for nominalisation because copula-plus-abstract-noun is where most avoidable nominalisations enter a draft. Stated honestly: "is" remains by far the commonest verb in this slot (683), so the rule is not "avoid the copula" — it is "do not use a copula plus a nominalised action where the subject could simply perform the action".

**Seen in.** pbtree, ROSE, pimtree, hdbscan, xu-alignment-ipdps-25 (sampled from 8-10 papers for this sub-topic, not all 119)

- "This model measures the total block transfers (I/O work) and their critical path (I/O span)." — *pbtree*, Abstract

- "This model reflects the reality that large real-world graphs tend to have at least an order of magnitude more edges than vertices." — *ROSE*, Section 1, Introduction

- "The search tree structure effectively maintains the ordering for a set of elements with dynamic updates" — *pbtree*, Section 1, Introduction

**Violation signature.** An inanimate subject followed by is / has / provides / serves plus an abstract noun plus "of" or "for": "the framework is responsible for the aggregation of the panels", "the instrument has the ability to identify the effect", "the model provides support for the handling of missing data". The real verb is inside the noun; the subject is standing idle.

**Revision.**

- Before: The instrument has the ability to provide identification of the treatment effect under weak assumptions.
- After: The instrument identifies the treatment effect under weak assumptions.

**Do not apply when.** The sentence genuinely defines or classifies ("X is a special case of Y") or predicates a property ("the estimator is consistent") — the copula is correct there and is by far the commonest verb in this slot (496 of the measured cases). The bar on personification is narrower than it first looks: this corpus routinely lets a mechanism decide and choose when the choice is made at run time ("our sampling scheme only chooses ...", "a shuffle that iteratively decides each element" — chooses 36 uses, decides 17). What stays with the authors are the mental and rhetorical verbs — believes (0 uses in 1.1M words), wants (4), argues, aims — and any decision the researcher made at design time.

<sub>Verifier: The move is supported — restricting to the/our/this + algorithm|approach|model|structure|method|technique|implementation|framework, I get is 496, has 78, uses 62, requires 39, takes 39, runs 30, achieves 25, processes 24, allows 22, maintains 20, proceeds 18, starts 18, applies 15, and the evasive forms are effectively absent (has the ability to 0, is capable of 1, provides support for 2, plays an important role 1). The honest framing in the why ("is" dominates, so the rule is not "avoid the copula") is correct and should be preserved. But the do_not_apply_when is contradicted by the corpus: i</sub>

---

## Put the gloss immediately after the word it explains, inside the noun phrase

**Move.** When a term will slow the reader — an abbreviation, a technical name, an unfamiliar sense of a common word — break the noun phrase at that word, close the gloss in parentheses, and continue. Run the device in reverse too: describe something in plain words, then let a parenthesis supply the standard name for it.

**Why it works.** A gloss parked at the end of the sentence forces the reader to carry the confusion through every intervening clause and then reread. Placing it at the point of difficulty means the sentence is understood on one pass, which is what lets these authors push three or four unfamiliar terms through a single sentence without a stall. It is also why the abbreviation-on-first-use bracket sits flush against the expansion rather than in a later sentence.

**Seen in.** RWS, Incremental, DP, fastbcc (sampled from 8-10 papers for this sub-topic, not all 119)

- "On the user (algorithm designer or programmer) side, it is a simple extension to the classic programming model with additional keywords for creating new tasks (e.g., fork) and synchronization (e.g., join) between tasks." — *RWS*, Introduction

- "We are interested in the depth (longest directed path) of iteration dependence graphs" — *Incremental*, Section 2, Iteration Dependences

- "we do not assume all processors run in lock-steps (the PRAM setting)" — *RWS*, Introduction

**Violation signature.** A term appears, several clauses run, and only then a trailing '(here X means Y)' or a following sentence opening 'By X we mean'. Also: an abbreviation used once and defined a paragraph later, or defined in a bracket that sits after the noun phrase rather than inside it.

**Revision.**

- Before: We regress log wages on the instrument and report heteroskedasticity-robust standard errors throughout, where by robust we mean the Huber-White sandwich estimator.
- After: We regress log wages on the instrument and report robust (Huber-White sandwich) standard errors throughout.

**Do not apply when.** The term is the sentence's subject rather than a passing reference — then it earns a defining sentence or a formal definition, and squeezing it into a bracket underweights it. Also skip when a glossary, notation table, or definition environment already carries the load, and when two glosses would land within a few words of each other, which turns the sentence into a stutter.

<sub>Verifier: Well supported and cleanly separable from the length pattern: this one is about placement, not size. The corpus runs 16,559 prose-carrying parentheses plus 4,881 bare-abbreviation brackets, and abbreviation-on-first-use is in 118/119 papers (1,357 definitions). The deferred alternative the signature names is near-absent: 'By X we mean' appears 9 times in 1.4M words, 'we mean' 12, 'here ... means' 5 — so a draft that defers its gloss is doing something these authors essentially never do, and that is checkable from a draft alone. All four exemplars demonstrate the claimed move, including the rev</sub>

---

## Let the clause before a colon name the category the right side will deliver

> Narrowed after corpus measurement contradicted the original claim.

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** Before a colon that opens a list, make sure the clause has already named the category the items belong to — 'applications', 'graph kernels', 'distributions', 'goals'. The category noun usually sits at the colon's left edge but may sit earlier in the clause ('There are two goals in designing efficient parallel algorithms: ...'). Add a count when the number is fixed and worth promising: about a quarter of this corpus's list colons do, and the payoff is that the next paragraph can say 'the first' and 'the second' without renaming anything. Treat the count as an option, not a requirement.

**Why it works.** The colon is the corpus's workhorse for qualification after the comma (2.35 per 1,000 words, four to five times either rare mark), and it is almost always a hinge into an enumeration rather than a rhetorical pause. Counting before the colon turns the list into a promise the reader can check, tells them where the list ends, and licenses the following paragraph to say 'the first' and 'the second' without renaming anything. The words immediately preceding a prose colon are dominated by exactly this class of nouns — steps, properties, parts, cases, operations, phases, categories, aspects, applications, components — or by 'as follows'.

**Seen in.** PacTree, kdtree, iterative, ParChain (sampled from 8-10 papers for this sub-topic, not all 119)

- "We consider four applications: graphs, inverted indices, 2D range queries and 1D interval queries." — *PacTree*, Section 6, Experiments

- "We study the performance of three fundamental graph kernels: breadth-first search (BFS), single-source betweenness centrality (BC), and maximal independent set (MIS)." — *PacTree*, Experiments, Graph Algorithm Performance

- "For synthetic datasets, we use 64-bit integer coordinates with two distributions: Varden and Uniform." — *kdtree*, Section 6, Experiments (Datasets)

**Violation signature.** In running prose, a colon after a bare verb or preposition with the list continuing inline — 'The reasons are: income, distance, and health', 'We tested for:', 'This depends on:'. A colon whose clause names no category at all, so the reader cannot tell what kind of thing is coming or how far the list runs. A stated count that does not match the number of items delivered.

**Revision.**

- Before: Our survey covered: household income, commuting time, and self-reported health.
- After: Our survey covered three domains: household income, commuting time, and self-reported health.

**Do not apply when.** The colon is doing restatement rather than enumeration — a single expansion of the preceding clause, as in 'This box can be used in queries to prune the subtree: when the query does not overlap with the box, the entire subtree can be skipped.' A count there would be nonsense. A displayed bullet list is exempt from the bare-verb rule: this corpus itself writes 'our contributions are:' and 'A few major distinctions include:' above a set of bullets, and 'as follows:' 79 times — the rule bites on inline lists. Drop the count when the number is unstable ('several', 'a number of') rather than inventing false precision, and avoid two colon-lists in consecutive sentences.

<sub>Verifier: The category half is supported; the count half is not, and the placement requirement is contradicted by the pattern's own fourth exemplar. Measured over prose colons (sentence-level, bibliography and pseudocode excluded): only 13.2% carry a numeral or number-word in the last five words before the colon, and 38% end on a plural noun. Restricting to the 691 colons whose right side is actually list-shaped, still only 27.1% carry a count and 48.5% end on a plural. So 'usually count it' is false — roughly a quarter, not a majority. Exemplar mismatch: 'There are two goals in designing efficient para</sub>

---

## Default to a period; the semicolon earns its keep on the second branch of a condition

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Write two sentences unless the second clause is the other case of the condition just stated ('...; otherwise, ...') or says the matching thing about the second member of a pair the reader is already holding side by side. Those are the two shapes where the mark tells the reader something a period cannot. A semicolon is also the only workable separator for list items that themselves contain commas. Elsewhere it is permissible but buys nothing, so make the period the default rather than the exception.

**Why it works.** At 0.63 per 1,000 words the semicolon cannot function as a general-purpose clause joiner in this register; it appears about once every page and a half. Confining it to alternation and pairing makes the mark itself informative — it tells the reader 'these two clauses are one thought, and the second completes the first', which a period cannot say and a comma-plus-'and' says too weakly.

**Seen in.** fastbcc, ParChain, kdtree, Incremental (sampled from 8-10 papers for this sub-topic, not all 119)

- "If 𝑇 is a BFS tree, there are no back edges; if 𝑇 is a DFS tree, there are no cross edges." — *fastbcc*, Preliminaries

- "prune the search; otherwise, we continue the search and recurse on the children." — *ParChain*, Section 5, Caching optimization

- "The orange arrows are new neighbors found on this round; the green arrow means the nearest neighbor is not updated on this round due to the reducibility property." — *ParChain*, Figure 1 caption

**Violation signature.** More than two or three semicolons on a page outside an enumerated list. A semicolon whose two clauses read identically when joined by 'and' or split by a period — substitute both and see whether anything is lost. Three or more clauses chained into one sentence by semicolons.

**Revision.**

- Before: Wage growth slowed after 2012; labour force participation also fell over the same period; both trends are visible in Figure 2.
- After: Wage growth slowed after 2012, and labour force participation fell over the same period. Figure 2 shows both trends.

**Do not apply when.** An enumerated list whose items themselves contain commas — there the semicolon is the only workable separator no matter how rare it is elsewhere, and the corpus uses it that way in '(1) ...; (2) ...; and (3) ...' runs. Disregard the scarcity rule in house styles that mandate semicolons in enumerations, as several legal and medical journals do. And do not treat every looser semicolon as a defect to be repaired: alternation and pairing account for well under half of this corpus's own prose semicolons, so the rule is about which uses are worth the mark, not about which are permissible.

<sub>Verifier: The scarcity premise is right (0.63/1k in the digest; my own count finds 2,223 semicolon characters but 1,058 of those are inside code and pseudocode listings, leaving prose use genuinely rare). The restriction is not: 'use a semicolon in two situations only' describes the corpus's prescription, not its behaviour. Of 307 clean prose semicolons — left side ending in a lowercase word, right side opening on a lowercase word, code and URLs excluded — the continuations are 'and' 36, 'the' 32, 'otherwise' 23 (7.5%), 'in' 15, 'however' 10, 'see' 10, 'it' 9, 'this' 8. Alternation plus matched pairing </sub>

---

## Hang the consequence on ', which' instead of opening a new 'This ...' sentence

**Move.** When a claim's implication would otherwise become a short following sentence opening 'This means / This allows / This implies', attach it to the clause you just finished — ', which means ...', ', which allows ...' — and keep claim and consequence in one sentence. The comma is what licenses the clause-level reading, so hold the underlying distinction: 'which' for clauses that add, always with the comma; 'that' with no comma when the clause is what identifies the noun.

**Why it works.** 3,295 of the corpus's 4,410 uses of 'which' (75%) carry a preceding comma, so the comma is a live signal that the modifier adds rather than identifies. About a quarter of them are ', which is', the definitional appositive; several hundred more take a consequence verb — means, gives, leads, allows, makes, implies, enables, results — with the whole preceding clause as antecedent. That construction is how these papers keep a claim and its implication in one sentence, which matters given that qualification here is appended rightward (median 5 words before the main verb).

**Seen in.** fastbcc, ParChain, Incremental, RWS, kdtree (sampled from 8-10 papers for this sub-topic, not all 119)

- "Unfortunately, in Tarjan-Vishkin, generating the skeleton 𝐺 ′ and computing CC on 𝐺 ′ take 𝑂 (𝑚) extra space, which greatly increases the memory usage and slows down the performance." — *fastbcc*, Introduction

- "The only parallel exact algorithm that works for the metrics that we consider and uses subquadratic space is by Zhang et al. [69], but it has not been shown to scale to large data sets." — *ParChain*, Introduction

- "In this paper, we consider three types of incremental algorithms, which we refer to as Type 1, 2, and 3, for lack of better names." — *Incremental*, Section 2, Iteration Dependences

**Violation signature.** A run of short sentences each opening 'This means...', 'This allows...', 'This implies...', where the previous sentence could have absorbed them. 'which' introducing a clause the sentence needs in order to identify its noun, with no comma ('households which had moved'). A comma before a restrictive 'that'. And the opposite failure: a ', which' that could be read as attaching to the nearest noun rather than to the whole clause.

**Revision.**

- Before: The survey excluded households which had moved in the previous year. This reduced the analysis sample by 12 per cent.
- After: The survey excluded households that had moved in the previous year, which reduced the analysis sample by 12 per cent.

**Do not apply when.** The rule is a tendency, not an absolute: about 1,000 uses of 'which' in the corpus lack a preceding comma, though roughly half are the pied-piped 'in which / for which / of which' form, which takes no comma by construction. So do not flag every bare 'which' as an error. Separately, do not demote a consequence to ', which' when it is the paragraph's point — a subordinate clause is the wrong place for the finding — and name the referent outright whenever clause-level 'which' could be read as attaching to the nearest noun instead.

<sub>Verifier: Numbers verified exactly: 4,410 uses of 'which', 3,295 (74.7%) comma-preceded, 501 (11.4% of all, ~45% of the non-comma remainder) pied-piped after in/for/of/at/on, and ', which is' 915 times = 27.8% of the comma uses. One correction: 'several hundred more take a consequence verb' is generous — clause-level consequence verbs after ', which' total about 250 (means 60, gives 44, leads 42, requires 41, allows 25, makes 24, enables 18, results 14, implies 13). Still a live device, just not several hundred. The reason for revising is billing, not truth. As named, the pattern leads with the restrict</sub>

---

## Never open on 'e.g.' or 'i.e.', always a comma after, and put the examples in brackets

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Write 'e.g.' and 'i.e.' with a following comma and never at the start of a sentence — in 1,725 uses this corpus starts a sentence with one three times. Set illustrative instances in parentheses as '(e.g., A, B, and C)', attached to the exact term they illustrate; 85% of 'e.g.' sits inside brackets, and bracketing the instances also lets the main clause keep a parallel shape that a stopped-mid-clause list would break. A restatement may sit in brackets too — 62% of 'i.e.' does — so pull it into the clause after a comma only when the argument actually leans on it.

**Why it works.** The split tracks necessity, and the corpus enforces it. 76% of 'e.g.' occurrences sit inside parentheses against 54% of 'i.e.', and both are sentence-initial 0% of the time; 'i.e.' and 'e.g.' take a following comma in about 86% of uses. An example is skippable and so belongs in the skippable container; a restatement is the clause's actual content and belongs where the reader cannot skip it. Bracketing the instances also lets a sentence keep a parallel three-verb or two-branch shape that a stopped-mid-clause list would break.

**Seen in.** iterative, fastbcc, ParChain, PacTree, RWS (sampled from 8-10 papers for this sub-topic, not all 119)

- "the key is to identify the dependences among “objects” (e.g., iterations, instructions, or input objects), and process them in the proper order" — *iterative*, Introduction

- "Functional interfaces have several advantages over mutating ones, including being safe for parallelism, allowing safe composition, permitting flexible implementations (e.g., using copies when helpful), and supporting snapshots." — *PacTree*, Introduction

- "The input graphs need to be undirected, i.e., each edge should appear twice in the input in both directions." — *fastbcc*, Appendix, artifact description

**Violation signature.** 'E.g.,' or 'I.e.,' opening a sentence. 'e.g.' or 'i.e.' with no comma after it. A restatement the argument depends on hidden inside brackets. A long list of illustrative instances halting the main clause mid-stride instead of sitting in brackets beside the term it illustrates.

**Revision.**

- Before: Several instruments have been used in this literature. Rainfall, distance to the coast and colonial legal origin are examples. The exclusion restriction (that is, that the instrument affects the outcome only through the regressor) is rarely tested.
- After: Several instruments have been used in this literature (e.g., rainfall, distance to the coast, and colonial legal origin). The exclusion restriction, i.e., that the instrument affects the outcome only through the regressor, is rarely tested.

**Do not apply when.** House styles differ: many UK and humanities styles set 'eg' and 'ie' without points or without the trailing comma, or require 'for example' and 'that is' spelled out in running text — follow the house style rather than this corpus. The bracketing rule inverts when the instances are themselves the finding rather than illustration; then they are the sentence's content and belong in the main clause. And do not move a parenthesised 'i.e.' into the clause as a matter of routine: the in-clause placement is a minority tendency (38% of uses here), so it earns the move only when the restatement is load-bearing.

<sub>Verifier: Three of the claims are sharp and replicate: across 836 uses of 'e.g.' and 889 of 'i.e.', sentence-initial position occurs 1 and 2 times respectively (effectively 0%), a following comma appears in 89.8% and 86.1% of uses, and 'e.g.' sits inside parentheses 85.2% of the time. The headline split does not survive: 62.3% of 'i.e.' uses are ALSO parenthesised, so 'keep the restatement in the sentence' describes the minority of the corpus's own practice — the pattern's why concedes this (its own figure is 54%) while the name and move assert the opposite, which is an internal contradiction rather tha</sub>
