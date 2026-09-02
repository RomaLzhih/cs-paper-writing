# Pass 4 — Shape

**Ask:** Does the main verb arrive early, and is everything after it hung on the right hinge?

**Do not touch in this pass.** Do not convert nouns to verbs or delete wrappers while restructuring — that is Pass 5, and doing it here means rebuilding the same sentence twice. Do not front a frame you demoted in Pass 1, and do not re-front a connective. Do not flag an isolated fronted frame: one sentence in five opens on one and about 90% of those have no fronting neighbour, so scope-setters, conditionals and locatives are the register's norm. Do not flag every bare 'which' (about half the un-commaed uses are the pied-piped 'in which / for which' form), and do not treat ', which leads to' as an error — the participial preference is 2:1, not a rule.

9 patterns.

---

## Complete the subject-verb bond early, then build the long sentence rightward

**Move.** Build a 35+ word sentence as a short complete predication followed by rightward expansion — a colon list, a 'which' relative, a 'where' gloss, a parenthetical — rather than by stacking modifiers between subject and verb or piling clauses in front of the subject. Keep the main verb inside about a dozen words even at that length: the corpus reaches it at a median of word 5, and only a tenth of its sentences pass word 15 first. Long sentences carry a colon, a 'where', a 'which' or a parenthesis three times as often as mid-length ones; that is where their length comes from.

**Why it works.** Measured over 55,212 non-bibliography sentences: the main verb arrives at median word 3 in sentences of 12 words or fewer, word 5 at 13-29 words, and still word 7 at 35+ words — length barely moves the subject-verb bond. What moves is what comes after it: colons appear in 23.5% of 35+ word sentences against 3.9% of mid-length ones, "where" in 8.9% against 2.0%, "which" in 15.0% against 6.7%, parentheses in 67% against 32%. The reader gets a whole proposition early, and every later clause attaches to something already understood.

**Seen in.** ParChain, FRT, edit-distance, cbfs, kcore, xu-ca-spaa-20, ED (sampled from 8-10 papers for this sub-topic, not all 119)

- "Our framework can be applied for any linkage criteria that satisfies the reducibility property, which ensures that the nearest neighbor distance of clusters can never be smaller as clusters merge (defined more formally in Section 2)." — *ParChain*, Introduction (36 words; verb at word 3)

- "For a graph with n vertices and m edges, our algorithm runs in O(m log n) time with high probability, which improves the previous upper bound of O(m log3 n) shown by Mendel et al. in 2009." — *FRT*, Abstract (37 words; verb at word 11 after an 8-word frame)

- "The suffix array (SA) [42] is a lexicographically sorted array of the suffixes of a string, usually used together with the longest common prefix (LCP) array, which stores the length of LCP between every adjacent pair of suffixes." — *edit-distance*, Sec. 2 Preliminaries (38 words; verb at word 5)

**Violation signature.** A sentence of 30 words or more in which more than about a dozen words pass before the main verb; two stacked introductory clauses before the subject ('Because X, and given that Y, the result ...'); or a subject separated from its verb by an embedded relative clause.

**Revision.**

- Before: Because the survey instrument was revised in 2014, and because the sampling frame, which excluded seasonal workers before that revision, was never reweighted, the year-over-year comparison in Table 3 should be read with care.
- After: The year-over-year comparison in Table 3 should be read with care, because the survey instrument was revised in 2014 and the earlier sampling frame excluded seasonal workers without reweighting.

**Do not apply when.** The condition genuinely governs the whole sentence and the claim cannot be parsed without it first — a "Given X, Y holds" definition, or a scope-setting proviso that would be misread if it arrived late. There the frame precedes, but keep it inside the 12-word ceiling.

<sub>Verifier: The core is confirmed by the corpus-wide numbers: main verb at median word 5, p75 9, p90 15, with qualification appended rightward. My own check of the rightward-expansion claim in 5,906 sentences of 35+ words vs 29,770 mid-length ones confirms the direction on every device: colon 10.5% vs 3.1%, 'which' 17.4% vs 7.2%, 'where' 8.8% vs 2.3%, parentheses 61.5% vs 31.5%. Two fixes. (1) The why's colon figure is inflated — 23.5% vs the 10.5% I measure on cleaned prose; the 3.4x ratio is the durable claim, so state the ratio and drop the raw percentage. (2) The name says 'within about seven words' w</sub>

