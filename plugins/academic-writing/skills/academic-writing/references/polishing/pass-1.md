# Pass 1 — First position

**Ask:** What occupies the first position of this paragraph and of this sentence — and did it earn that slot?

**Do not touch in this pass.** Do not touch wording inside the sentence: no hedges, no nominalisations, no light verbs, no parenthesis surgery. Do not fix a single pronoun or demonstrative yet — reordering will change what each one points at, and Pass 3 resolves all of them at once against the final order. Do not delete a connective that is doing real work mid-paragraph; this pass only relocates paragraph-initial ones and deletes those the parallelism has already replaced. Do not shorten a long sentence yet: Pass 4 rebuilds it around its verb. Do not flag a 25-word paragraph opener or a first-person opener ('We show…', 'Our method…'): openers run a median 17 words against 20 for middles, and 13% of paragraphs open on We/Our — the same rate as mid-paragraph sentences.

19 patterns.

---

## Open each paragraph on the noun it is about, not on a connective

**Move.** Put the paragraph's topic in subject position in its first sentence and delete any leading However/Therefore/Moreover/Furthermore/Additionally; let the link to the previous paragraph be carried by the topic noun itself rather than by a relation word.

**Why it works.** The reader's first fixation lands on what the paragraph is about instead of on a relation to material they have already left. Measured over 7,264 heuristically-segmented paragraphs across all 119 papers with one consistent classifier: paragraph-FIRST sentences are bare-subject 55.6% and connective-initial only 2.5%, while paragraph-LAST sentences are bare-subject 39.4% and connective-initial 10.5%. Connective-fronting is a four-times-rarer event at the top of a paragraph than at the bottom. (My classifier is coarser than the digest's taxonomy, so absolute levels differ slightly from its corpus-wide 46.4% bare-subject / 6.4% connective; the cross-position differences are what the measurement supports.)

**Seen in.** edit-distance, ParChain, kcore, RWS, cbfs, pimzd, ED (sampled from 8-10 papers for this sub-topic, not all 119)

- "Edit distance is a fundamental problem in computer science, and is introduced in most algorithm textbooks (e.g., [14, 15, 23])." — *edit-distance*, Introduction (paragraph opening)

- "The nearest-neighbor chain (NNC) algorithm [45] is a popular algorithm that can be used for a wide range of HAC metrics" — *ParChain*, Introduction (paragraph opening)

- "Many other parallel 𝑘-core implementations, such as PKC [38] and ParK [17], use the online approach." — *kcore*, Introduction (paragraph opening)

**Violation signature.** Three or more paragraphs in one section open with However, Moreover, Therefore, Furthermore, Additionally, In addition, or On the other hand; or a paragraph's first sentence takes as its subject a bare This/These or a third-person pronoun (It, They, Their) whose referent sits in the paragraph just finished. A first-person opener ('We show...', 'Our estimator...') is NOT a violation: 13% of this corpus's paragraphs open that way, the same rate as mid-paragraph sentences.

**Revision.**

- Before: However, there is a second source of measurement error that prior surveys have not addressed.
- After: A second source of measurement error has gone unaddressed in prior surveys.

**Do not apply when.** The paragraph's entire job is to overturn the one immediately before it and the reversal, not the new topic, is the point — the corpus still opens 2.5% of paragraphs on a connective. Also exempt: the first paragraph after a section heading, which may legitimately open "In this section, we ...".

<sub>Verifier: Independently re-measured over 7,188 3+-sentence paragraphs with my own classifier and it holds hard: connective-initial 1.9% at paragraph-FIRST vs 7.3% mid vs 10.9% LAST; bare 'This/These + relational verb' 0.3% first vs 3.0% last; third-person pronoun subject (It/They/Their) 0.4% first vs 2.0% last. That matches the validation file's 1.8% and is the strongest single finding in the corpus. Exemplars all demonstrate the positive move (topic noun in subject position at a paragraph top); three of four verify as paragraph-initial in my reflowed segmentation, and the kcore one lands mid-block only</sub>

---

## Let the paragraph's opening sentence reach its claim before its qualifications

> Narrowed after corpus measurement contradicted the original claim.

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** Write the paragraph's first sentence so the main claim is complete before any condition, exception or hedge, then put those in the sentences that follow; when a topic sentence has grown a fronted 'Although/While/Because' clause plus a relative, split it into two or three sentences. Treat this as a tendency, not a rule: paragraph openers run a median 17 words against 20 for middles and are more often short (25th percentile 10 words vs 14), but a quarter of them still carry a subordinate clause.

**Why it works.** Measured across the same 7,264 paragraphs: first sentences run a median of 17 words with 31.8% at 12 words or fewer and 15.5% at 35+; middle sentences run a median of 19 words with only 21.2% short and 18.3% at 35+. The topic sentence is systematically the leaner one. The reader gets a proposition small enough to hold while the qualifications arrive, instead of a proposition that is already three clauses deep before it is stated.

**Seen in.** RWS, kcore, cbfs, ParChain, edit-distance (sampled from 8-10 papers for this sub-topic, not all 119)

- "This paper presents a simplified analysis in Section 3." — *RWS*, Introduction (paragraph opening; the potential-function caveat follows in the next sentence)

- "We present our algorithm framework in Alg. 1." — *kcore*, Sec. 3.1 Framework (paragraph opening)

- "To achieve high performance, we design an efficient parallel algorithm." — *cbfs*, Introduction (paragraph opening; work-efficiency and span qualifications follow)

**Violation signature.** A paragraph's first sentence runs past ~35 words, or its main claim is still incomplete past the halfway point because a fronted subordinate clause ('Although...', 'While...', 'Given that...') and a relative clause come first. A 25-word opener whose claim lands in the first clause with the qualification trailing is normal — that is the corpus's 75th percentile for openers — and must not be flagged.

**Revision.**

- Before: Although the effect is smaller in the pooled sample and disappears once industry controls are added, the wage premium associated with certification, which we measure using the 2019 wave, is positive.
- After: Certification carries a positive wage premium. We measure it using the 2019 wave. The effect shrinks in the pooled sample and disappears once industry controls are added.

**Do not apply when.** The paragraph is a formal definition, theorem statement, or proof step, where the qualification is constitutive and splitting it off would make the opening sentence false as written. Also do not flag on length alone: one paragraph opener in six in this corpus runs 30 words or more.

<sub>Verifier: Contradicted as stated. The validation file already warns that this effect is 2-3 words at the median and that a 24-word opener must not be flagged on this evidence. My own pass: paragraph-first median 17 words vs 20 for middles, p75 25 vs 27, 16.3% of openers run 30+ words and 9.6% run 35+; 25.1% of paragraph openers contain a subordinate or relative clause marker, 14.4% open with a fronted element, 9.1% carry a hedge. So 'no fronted condition, no hedge, and no relative clause' describes neither the corpus nor anything the measurement can support — one opener in four is qualified and one in s</sub>

---

## End the paragraph with a short consequence sentence, and let it carry the backward link

**Move.** When a paragraph has been accumulating evidence, cases or numbers, give it a closing sentence that says what they mean — and spend the backward link there ('This/These + noun', 'As a result', 'Therefore', 'Hence') rather than at the top of the paragraph. Not every paragraph needs one; the point is that this slot, not the paragraph's first sentence, is where a connective belongs: paragraph-final sentences open on a connective 10.9% of the time against 1.9% for paragraph openers.

**Why it works.** Measured across 7,264 paragraphs: paragraph-final sentences are connective-initial 10.5% (against 2.5% for first sentences) and demonstrative-initial 6.7% (against 3.1%), and the length drops back to a median of 17 words with 30.8% at 12 or fewer, after middles that run longest. The interpretation, not the evidence, is what the reader carries into the next paragraph, and putting the backward link here spends the connective where it does work.

