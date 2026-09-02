# Pass 3 — Reference

**Ask:** For every pronoun, demonstrative, ordinal and resumptive in this paragraph, can the reader resolve it without looking back more than one sentence?

**Do not touch in this pass.** Do not rename anything — Pass 2 settled the names, and a 'clearer' synonym introduced here re-breaks it. Do not enforce name-repetition inside a comparison: the pattern demanding a full name in every because-clause was REJECTED (39 corpus sentences read 'X is faster than Y because it …'), so a pronoun that resumes the main-clause subject is correct and must not be flagged. Do not flag 'this issue', 'this problem' or 'this case' as empty shell nouns (27, 80 and 256 uses). Do not flag a bare 'This' opening a paragraph as an automatic error — 15% of paragraph-initial demonstratives in the corpus are bare; treat it as a prompt to check the referent. Leave hedges, verbs and punctuation alone.

8 patterns.

---

## Reserve the bare demonstrative for the consequence slot

**Move.** Open a sentence with a bare "This" only when the predicate is one that can take a proposition or a just-described action as its subject — is, is because, means, gives, leads to, implies, allows, requires, indicates, and the causal group makes/increases/reduces/takes. The moment the sentence predicates something only a concrete object can do, the noun goes back on the demonstrative. Plural "These" is far stricter than singular "This": in the corpus, sentence-initial "This" is bare half the time (1,127 of 2,251) but sentence-initial "These" carries a noun 297 times against 18 bare, so give "These" a noun by default.

**Why it works.** A bare "This" is resolved as "the statement I just finished", and a relational verb confirms that resolution within two words, so no search is needed. A content verb instead sends the reader back to hunt for a concrete agent or patient, and the hunt fails because the antecedent was a proposition, not a thing. This refines rather than contradicts the digest: its 915 bare demonstrative subjects are not a free alternative to the 1799 noun-carrying ones but a separate slot — the sentence-initial bare demonstratives in the corpus take almost exclusively relational predicates (is, can, means, gives, indicates, leads, requires, allows, implies, guarantees, ensures).

**Seen in.** stepping, DP, fastbcc, mvgc, impdecomp, psi (sampled from 8-10 papers for this sub-topic, not all 119)

- "In almost all experiments, the social and web graphs show a similar trend. This is because they follow similar power-law-like degree distribution." — *stepping*, Experiments

- "Algorithm 2 uses a tree-based structure to provide tight work bounds for applying a batch of modifications or extractions. This is asymptotically better than batch-dynamic search trees [19, 21, 85]." — *stepping*, Data structure implementation

- "In Section 4.1 we show the symmetric cache complexity. This is a direct extension of the classic result by Hong and Kong [56] to an arbitrary dimension." — *DP*, Introduction / roadmap

**Violation signature.** A sentence opening on a bare "This"/"These" whose verb needs a concrete agent or patient ("This was collected in 2019", "These increased by twelve points"); note a be-verb does not make it safe, since "This was recomputed" is a content predicate wearing a copula. Also: any bare "These" opening a sentence; a bare demonstrative whose referent sits two or more sentences back; a bare demonstrative reaching across a section heading.

**Revision.**

- Before: Households in the treatment arm reported higher savings, and attrition was concentrated in the control arm. This was recomputed after reweighting.
- After: Households in the treatment arm reported higher savings, and attrition was concentrated in the control arm. The savings gap was recomputed after reweighting.

**Do not apply when.** The preceding sentence offers two candidate propositions (a concession plus a claim, or a coordinated pair) — there the noun is required even with a relational verb. Paragraph openings are a tendency, not a rule: 85% of paragraph-initial demonstratives in the corpus carry a noun ("This section", "This result") but 15% are bare ("This is asymptotically optimal…", "This follows from Chernoff bound"), so treat a bare one at a paragraph start as a cue to re-check the referent rather than an automatic error.