---

## Flag the plain-words gloss as approximate, and give the precise statement the identical name

> Narrowed after corpus measurement contradicted the original claim.

**Move.** When a term's precise statement needs machinery, attach a one-sentence gloss explicitly marked as approximate — 'Roughly speaking, recorded-once means that each data structure node is the new value of a successful CAS at most once'; 'At a high level, the relaxed PIP model provides similar properties to the classic in-place PRAM model' — and let the exact statement stand wherever it belongs, before or after the gloss. The gloss and the exact statement must use the same term string with no rewording; that identity is what lets the reader treat them as one term instead of two.

**Why it works.** The introduction's reader gets a working meaning without the machinery and the technical reader finds the exact statement later; because both places use the identical string, they read as one term rather than two, which is what makes the deferral safe.

**Seen in.** vcas, PIP, closest, iterative_2, psi, SAGE (sampled from 8-10 papers for this sub-topic, not all 119)

- "This optimization applies to many concurrent data structures that satisfy the recorded-once property we introduce. Roughly speaking, recorded-once means that each data structure node is the new value of a successful CAS at most once." — *vcas*, 1 Introduction — Avoiding Indirection and Other Optimizations

- "At a high level, the relaxed PIP model provides similar properties to the classic in-place PRAM model, and the strong PIP model puts further restrictions on memory allocation that allows PIP algorithms to simultaneously achieve small auxiliary space and low span." — *PIP*, 1 Introduction

- "At a high level, Si′ contains points that are far enough from each other, and the threshold di that defines whether points are "far enough" decreases for increasing i." — *closest*, 2.1 Sparse Partition

**Violation signature.** A coined term introduced with only a forward pointer ('we introduce the notion of X; see Definition 4', 'as defined in Section 5') and no plain-language sense anywhere near it; or a gloss and its precise statement under different names ('we call this the coverage condition' … 'Definition 4 (Reach Property)'). Detector: for each term you coin, check that a reader who stops at the first mention leaves with a usable meaning, and that the string naming it is character-for-character identical in both places.

**Revision.**

- Before: We introduce the notion of exposure-tolerance and prove its properties in Definition 3.2. Section 5 applies the tolerance criterion to the cohort data.
- After: We introduce a property we call exposure-tolerance; roughly speaking, a cohort is exposure-tolerant if raising the dose never lowers the measured response. Definition 3.2 makes exposure-tolerance precise, and Section 5 applies it to the cohort data.

**Do not apply when.** The term is transparent from its parts, or an approximate gloss would be wrong rather than merely imprecise — a gloss a reader could mistake for the definition and then misapply is worse than an honest forward reference. Closest also shows the reverse order is fine: a formal definition first, followed by the "At a high level" gloss. Do not gloss twice.

<sub>Verifier: The gloss device is live: 164 explicitly-marked informal glosses across 67 of 119 papers (At a high level 80, Intuitively 61, Roughly speaking 9, Informally 4), and all three exemplars are genuine glosses attached to their terms. The identical-string requirement is the part that belongs in a terms library and it is sound. But the stated architecture — introduction gloss, machinery deferred to a numbered definition — is a minority arrangement in this corpus and drags portability down with it. Only 25 of the 67 gloss-using papers contain any numbered Definition at all; just 6% of gloss markers a</sub>

---

## Announce the count and the category noun before you enumerate

**Move.** Before the items arrive, write a cataphoric sentence naming how many there are and what kind of thing they are ("two major challenges", "three key optimizations", "several distinct axes"), then deliver exactly that many.

**Why it works.** The reader opens the right number of empty slots before the content arrives, so each item is filed on receipt instead of re-parsed; the count also tells the reader where the list ends, which matters when items grow to paragraph size. A cardinal plus a category noun of this shape occurs in 88/119 corpus papers, and 85/119 use a cataphoric "as follows"; the digests do not measure list structure, so this rests on reading plus my own counts.

