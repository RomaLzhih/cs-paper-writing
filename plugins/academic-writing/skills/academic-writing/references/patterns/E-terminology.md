# E. Precision and terminology

7 patterns, ordered by how much each would improve a weak draft.

---

## Name it once, then never rename it: bind the handle inside the sentence that first describes the thing

**Move.** The first full description of a concept — yours or a cited artifact's — carries its name in the same sentence, attached by an explicit performative clause ("which we refer to as X", "we call Y an X") or, for prior work, by a short name plus an appositive gloss saying what kind of thing it is ("Aspen [18], a state-of-the-art graph-streaming system"); later sentences use the name and do not re-cite.

**Why it works.** The reader never holds an unnamed description in working memory, and never meets a name whose referent must be reconstructed backwards; once named, the work can be criticised, compared and built on as an object, with no bracket number held in mind and no trip to the bibliography mid-argument.

**Evidence.** 18 papers, union of the E and F samples (12 each) — the widest attestation in the library. Load-carrying check: edit-distance mentions AALM 24 times with three brackets; ROSE mentions BGSS 13 times with two.

**Exemplars.**

- "We consider three types of randomized incremental algorithms, which we refer to as Type 1, 2, and 3, for lack of better names." — *incremental*, 2 Preliminaries
- "We call the process to compute the true score of a vertex an evaluation." — *im*, 2 Preliminaries
- "BYO is based on the Graph Based Benchmark Suite (GBBS) [37, 38], a high-performance graph-algorithm framework implemented on top of a CSR container." — *p2307-wheatman*, 1 Introduction

**Violation signature.** A concept carried for several sentences under rotating descriptions ("the extra buffer", "this temporary array", "the scratch space") that acquires a name later; a term whose first appearance is in a heading, caption or table header with no binding sentence in running prose; a tool or dataset appearing as a bare bracket ("we used [22] to compute alignment scores"); the same work re-cited by number a dozen times because it never got a name. Detector: for every technical term, find its first body-text occurrence and check for a naming verb (call / refer to as / denote / term) in that same sentence.

**Revision.**

- Before: The system keeps a small amount of state that lets it skip work it has already done. This stored state is consulted before each pass. We scored responses with the instrument of [14], and later compare our scores with those produced by [14].
- After: The system keeps a small amount of state that lets it skip work it has already done, which we call the memo table. The memo table is consulted before each pass. We scored responses with the Reading Fluency Inventory [14], a 24-item clinician-administered scale, and later compare Inventory scores with those from the shorter screener of [22].

**Do not apply when.** The concept or the cited work appears exactly once. A name that is never re-invoked is pure overhead, and invented handles that appear twice make the paper harder to read, not easier.

---

## Legislate term collisions out loud, at the point of collision

**Move.** Wherever two words could name one thing, or one word or symbol could name two things, one flagged sentence — often a footnote or one-clause parenthetical at the first place the collision could bite — assigns each word to exactly one referent and gives the reason: "To avoid confusion…", "to avoid conflicting terminology", "For clarity, in this work, we will always call…". Deliberate reuse of a symbol is declared as reuse.

**Why it works.** The mapping is handed over once instead of being inferred from a dozen ambiguous uses, a later apparent inconsistency reads as declared convention rather than slip, and readers from the other community see that you know their usage rather than that you are ignorant of it.

**Evidence.** 8 papers, union of the E and H samples. The corpus splits on the ruling but never on the act of ruling: am-tree declares two words identical, xu-ppcsr forces the same pair apart.

**Exemplars.**

- "In other works, vertices are sometimes called nodes. For clarity, in this work, we will always call these graph elements vertices and use nodes to refer to the implicit PMA tree." — *xu-ppcsr-alenex-21*, Section 4, footnote 4
- "We will refer to these operations as fuse and divide operations, to avoid conflicting terminology." — *pbtree*, 2 Preliminaries, B-trees
- "We use node and vertex interchangeably in this paper." — *am-tree*, 2.1 Preliminaries

**Violation signature.** Two words for the same object drift through the paper with no statement of their relation; or a word is used with two referents — an object of study and a component of the apparatus — and no sentence says which is meant where; or a symbol acquires a second meaning unacknowledged, so a careful reader cannot tell a convention from a typo. Detector: for each near-synonym pair in the draft, search for a sentence that rules on it; absence is the defect.

**Revision.**

- Before: Each segment is scored by the reader model, and the reader is shown the resulting segments. Groups were nested inside clusters, and each cluster was analysed separately.
- After: What the parsing literature calls a chunk we call a segment throughout, to avoid a clash with the storage chunks of Section 4; we reserve reader for the human annotator and call the automatic component the scorer. We reserve group for the treatment arm and cluster for the recruitment site.