<sub>Verifier: Core claim holds and is the best-measured of the eight. Re-measuring sentence-initial bare demonstratives over all 119 papers (1,148 instances after excluding noun-carrying heads): 90% take a relational/consequential predicate — is 448, can 105, means 84, gives 64, indicates 48, leads 37, requires 28, allows 28, proves 22, guarantees 13, implies 12. The 10% residue (makes 16, avoids 14, takes 13, reduces 5, increases 6) is not a counterexample: I read 14 of them and every antecedent is the whole preceding action ('This takes O(1) messages and O(1) whp PIM work'), so the operative test is 'can </sub>

---

## Give the demonstrative a noun that classifies the antecedent, not one that repeats it

> Narrowed after corpus measurement contradicted the original claim.

**Move.** When pointing back at something the previous sentences described but never named, write "this/these + an abstract noun that says what kind of thing it was" — trend, asymmetry, skewness, tradeoff, property, insight, approach, step, issue, improvement — supplying a label the antecedent itself lacked.

**Why it works.** The label converts a stretch of description into a countable thing that can take the subject slot and carry the next claim, and the noun chosen does argumentative work: calling the two preceding clauses "this tradeoff" is exactly what licenses the verb "overcomes". The label is then reusable as a term for the rest of the paper, so the cohesion device and the terminology are the same move.

**Seen in.** xu-cpma-ppopp-24, xu-terrace-sigmod-21, impdecomp, psi, covertree_2, mvgc, DP, fastbcc (sampled from 8-10 papers for this sub-topic, not all 119)

- "When compared with cache-optimized trees, PMAs were slower to update but faster to scan. The batch-parallel CPMA overcomes this tradeoff between updates and scans by optimizing for cache-friendliness." — *xu-cpma-ppopp-24*, Abstract

- "The reason for this asymmetry, roughly speaking, is that writing to memory requires a change to the state of the material, while reading only requires detecting the current state." — *impdecomp*, Introduction

- "This skewness presents unique challenges for efficiently representing dynamic graphs." — *xu-terrace-sigmod-21*, Introduction

**Violation signature.** A paragraph where successive claims are hooked on with bare "this"/"it" and the reader must reconstruct the referent; "this" plus a genuinely contentless shell noun — "this fact" (3 uses in 1.1M words), "this aspect" (0), "this thing" (0) — used where the noun classifies nothing; or a demonstrative that merely copies the head noun of the previous sentence where a classifying noun would have advanced the argument. Do not flag "this issue", "this problem" or "this case" (27, 80 and 256 uses): these authors treat them as ordinary classifying nouns.

**Revision.**

- Before: Uptake was high in urban clinics and negligible in rural ones. This has consequences for the rollout schedule.
- After: Uptake was high in urban clinics and negligible in rural ones. This geographic gap has consequences for the rollout schedule.

**Do not apply when.** The classifying noun would be vaguer than the thing it replaces, or would smuggle in a judgment you have not yet argued — "this failure", "this flaw", "this error" before the evidence is on the page. An empty or tendentious shell noun is worse than the bare demonstrative.

<sub>Verifier: The move is real and well supported: 7,161 noun-carrying demonstratives corpus-wide, and the top heads are exactly the classifying kind — approach 138, idea 60, property 37, challenge 29, technique 27, observation 14, assumption 24, recurrence 24, plus the labels the exemplars use (this tradeoff 8, this asymmetry 8, this skewness 2). The empty-shell prohibition is confirmed at the extremes: 'this fact' 3 uses in 1.1M words, 'this aspect' 0, 'this thing' 0. One clause is contradicted: the violation signature lists 'this issue' as a contentless shell noun, but the corpus uses 'this issue' 27 tim</sub>

---

## Close a citation string or enumeration with "These + class noun"

> Narrowed after corpus measurement contradicted the original claim.

**Move.** After a bracketed reference string, a run of examples, or a bulleted enumeration, make the next sentence's subject "These + the noun that names the class" — these studies, these systems, these techniques, these matrices, these bounds. Never leave "These" bare: sentence-initial "These" carries a noun 297 times against 18 bare. A plain "They" is a legitimate second choice, but only when the preceding sentence already named the group with a head noun of its own.