**Seen in.** kcore, FRT, RWS, edit-distance, pimzd, slc, xu-ca-spaa-20 (sampled from 8-10 papers for this sub-topic, not all 119)

- "This justifies why our solution with VGC can achieve better parallelism than Julienne." — *kcore*, Sec. 4 (paragraph-final)

- "As a result, this overhead diminishes the benefits of parallelism." — *kcore*, Sec. 4 (paragraph-final)

- "These properties are essential to guarantee the correctness and the stated time bound." — *FRT*, Sec. 3 (paragraph-final)

**Violation signature.** An evidence or results paragraph whose last sentence is one more data point, citation, or table reference, with no sentence anywhere in the paragraph saying what the numbers mean — especially a run of three or more such paragraphs; or a last sentence that raises a caveat the paper never returns to.

**Revision.**

- Before: Firms in the second quartile reported a 7% decline and firms in the third quartile a 4% decline. Data for the fourth quartile were collected in a separate wave.
- After: Firms in the second quartile reported a 7% decline and firms in the third quartile a 4% decline. The decline therefore tracks firm size rather than sector.

**Do not apply when.** The paragraph is an enumerated list, a definition block, or a roadmap, where the last item is simply the last item. Do not append a verdict that only restates the opening sentence in other words. And do not treat a paragraph that ends on a forward-pointing sentence as defective — handing off to the next paragraph is a legitimate close.

<sub>Verifier: The positional differential is real and I reproduce it independently: paragraph-LAST sentences are connective-initial 10.9% against 1.9% at paragraph-first (5.7x) and demonstrative-initial 6.9% against 2.4%; consequence-marked openers (This/These/Thus/Therefore/Hence/As a result/Overall) are 11.7% of last sentences vs 8.2% of middles. All four exemplars verify as genuinely paragraph-final in short (4-8 sentence) paragraphs and each does say what the preceding material means, so they demonstrate the move cleanly. The overreach is the imperative: about one paragraph-final sentence in nine opens </sub>

---

## In a run of case-by-case sentences, front the varying coordinate and keep the frames identical

> Narrowed after corpus measurement contradicted the original claim.

**Move.** When two or more consecutive sentences make the same kind of claim about different cases, rounds, datasets or regimes, move the distinguishing phrase to the front of each and keep the frames grammatically parallel — same preposition, same shape — so the shared predicate recedes and only the difference is salient. Keep each frame short: corpus frames run a median of 4 words, p90 11.

**Why it works.** The fronted phrase becomes the column header of a small table the reader builds while reading, so the shared predicate recedes and only the difference is salient. The corpus baseline makes the frame a marked choice — 13.8% prepositional-frame and 7.5% subordinate-clause openings — and it is spent on contrast. The frames are kept short so the marking costs little: measured over 14,042 fronted frames, median 5 words, p75 9, p90 12.

**Seen in.** ParChain, pimzd, kcore, cbfs, ED, edit-distance (sampled from 8-10 papers for this sub-topic, not all 119)

- "In complete linkage [51, 58], the distance between two clusters is the maximum distance between a pair of points, one from each cluster." — *ParChain*, Sec. 2 Background

- "In unweighted average linkage [39, 62], the distance between two clusters is the average distance between pairs of points, one from each cluster." — *ParChain*, Sec. 2 Background (the next sentence in the same run)

- "For PIM programs, it measures the PIM time, the maximum work on any PIM core within a round." — *pimzd*, Sec. 2 (third sentence of a For-CPU / For-off-chip / For-PIM run)