**Do not apply when.** Only one candidate word is ever in play and no established literature attaches a competing sense to it. A disambiguation sentence for a word nobody could misread spends the reader's attention and implies a subtlety that is not there.

---

## Back-reference a named artifact by its name, never by "our approach"

**Move.** Once an artifact has a coined name, every later mention uses the name. The possessive survives only in apposition at first introduction ("we present our framework ParChain") or for a plural set with no single name ("our algorithms").

**Why it works.** A name is a fixed handle; "our approach" shifts referent as the paper accumulates approaches, and forces a re-scan.

**Evidence.** 12 of the 12 papers read for dimension E. Counts re-verified for this pass: am-tree writes AM-tree 103 times, p2307-wheatman writes BYO 138 times, xu-ppcsr writes PPCSR 89 times, and all three contain zero occurrences of "our (approach|method|system|framework|technique|model)".

**Exemplars.**

- "This feature of BYO greatly simplifies the process of including a new graph container in the benchmark." — *p2307-wheatman*, Introduction
- "The advantage of PaC-IM is more significant on larger graphs, both in time and space." — *im*, 5 Experiments
- "PPCSR is especially well-suited to graph traversals" — *xu-ppcsr-alenex-21*, Conclusion

**Violation signature.** Sentences beginning "Our approach / Our method / Our system" in a paper that has already named the thing. Grep for `our (approach|method|system|framework|technique|model)`; in a paper with a named artifact every hit outside a first-mention apposition is a rewrite candidate, and a name-to-possessive ratio below roughly 20:1 means the name is not being used as the handle.

**Revision.**

- Before: Our method reduces the annotation burden. It was evaluated on three corpora. This shows the approach generalises.
- After: SpanLink reduces the annotation burden. We evaluated SpanLink on three corpora. These results show that SpanLink generalises.

**Do not apply when.** The contribution is a set of results or a class of techniques with no single artifact — then "our algorithms" is the honest plural and coining an umbrella name would overclaim. Inapplicable at the first mention itself, where "we present X, a …" must still perform the introduction.

---

## Convert every gradable adjective into a defined predicate before you evaluate with it

**Move.** Words that would otherwise be judgments (tall, heavy, balanced, stable, optimal, low) first get an explicit "we say X is A if <stated condition>" definition, and the complement is named in the same sentence or the next ("…and a short tree otherwise").

**Why it works.** The adjective then does exact work at every later appearance and a reader can check the claim instead of trusting the author's tone; naming the complement stops the reader inventing a private meaning for "not A".

**Evidence.** 8 of the 12 papers read for dimension E. The complement half was attacked separately and survives in three independent papers (pbtree "and a short tree otherwise", am-tree "is balanced or size-balanced otherwise", joinable "and false otherwise").

**Exemplars.**

- "We say a tree Ti is a tall tree if it has height h∗ , and a short tree otherwise." — *pbtree*, 4.1 B-Way Join
- "We say that a filter or partition is stable if the elements in the output are in the same order as they appear in A." — *PIP*, 2 Preliminaries
- "For a node 𝑥 and its parent 𝑦, we say 𝑥 is a heavy child of 𝑦 if size[𝑥] > (2/3)size[𝑦]." — *am-tree*, 3 The AM-tree

**Violation signature.** An evaluative adjective ("high", "large", "sparse", "robust", "severe") used as though it named a category the reader can sort objects into, with no "we say … if …" or "we define … as …" sentence anywhere. Detector: list every adjective the paper uses to partition its objects; each should have a definition sentence with a threshold in it.

**Revision.**

- Before: We restrict attention to large trials, and analyse small trials separately.
- After: We call a trial large if it enrolled at least 200 participants, and small otherwise. We restrict attention to large trials and analyse small trials separately.

**Do not apply when.** The adjective is ordinary description that carries no claim and sorts nothing — "a simpler proof", "a natural generalisation". Defining those manufactures false precision and swells the preliminaries with entries nobody will consult.

---

## Stamp every convention with the scope over which it holds

**Move.** Each definition, notation, and simplifying assumption is introduced with an explicit range marker — "throughout this paper", "in the rest of the section", "unless otherwise specified", "Other problems are defined in their respective sections".

**Why it works.** A convention with no stated range is either over-applied or forgotten. The marker also lets the preliminaries stay short by legitimately deferring local definitions, and tells a reader in Section 5 to stop searching the front matter.

**Evidence.** 7 of the 12 papers read for dimension E.

**Exemplars.**

- "Here we define the problems that are used in multiple places in this paper. Other problems are defined in their respective sections." — *PIP*, 2 Preliminaries
- "For simplicity, throughout this paper we assume that the edge weights are distinct." — *am-tree*, 2 Preliminaries
- "Unless otherwise specified, all divisions in pseudocode are integer division (rounded down)." — *xu-ppcsr-alenex-21*, Section 4, footnote 5