**Why it works.** A bracket or a list is not a noun phrase, so there is nothing for a pronoun to pick up; the class noun supplies the missing head and, by choosing which class word to use, tells the reader which property of the group the argument is about to exploit.

**Seen in.** xu-terrace-sigmod-21, xu-phil-web, fastbcc, xu-cpma-ppopp-24, stepping, DP (sampled from 8-10 papers for this sub-topic, not all 119)

- "These techniques greatly improve locality in computations on static graphs, but do not easily translate to graphs that evolve over time." — *xu-terrace-sigmod-21*, Introduction

- "All but two are from the University of Florida Sparse Matrix Collection [1]. These matrices were chosen to represent a variety of application domains and block structures." — *xu-phil-web*, Evaluation, Test Cases

**Violation signature.** A sentence immediately after a reference or bullet list that begins "These are…", "These allow…", "This shows…", or "All of them…" with no head noun naming what the list contained; a "these" whose class the reader must infer from the bracketed numbers; or a "They" whose only available antecedent is the bracket itself rather than a noun in the preceding sentence.

**Revision.**

- Before: Several studies have measured the effect in adolescents [4, 9, 17]. They all rely on self-reported intake.
- After: Several studies have measured the effect in adolescents [4, 9, 17]. These surveys all rely on self-reported intake.

**Do not apply when.** The group is already named by a head noun in the preceding sentence and remains the topic. Repeating the noun then stutters, and the corpus uses plain "They" there — 16 times against 28 "These + noun" in the sentence right after a citation-ending sentence, so the pronoun is a live option and not a defect to flag.

<sub>Verifier: Half the move survives measurement and half is contradicted. Confirmed: a bare plural demonstrative is genuinely near-absent — sentence-initial "These" carries a noun 297 times against 18 bare (94%), and after a sentence ending in a bracket citation the split is 28 "These + noun" against 3 bare. Contradicted: 'never "they"'. Sentences immediately following a citation-ending sentence open with "They" 16 times against those 28 — a 2:1 preference, not a prohibition. And the 16 are not sloppy: 'Delaunay algorithms … date back to the 1970s [36]. They are based on the rip-and-tent idea', 'the rake c</sub>

---

## Spend a pronoun on one hop only

**Move.** Use "it"/"they" only in the sentence directly after the referent is introduced, and only while that referent is still the grammatical subject — the pronoun inherits the subject slot, it does not search. At the next sentence, or at any switch of subject, the noun comes back. Corpus: 637 single-sentence pronoun resumptions, 21 two-sentence chains, one three-sentence chain in 1.1M words.

**Why it works.** At one hop with a unique candidate, a pronoun costs the reader nothing; each extra hop, and each competing noun of the same number, converts a free reference into a search. The corpus's pronouns are almost always single: one "It" sentence elaborating the thing just named, then the noun returns.

**Seen in.** fastbcc, mvgc, covertree_2, xu-cpma-ppopp-24, xu-terrace-sigmod-21 (sampled from 8-10 papers for this sub-topic, not all 119)

- "Later, Tarjan and Vishkin proposed the canonical parallel BCC algorithm [65]. It uses an arbitrary spanning tree (AST) (a spanning tree with any possible shape) of the graph instead of the depth-first tree." — *fastbcc*, Introduction

- "A remove(B) first sets B’s status to marked at line 44. It then stores the frozen Descriptor in both B->leftDesc and B->rightDesc." — *mvgc*, Version-list implementation

**Violation signature.** A pronoun chain running three or more sentences on the same referent; a pronoun whose intended referent was not the subject of the preceding sentence; or a pronoun resuming after an intervening figure reference, displayed equation, table, or parenthetical list.

**Revision.**