**Violation signature.** A run of case-by-case sentences in which the distinguishing condition arrives at the end ('The distance is the maximum pairwise distance under complete linkage. Average linkage instead uses the mean...'); or a run whose frames are fronted but structurally mismatched ('Under complete linkage, ... / When average linkage is used, ... / For Ward's linkage, ...'); or a reported magnitude with no scope stated anywhere in its sentence.

**Revision.**

- Before: The effect is strongest among households in the lowest income decile. Households in the top decile show no effect, though. An intermediate effect appears in the middle deciles.
- After: In the lowest income decile, the effect is strongest. In the middle deciles, it is intermediate. In the top decile, it disappears.

**Do not apply when.** This is not a ban on the isolated fronted frame. One sentence in five in this corpus opens on a fronted frame, and about 90% of those have no fronting neighbour at all — scope-setting ('For a graph with n vertices and m edges, ...'), conditionals, and locatives are the register's norm, not a marked choice needing contrastive justification. The frames worth moving rightward are the ones running past about a dozen words (p90 is 11), and those carrying nothing the reader needs before the claim.

<sub>Verifier: The exclusivity claim is contradicted outright. I extracted every non-connective fronted frame (initial preposition/subordinator + comma) in multi-sentence paragraphs: 10,107 of them, 20.0% of sentences. Only 934 (9.2%) have an adjacent sentence fronting the same preposition; even on the loosest definition of a run — any neighbouring sentence with any fronted frame, which over-counts coincidence — only 34.6% qualify. So between two-thirds and nine-tenths of this corpus's fronted frames are isolated, and the commonest heads (In 2546, For 1710, To 1070, If 684, As 633, Since 548, When 485) are s</sub>

---

## Cap the announcing clause at the counted noun and expand after a colon

> Narrowed after corpus measurement contradicted the original claim.

**Move.** When a sentence must carry several internally complex items, end the main clause on the noun that names and counts them ("three properties", "two key optimizations", "the following perturbations"), put the colon there, and let the items follow.

**Why it works.** The reader learns the shape — how many, of what kind — before any content, and can then consume the items incrementally without holding a syntactic frame open. 343 sentences across the corpus place a count word or "the following" immediately before a colon, and the colon is the signature device of the long sentence (23.5% of 35+ word sentences carry one, against 3.9% of mid-length sentences); semicolons, otherwise near-absent at 0.63 per 1,000 words, appear almost only as the separator inside such a list.

**Seen in.** FRT, xu-ca-spaa-20, kcore, cbfs, ParChain, slc (sampled from 8-10 papers for this sub-topic, not all 119)

- "The algorithm has three properties: it only requires linear time in the number of edges in the input graph; the computed distances have a distance preserving property;" — *FRT*, Abstract

- "We show that worst-case profiles are robust to all of the following perturbations: randomly tweaking the size of each box by a constant factor, randomly shifting the start time of the algorithm, and randomly (or even adversarialy) altering the recursive structure of the profile." — *xu-ca-spaa-20*, Introduction

- "We compare our implementation against three state-of-the-art parallel implementations: Julienne, ParK and PKC" — *kcore*, Introduction

**Violation signature.** A sentence over 30 words whose coordinated items are strung on "and ... and ..." or on commas with no announcing head; or a head that characterises the items without counting or naming them ("we make several contributions that are important, including ..."); or a colon placed after a verb or preposition that still needs its object ("The three sources are: X, Y, and Z").

**Revision.**

- Before: We collected administrative tax records and we also ran a household survey, and in addition we conducted interviews with forty firm managers, and these together form the basis of the analysis.
- After: The analysis draws on three sources: administrative tax records, a household survey, and interviews with forty firm managers.

**Do not apply when.** There are only two short, parallel items — a colon there is heavier than the "and" it replaces. Also skip it when the items are full sentences that would each be better as their own sentence; the colon buys nothing once the list stops being a list.

<sub>Verifier: Move, exemplars and violation signature are all sound and portable: 1,130 colons introduce a list or explanation across 115/119 papers, I count 240 sentences placing a count word or 'the following' + noun immediately before a colon (the pattern says 343 — same order, softer than claimed), and the colon-after-a-verb-still-needing-its-object defect it names ('The three sources are: X, Y, Z') really is rare at 65 uses in 1.1M words. All four exemplars put a counted or named head immediately before the colon and expand after it, so they demonstrate the move exactly. Two factual corrections belong </sub>

---

## Give each naming or notation act its own short sentence, placed the moment the thing exists

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Give a term coinage, a notation convention, or a standalone figure pointer its own clause, placed immediately after the sentence that first introduces the object, so the term is available for reuse from the very next sentence. Prefer a dedicated short sentence — corpus naming sentences run a median of about 15 words, and 'We call ...' sentences about 13 — and do not chain two naming acts into one sentence.

**Why it works.** The short sentence in this corpus is defined by its act, not by contrast with its neighbours. Of the 23.1% of sentences at 12 words or fewer, the commonest openers are exactly these acts: "We use" (134), "We assume" (78), "We call" (59), "An example/An illustration" (39/26), "We refer" (30). Isolating the act keeps the content sentence about content and makes the term available for reuse from the very next sentence. Note a folk rule this corpus does NOT follow: short sentences are not preferentially placed after long ones — the sentence preceding a ≤12-word sentence is >=30 words only 18.8% of the time, about the corpus base rate — so placement is governed by the act, not by rhythmic contrast.

**Seen in.** kcore, edit-distance, ED, cbfs, pimzd, ParChain, slc, FRT (sampled from 8-10 papers for this sub-topic, not all 119)

- "We call A the active set." — *kcore*, Sec. 3.1 Framework (immediately after the sentence introducing the set)

- "We refer to these distributed nodes as master nodes." — *pimzd*, Sec. 3

- "We use string and sequence interchangeably." — *edit-distance*, Sec. 2 Preliminaries

**Violation signature.** A coined term is used in later sentences with no defining sentence or appositive anywhere; or the coinage rides inside a relative clause of a sentence that is simultaneously asserting something else, so the reader must hold a claim and a definition at once ('..., which we call the survivor pool, and which is updated each period'); or several notation conventions are chained into one sentence with semicolons.

**Revision.**

- Before: The model tracks the subset of firms that have not yet exited, which we call the survivor pool, and updates it at the end of each period.
- After: The model tracks the subset of firms that have not yet exited. We call this set the survivor pool, and update it at the end of each period.

**Do not apply when.** A figure or table is cited in support of a claim the sentence already makes — the trailing 'as shown in Figure 3' is right there, and 96 of 119 papers use that form. Skip the naming sentence when the term is used only once afterwards. And do not treat the embedded appositive as an error: ', which we call X' and ', called X' together appear about as often as the standalone naming sentence in this corpus, and are the right choice when the host sentence's only job is to introduce the object.

<sub>Verifier: The placement claim is good and the honest note in the why — that this corpus does NOT put short sentences after long ones (18.8%, base rate), so the short sentence is defined by its act rather than by rhythmic contrast — is a genuine finding worth preserving; it kills a real folk rule. Two things fail. (1) 'Never as a relative clause bolted onto a sentence' is contradicted: embedded naming is a live device at roughly the same frequency as the standalone form — 79 uses of 'which/that we call/refer to/denote' plus 124 appositives of the ', called / denoted / known as' type, against 236 sentence</sub>

---

## When items outgrow a clause, promote them to paragraphs and put the constant frame in each topic sentence

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** When an item outgrows its clause, promote every item in the list to its own paragraph or run-in-headed block, and make each opening repeat a constant: either the frame verbatim ('Our first contribution is ...' / 'Our second contribution is ...') or a fixed head shape ('Compressed vs uncompressed.' / 'Functional vs in-place.'), with only the distinguishing word varying. Repeat the frame word for word rather than varying it for elegance — the repetition is the structural signal.

**Why it works.** A template in the opening position keeps the enumeration visible across arbitrary amounts of intervening detail, so items can differ in length by a factor of five without the list dissolving. The corpus repeats the frame verb verbatim rather than varying it for elegance — the repetition is the structural signal.

**Seen in.** im, kcore, p2307-wheatman, PPM, ch, scc (sampled from 8-10 papers for this sub-topic, not all 119)

- "Our first contribution is a compression scheme for sketches on undirected graphs and the IC model" — *im*, 1 Introduction

- "Our second contribution is two new parallel data structures for seed selection." — *im*, 1 Introduction

- "The model is motivated by two complimentary trends. Firstly, it is motivated by upcoming non-volatile memories" — *PPM*, 1 Introduction

**Violation signature.** A numbered or bulleted list in which one item runs to forty-plus words while its neighbours run to ten, with nothing but a comma and the number holding it. Or paragraphs that begin an enumeration ("First, ...") and then abandon the template for the remaining items. Or ordinal markers buried mid-paragraph where the reader scanning left margins cannot see them.

**Revision.**

- Before: Our contributions are (1) a sampling design that corrects for non-response, which we develop by first characterizing the response propensity, then estimating it from administrative records, and finally reweighting, and which we validate on three national surveys; (2) an implementation; (3) an evaluation.
- After: Our first contribution is a sampling design that corrects for non-response. We characterize the response propensity, estimate it from administrative records, and reweight accordingly; Section 4 validates the design on three national surveys. Our second contribution is a reference implementation. Our third contribution is an evaluation against two existing corrections.

**Do not apply when.** There are only two items and both are short — promoting them to paragraphs inflates them, and one sentence with a coordinator is tighter. Also do not force a shared opening template onto items so heterogeneous that the template misdescribes one of them.

<sub>Verifier: The move is real, portable and has a sharp violation signature (one 40-word item beside 10-word neighbours; a template abandoned after 'First,'). The im pair ('Our first contribution is ...' / 'Our second contribution is ...') and the PPM quote ('The model is motivated by two complimentary trends. Firstly, it is motivated by upcoming non-volatile memories') demonstrate verbatim frame repetition exactly as claimed. The p2307-wheatman exemplar does not: 'Compressed vs uncompressed. CPMA [83], CPAM [35], and Aspen [36] all support compression' is a lone run-in head whose sibling heads ('Functiona</sub>

---

## Word contrasted items so the contrast occupies the same slot

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** When two items, or two consecutive sentences, are meant to be diffed against each other — opposed alternatives, or comparable results — build them on the same template with the varying terms in matching positions, so that exactly one constituent changes and the reader reads that constituent as the axis.

**Why it works.** Aligned slots let the opposition register before the sentence finishes: the reader sees that only one constituent changed and reads that constituent as the axis. When the frames differ, the reader has to reconstruct what varies before they can judge it, and any contrastive connective is doing work the wording should have done.

**Seen in.** kcore, PPM, p2307-wheatman, im, ch, scc (sampled from 8-10 papers for this sub-topic, not all 119)

- "Our contributions include 1) an algorithmic framework that can achieve work-efficiency using various peeling strategies, 2) a sampling scheme to reduce contention on high-degree vertices on dense graphs" — *kcore*, 8 Conclusion

- "Papers focusing on memory faults (e.g., [1, 22, 29] among a long list of such papers) consider models in which individual memory locations can fault." — *PPM*, 1 Introduction, Related Work

- "Papers focusing on processor faults (e.g., [6] among an even longer list of such papers) either do not consider memory faults or assume that all memory is volatile." — *PPM*, 1 Introduction, Related Work

**Violation signature.** Two items presented as alternatives or as a contrast but built on different frames — one a passive clause and one a noun phrase, or one naming a mechanism and the other naming an outcome — so the reader must work out which constituent is the variable. A reliable tell: the pair needs "In contrast," or "On the other hand," to be understood as a pair at all, and the two sentences share almost no wording.

**Revision.**

- Before: Method A partitions the sample by income decile. In contrast, high-variance strata are what Method B uses as its basis for splitting.
- After: Method A partitions the sample by income decile; Method B partitions it by outcome variance.

**Do not apply when.** The two things are not actually symmetric. Forcing a matched frame onto a main result and a minor caveat gives them equal billing and misleads; and holding the template at the cost of an inaccurate verb ("finds" where the paper actually "assumes") buys shape with precision.

<sub>Verifier: The move is strong and the PPM pair is the best exemplar in the whole topic — 'Papers focusing on memory faults ... consider models in which ...' against 'Papers focusing on processor faults ... either do not consider memory faults or ...' holds the frame and moves only the axis. The violation signature is excellent and field-independent: the pair needs 'In contrast,' to be readable as a pair at all, and the two sentences share almost no wording. But the kcore exemplar is a mismatch: 'Our contributions include 1) an algorithmic framework ... 2) a sampling scheme ...' is a four-item contributio</sub>

---

## Spend a sentence boundary on the conclusion, not on every step: a minor inference rides into the tail of its premise as ", and thus …"

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Decide how much a consequence is worth before choosing its grammar. If it is the claim the passage exists to establish — the result, the bound, the design decision — give it its own sentence and front the connective; "Therefore,", "Hence," and "Thus," are all normal in that slot (464 / 265 / 252 sentence-initial uses), so the choice among them is not a choice of weight. If it is a step the reader will grant instantly, do not spend a boundary on it: append it to the sentence that states its premise as ", and thus …" — the coordinated tail is thus's territory (250 "and thus" against 122 "and hence" and 77 "and therefore"). A third option, for a consequence that is a property of a subject already on stage, is to drop the adverb after the auxiliary: "X is therefore Y" (99 post-auxiliary uses). The live opposition is fronted-connective sentence versus coordinated tail, not one word versus another.

**Why it works.** The three words are not synonyms in use; they are three weights. Measured over the corpus: "thus" (811 uses) and "hence" (540) live inside sentences — two-thirds of every lower-case use of each rides on a coordinating "and" (268 of 402 for thus, 122 of 181 for hence). "Therefore" (1,003) fronts 69% of the time, and its embedded uses are mostly post-auxiliary ("is therefore" 72, "are/can/will therefore" 25) rather than "and therefore" (77). A sentence boundary is an assertion of importance, so a draft that gives every micro-inference its own "Therefore," tells the reader to brake for nothing, and by the time the real conclusion arrives the signal is spent.

**Seen in.** kcore, am-tree, ch, lis, psi, PacTree (sampled from 8-10 papers for this sub-topic, not all 119)

- "The cost validation step is proportional to the number of vertices in the sample mode, and thus is bounded by the active set size. Therefore, the proof in Thm. 3.1 still holds." — *kcore*, Sec. 4.1.5, Cost Analysis

- "The second primitive, Calibrate, modifies the tree to obey the AM-rule, and thus restores the logarithmic tree height." — *am-tree*, Introduction

- "Therefore, we need a parallel data structure that supports frequent and concurrent insertions, while providing fast query performance." — *ch*, Sec. 4

**Violation signature.** Three or more short sentences in a row each opening "Therefore," / "Thus," / "Hence," for steps no reader would dispute, so the paragraph reads as a numbered chain rather than as an argument with one destination. The mirror-image defect: the paragraph's actual conclusion arrives buried in a tail clause after "and thus", with no sentence of its own.

**Revision.**

- Before: Each firm faces the same input price. Therefore, marginal cost is identical across firms. Therefore, the cost-minimising allocation is symmetric. Therefore, welfare depends only on the aggregate quantity.
- After: Each firm faces the same input price and thus has identical marginal cost, which makes the cost-minimising allocation symmetric. Therefore, welfare depends only on the aggregate quantity.

**Do not apply when.** Inside a step-by-step proof or derivation, where each step is a separate assertion the reader must be able to cite back to — there a per-step "Therefore, X" is the register, and the corpus does exactly this in its analysis sections. Do not compress when the consequence itself needs qualification, a citation, or a subject with its own modifiers; a tail clause carrying all that is worse than a sentence. And do not treat this as a ranking of the three adverbs: swapping "Therefore," for "Hence," at the front of a sentence changes nothing, since hence fronts almost as often as therefore (64% vs 68%).

<sub>Verifier: The three-weights framing is half wrong. The pattern claims "thus (811) and hence (540) live inside sentences" against a boundary-taking "Therefore". Measured: hence is 64% sentence-initial (^Hence, 265) against therefore's 68% (^Therefore, 464) — the digest itself bands hence at 65%, so "hence lives inside sentences" contradicts the yardstick. Only thus genuinely embeds (47% initial). The "and" claim survives for the embedded uses (and thus 250, and hence 122, and therefore 77), and "its embedded uses are mostly post-auxiliary" is an overstatement (AUX+therefore 99 vs and-therefore 77). What </sub>

---

## Put "however" directly behind whatever carries the contrast

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** Front "However," when the whole proposition turns. When only one constituent is contrastive — the subject ("The strict version, however, …") or a scope frame ("In the placebo group, however, …") — lead with that constituent and set "however" immediately after it, between commas. The rule is positional and easy to apply: the word sits behind the term that changed.

**Why it works.** Placement is measured: 878 sentence-initial, 188 medial, 14 final; the digest puts fronting at 78% of uses. The medial cases are not a tic. In them, the element that precedes "however" is almost always the swapped variable — a different structure, a different regime, a different data condition. Fronting those would put a contentless "However," in first position and make the reader wait to learn what changed, whereas embedding delivers the changed term in the reader's first three words. Sentence openings are where this corpus does its signposting: 46.4% of sentences open on a bare subject and 13.8% on a prepositional frame, against 6.4% on a connective.

**Seen in.** am-tree, kcore, xu-ppcsr-alenex-21, psi, PacTree (sampled from 8-10 papers for this sub-topic, not all 119)

- "The strict AM-tree, however, requires maintaining the child pointers in each node, which may increase performance overhead in practice." — *am-tree*, Introduction

- "On sparse graphs, however, Julienne may have poor performance due to the overhead of enabling race-freedom and fully synchronized subrounds in the offline algorithm." — *kcore*, Sec. 6, Experiments

- "It requires that the writer is sequentialized, however." — *xu-ppcsr-alenex-21*, body, comparison with prior structures

**Violation signature.** Every contrastive sentence in the draft opens "However,", including ones whose contrast is a single swapped noun or condition that then sits buried in mid-sentence — visible as consecutive paragraphs beginning with the same word. Also: a medial "however" without its pair of commas, or one placed after a constituent that is not the thing that changed.

**Revision.**

- Before: Serum titres rose within a week in the vaccinated group. However, titres in the placebo group stayed at baseline for the full trial.
- After: Serum titres rose within a week in the vaccinated group. In the placebo group, however, titres stayed at baseline for the full trial.

**Do not apply when.** When the contrast is in the predicate — the same subject, now behaving unexpectedly — front it; hunting for a constituent to hang "however" on only adds commas. And clause-final "however" is nearly extinct here (14 uses in 1.1M words): keep it for a genuine afterthought caveat, at most once in a paper.

<sub>Verifier: Move, rationale and signature all hold. My recount gives 795 initial / 214 medial / 13 final (the pattern's 878/188/14 drifts slightly, direction unchanged), and fourteen randomly sampled medial cases confirm the functional claim that the constituent before "however" is the swapped variable: "In our case, however", "In the Insert version, however", "These frameworks, however", "If the desired memory is not in cache, however". The positional rule is mechanical enough to apply to a draft, and the signature (every contrastive sentence opening "However,"; a medial however missing its commas) is de</sub>

---

## Add with an embedded "also"; keep "Also," off the front by default; promote to "Furthermore," only when the addition opens a new unit

> Narrowed after corpus measurement contradicted the original claim.

**Move.** To add one more thing about a subject already on stage, put "also" after the subject or auxiliary — "We also show …", "The structure also supports …" — so the addition costs the reader no structural work; that is what happens to 94% of the corpus's "also" (2,331 of 2,478 uses clause-internal, "We also …" opening 402 sentences). Do not let "Also," become your default additive connective, and never open a paragraph with it: of 139 sentence-initial uses, 7 stand at a paragraph's head. When the added item really is a new top-level item that should be flagged as one, front "Furthermore," or "In addition," instead.

**Why it works.** The corpus keeps two additive registers and nothing in between: a silent one inside the clause and a marked one at the sentence front. "Also" is sentence-initial in only 6% of its uses; 668 sit between a subject and its verb, and "We also …" alone opens 424 sentences. Fronted "Also," accounts for 132 uses in 1.1M words and clusters in a handful of papers, while "Furthermore," (207 sentence-initial) and "In addition," (65) are spread across the corpus. In all eight papers I read there is not one sentence-initial "Also,". The reason is functional: a fronted connective claims a discourse boundary, and "Also," claims one while carrying no information about what kind — so it wastes the strongest position in the sentence.

**Seen in.** psi, lis, kcore, am-tree, p2307-wheatman (sampled from 8-10 papers for this sub-topic, not all 119)

- "We also present comprehensive experiments comparing the performance of various parallel spatial indexes and share our findings at the end of the paper." — *psi*, Abstract

- "We also extend our algorithm to the weighted LIS (WLIS) problem, which has a similar DP recurrence as LIS but maximizes the weighted sum instead of the number of objects in an increasing subsequence." — *lis*, Introduction

- "Furthermore, we design a hierarchical bucket structure to optimize performance for graphs with high coreness values." — *kcore*, Abstract

**Violation signature.** Two or more sentences beginning "Also," in one paragraph, each really a further predicate of the same subject; or an "Also," standing at the head of a paragraph. A single fronted "Also," inside a paragraph is not by itself a defect. The opposite tell: "Furthermore," spent on one more small predicate of the subject already in play, so the reader braces for a new point and gets a footnote.

**Revision.**

- Before: The model predicts the observed price path. Also, it reproduces the volume spike at the announcement. Also, it is robust to the choice of window.
- After: The model predicts the observed price path and reproduces the volume spike at the announcement. It is also robust to the choice of window.

**Do not apply when.** When the added item genuinely opens a new unit of the argument — a new contribution, a new body of evidence, usually with a new subject — burying it in an embedded "also" hides the seam, and "Furthermore," is right. Inside a list already run on "First, … Second, …", let the ordinals carry the addition rather than stacking "also" on top of them. And the target is the habit, not the token: sentence-initial "Also" appears 139 times across 55 of 119 papers, so one mid-paragraph is inside the register.

<sub>Verifier: The preference is right; the prohibition and its supporting claim are not. "Also" is overwhelmingly clause-internal (2,331 of 2,478 uses; "We also …" opens 402 sentences), which fully supports the default. But the pattern says fronted "Also," "clusters in a handful of papers", and that is contradicted at 119: sentence-initial "Also" appears 139 times across 55 of 119 papers (113 "Also," across 46), most of them one or two per paper — a thinly spread minority form, not a handful of offenders. The agent's "in all eight papers I read there is not one sentence-initial Also," is true of its sample </sub>

---

## Use the register's common word for each relation; do not reach for a rarer synonym to avoid repeating yourself

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Fix one word per logical relation and reuse it across the paper: contrast is "however", side-by-side comparison is "in contrast", likeness is "similarly", consequence is "therefore"/"thus"/"hence". Do not substitute "nevertheless", "nonetheless", "conversely", "by contrast", "on the contrary", "likewise", "consequently" or "accordingly" merely to avoid using the same word twice — a reader who meets a different word assumes a different relation and starts hunting for a distinction you never intended. If two neighbouring sentences would both open on the same connective, the repair is to join or reorder them, not to swap in a rarer word.

**Why it works.** The repertoire in this register is tiny and worked hard. However 1,022 against nevertheless 17, nonetheless 6, notwithstanding 0. In contrast 106 against by contrast 2, conversely 4, on the contrary 2. Similarly 156 across 76 papers against likewise 4 and analogously 0. Therefore 1,003, thus 811, hence 540, against consequently 19 and accordingly 13. Papers repeat the same connective two sentences running rather than substitute a rarer synonym. A connective is a signpost, not a word: a reader who meets a different word assumes a different relation and starts looking for a distinction the writer never intended.

**Seen in.** p2307-wheatman, lis, kcore, psi, am-tree (sampled from 8-10 papers for this sub-topic, not all 119)

- "However, the hash set was worse on algorithms compared to the B-tree. However, specialized containers can overcome the query-update tradeoff on the largest batches" — *p2307-wheatman*, Sec. 6, Experiments

- "Therefore, the smallest low-bit among them must be exceptional and will be handled by the base cases on Lines 7–11. Therefore, for each key in 𝐵, only one of the recursive calls will be “meaningful”." — *lis*, Sec. 5, parallel vEB tree

**Violation signature.** One paragraph carrying "however", "nevertheless" and "on the other hand" for what is a single contrast; or a section-length thesaurus spread — "thus", "consequently", "accordingly", "hence" — with no principle governing which appears where. Any "notwithstanding", "conversely" or "likewise" used as a connective is worth challenging: together they amount to about a dozen uses in 1.1M words, against 1,022 for "however".

**Revision.**

- Before: Antibody levels fell after six months. Nevertheless, protection against severe disease persisted. Conversely, protection against infection did not.
- After: Antibody levels fell after six months. However, protection against severe disease persisted. Protection against infection, however, did not.

**Do not apply when.** When two markers in one passage genuinely mark different relations — a concession and a consequence — collapsing both onto one word is worse than using two. And this is a rule about vocabulary, not a licence to stack connective-opening sentences: identical back-to-back openings are rare here (18 adjacent pairs in 10,907 paragraphs), and three in a row is a sign the sentences should be joined or reordered.

<sub>Verifier: Two claims are bundled here and only one holds. The repertoire claim is strongly confirmed and is worth keeping precisely because it contradicts the usual advice to vary word choice: however 1,022 against nevertheless 17 / nonetheless 6 / notwithstanding 0 as a connective (its 11 raw hits are 10 copies of a funding-boilerplate sentence plus one preposition); in contrast 130 against by contrast 2, conversely 4, on the contrary 5; similarly 221 in 90 papers against likewise 6 and analogously 3; therefore/thus/hence 1,975 against consequently 24 and "Accordingly," 12. The licence to repeat "inclu</sub>

---

## Delete the connective when parallel syntax or a matched pair of frames already carries the relation

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** When you compare several items on the same properties, write them in the same grammatical shape — [item] [verdict on property A] [verdict on property B] — and put no connective between them; the repeated frame is the comparison. When you split one claim across two domains, open the two sentences with a matched pair of scope frames ("In theory, … In practice, …") and keep the rest of the wording parallel; the pairing is the connective. In both cases the first words of each sentence should be the item or the frame, not a signpost.

**Why it works.** This corpus signals structure by what a sentence starts with, not by a marker planted in front of it: 46.4% of sentences open on a bare subject, 13.8% on a prepositional frame, and only 6.4% on a connective — and of paragraphs with three or more sentences, just 1.8% open with any fronted connective at all. A repeated syntactic shape tells the reader "same kind of claim, next item" before they have finished three words, which is faster than a connective can; a connective in front of an already-parallel sentence adds a word and takes credit for work the syntax has already done.

**Seen in.** psi, am-tree, lis, kcore, ch (sampled from 8-10 papers for this sub-topic, not all 119)

- "Orth-trees offer competitive query performance and faster updates due to their simpler invariant (splitting at spatial medians). R-trees/BVHs encompass a large family of solutions; they usually provide the simplest and fastest updates but slower queries." — *psi*, Introduction

- "In theory, the cost bounds of using AM-trees for temporal graphs match the best-known results using linkcut trees or other data structures. In practice, we compare AM-tree to both the theoretically-efficient solution and stateof-the-art practical solutions." — *am-tree*, Conclusion

- "For example, in 3D games, moving objects must be reflected quickly to affect lighting and collision detection, whereas GIS applications often ingest high-volume sensor streams where total update throughput is critical." — *psi*, Introduction

**Violation signature.** A comparison list in which each item is introduced by a different connective — "On the other hand", "Meanwhile", "By comparison" — while the sentences themselves have unrelated shapes, so the reader gets the relation only from the marker and never sees the pattern. Also: a paragraph in which the first sentence of every item begins with a connective rather than with the item's name.

**Revision.**

- Before: Randomised trials give unbiased estimates but are costly to run. On the other hand, natural experiments are cheaper, although identification is weaker. Meanwhile, structural models can extrapolate, but they depend on functional-form assumptions.
- After: Randomised trials give unbiased estimates but are costly to run. Natural experiments are cheaper, with weaker identification. Structural models extrapolate beyond the sample, at the cost of functional-form assumptions.

**Do not apply when.** When the items are not genuinely parallel — different kinds of claim, or different properties for each — forcing them into one shape distorts them, and an honest connective beats a false symmetry. When the relation is a reversal rather than a comparison (the second sentence denies what the first implied), parallel shape cannot show it: mark it explicitly. And the target is the sentence-front signpost only: joining two compared items inside one sentence with a subordinator ("…, whereas …" — 80 uses, 98% of them mid-sentence) is the corpus's normal alternative, not a violation.

<sub>Verifier: The move rests on the two strongest numbers in the whole measurement set — 46.4% of sentences open on a bare subject and 13.8% on a prepositional frame against 6.4% on a connective, and only 1.8% of multi-sentence paragraphs open on a fronted connective — and it converts them into something a writer can act on (write the items in one shape, or pair the frames, and delete the signpost). Not a platitude: it names the replacement device, not just the deletion. Exemplar 1 (Orth-trees / R-trees, two items in matched shape, no connective) and exemplar 2 ("In theory, … In practice, …") both land. Exe</sub>

---

## End the sentence on the new item; open the next sentence with it

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Put what the reader already has before the main verb and what you are introducing at or near the end of the clause. When that end-item is a term the argument will keep using, make it the subject of the next sentence — verbatim or shortened — so it is picked up while it is still fresh. Once a count has been announced ('two simple primitives'), ordinals carry the relay: 'The first primitive, X, ...' / 'The second primitive, Y, ...'. Relay the terms that carry the argument, not every sentence: the corpus links only about a quarter of consecutive sentence pairs this way and lets the rest open on a fronted frame or a plain new subject, and even its own chains typically run two sentences before handing off to an adjunct.

**Why it works.** The corpus reaches its main verb fast (median 5 words before it, p75 9) and appends qualification rightward, so the last constituent is the reader's freshest item. With 46.4% of sentences opening on a bare subject, the subject slot is where cohesion actually gets carried; a new term introduced sentence-finally and picked up as the next subject is never left dangling. In BF the chain runs 'binary forking' -> 'efficient scheduling' -> 'the number of available processors' across three sentences, each subject lifted verbatim from the tail before it.

**Seen in.** BF, am-tree, stepping, ppsp, readwrite, cbfs (sampled from 8-10 papers for this sub-topic, not all 119)

- "Binary forking is important since it allows for efficient scheduling in both theory and practice, especially in the asynchronous setting [2, 11, 26, 35]. Efficient scheduling can be achieved even when the number of available processors changes over time [11]" — *BF*, Introduction

- "The binary-forking model falls into the class of multithreaded models [11, 26, 34, 35, 44]. Multithreaded computational models assume a collection of threads (sometimes called processes or tasks) that can be dynamically created, and generally run asynchronously." — *BF*, Section 2, Models and Simulations

- "Time information can be integrated in different settings. A classic setting is that each edge has a timestamp, and a query, such as connectivity, is augmented with a time interval" — *am-tree*, Introduction

**Violation signature.** A term that arrives at the end or in the middle of a sentence, is plainly meant to matter, and then never returns as a subject — or returns three or four sentences later, so the reader must search backwards for it. Second tell: a term introduced deep inside a long sentence and made the subject of the next one, so the hand-off jumps over material the reader has to re-scan. Do not flag a sentence merely because its subject is new; check whether a term the paragraph depends on was dropped after its first appearance.

**Revision.**

- Before: Antigen dose determines the strength of the response. T-cell exhaustion follows chronic stimulation. Checkpoint blockade can reverse this state in some patients.
- After: The strength of the response is set by antigen dose. A sustained high dose keeps T cells chronically stimulated, and chronic stimulation drives them into exhaustion. Exhaustion is reversible: checkpoint blockade restores function in some patients.

**Do not apply when.** Most sentences do not relay at all, and a subject with no link to the previous tail is the corpus's commonest shape, not a defect — do not audit every transition. Contrastive or emphatic focus deliberately fronts the new item ('Antigen dose, not receptor affinity, sets the threshold'), and a sentence whose entire point is the new item has nothing left to put after it. Do not relay through a term you will never use again; forcing a hand-off in every sentence produces a daisy chain that wanders. Skip the check on a paragraph's first sentence, which has a different job, and on any sentence whose link is carried by a fronted adjunct instead of the subject. The paragraph's last sentence should land on the consequence, not on a hook for a sentence that is not coming.

<sub>Verifier: End-focus is sound and consistent with the corpus (main verb at median word 5, qualification appended rightward), and all five quotes really do show a tail item lifted into the next subject. What fails at 119 papers is the universal form 'repeat, so every subject can be found in the previous sentence's tail'. I measured all 41,156 consecutive sentence pairs inside paragraphs: counting a link whenever the sentence's first four words contain an anaphor (This/These/It/They/Such) OR a content stem repeated from the previous sentence, only 27.6% link back at all and only 15.8% link to the previous </sub>

---

## Introduce a new entity in the predicate of a sentence whose subject is already given

> Narrowed after corpus measurement contradicted the original claim.

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** When a new named thing enters mid-paragraph, prefer not to make it the subject of the sentence that introduces it. Build the subject out of nouns the reader already holds — typically a category noun carrying a superlative, ordinal, or quantifier: 'One of the most widely used techniques', 'One major reason for this gap', 'a known optimization', 'one potential reason' — and let the new name arrive after the verb, at the end of the clause. The next sentence can then take that name as its subject. The subject does double duty: it re-asserts the link to the previous sentence while the superlative or quantifier tells the reader how the new item ranks among things of its kind.

**Why it works.** This copular identifying sentence is the corpus's workhorse for presenting a new entity, and it does two jobs at once: the subject re-asserts the link to the previous sentence while the superlative or quantifier tells the reader how the new item ranks among things of its kind. Note what it replaces: the bare frame 'There is/are X that ...' occurs exactly once in 1.1M words. This is not a blanket ban on existentials — 'there is/are' appears 862 times and 'there exists' 177 — but the corpus does not use an empty existential subject plus a stacked restrictive clause to carry content that a real subject could carry.

**Seen in.** ppsp, cbfs, geograph, stepping, am-tree (sampled from 8-10 papers for this sub-topic, not all 119)

- "many existing techniques can accelerate PPSP. One of the most widely used techniques is the bidirectional search (BiDS)." — *ppsp*, Introduction

- "we are unaware of any work parallelizing the BiDS. One major reason for this gap is the inherent distinction in the approach of parallel SSSP compared to its sequential counterpart." — *ppsp*, Introduction

- "Sequentially, when running BFS on a cluster of nearby vertices, a known optimization is using bit-parallelism." — *cbfs*, Abstract

**Violation signature.** A term the reader has never met standing as the grammatical subject of the very sentence that first introduces it, mid-paragraph, where the previous sentence had a link to offer — most visibly an acronym, a coined method name, or a proper name of a technique. Not a tell: a new topic noun as the subject of a paragraph's or section's first sentence, and not existentials as such — 'There are two reasons that...', 'There are several algorithms that...' are normal in this register (191 sentence-initial existentials in 87 of 119 papers). An existential is only a defect when its relative clause carries the whole predicate about one new entity that could simply have been the subject.

**Revision.**

- Before: Bystander activation accounts for part of the effect. It occurs when cytokines stimulate T cells whose receptors do not match the antigen.
- After: One mechanism behind the effect is bystander activation: cytokines stimulate T cells whose receptors do not match the antigen. Bystander activation is hard to quantify, and most estimates of it are indirect.

**Do not apply when.** At a paragraph or section opening, where the new noun is the topic being announced, put it in the subject and spell it out in full — the presentational frame is for mid-paragraph arrivals. Skip it when the entity is already familiar to the readership (a standard method, a canonical dataset, a well-known result), where the frame reads as ceremony; and when the subject already carries a strong given link and the new item can ride in the predicate of an ordinary transitive clause. Do not stack them: three consecutive 'One reason is ... / Another example is ...' sentences flatten a paragraph into a list. An existential with a count ('There are two reasons that...') is the register's normal way to open an enumeration or a survey of prior work; leave it alone.

<sub>Verifier: The frame itself is real: sentence-initial 'One/Another + category noun' (reason, example, approach, technique, way, challenge, advantage, ...) occurs 203 times in 86 of 119 papers, so the device transfers. Three defects. (1) EXEMPLAR MISMATCH: the geograph quote demonstrates the inverse of the claimed move. In context the paragraph has just discussed graph conversion for semi-supervised learning; 'Transportation planning is another example where the approach of converting data to a graph format is commonly used' puts the NEW item ('Transportation planning') in the subject and the GIVEN catego</sub>

---

## Second mention definite and short: strip the modifiers when the term comes back

**Move.** Bring a term back as a subject with 'the' and with its modifiers stripped: 'the binary-forking model' returns as 'The model'; 'a collection of threads' returns as 'Each thread'; 'a cache miss' returns as 'The cache miss'; a name introduced with a trailing 'which is...' returns as 'It'. The article says 'you have this now'; the shortening says 'and it is the same one', and it keeps the subject light enough to reach the verb quickly. On first mention, give the reader something to attach the later 'the' to: a common-noun coinage takes an indefinite article, a named artifact takes its full name with the abbreviation in parentheses, and either way the defining material goes in a trailing non-restrictive relative or appositive rather than inside the subject.

**Why it works.** The article and the length of the noun phrase are the cheapest given-new markers English has, and they cost no extra words. Shortening also keeps the subject light, which is what lets the corpus reach its main verb at a median of five words. A trailing non-restrictive relative clause ('which is a hybrid of Dijkstra's algorithm and the Bellman-Ford algorithm') is the standard place to load the definition, precisely so the next sentence can open on a one-word subject.

**Seen in.** readwrite, BF, stepping, am-tree, cbfs (sampled from 8-10 papers for this sub-topic, not all 119)

- "Any reference to a word in a block that is not resident is a cache miss and requires a memory transfer from the secondary memory. The cache miss can replace a block in the cache with the loaded block" — *readwrite*, Section 2, Preliminaries and Models

- "In this paper we present several results on the binary-forking model. The model assumes a collection of threads that can be created dynamically and can run asynchronously in parallel. Each thread acts like a standard random-access machine (RAM)" — *BF*, Introduction

- "most existing parallel SSSP implementations [12, 45, 72, 92] are based on Δ-Stepping [70], which is a hybrid of Dijkstra’s algorithm [48] and the Bellman-Ford algorithm [13, 52]. It determines the correct shortest distances in increments of Δ" — *stepping*, Introduction

**Violation signature.** A noun phrase wearing 'the' on its first appearance in the paper, with no antecedent anywhere earlier. The mirror-image tell: the same five- or six-word noun phrase repeated in full as the subject of four consecutive sentences. A third: an entity introduced as 'a X' that returns under a different word entirely, so the reader cannot tell whether it is the same thing.

**Revision.**

- Before: The regulatory sandbox reduced compliance costs. A regulatory sandbox is a supervised environment in which firms test products under relaxed rules. Within that supervised environment for testing products under relaxed rules, costs fell by 12%.
- After: Several regulators have set up a regulatory sandbox, a supervised environment in which firms test products under relaxed rules. The sandbox cut compliance costs by 12%.

**Do not apply when.** Proper names, acronyms defined in parentheses, generics and unique referents legitimately skip the indefinite first mention: 'the literature', 'the 2008 crisis', 'the innate immune system', and the paper's own headline artifact, which the title and abstract have already introduced. And when two entities in play share a head noun, the shortening is what creates the ambiguity — 'The model' cannot serve while both a structural model and a reduced-form model are live, so keep the distinguishing modifier for as long as the contrast is open.

<sub>Verifier: The load-bearing half is real craft and is what the exemplars actually show: strip the modifiers when the term comes back ('the binary-forking model' returns as 'The model'; 'a collection of threads' as 'Each thread'), and load the definition into a trailing non-restrictive relative or appositive so the next sentence can open on a one-word subject ('Delta-Stepping [70], which is a hybrid of Dijkstra's algorithm and the Bellman-Ford algorithm. It determines...'). That is consistent with the corpus reaching its main verb at median word 5, and the mirror-image tell (the same six-word noun phrase </sub>

---

## Package the previous sentence into a noun phrase, and make that the subject

**Move.** When the given information is a whole proposition rather than an entity, compress it into a noun phrase headed by a noun that classifies it, and put that phrase in subject position: 'This complexity is impractical', 'This process is repeated', 'This work has focused on', 'writing such programs can be challenging'. Choose the head noun deliberately — it is your reading of what the previous sentence was.

**Why it works.** Measured across the corpus, 'This/These + noun' occurs 1,799 times against 915 bare demonstrative subjects, so about two thirds of demonstratives carry a noun; 'such + noun' occurs 1,635 times in 118 of the 119 papers. Beyond disambiguation, the classifying noun does interpretive work no pronoun can: calling the previous sentence a 'gap', a 'complexity', an 'observation', or a 'process' tells the reader how to file it before the new predicate arrives.

**Seen in.** ED, am-tree, readwrite, geograph, BF (sampled from 8-10 papers for this sub-topic, not all 119)

- "The classic dynamic programming (DP) solution can compute edit distance in O(nm) work (number of operations) between two strings of sizes n and m. This complexity is impractical if the input strings are large." — *ED*, Introduction

- "This operation first identifies whether 𝑦 has a heavy child 𝑥. If so, 𝑥 will be promoted and removed from 𝑦’s subtree. This process is repeated until 𝑦 is balanced." — *am-tree*, Section 4, Strict AM-tree

- "Several papers [7, 18, 21, 28, 30, 36] have looked at read-write asymmetries in the context of NAND flash memory. This work has focused on" — *readwrite*, Introduction, Related Work

**Violation signature.** A sentence opening 'This is ...', 'This means ...', 'These allow ...', 'It follows ...' where the sentence before it offers two or more things the demonstrative could point at. Two such sentences in a row, or a paragraph whose every back-reference is a bare 'it' or 'this', is the stronger signal.

**Revision.**

- Before: The estimator requires the instrument to be uncorrelated with unobserved ability. It is hard to defend for schooling instruments.
- After: The estimator requires the instrument to be uncorrelated with unobserved ability. This exclusion restriction is hard to defend for schooling instruments.

**Do not apply when.** The bare form is not banned, and a rule saying so would contradict the measurements: bare 'This/These' opens 915 clauses in this corpus. It is the right choice when the antecedent is the entire immediately preceding clause and nothing competes — BF writes 'However, this has a O(log n) overhead in span. This means that algorithms that are optimal on the PRAM are not necessarily optimal when mapped to the binary-forking model.' If the only noun you can find is a filler ('This fact', 'This aspect', 'This thing'), use the bare form. Avoid it too where the classifying noun would smuggle in a claim you have not established — do not call something 'This problem' before you have shown it is one.

<sub>Verifier: The best-grounded pattern in the topic and the only one whose do_not_apply_when actively defends itself against the measurements rather than glossing them: it states outright that the bare form is not banned, cites the 915 bare demonstrative subjects, gives a corpus example of the bare form used correctly, and adds the genuinely useful refinement that a filler head noun ('This fact', 'This aspect') is worse than the bare form. The 1,799-vs-915 and 'such + noun' 1,635/118-papers figures match the digest and validation file exactly. The four exemplars all illustrate: 'This complexity is impracti</sub>

---

## Carry the link in a fronted adjunct when the subject cannot

> Narrowed after corpus measurement contradicted the original claim.

**Move.** When the subject has to be new material, or has to be 'we', move the given item into a short fronted phrase and let the subject be whatever the clause needs: 'Regarding the relationships between objects, time can usually be a crucial component'; 'Using the query graph, we develop algorithms ...'; 'As for (ii), we choose not to ...'; 'Given the broad applicability, ...'. Enumerated labels created earlier — (i), (ii), a numbered goal, a named step — make especially cheap handles for these frames. Keep the frame to a phrase: the corpus hits its main verb at a median of 5 words and a p90 of 15, so one adjunct, not a stacked pair.

**Why it works.** 12.3% of the corpus's sentences take 'we' as the subject, and many more put a new entity there; none of those subjects can serve as the anaphoric link. The corpus compensates in the pre-subject slot: 13.8% of sentences open with a prepositional frame and 2.7% with a participle. Keep the frame short — the corpus hits its main verb at a median of 5 words and a p90 of 15, so this is a phrase, not a stacked pair of clauses.

**Seen in.** am-tree, readwrite, ppsp, geograph, BF (sampled from 8-10 papers for this sub-topic, not all 119)

- "It is relevant to lots of applications as it abstracts real-world objects as vertices and their relationships as edges. Regarding the relationships between objects, time can usually be a crucial component." — *am-tree*, Introduction

- "Emerging NVMs, in contrast, do not suffer from (i) because they can write arbitrary bytes in-place. As for (ii), we choose not to focus on wear out" — *readwrite*, Introduction, Related Work

- "Using the query graph, we develop algorithms for batch PPSP queries based on both BiDS and SSSP." — *ppsp*, Introduction

**Violation signature.** A 'we'/'our'-subject sentence that opens cold on material the reader has not met, so how it follows from the previous sentence only resolves at the end of the clause. Second tell: in a run of we-sentences, the word that connects each sentence back to the last sits after the verb, or is absent — read each sentence and count how far in you get before finding it. A run of three consecutive 'We' openings is not itself the defect (90 of 119 papers in this corpus contain one); the missing pre-subject link is.

**Revision.**

- Before: Two robustness checks are reported in Table 4. We re-estimate the model on the 1995-2005 subsample and we drop the top decile of firms.
- After: Two robustness checks are reported in Table 4. For the first, we re-estimate the model on the 1995-2005 subsample; for the second, we drop the top decile of firms.

**Do not apply when.** The subject already carries the link — 'In this setting, the model assumes ...' where 'the model' was the last sentence's topic adds nothing. A run of we-sentences that is genuinely a list of parallel contributions ('We show ... We prove ... We implement ...') is a parallelism device, and inserting a frame before each one breaks the parallelism it depends on. Do not let frames accumulate: two stacked adjuncts push the main verb past the corpus's p90 of 15 words. And a frame that only restates what the reader can see ('In this paragraph, ...') is filler, not a link.

<sub>Verifier: The move is well grounded and fills the exact gap the end-focus pattern leaves: 13.8% prepositional frames plus 2.7% participials against 12.3% we-subjects, and the corpus's median of 5 words before the main verb correctly forces this to be a phrase rather than stacked clauses. The exemplars illustrate ('Regarding the relationships between objects...', 'As for (ii), we choose not to...', 'Using the query graph, we develop...'), and the enumerated-label handle ((i)/(ii)) is a genuinely transferable trick. Two corrections. (1) The second tell fails against the corpus: runs of three or more conse</sub>

---

## Open a paragraph on its topic spelled out in full, and demote the connective

**Move.** At a paragraph boundary the antecedent is too far back for a pronoun, so restate the link as a full noun phrase and put it in the opening subject slot: 'The strict AM-tree, however, requires ...'; 'The approach of converting the original data into a graph is commonly used ...'; 'Edit distance is a fundamental problem ...'. If the paragraph turns against the previous one, move the connective past the subject rather than fronting it. A bold run-in heading can supply the topic instead, and only then may the first sentence open on a bare 'This'.

**Why it works.** Of the 7,188 paragraphs with three or more sentences in this corpus, only 127 — 1.8% — open with a fronted connective. This is not connective-avoidance: 'however' appears 1,022 times in 118 of the 119 papers and is sentence-initial 78% of the time. The connective opens sentences inside a paragraph; the noun opens the paragraph. Repeating the noun in full also re-anchors a reader who skipped ahead, which a pronoun cannot do across white space.

**Seen in.** am-tree, geograph, ED, readwrite, BF (sampled from 8-10 papers for this sub-topic, not all 119)

- "The strict AM-tree, however, requires maintaining the child pointers in each node, which may increase performance overhead in practice." — *am-tree*, Introduction, opening of the lazy-version paragraph

- "The approach of converting the original data into a graph is commonly used in machine learning to perform semisupervised learning [54]. Here the data points are associated with feature vectors" — *geograph*, Introduction

- "Edit distance is a fundamental problem in computer science, and is introduced in most algorithm textbooks (e.g., [14, 15, 22])." — *ED*, Introduction, second paragraph

**Violation signature.** Read only the first word of every paragraph. If 'However', 'Moreover', 'Furthermore', 'In addition', 'Therefore', or 'Also' turns up there more than once or twice in a whole paper, the paragraphs are being welded together by connective instead of by topic. Second check: a paragraph opening on a bare 'It', 'This', or 'They' with no run-in heading above it to supply the referent.

**Revision.**

- Before: However, the wage premium disappears once we control for firm age.

Moreover, the German sample shows the same pattern.
- After: The wage premium, however, disappears once we control for firm age.

The German sample shows the same pattern.

**Do not apply when.** A paragraph that genuinely reverses the whole preceding stretch of argument can earn a fronted 'However' — the corpus does exactly this 127 times. The finding is about habit, not about any single instance. It also does not apply where a run-in heading, a numbered list item, or a definition environment already names the topic, or in a short results paragraph whose first sentence is a pointer to a table or figure.

<sub>Verifier: I re-ran this independently rather than trusting the validation file, and it holds: of 7,188 paragraphs with three or more sentences, 108 open with a fronted connective on my connective list (validation.md reports 127 with a slightly wider list) — median 1 per paper, and only 9 of 119 papers exceed two. That makes the violation signature's threshold ('more than once or twice in a whole paper') empirically calibrated rather than guessed, which is rare among these patterns. The pattern is also careful in the right place: it does not turn into connective-avoidance, and it states the discriminatio</sub>
