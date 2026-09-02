# Contested choices

Where the corpus genuinely splits, the split is recorded with the condition that governs it.
None of these is resolved by majority vote: a 7-5 count across well-written papers is a
signal that both options are live and something else decides which one is right.

Use this file when a review finding would otherwise read as "the paper should have done X"
and the corpus itself does both X and not-X.

---

### Say which way it went before you say how much (B) *vs.* Name the exhibit inside the sentence that states the number (G)

Not opposed — the exhibit-as-subject construction carries the verdict inside its that-clause ("Table 8 shows that Terrace is 1.6-1.9x slower than Ligra"), which satisfies both. What both forbid is the bare pointer ("Table 3 shows our results.") and the opening number dump. Condition: in a results section make the exhibit the subject AND put the direction in the complement; in the introduction the exhibit rides as a parenthetical on a claim the authors own; in the abstract the number appears with no pointer.

---

### Advance a design paragraph by naming the defect of the thing you just described (C) *vs.* Announce the cardinality, then hold one frame per item (C)

Genuinely opposing instructions for advancing a multi-part passage; the condition is whether the items are causally dependent. Test: can the items be reordered without loss? If yes they are parallel — announce the count and hold one frame. If no — step two exists because step one failed — use the defect chain, because ordinals flatten the dependency and hide why each step was taken. Both entries kept, each carrying the other as its do_not_apply_when.

---

### Use "Note that" to fence a caveat or block a misreading (C) *vs.* Concede at the point of the claim (B)

Opposed on whether a limitation should be marked as an aside or stated flat. The governing variable is what the caveat qualifies: an edge case, scope limit or possible misreading of a local claim gets the marker and stays inside the paragraph; a limitation of the contribution itself gets an owned, unmarked sentence adjacent to the claim. Wrapping a contribution-level limitation in "Note that" is the failure mode both entries name.

---

### Gloss the standard term, then retire the rival synonym (E) *vs.* Legislate term collisions out loud (E)

Both are right under different conditions, and the corpus splits on the ruling while never splitting on the act of ruling. The condition is whether a second referent exists that the rival word must cover. Two referents → force the words apart (xu-ppcsr: vertices vs nodes). One referent → either retire the rival after one gloss or declare them interchangeable in one sentence (am-tree: "We use node and vertex interchangeably"). Silent alternation is what both forbid.

---

### Never write the agentless research passive; keep "we" visible (D) *vs.* Choose the subject of a results claim by the claim's scope — drop the observer for a local verdict (D)

Not a real conflict, and worth stating so a reviser does not over-apply the first. The ban is on the agentless PASSIVE ("it was observed that"), not on agentless actives with a concrete subject: "Pkd-trees have the best performance" is active and its subject is what the sentence is about. The shared rule is that the subject slot goes to whatever the sentence is about — the artefact for a local verdict, the authors for a judgement over many measurements, the term for a definition.

---

### Hedge the priority claim, state the result flat (D) *vs.* Match the claim verb to the class of evidence — "we project", "we expect" (D)

Compatible; one rule underlies both. The hedge marks the part that could not be checked. On a measured or derived quantity a hedge is a defect; on an extrapolation past the measured range it is mandatory, and "we project" is then the honest verb rather than a hedged "we show". A draft is wrong when hedge strength does not track evidence class in either direction.

---

### Close the abstract on a checkable number with comparator and scope (A) *vs.* When the product is knowledge, put the proposition in the abstract (A) *vs.* psi, which closes its abstract on a pointer to its findings section

The invariant is that the abstract's last sentence must be checkable; the currency differs by contribution type. Artifact papers cash it as a number with a named comparator and stated scope; study papers cash it as the proposition that came out. A promise ("experiments demonstrate effectiveness", "we report our findings in Section 5") fails both, and psi's pointer is licensed only because its contribution is a comparative study whose findings do not reduce to one ratio.

---

### Lead the evaluation with what it found (B) *vs.* scc and ParChain, which open their evaluations with "Setup."/"Testing Environment."

A documented split, not an error, and the condition is scale. Many baselines across many datasets earn a findings-first map, because otherwise every table arrives with no question attached; a single system with one baseline and one table gets a findings block that merely duplicates the caption. Second condition: when the setup contains a choice the reader must accept before any number means anything (a non-standard metric, a contested split), define that first regardless of scale.

---

### Delete the "organized as follows" paragraph (A) *vs.* xu-ppcsr-alenex-21, which carries one

An exception with a measured base rate, not a disagreement: a roadmap paragraph appears in 17/119 papers (14%), so 86% do without one. Resolution: per-claim pointers are the rule; a roadmap is optional and permitted for long documents or mandating templates, but it never substitutes for the pointers. A draft with a roadmap and fewer than about five in-text cross-references has the pattern backwards.

---

### Run the technical core citation-free (F) *vs.* Restate an imported result as a numbered Fact carrying its citation (H)

Compatible once the citation's function is distinguished. What the F pattern bans in the core is grounding citations scattered through the argument; a restated Fact with its source attached IS the provenance form that pattern requires. The genuine exception both share: a section that extends a prior proof should re-cite at the extended step (DP re-cites Hong and Kung at the proof rather than once in the framing), so a reader can verify the chain.