- Before: The registry links hospital records to the insurance claims database. It has been updated annually since 2004, and it now covers eighty percent of the population. It is therefore suitable for our design.
- After: The registry links hospital records to the insurance claims database. It has been updated annually since 2004 and now covers eighty percent of the population. The registry is therefore suitable for our design.

**Do not apply when.** A rival entity with a short proper name is on stage — then repeat the name instead of pronominalising; or the passage is a definition in which several entities of the same type are live, where the corpus uses "that + noun".

<sub>Verifier: The headline is the single best-confirmed claim in this topic. Counting runs of consecutive sentences opening on a referential It/They (expletives excluded) across all 119 papers: 637 runs of length 1, 21 of length 2, and exactly 1 of length 3 in 1.1M words. So 'the corpus's pronouns are almost always single' is right at 96.7%, and 'a pronoun chain running three or more sentences' is a violation signature that a reader can apply to a draft with no corpus knowledge and that the corpus essentially never trips. One clause needs narrowing: the move licenses the pronoun 'only when it is the sole ca</sub>

---

## Use "such + noun" to move from the instance to the kind

**Move.** When the next sentence generalises over everything of the type just described rather than continuing about the specific instance, open it with "such + the class noun" — such algorithms, such graphs, such cases, such queries — instead of "these + noun". About half the corpus uses the device (109 sentence-initial instances in 58 of 119 papers), so it is a live option at a genuine instance-to-kind turn, not a device to reach for at every back-reference.

**Why it works.** "This/These" asserts that the reference is to the very items just mentioned; "such" says "any of this kind". Using the right one tells the reader, at the first word of the sentence, whether the claim that follows is about the example or about the class — a distinction the reader would otherwise have to infer from the whole sentence.

**Seen in.** DP, stepping, fastbcc, covertree_2, psi (sampled from 8-10 papers for this sub-topic, not all 119)

- "Sequential cache-oblivious algorithms are flexible and portable, and adapt to all levels of a multi-level memory hierarchy. Such algorithms are well studied [8, 28, 39]" — *DP*, Preliminaries

- "This property requires researchers to rethink the design of algorithms and software, and optimize the existing ones accordingly to reduce the writes. Such algorithms are referred to as the write-efficient algorithms [52]." — *DP*, Introduction

**Violation signature.** A generalising sentence that opens "These + noun" when the claim is really about a class rather than the listed members; or "such" used as a bare pronoun ("as such", "such is the case") instead of as a determiner on a noun — the bare pronoun forms total 6 uses in 5 papers.

**Revision.**

- Before: One cohort excluded participants who had already seroconverted. These studies are hard to compare with population surveys.
- After: One cohort excluded participants who had already seroconverted. Such designs are hard to compare with population surveys.

**Do not apply when.** You mean exactly the items just listed and no others: "such" silently widens the claim to unexamined members of the class. Also drop the idea of coining a noun from the verb for an action antecedent ("such removals") — that is one use in 1.1M words; the corpus's "such" heads are ordinary class nouns already on the page.

<sub>Verifier: The device is real but smaller than the validation note implies, and one instruction inside the move is unsupported. The validation doc's '1,635 uses across 118/119 papers' conflates three different constructions: I measure 'such as' 608, 'such that' 414, 'such a/an' 121, and only ~370 uses (88 papers) of the anaphoric 'such + class noun', of which 109 (58/119 papers) are the sentence-initial 'Such X …' the pattern is actually about. So the pattern is supported by roughly half the corpus, not by 118 of 119 papers — worth stating honestly since a writer told 'this is heavily used' will overuse </sub>

---

## Never leave "the former/the latter" bare — attach the noun or name the alternative

> Narrowed after corpus measurement contradicted the original claim.

> One exemplar is verbatim but does not fully illustrate the move — see the verifier note.

**Move.** Resume a two-way split by naming the alternative outright. If a resumptive is used at all, attach the noun that classifies what it points at ("in the latter case", "the latter two problems", "the latter model") and use it only when both alternatives were enumerated in the sentence immediately before. Corpus: 30 uses of former/latter in 1.1M words across about 20 of 119 papers, 24 of them carrying a noun and 6 bare — these authors overwhelmingly re-name rather than index, and when they do index they never index bare.