**Seen in.** im, pimtrie, ch, kcore, p2307-wheatman, PPM, scc, lis (sampled from 8-10 papers for this sub-topic, not all 119)

- "Two major challenges exist to scale sketch-based approaches to billion-scale graphs. The first is the space." — *im*, 1 Introduction

- "This creates two main challenges for adapting existing radix trees or tries to the PIM setting: (C1) how to map their nodes/edges to PIM modules in a way that achieves good load balance across the modules" — *pimtrie*, 1 Introduction

- "We observe two major challenges. First, identifying the vertices to contract involves simulating contractions on many (if not most) vertices, which calculates distances for numerous vertex pairs." — *ch*, 1 Introduction

**Violation signature.** A list starts cold — the first item appears ("First, ...", a bullet, "One issue is...") with no preceding sentence saying how many items there are or what category they belong to. Or the announcement hedges a number the writer knows ("several factors", "a number of reasons", "various challenges") and then delivers a closed list. Or the announced cardinal does not match the items delivered — says "three", gives four, or gives three and then adds a fourth with "finally".

**Revision.**

- Before: We identify challenges in the current approach. Assay reproducibility varies across labs. In addition, the reference panel is incomplete. Sample sizes are also uneven across cohorts.
- After: The current approach faces three challenges. First, assay reproducibility varies across labs. Second, the reference panel is incomplete. Third, sample sizes are uneven across cohorts.

**Do not apply when.** The enumeration is genuinely open-ended or illustrative — then "such as" or "including" is correct and a cardinal falsely claims the list is exhaustive. Also skip the number when the list is still volatile in drafting and the count is repeated in an abstract, an intro, and a conclusion that will drift apart.

<sub>Verifier: Best-supported pattern in the topic and the agent's own numbers check out: I count 'as follows' at 210 uses in exactly 85/119 papers, matching its claim, and cardinal/quantifier + category noun at 1096 uses in 114/119 (validation independently says 118/119 with a looser regex). Exemplars all demonstrate the announce-then-deliver move (im: 'Two major challenges exist... The first is the space'). Portable, and the violation signature is checkable from a draft alone: count the announced cardinal, count the delivered items. One calibration for whoever writes the skill entry, not a defect: hedged q</sub>

---

## Give every item in a list one grammatical category, and pick the category from the items' job

**Move.** Every item in one list shares a head category — all bare noun phrases, or all finite clauses, or all gerunds — and the list never mixes them. Fitting the category to the items' job (noun phrases for deliverables and artifacts, finite clauses for claims and findings) is a sensible default rather than a corpus rule: the evidence for the fit is a single paper that runs one list of each kind.

**Why it works.** The reader infers the frame from item one and reads the rest as substitutions into it; a switch of category mid-list forces a re-parse and signals, falsely, that the switched item is a different kind of thing. One paper in the corpus runs both lists, four items each, and keeps each internally pure, which shows the choice is conditioned on content type rather than author habit.

**Seen in.** arxiv-2305.04359, scc, kcore, xu-spma-alenex-23, PPM, p2307-wheatman, lis (sampled from 8-10 papers for this sub-topic, not all 119)

- "1. A variety of general and specific techniques to parallelize existing graph-based ANNS algorithms to scale to billions of points (Sec. 3)." — *arxiv-2305.04359*, 1 Introduction, contribution list

- "1. Graph-based algorithms are especially capable at achieving high recall (greater than .9) at the scale of billions of points for QPS in the 10k–200k range." — *arxiv-2305.04359*, 5.6 Conclusions from Experiments

- "(1) Two general techniques (vertical granularity control and parallel hash bag) to optimize the performance of graph traversal. (2) Fast implementations on SCC, CC, and LE-lists using the proposed techniques." — *scc*, 1 Introduction, contribution list