**Violation signature.** Assumptions appear as bare unscoped sentences ("Weights are distinct.", "We ignore missing data.") with nothing to say whether they hold everywhere or only here; or a preliminaries section has swollen to hold every definition in the paper. Detector: list every assumption sentence and ask of each "until when?" — if the text does not answer, the marker is missing.

**Revision.**

- Before: We assume responses are missing at random. Coding was done by two annotators.
- After: Throughout the paper we assume responses are missing at random; Section 6 relaxes this. Coding was done by two annotators.

**Do not apply when.** Short papers with a single method section, where every convention is trivially global and stamping each becomes noise. And never stamp a scope you do not honour: a "throughout this paper" that a later section quietly violates is worse than no marker at all.

---

## Gloss the standard term at its first appearance in prose, name the rival synonym once, then never use it again

**Move.** A term the paper's own audience already knows still gets a two-to-six-word parenthetical gloss the first time it appears in running prose, and the gloss frequently names the synonym a neighbouring subfield would use; the rival word is then never used again as a standalone term.

**Why it works.** Readers arriving from an adjacent subfield get the translation once, without the paper alternating between two words for its whole length. The retirement is measurable: after the gloss, RWS uses "span" 38 times and "depth" 3 (two gloss sites plus a bibliography title); PIP uses "span" 82 times and "depth" 6 (two glosses, three "recursion depth" — a different concept — and one reference).

**Evidence.** 6 of the 12 papers read for dimension E. Counts above re-verified by grep for this pass; the first-pass figures (93 and 37) were wrong.

**Exemplars.**

- "parallel algorithm design has mostly focused on solutions with low work (number of operations) and span (depth or longest critical path) complexities." — *PIP*, Introduction
- "span (aka. depth, the longest critical path of dependences), cache size, and cache block size, respectively (definitions in Section 2)" — *RWS*, Introduction
- "an Application Programming Interface (API), or a specification for how two system components communicate with each other, provided by the container" — *p2307-wheatman*, Introduction

**Violation signature.** The same object is a 'cohort' in one paragraph and a 'sample' in the next, with no sentence establishing they are the same; or a field-standard term is used bare in the introduction and defined only in Section 3. Detector: count both members of each candidate synonym pair, then inspect every occurrence of the minority word — each should be a gloss site, a heading, a bibliography title, or a demonstrably different concept. Any minority-word occurrence that is a live use of the same referent means the retirement failed; a 3:2 split means it was never attempted.

**Revision.**

- Before: We measure attrition across waves. Dropout was higher in the second wave, and the loss rate stabilised thereafter.
- After: We measure attrition (the share of enrolled participants who do not complete a wave) across waves. Attrition was higher in the second wave and stabilised thereafter.

**Do not apply when.** The two words genuinely denote different things in your paper — then the collision-legislating pattern applies instead: keep both and rule on the distinction rather than collapsing them. Also skip the gloss for a term every reader of the venue defines identically and that your paper uses only in passing.

---

## Grant the shorthand explicitly instead of dropping qualifiers silently

**Move.** Before abbreviating a notation or phrase — dropping a subscript, argument, or modifier — the paper states the licence in one clause: "With clear context we drop X", "For brevity, we refer to … as just …".

**Why it works.** The reader is told the long and short forms name one object, so a later apparent inconsistency reads as convention rather than error. Note that the meta-language itself is deliberately unvaried: seven of the twelve sampled papers reach for almost the identical formula, and 34 of 119 corpus files match the formula family — the corpus is uniform in its housekeeping prose while varied elsewhere.

**Evidence.** 7 of the 12 papers read for dimension E.

**Exemplars.**

- "With clear context, we drop the superscript 𝑋 ." — *covertree_2*, 2 Preliminaries
- "When clear from context, we drop the “in n.”" — *joinable*, 2 Notation
- "For brevity, we refer to the auxiliary space in future references to the relaxed PIP model as just the heap-allocated space." — *PIP*, 3.2 The Relaxed PIP Model

**Violation signature.** The full form appears in the definition and a clipped form everywhere after, with no sentence connecting them: "the posterior predictive distribution" becomes "the predictive". Detector: for each multi-word defined term, check whether a shorter variant appears later and whether any sentence licenses it.

**Revision.**

- Before: We compute the posterior predictive distribution for each site. The predictive is then compared across sites.
- After: We compute the posterior predictive distribution for each site; where the context is clear we call it simply the predictive. The predictive is then compared across sites.

**Do not apply when.** The abbreviation is one the field already uses without ceremony, or the full form appears only twice — announcing a shorthand for a term used twice is more machinery than the saving is worth.