**Why it works.** Measured over the 1.1M-word corpus, "the former" occurs 5 times and "the latter" 26 times across 20 of 119 papers, while "respectively" occurs 418 times — these authors overwhelmingly re-name rather than index. The surviving uses are all determiners on a noun, never a bare noun phrase standing in for a name, because a bare "the latter" forces the reader to re-parse and count the previous sentence's alternatives.

**Seen in.** mvgc, fastbcc (sampled from 8-10 papers for this sub-topic, not all 119)

- "This could fail for two reasons: B has already been spliced out, so there is no need to proceed, or there is a splice(A,D,B) that has been partially completed" — *mvgc*, Correctness of the version list

- "In the latter case, the remove that is splicing out D will also splice B after D, so again there is no need to proceed with the splice of B." — *mvgc*, Correctness of the version list

**Violation signature.** "The former" or "the latter" standing alone as a noun phrase with no noun attached ("The latter is more common in concentrated markets"); or either of them pointing back to alternatives named more than one sentence earlier, so the reader has to re-parse and count.

**Revision.**

- Before: Firms can either raise prices or cut output. The latter is more common in concentrated markets.
- After: Firms can either raise prices or cut output. Cutting output is more common in concentrated markets.

**Do not apply when.** The two alternatives are clause-length or formula-length descriptions enumerated in the sentence just before, so repeating one would swamp the sentence: "in the latter case" is then the shorter and clearer resumption, and is exactly where the corpus uses it. This also covers a paragraph that runs "In the former case … In the latter case …" through a two-case analysis — the corpus does this, so do not flag the pair on proximity alone; flag only the bare form.

<sub>Verifier: The substance matches the corpus and the worked precedent, but two numbers and two signature clauses are wrong. My count over the cleaned corpus: 'the former' 5, 'the latter' 25, together 30 uses in ~20 of 119 papers; of these, 24 attach a noun ('the latter case' 15, 'the latter two problems', 'the latter model', 'the latter measure') and 6 are bare ('For the latter, used by four of our algorithms', 'Pseudo is relatively slower on the former', 'the former is intuitively a better alignment than the latter'). So: rare overall, and bare in only a fifth of its uses — exactly the validation doc's f</sub>

---

## Bind the anaphor with "that + noun" when the type is populated

**Move.** When an entity was introduced indefinitely or under a quantifier — "a node", "each node", "a leaf", "a household" — resume it with "that + the same noun" rather than "it" or a bare "the noun", including within the same sentence: "The height of a node is the distance from that node to a leaf." This is the marked minority form ("the node" outnumbers "that node" 213 to 32), so spend it exactly where a second instance of the type could otherwise be read in; corpus-wide it appears 280 times across 81 of 119 papers.

**Why it works.** "It" identifies only number; "that node" identifies which one, so the reader never has to test the rival readings that a populated type creates. Corpus-wide the construction is a working tool, not a flourish: "that node" 33 uses, "that point" 28, "that leaf" 19, "that vertex" 17, with 59 of 119 papers using some "that + count noun" anaphor.

**Seen in.** xu-terrace-sigmod-21, xu-cpma-ppopp-24, impdecomp (sampled from 8-10 papers for this sub-topic, not all 119)

- "The height of a node is the distance from that node to a leaf." — *xu-terrace-sigmod-21*, Preliminaries, PMA background

- "The upper and lower density bounds in each node are related to the height of that node." — *xu-terrace-sigmod-21*, Preliminaries, PMA background

- "If a leaf violates its density bound, the algorithm then walks up the implicit PMA tree from that leaf until it finds a node that respects its density bound." — *xu-cpma-ppopp-24*, Batch-update algorithm

