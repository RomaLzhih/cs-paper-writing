# Pass 2 — Names

**Ask:** Does every concept in this passage travel under exactly one name, and was that name introduced after the thing it names?

**Do not touch in this pass.** Do not vary a word for freshness anywhere in this pass — repetition of the discriminating modifier is the whole point, and the elegant-variation instinct is the defect being removed. Do not resolve pronouns or demonstratives (Pass 3), and do not reorder the sentences Pass 1 has just arranged. Do not coin a compound the field does not already use just to kill an 'of' — that is Pass 5's business and it is subordinate to this pass's consistency rule. Leave headings, cited titles, and definition environments alone.

9 patterns.

---

## Repeat the discriminating word verbatim; let only the generic classifier vary

**Move.** Fix the element that distinguishes the term from its neighbours — a contrasting modifier (sparse/dense, strong/relaxed) or a coined stem (recorded-once, phase-parallel) — and reproduce it character-for-character on every mention; if the prose needs variety, change only the generic head noun that follows it (traversal/method/approach, property/requirement, framework/algorithm).

**Why it works.** The discriminating element is the reader's index into the definition, so altering it forces a re-lookup; the generic head carries no distinguishing information, so swapping it costs the reader nothing and relieves the pressure that otherwise pushes writers into renaming the concept itself.

**Seen in.** SAGE, vcas, iterative_2, PIP, arxiv-2208.09809, psi, closest (sampled from 8-10 papers for this sub-topic, not all 119)

- "The sparse traversal processes the out-edges of the current frontier to generate the next frontier." — *SAGE*, 4.1.1 Existing Memory-Inefficient Graph Traversal

- "However, the sparse method can be memory-inefficient because it allocates an array with size proportional to the number of edges incident to the current frontier" — *SAGE*, 4.1.1 Existing Memory-Inefficient Graph Traversal

- "The recorded-once requirement is naturally satisfied by CT and the BST from [4], but not by NBBST" — *vcas*, Experiments — Recorded-Once

**Violation signature.** List every noun phrase in the draft that names the same central construct. If that list contains more than one distinct modifier or stem — "the sparse pass" in §3, "the push-based scheme" in §4, "the lightweight variant" in §5 — the pattern is violated, and a reader cannot tell whether one thing or three are meant.

**Revision.**

- Before: We first estimate the short-horizon elasticity. The brief-window coefficient is then compared with the long-run figure, and the extended-horizon estimate appears in Table 2.
- After: We first estimate the short-horizon elasticity. The short-horizon estimate is then compared with the long-horizon elasticity, and the long-horizon estimate appears in Table 2.

**Do not apply when.** The head noun is part of the name rather than a classifier. Fixed compounds keep both halves on every mention — binary-forking model (61 of 61 uses), cover tree (50 of 52), overlay graph (43 of 44), closest pair — and swapping the head there renames the object. Also hold the head fixed when the classifier itself carries a distinction the paper relies on: algorithm vs. implementation, model vs. machine, problem vs. solution, assay vs. result, as vcas does in keeping 'implementation' for code and 'algorithm' for method. Vary the head only where it is genuinely generic (method/approach/technique, property/requirement) and the modifier alone identifies the thing.