**Violation signature.** Within one bulleted or numbered list, some items are verbless noun phrases and others are full sentences with a subject and finite verb; or items alternate between "-ing" and "to VERB" heads; or terminal periods appear on some items and not others. Detectable by reading only the first two words of every item and checking they are the same part of speech.

**Revision.**

- Before: Our contributions are: (1) A new estimator for treatment effects under interference. (2) We show that the estimator is consistent. (3) An open-source implementation.
- After: Our contributions are: (1) a new estimator for treatment effects under interference; (2) a consistency proof for that estimator under weak overlap; (3) an open-source implementation in R.

**Do not apply when.** The list is a glossary or interface list where each item is a term plus a gloss. There the item head is fixed by the term, and the constant to hold is the gloss's opening verb form — every gloss imperative, or every gloss third-person, but never mixed within one list.

<sub>Verifier: The uniformity half is sound and its violation signature is unusually mechanical (read the first two words of each item, check the part of speech), which is what saves it from being the standard style-manual parallelism platitude. The category-SELECTION half is overreach: the 'why' rests on one paper (arxiv-2305.04359) running an NP contribution list and a clause findings list, and then claims this 'shows the choice is conditioned on content type rather than author habit'. n=1 shows nothing of the kind. Exemplars 1 and 2 are single items from that one paper and only illustrate the category-cho</sub>

---

## Set the coordination seam at the first point of difference, and repeat the frame word only when an arm runs long

**Move.** For short coordinated arms, move every shared word left of the coordinator so only the contrasting words sit inside it; once an arm runs past roughly a line, repeat the frame's head noun or preposition on the second arm instead of eliding it.

**Why it works.** Stripped short arms make the contrast a single visual jump with nothing to re-read; long arms joined by a bare "and" leave no marker for where the second arm begins, so the reader has to backtrack to find the seam. Measured over the corpus myself (not in the digests): 2,505 in-sentence "A, B, and C" triples have mean item lengths 6.2 / 6.6 / 7.5 words, and only 38 of them repeat the same first word in all three items — shared material is normally stripped, not echoed.

**Seen in.** kcore, PPM, scc, im, p2307-wheatman, lis, ch, pimtrie (sampled from 8-10 papers for this sub-topic, not all 119)

- "Existing implementations perform the peeling process in either an online or an offline manner." — *kcore*, 1 Introduction

- "there is a tension between the desire for high work capsules that amortize the capsule start/restart overheads and the desire for low work capsules that lessen the repeated work on restart" — *PPM*, 2 The Persistent Memory Model

- "None of this work defines an algorithmic cost model, presents a work-stealing scheduler, or provides the provable bounds in this paper." — *PPM*, 1 Introduction, Related Work

**Violation signature.** Two short arms that each repeat words already present in the other ("improves both the accuracy and improves the speed", "both in theory and also in practice"), or a subject and verb restated for each arm of a three-item series ("the model does not handle X, the model does not handle Y, and the model does not handle Z"). Conversely: two arms each running over a line, joined by a bare "and", with no repeated head noun to mark the seam.

**Revision.**

- Before: The protocol reduces both the cost of screening and it reduces the time to result. The trade-off is between the benefit of casting a wide net, which catches rare cases early, and a narrow net's low false-positive rate.
- After: The protocol reduces both the cost and the time of screening. The trade-off is between the benefit of a wide net, which catches rare cases early, and the benefit of a narrow net, which keeps false positives low.

**Do not apply when.** Stripping the shared word changes the grammar or the meaning ("interested in and committed to the reform" needs both prepositions), or the two long arms genuinely share one modifier, in which case repeating the head noun invents a second entity where there is one.

<sub>Verifier: Both halves survive independent measurement. Strip-the-shared-material: I extracted 4,735 in-sentence 'A, B, and C' triples with a different regex from the agent's and found the same first word repeated in all three items only 9 times (0.2%); the agent's own count was 38 of 2,505 (1.5%). Different regexes, same conclusion — shared material is stripped, not echoed. Repeat-the-head-on-long-arms, which I initially suspected was a rarity like the paired em-dash, is in fact live: a repeated head noun across long coordinated arms ('the desire for X ... and the desire for Y') occurs 146 times in 78/1</sub>