**Violation signature.** A definitional or procedural sentence that introduces an entity indefinitely ("a node", "each firm") and then resumes it with "it", "its", or a bare "the node" while other instances of the same type are in play; or two instances of one type in a sentence sharing a single "it" that could attach to either.

**Revision.**

- Before: The premium charged to a household depends on its risk score, and it is recalculated each year.
- After: The premium charged to a household depends on that household's risk score, and the premium is recalculated each year.

**Do not apply when.** Only one instance of the type is live in the passage. "That" then signals a contrast the reader looks for and cannot find, and plain "the" or "it" is the correct, lighter choice.

<sub>Verifier: Confirmed as a real working device, with the counts close enough to stand: I measure 'that node' 32 (17 papers), 'that leaf' 17 (10), 'that vertex' 15 (9), and 280 'that/those + count noun' anaphors across 81 of 119 papers — broader than the pattern's claimed 59, so the claim is conservative. Two corrections. 'That point' is given as 28; I count 21, six of which are the temporal idiom 'at that point', leaving ~15 genuine anaphors. And the move needs its actual trigger stated: all three exemplars resume an antecedent introduced indefinitely or under a quantifier — 'a node … that node', 'each no</sub>

---

## Re-supply the head noun on an ordinal once the list has drifted out of working memory

> Narrowed after corpus measurement contradicted the original claim.

**Move.** Carry the category noun on an ordinal by default — 'The second challenge is ...', 'The second axis ...' — since noun-carrying ordinals outnumber bare ones about 7:1 in the corpus. Drop to the bare ordinal only when it closes a frame the reader still has open: a bare 'The first is ...' earlier in the same paragraph, with at most a few sentences of elaboration between them. Across a paragraph break, heading, figure or page, the noun comes back.

**Why it works.** A bare ordinal is an anaphor whose antecedent is the category noun in the announcement. Past a short span that antecedent is no longer active and the reader must scroll back to recover what kind of "second" this is. Re-supplying the noun costs one word and removes the lookup. The digest's cohesion count (roughly two-thirds of demonstratives carry their noun) is the same instinct applied to ordinals.

**Seen in.** im, p2307-wheatman, ch, kcore, lis, scc, pimtrie (sampled from 8-10 papers for this sub-topic, not all 119)

- "The second is insufficient parallelism." — *im*, 1 Introduction (three sentences after the announcement)

- "The second axis evaluates existing graph-algorithm frameworks compared to BYO" — *p2307-wheatman*, 1 Introduction, Benchmark results (across a paragraph break)

- "The second challenge is to dynamically maintain the graph in parallel, since the graph may experience rapid changes" — *ch*, 1 Introduction (after four sentences of elaboration)

**Violation signature.** A bare 'The second' or 'The third' standing as subject when no bare 'The first is ...' is open in the same paragraph, or when a paragraph break, heading, figure or table sits between the announcement and the item. Also a bare ordinal whose announcing sentence named no category noun at all, leaving nothing for it to be an ordinal of. Same test for a bare 'This' or 'the latter' reaching back across a paragraph boundary.

**Revision.**

- Before: We face two obstacles. First, participation is self-selected. [six sentences of detail about selection] The second is measurement error in the exposure variable.
- After: We face two obstacles. First, participation is self-selected. [six sentences of detail] The second obstacle is measurement error in the exposure variable.

**Do not apply when.** The items sit in back-to-back short sentences built on the same bare frame ('The first is space; the second is time'). There the category noun is still live and repeating it is padding.

<sub>Verifier: Right instinct, wrong default. The pattern says an item within a sentence or two of the announcement 'takes the bare ordinal', implying bare is the near-range norm. Measured: bare ordinal subjects ('The second is ...') number 14 in 1.1M words across 11 papers, against 106 noun-carrying ordinals ('The second challenge is ...', 'The second approach ...') across 58 papers — roughly 7:1 for the noun, and the two forms coexist at short range (integer-sort writes 'The first case is when ... The second is when ...' three sentences apart). Reading all 14 bare instances shows the real licensing conditi</sub>