<sub>Verifier: Core claim survives measurement well. Coined/discriminating modifiers are reproduced character-for-character across a paper: 'binary-forking model' 61/61 uses in arxiv-1903.04650, 'cover tree' 50/52 in covertree_2, 'overlay graph' 43/44 in ch, 'closest pair' 44/50 in closest. The exemplars are on target: I read SAGE 4.1.1 in full and it genuinely writes 'The sparse traversal … The dense traversal … The dense method … the sparse method', modifier frozen, head varying; vcas does the same with 'recorded-once requirement' / 'recorded-once property'. The unsharpened version of this ('be consistent </sub>

---

## Never let "the former"/"the latter" stand bare — attach the noun that re-identifies it

> Narrowed after corpus measurement contradicted the original claim.

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** In a two-way contrast the second item may be compressed, but only into a phrase that still names a kind: 'the latter case', 'the latter two problems', 'the former model', 'the latter condition'. Leave the bare form out — 'Pseudo is relatively slower on the former', 'For the latter, we rely on BLAST' — and where the compression would be bare, repeat the item's own name instead, reusing the first clause's verb frame so the comparison is the only thing that varies ('algorithms in [6, 33] can be mapped to the strong PIP model, and algorithms in [3, 36] can be mapped to the relaxed PIP model').

**Why it works.** Parallel naming plus a parallel frame leaves exactly one thing varying, which is the comparison itself; "the latter" makes the reader count backwards before understanding. The habit is measurable: "the former" occurs 6 times in the corpus's 1.1M words (6/119 papers) and "the latter" 33 times (25/119) — the same near-absence band the digest records for "due to the fact that" (11) and "a lot of" (8).

**Seen in.** PIP, ParrallelARWC, iterative_2, ParGeo, SAGE (sampled from 8-10 papers for this sub-topic, not all 119)

- "Based on our model definitions, algorithms in [6, 33] can be mapped to the strong PIP model, and algorithms in [3, 36] can be mapped to the relaxed PIP model." — *PIP*, 3 Models for Parallel In-Place Algorithms

- "A dummy task is always the right child of a real task, so stealing a dummy task could entail writing out three frames." — *ParrallelARWC*, Proof of Lemma 2.1

- "Type 2 algorithms aim to wake up an object when the last object it depends on is finished." — *iterative_2*, Abstract

**Violation signature.** 'the former', 'the latter', or 'the first/second one' with no noun after it — the pointing word is carrying the reference alone. Detector: delete the pointing phrase and read the sentence; if nothing left in it names what was pointed at, the reader has to count backwards to the previous sentence. Apply the same test to an 'it' or 'this one' in a clause that has two candidate antecedents.

**Revision.**

- Before: We compare the fixed-effects specification with the instrumented specification. The former is cheaper to estimate, whereas the latter is characterised by robustness to omitted confounders.
- After: We compare the fixed-effects specification with the instrumented specification. The fixed-effects specification is cheaper to estimate; the instrumented specification is robust to omitted confounders.

**Do not apply when.** The antecedent is the subject of the immediately preceding clause and nothing competes for it — a pronoun is correct there and repeating the name stammers. Ordinals with an antecedent in the same sentence are normal in this register (16 uses across 12 papers) and should not be flagged mechanically. Drop the repeat-both-names half for lists of three or more parallel items, where naming each in every clause swamps the sentence.

<sub>Verifier: This is the exact case the validation pass was built to catch, and the pattern is on the wrong side of it. Its counts are right (I measure 6 'the former', 34 'the latter', 40 total in 27 papers) but its inference is wrong: 30 of the 40 uses carry a noun — case 18, two 6, three 2, plus model, part, condition, measure — and only about 10 are bare. The corpus does not avoid the construction; it avoids the BARE construction, and filing it in the 'near-absence band' with 'due to the fact that' misreads the data. The blanket ban on 'the first/second one' is also too strong: 16 uses across 12 papers,</sub>

---

## Declare the second name once, at the definition — a parenthesis is enough

> Narrowed after corpus measurement contradicted the original claim.

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** Where a concept circulates under two names, put both side by side exactly once, at the point the concept is defined, and then use one. The commonest form in this corpus is a bare parenthesis inside the defining sentence — 'the span (depth) is the length of the longest sequence of dependent instructions' (26 papers) — not a declaration with a reason; a short reason ('For simplicity, we use the term "R-tree"'; 'to avoid confusion with the greedy MIS algorithm, we use the term MFS') is available but optional. An explicit licence to alternate ('We use node and vertex interchangeably', 13 papers) is equally acceptable. What is not acceptable is a synonym that enters later with no declaration anywhere.

**Why it works.** The reader receives the mapping once and then reads without translating; naming the reason converts what looks like an arbitrary preference into a service. The discipline is visible corpus-wide: across the ten papers read, each commits to exactly one of "span" and "depth" for the same quantity — SAGE, ParGeo and closest use depth and never span; PIP, psi, covertree_2, arxiv-2208.09809, iterative_2 and ParrallelARWC use span, with depth reserved for unrelated senses such as tree depth.

**Seen in.** psi, iterative_2, SAGE, PIP, closest, arxiv-2208.09809 (sampled from 8-10 papers for this sub-topic, not all 119)

- "they share the same underlying concept. For simplicity, we use the term “R-tree” to refer to the general idea of object-partitioning trees." — *psi*, 2 Preliminaries and Related Work — Object-partitioning Trees

- "In this paper, to avoid confusion with the greedy MIS algorithm in Sec. 5.3, we use the term MFS." — *iterative_2*, 3 (footnote 2)

- "An algorithm’s work is the total number of instructions, and the span (depth) is the length of the longest sequence of dependent instructions in the computation." — *iterative_2*, 2 Preliminaries — computational model

**Violation signature.** A synonym appears in a later section with no earlier sentence tying it to the term already in use — 'depth' in the methods and 'span' in the analysis; 'seroconversion' in §2 and 'antibody response' in §5. Detector: for each concept, list its names in order of first appearance; every name after the first must have a declaration at or before its own first use.

**Revision.**

- Before: We measure willingness to pay for the amenity. Section 4 reports how reservation prices vary with income, and Section 5 decomposes the valuation by cohort.
- After: We measure willingness to pay (also called reservation price) for the amenity; we use willingness to pay throughout. Section 4 reports how willingness to pay varies with income, and Section 5 decomposes it by cohort.

**Do not apply when.** The paper's contribution is to separate the two names; or the abstract and introduction must be findable by readers of both literatures, in which case keep the paired form up front and collapse to one term after the declaration, as psi does with 'R-trees/BVHs'. Do not manufacture a reason for the choice — most of this corpus states none.

<sub>Verifier: The commitment half is confirmed and is the strongest thing here: exactly 2 of 119 papers use both 'work and span' and 'work and depth', and 26 papers print the pair once as a bare parenthesis ('the span (depth) is the length of the longest sequence of dependent instructions') and then never alternate. But the prescribed FORM is not what the corpus does. A stated reason is rare — 'we use the term' 8 uses in 8 papers, 'For simplicity, we use/call/refer' 10 in 8 papers, 'to avoid confusion' 5 in 5 — while the unadorned parenthetical pairing is three times commoner. And 'never alternate' is contr</sub>

---

## Coin the name attached to its category noun, and keep the category noun for the first re-mentions

**Move.** Introduce a new name with its kind visible: either build the category into the name ('forking task', 'sparse partition', 'BDL-tree') or put the name in apposition to a category noun ('an auxiliary data structure, which we refer to as a graphFilter'; 'the BDL-tree, a new parallel data structure that supports batch-dynamic operations'). Three quarters of this corpus's coining sentences carry a category noun, and most of the rest have the category inside the coined name. Where the name is opaque — an invented token that says nothing about its kind — carry the category word on the next mention or two ('The graphFilter data structure can be viewed as…') before letting the bare name stand alone.

**Why it works.** The category noun tells the reader what kind of thing the new word is, so the sentences that immediately follow the coinage are parseable before the definition has been absorbed; a bare invented noun forces the reader to hold an untyped token.

**Seen in.** SAGE, ParGeo, vcas, ParrallelARWC, closest, psi, iterative_2 (sampled from 8-10 papers for this sub-topic, not all 119)

- "we build an auxiliary data structure, which we refer to as a graphFilter, that efficiently supports updating a graph with a sequence of deletions." — *SAGE*, 4 Semi-Asymmetric Graph Filtering

- "The graphFilter data structure can be viewed as a bit-packed representation of the original graph that supports mutation." — *SAGE*, 4 Semi-Asymmetric Graph Filtering

- "For kd-trees, we develop the BDL-tree, a new parallel data structure that supports batch-dynamic operations (construction, insertions, and deletions) as well as exact k-NN queries." — *ParGeo*, 1 Introduction

**Violation signature.** A coined name first appears as a bare noun with no category word anywhere in the sentence ("We then apply Reweaving to each sample"), or as a bare adjective or verb with no head ("we use Chunked to cut memory"). Detector: search for the coinage's first occurrence and check whether the same sentence contains a common noun naming its kind.

**Revision.**

- Before: We introduce Contrast Anchoring and apply it before the second wave. Contrast Anchoring reduces attrition bias by roughly a third.
- After: We introduce a weighting scheme, which we call contrast anchoring, and apply it before the second wave. The contrast-anchoring scheme reduces attrition bias by roughly a third.

**Do not apply when.** The coined name already contains its category ("BDL-tree", "sparse partition", "forking task") — bolting on a second one ("the BDL-tree tree structure") is redundant. And after two or three uses the bare name is correct; carrying the category noun to the end of the paper is padding.

<sub>Verifier: First half measured and confirmed: of 142 coining sentences ('we call X', 'which we refer to as X'), 105 (74%) contain a category noun, and most of the remaining 37 carry the category inside the coined name itself ('frontier buckets', 'base register', 'light keys', 'path sketch', 'cluster distance vector'), which the pattern's own do_not_apply_when anticipates. All four exemplars demonstrate the move — graphFilter by apposition, BDL-tree by apposition, 'forking task' by building the category into the name. Second half is weaker than stated. I could only confirm category retention on re-mention</sub>

---

## Shorten a long term only to its head noun, and only while nothing competes for that head

> Narrowed after corpus measurement contradicted the original claim.

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** After a multi-word term is introduced, later mentions in the same passage may contract to the bare head with a definite article — 'the framework', 'the model', 'the tree' — for as long as exactly one thing of that kind is in scope. The full term returns the moment a second one enters: PIP, which sets a strong PIP model against a relaxed PIP model, uses bare 'the model' zero times in the whole paper. Contract to the head, never to a synonym you have not declared.

**Why it works.** A single salient referent is tracked effortlessly, so the contraction buys brevity for free; once a competitor is in scope the bare head becomes genuinely ambiguous, and the modifier that returns is the one that resolves it. This is the corpus's only licensed abbreviation of a term — the alternative, substituting a synonym, never occurs.

**Seen in.** iterative_2, SAGE, closest, vcas, PIP, arxiv-2208.09809 (sampled from 8-10 papers for this sub-topic, not all 119)

- "we propose the phase-parallel framework. The framework assigns a rank to each object and processes the objects based on the order of their ranks." — *iterative_2*, Abstract

- "The model, called the Parallel Semi-Asymmetric Model (PSAM), consists of a shared asymmetric large-memory with unbounded size that can hold the entire graph" — *SAGE*, 1 Introduction

- "the PSAM model permits writes to the large-memory, which are ω > 1 times more costly than reads." — *SAGE*, 1 Introduction

**Violation signature.** A definite bare head — "the model", "the assay", "the estimator" — used in a paragraph where two or more things of that kind have already been named. Conversely, the full multi-word term repeated in every sentence of a paragraph in which it is the only candidate.

**Revision.**

- Before: We calibrate the two-sector overlapping-generations model. The two-sector overlapping-generations model matches the savings rate, and the two-sector overlapping-generations model is then extended with bequests.
- After: We calibrate the two-sector overlapping-generations model. The model matches the savings rate and is then extended with bequests. Once the one-sector benchmark is reintroduced, the two-sector model is again named in full.

**Do not apply when.** The passage compares two variants of the same kind — the strong model against the relaxed model, the sequential tree against the parallel tree, the treated cohort against the control cohort. Then every mention carries its modifier however repetitive it feels.

<sub>Verifier: The competition rule is confirmed by a clean natural experiment: PIP runs a 'strong PIP model' (14 uses) against a 'relaxed PIP model' (17 uses) and writes bare 'the model' zero times in the entire paper, while iterative_2, which has only one framework in scope, contracts to 'The framework' in the abstract. Bare definite heads are common corpus-wide ('the algorithm' 1,569 in 103 papers; 'the tree' 888 in 76). Two defects. (a) The why-clause asserts 'the alternative, substituting a synonym, never occurs' — an absolute the measurements contradict: 13 papers explicitly license synonym alternation</sub>

---

## Re-expand an abbreviation at the first use in each major division, not once for the paper

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Give the full form with the parenthesised abbreviation at first use, then expand it again at the first use in the body and again at the head of the section that owns the term; between those points use the short form alone. Two expansions is this corpus's median and three is common when the owning section is far from the definition. Keep the head noun attached when the abbreviation stands for a modifier ('the vEB tree', 'the PIP model', 'the LIS algorithm'), and drop it when the abbreviation is itself a complete noun phrase.

**Why it works.** Readers enter at the abstract, at a section, or at the conclusion; re-expansion costs three words and removes a lookup for each entry point. The head-noun rule keeps the short form grammatical — arxiv-2208.09809 uses "vEB" 158 times and 121 of those are immediately followed by "tree" or "trees", because "vEB" alone is a person's name; every one of PIP's 27 "PIP model" and 68 "PIP algorithm(s)" keeps its head, while LIS, MIS and EBR stand bare because their expansions are complete noun phrases.

**Seen in.** arxiv-2208.09809, covertree_2, PIP, SAGE, iterative_2, ParGeo (sampled from 8-10 papers for this sub-topic, not all 119)

- "In theory, we parallelize the van Emde Boas (vEB) tree [74] and integrate it into range trees to achieve a better work bound for WLIS." — *arxiv-2208.09809*, 1 Introduction

- "The van Emde Boas (vEB) tree [74] is a famous data structure that implements the ADTs of priority queues and ordered sets and maps for integer keys and is introduced in textbooks (e.g., [27])." — *arxiv-2208.09809*, 5 Parallel van Emde Boas Trees

- "The strong PIP model assumes a fork-join computation only using O(log n)-word auxiliary space in a stack-allocated fashion for an input size of n when run sequentially" — *PIP*, 3.1 The Strong PIP Model, Definition 1

**Violation signature.** An abbreviation defined once on page 2 and used bare on page 11 with no intervening expansion; or an abbreviation whose expansion ends in a modifier used as a bare noun — 'we insert into the vEB', 'an efficient PIP'. Detector: for each abbreviation, list the positions of its expansions and its first use in each section; any section whose first use is several pages from the nearest expansion needs one.

**Revision.**

- Before: We use hierarchical Bayesian estimation (HBE) in Section 1. [nine pages later] Section 6 extends HBE to unbalanced panels, and we compare HBE with maximum likelihood.
- After: We use hierarchical Bayesian estimation (HBE) in Section 1. [nine pages later] Section 6: Hierarchical Bayesian estimation (HBE) extends naturally to unbalanced panels; we compare the HBE estimator with maximum likelihood.

**Do not apply when.** The abbreviation is more familiar to the venue's readers than its expansion (DNA, GDP, CPU, ELISA) — expanding it even once is condescending, and where the expansion already ends in the head noun ('assay'), the bare form takes no extra head. Never expand twice within the same section; that reads as an editing slip. Four expansions across a paper is padding, not courtesy.

<sub>Verifier: Re-expansion is real and common: matching expansions to their own initials, 94 of 119 papers expand at least one abbreviation twice or more, 209 (paper, abbreviation) pairs are expanded 2+ times, and 26% of those pairs have their second expansion more than a fifth of the document after the first. The head-noun half is confirmed on the pattern's own cases: 'vEB' 158 uses in arxiv-2208.09809 with 134 immediately followed by tree/trees; PIP 160 uses with 81 'PIP algorithm(s)' and 40 'PIP model(s)'. The vEB exemplar pair (intro expansion, then re-expansion at the head of §5 that owns the term) is </sub>

---

## Derive the rest of the vocabulary from the stem you defined; negate with non- only where the field offers no antonym

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Build the noun and the adjective on the stem you already defined — sparse/sparsity, biconnected/biconnectivity, adaptive/adaptivity — instead of reaching for a different root, and coin a new term inside the frame of an established one so it inherits the paradigm ('round-efficiency' beside 'work-efficiency'). For the complement, use the field's standard antonym when one exists: this corpus writes 'dense' against 'sparse' 151 times to 9 for 'non-sparse', and 'sequential' against 'parallel' throughout. Build non-X on your own stem only when the term is one you coined or the field supplies no opposite — non-trivial (105), non-empty (69), non-core (13).

**Why it works.** A reader parses "non-core point" or "round-efficiency" with no new lookup because the form is visibly derived from a term already in play; a fresh word for the complement reads as a third concept and quietly doubles the glossary. Corpus-wide the complement is built with "non-" on the stem rather than with an antonym: non-trivial 91, non-adaptive 63, non-empty 60, non-leaf 20, non-core 11, non-sparse 9.

**Seen in.** closest, covertree_2, iterative_2, SAGE, psi, PIP (sampled from 8-10 papers for this sub-topic, not all 119)

- "We say that point p is sparse in Gi relative to S if Ni (p, S) = ∅." — *closest*, 2.2 A Grid-Based Implementation of Sparse Partition

- "We use this notion of sparsity to compute" — *closest*, 2.2 A Grid-Based Implementation of Sparse Partition

- "We refer to this property as round-efficiency. This paper presents work-efficient and round-efficient algorithms for a variety of classic problems and propose general approaches to do so." — *iterative_2*, Abstract

**Violation signature.** A term you defined and a later form of the same idea sitting on unrelated roots: 'robust estimator' in one sentence and 'the reliability of the procedure' in the next; 'we call these stable holdings' then 'volatile assets are excluded'. Detector: for each term you define, write out its adjective, its noun and its complement; if any of the three rests on a different root and the field does not already supply that word, put it back on the stem.

**Revision.**

- Before: We call a household liquidity-constrained if it holds less than one month of income in deposits. Cash-rich households are excluded, and we report how financial slack varies by region.
- After: We call a household liquidity-constrained if it holds less than one month of income in deposits. Non-constrained households are excluded, and we report how liquidity-constrainedness varies by region.

**Do not apply when.** The field already supplies an established name with its own literature attached — 'core', 'border' and 'noise' points are all standard, and a derived 'non-core clustered point' would be worse; the same holds for dense/sparse, sequential/parallel, static/dynamic. Also skip it where the non- form scopes ambiguously ('non-linear-time algorithm') or where the derived noun does not exist in the language.

<sub>Verifier: The derivational half holds: the corpus builds nouns and adjectives on stems it has already defined (closest: 'point p is sparse' then 'this notion of sparsity'; iterative_2 coins 'round-efficiency' inside the established 'work-efficient' frame; biconnectivity 101, adaptivity 83, reachability 327). All three exemplars illustrate it. The negation half is stated corpus-wide and is contradicted. 'Corpus-wide the complement is built with non- on the stem rather than with an antonym' is false by an order of magnitude: dense 151 uses against non-sparse 9; sequential 1,507; static 240 / dynamic 1,069</sub>

---

## Gloss a term inside parentheses on first use; do not spend a sentence saying what a parenthesis can carry.

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Put the expansion, the plain-language equivalent, the unit or the example in parentheses immediately after the term, and let the main clause run on to its point. A restatement earns its parentheses only when it changes vocabulary — technical term into plain words, plain words into notation. It never earns them by repeating.

**Why it works.** Parentheticals run 24.94 per 1,000 words, against 0.46 for em-dashes and 0.63 for semicolons — the corpus routes almost all of its asides through parentheses. "(i.e.," appears 479 times and "(e.g.," 634. Meanwhile "we define" appears 119 times against "which is defined as" once: definitions are either an active clause or a parenthesis, never a limp passive relative.

**Seen in.** PIP, kdtree, joinable, scc, RadiusStepping (sampled from 8-10 papers for this sub-topic, not all 119)

- "Traditionally, parallel algorithm design has mostly focused on solutions with low work (number of operations) and span (depth or longest critical path) complexities." — *PIP*, Introduction

- "We proved that our algorithms have strong theoretical bounds in work (sequential time complexity), span (parallelism), and cache complexity." — *kdtree*, Abstract

- "Another approach is to update the trees in parallel by supporting “bulk” operations such as inserting a collection of keys (multi-insert), taking the union of two trees, or filtering the tree based on a predicate function." — *joinable*, Introduction

**Violation signature.** A standalone sentence whose entire content is a gloss short enough to sit in parentheses -- "Here, X refers to ...", "X is defined as ..." where the definition is a short noun phrase and the term is used only once or twice afterwards -- or an "In other words, ..." sentence that repeats the previous sentence in the same vocabulary at the same level of abstraction. Test: if the gloss fits in parentheses without breaking the host sentence's spine, it belonged there.

**Revision.**

- Before: We report the seroconversion rate for each arm. The seroconversion rate is the fraction of subjects whose titre rises fourfold.
- After: We report the seroconversion rate (the fraction of subjects whose titre rises fourfold) for each arm.

**Do not apply when.** The definition is load-bearing, will be used repeatedly, or carries its own notation, conditions or edge cases -- then it gets a full sentence or a numbered definition. Do not read this as a ban on passive definitions: "(is|are) defined as/to be/by" appears 80 times in 51/119 papers, almost always introducing formal notation, and it is only the string "which is defined as" (1 use) that the corpus avoids. Do not set a gloss off with em-dashes instead: at 0.46 per 1,000 words, against 24.9 for parentheses, the dash is reserved for a sharper break than a gloss. And "In other words" is not banned (57 uses in 36 papers), only rationed to restatements that actually shift register.

<sub>Verifier: The parenthesis half is solidly measured and matches the digest: "(i.e.," 479 in 94/119 papers, "(e.g.," 634 in 101/119, parentheticals 24.94/1k against em-dash 0.46 and semicolon 0.63, so the corpus really does route its asides through parentheses, and the ban on substituting em-dashes is consistent with the 25 paired-dash asides in 14/119 papers. The definition half overreaches. "which is defined as" is indeed 1 use, but that single string is doing all the work for the claim that definitions are "never a limp passive relative": "(is|are) defined as/to be/by" appears 80 times in 51/119 papers</sub>

---

## Describe the thing first, name it last, then use the name

**Move.** Give the description in full. Put the coinage in end position with a naming verb — 'We will refer to this approach as X', 'We refer to this algorithm as the Y algorithm', 'We call this the Z policy'. Only from the following sentence onward should the name work as a subject or object, usually re-entering as a demonstrative plus its head noun ('This policy is competitive with ...').

**Why it works.** A label is useless until the reader has the thing it labels, so a paper that names first makes the reader carry an empty token. Putting the name in the sentence's final slot places it exactly where new information belongs; from the next sentence on it is given, and can be a one-word subject. The frame is live in the register: 'refer to ... as' appears 91 times across 55 of the 119 papers, and 'we call' 192 times.

**Seen in.** cbfs, readwrite, am-tree, ppsp (sampled from 8-10 papers for this sub-topic, not all 119)

- "We will refer to this approach as cluster-BFS (C-BFS), and present more details in Sec. 3." — *cbfs*, Introduction

- "Akiba et al. [1] used this idea in the exact two-hop distance oracle but only considered the special case for d = 2 (a star-shaped cluster: a vertex and its neighbors). We refer to this algorithm as the AIY algorithm." — *cbfs*, Introduction

- "We call this the read-write LRU policy. This policy is competitive with the optimal offline policy" — *readwrite*, Section 2, Preliminaries and Models

**Violation signature.** An acronym or coined name used as a subject in, or before, the sentence that defines it. The related tell: a definition folded into a parenthesis inside the subject noun phrase — 'Sandbox-graduated firms (firms that completed supervised testing and then entered the general regime) raised more capital' — instead of being given its own clause first.

**Revision.**

- Before: Sandbox-graduated firms (firms that have completed a supervised testing period and then entered the general regulatory regime) raised more capital in the following year.
- After: Some firms complete a supervised testing period and then enter the general regulatory regime; we call these sandbox-graduated firms. Sandbox-graduated firms raised more capital in the following year.

**Do not apply when.** The name is already standard in the field and needs no coining, or it is the paper's headline artifact, which the title and abstract have already introduced. Do not run the ceremony for a name you will use twice — the naming sentence then costs more than the abbreviation saves. And a name given inside a definition environment or a run-in heading is already anchored; do not restate it.

<sub>Verifier: All three quotes illustrate the move exactly, including the re-entry as demonstrative-plus-head-noun in the readwrite pair ('We call this the read-write LRU policy. This policy is competitive with...'). The device is confirmed live and, if anything, under-counted: the 'why' says 'refer to ... as' appears 91 times in 55 papers and 'we call' 192 times, whereas I measure 'refer to X as' 128 times in 66/119, 'referred to as' 120 in 57/119, and 'we call' 203 in 77/119 (validation.md's family total is 296 in 87/119). The numbers in the 'why' should be corrected upward, but they point the same way an</sub>