---

## Place the correlative marker at the first point of difference

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Put 'both...and', 'either...or', 'not only...but also' as late in the sentence as possible, so that everything the two arms share sits to the left of the marker and the two arms are the same grammatical category. Reserve 'not only...but also' for a pair whose second member is genuinely unexpected — it appears 35 times in 1.1M corpus words (31/119 papers), against 'both...and' in 117/119.

**Why it works.** A correlative promises a matched pair; placing the marker as late as possible is what makes the two arms the same grammatical category, which is what the promise means. Ending on the heavier arm also lets the sentence close on the point rather than trailing off on a two-word tail. The corpus lets the second element break symmetry when the predicates differ in type — "but is also of independent interest" repeats the verb rather than forcing a false match.

**Seen in.** pimtrie, p2307-wheatman, im, kcore, PPM, ch, scc (sampled from 8-10 papers for this sub-topic, not all 119)

- "It is not only the first radix-based index designed for PIM systems, but also the first radix tree that asymptotically benefits from batch-parallel processing, for worst-case data and query skew." — *pimtrie*, 1 Introduction

- "change not only the container but also important graph-algorithm details, making the source of any measured improvements unclear." — *p2307-wheatman*, 1 Introduction

- "These analyses not only lead to good practical performance but also help to understand how the techniques interplay." — *im*, 7 Conclusion

**Violation signature.** Material identical on both sides of the correlative — a subject, auxiliary, or verb restated after "but also" or "or" when it could have sat left of the marker ("not only does it reduce cost, but it also reduces error"). Also: arms of different grammatical type ("not only in the lab but also we tested it in the field"), a "not only" with no answering "but also", or a long first arm followed by a three-word second arm.

**Revision.**

- Before: Not only the survey was cheaper to run, but also it produced higher response rates than the interview protocol did.
- After: The survey was not only cheaper to run but also more likely to be answered than the interview protocol.

**Do not apply when.** The two arms are genuinely different grammatical types and no rewrite matches them — drop the correlative and write two sentences rather than bending an arm to fit. Do not force the heavier element second: in the corpus's own correlative pairs the second arm is longer only 14 times in 22 and the medians are equal, so order the arms by logic, not by weight.

<sub>Verifier: The second clause of the name fails measurement. Across the corpus's own 'not only ... but also' pairs the second arm is longer in only 14 of 22 (64%) and the medians are identical (7 words vs 7), so 'let the second element carry the weight' is not what these authors do. Frequency also needs stating: 'not only' is 35 uses in 31/119 papers — near the rarity of the paired em-dash aside — while 'both...and' is 117/119 and 'either...or' 100/119, so the rule must be anchored on both/either or it governs almost nothing. The marker-placement half is supported (21 of 29 'not only...but' instances rest</sub>

---

## Name list items where you list them, and never leave a back-reference bare

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Give each item a short handle at the moment of enumeration — a coined name, or an acronym defined in parentheses — and use the handle for later references; both devices are near-universal in the corpus (parenthesised abbreviations 119/119 papers, 'we call'/'we refer to' 102/119). Where a positional back-reference is genuinely tighter than the name, keep it but attach the noun that re-identifies the referent: 'the latter case', 'the second challenge', never a bare 'the latter' or 'the first of these'.

**Why it works.** A positional back-reference makes the reader count backwards into the list; a name resolves from local memory and survives the reordering or insertion of items during revision. My own count over the corpus: "the latter" appears in only 20/119 papers, and letter tags such as "(C1)" in 6/119 — tags are the variant reserved for items cross-referenced pages later.

**Seen in.** scc, im, pimtrie, kcore, ch, arxiv-2305.04359 (sampled from 8-10 papers for this sub-topic, not all 119)

- "we apply the proposed techniques to two more algorithms: connected components (CC) and least-element lists (LE-lists)." — *scc*, 1 Introduction

- "Our paper discussed two techniques: sketch compression and parallel CELF. Sketch compression uses the idea of memoization." — *im*, 7 Conclusion, Limitations and Future Work

- "are explicitly designed to address challenge C2, but x-fast tries and y-fast tries support only fixed-length keys, and how to address challenge C1 for z-fast tries is still an open problem." — *pimtrie*, 1 Introduction

**Violation signature.** A bare 'the former', 'the latter', or 'the first of these' with no noun attached — 7 such uses in 1.1M corpus words. Or a positional reference ('the second issue mentioned above', 'as noted in point (3)') reaching across a paragraph or section boundary to an item that was never given a name. Or a tag introduced in a list and never referred to again anywhere in the paper.

**Revision.**

- Before: We study two mechanisms by which the policy could raise wages. [two paragraphs of exposition] The latter mechanism accounts for most of the observed gap.
- After: We study two mechanisms by which the policy could raise wages: peer referral and wage posting. [two paragraphs] Wage posting accounts for most of the observed gap.

**Do not apply when.** Both items were named in the immediately preceding clause and their names are long — 'the latter case' beats repeating a six-word name twice in one sentence. Do not reach for bracketed tags ((C1), (P2)) as the default handle: only 3/119 corpus papers use them and all three come from one group; reserve them for items cross-referenced pages later.

<sub>Verifier: This is exactly the over-strong rule the validation pass already corrected, arriving for a fourth time. The corpus does not avoid former/latter (39 uses, 26/119 papers); it avoids the BARE form (7 uses in 1.1M words), and 82% of uses carry a re-identifying noun. The name as written prescribes the deletion, not the narrowing. A second numeric claim is also wrong in the direction that matters: the pattern says letter tags such as '(C1)' appear in 6/119 papers, but I count 15 such tags in 3/119, and all three are PIM papers from one author group — so the bracketed tag is a single lab's idiosyncra</sub>

---

## Keep the parenthesis skippable: no turn in the argument inside brackets

**Move.** Put in parentheses only material the sentence can lose without changing what it asserts — a symbol, an abbreviation, a source, a magnitude, a two-word gloss, a scope limit — and keep a prose parenthesis under about fifteen words. Never bracket a concession about your own claim, a hedge on your own finding, or a second finite claim the argument depends on. A compact contrastive scope-limiter ('but not writes', 'although rare') is fine; a reversal is not.

**Why it works.** Parentheses are this corpus's default aside (24.9 per 1,000 words, roughly 50x the em-dash), and that only works because the reader has learned that skipping one costs nothing. The measurements are severe: the median parenthetical is 1 word, 92% are 5 words or fewer, 99.4% are 15 or fewer, and only 65 of 46,374 parentheses (0.14%) stand as their own sentence. Content is policed just as hard: 'however' appears inside parentheses once in 1,080 uses, 'unfortunately' 0 times in 72, 'we believe' 0 times in 196. Once a bracket can hold a reversal, the reader must read every bracket at full attention and the device stops buying anything.

**Seen in.** fastbcc, PacTree, kdtree, RWS, iterative (sampled from 8-10 papers for this sub-topic, not all 119)

- "Tarjan-Vishkin algorithm has 𝑂 (𝑛+𝑚) optimal work (number of operations) and polylogarithmic span (longest dependent operations), assuming an efficient parallel CC algorithm." — *fastbcc*, Introduction

- "This is analyzed both in terms of the work (runtime sequentially) and span (longest dependent path in parallel)." — *PacTree*, Introduction

- "We say a BCC algorithm is space-efficient if it uses 𝑂 (𝑛) auxiliary space (other than the input graph)." — *fastbcc*, Introduction

**Violation signature.** A parenthesis running past about fifteen words; a bracket containing a full second claim, or 'we believe', 'unfortunately', or any concession about your own result; a capitalised bracketed sentence standing between two other sentences. Test: delete every parenthesis in the paragraph. If a sentence now says something false, misleading, or overclaimed, that bracket was carrying load it should not carry.

**Revision.**

- Before: The estimator is unbiased (although, as we discuss below, it can be badly biased when the sample is small, which is a real limitation of the approach and one reviewers have raised).
- After: The estimator is unbiased in large samples (n > 500). In small samples it can be badly biased, a limitation we return to in Section 5.

**Do not apply when.** Fields whose reporting conventions put fixed statistical furniture in brackets — (b = .32, SE = .07, p < .001), (95% CI 1.2-3.4) — where the length is not a stylistic choice. Do not take 'the median parenthetical is one word' as a target: that median comes from mathematical notation and bare abbreviations, and among parentheses carrying prose the median is three words with a working ceiling near fifteen. And do not read the length rule as licence to promote a genuinely optional half-paragraph of worked detail into the main text: that belongs in a footnote or appendix, not in a longer bracket.

<sub>Verifier: The quoted statistics all replicate (46,593 paren pairs; median 1 word; 92.4% <=5 words; 99.4% <=15; 67 capitalised bracketed sentences; 'however' 4/1080 inside brackets, 'unfortunately' 0/72, 'we believe' 0/181). But the length figures are a notation artifact and would mislead an economist or immunologist: 19,601 of the 46,593 parens (42%) contain no alphabetic run of three characters at all (they are symbols like (n), (G)), 4,881 more are a bare abbreviation and 4,839 a numeric label. Restricted to the 16,559 parens that actually carry prose, the median is 3 words and only 82% are <=5 — so '</sub>

---

## Spend the em-dash once: one unpaired dash, after an abstract claim, delivering the concrete thing that makes it true

**Move.** When you have just stated something general and the next thing the reader needs is the specific mechanism, number, or condition behind it, join them with a single em-dash rather than a period, a colon, or 'because'. Do not use paired dashes to interrupt a sentence.

**Why it works.** At 0.46 per 1,000 words the em-dash runs to roughly one per two pages, and the scarcity is the point: a mark the reader meets rarely still registers as an event. Used unpaired at the hinge it reads as 'here is the thing itself', collapsing the distance between claim and evidence without the ceremony of a new sentence and without the list-promise a colon makes. The corpus is consistent about the shape: of 540 sentences containing an em-dash, 498 (92%) contain exactly one.

**Seen in.** PacTree, kdtree, iterative, fastbcc, Incremental (sampled from 8-10 papers for this sub-topic, not all 119)

- "However they come at a cost of high space usage—every element requires a node in the tree." — *PacTree*, Introduction

- "For construction, the performance gain is from better cache complexity—data movement can be greatly saved by constructing multiple levels in one round." — *kdtree*, Introduction

- "This framework provides good parallelism—for a DG of depth 𝐷, we only need 𝑂 (𝐷) rounds." — *iterative*, Introduction

**Violation signature.** More than about one em-dash per two pages. Paired dashes bracketing a mid-sentence aside (that job belongs to parentheses or commas here). A dash whose right-hand side merely continues the narrative instead of instantiating the claim on its left — 'we ran the experiment—then we analysed the data'.

**Revision.**

- Before: Take-up of the subsidy was low. This was because the application form required three separate proofs of address.
- After: Take-up of the subsidy was low—the application form required three separate proofs of address.

**Do not apply when.** Nothing on the left is general enough to need instantiating: two coordinate facts want a period or a semicolon, not a dash. A second dash in the same paragraph is not an error — about a quarter of consecutive em-dashes in the corpus fall within one paragraph — but the typical spacing is roughly a page, so the second one should be earning something rather than becoming a habit. And some house styles (several UK journals, most legal writing) restrict the em-dash outright; there, use a colon or a fresh sentence.

<sub>Verifier: Every number checks out exactly: 642 em-dashes, 0.449/1k, and of 540 sentences containing one, 498 (92%) contain exactly one. I sampled 40 of the 406 prose single-dash sentences and the claimed shape dominates almost without exception — 'they come at a cost of high space usage—every element requires a node in the tree', 'the two algorithms perform similarly—FAST-BCC is about 1.1x faster'. The abstract-then-instance reading is real, not imposed. Two narrowings. First, the mark is not exotic per paper: 97/119 papers use it, so the rule is about frequency and shape, not about avoidance. Second, '</sub>
