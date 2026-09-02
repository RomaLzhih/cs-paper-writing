# Known gaps

What this skill does not cover, and why. Written so a reviewer knows when to stop trusting it
rather than discovering the boundary by being given bad advice.

The corpus is 119 papers in parallel algorithms and data structures, from three research
groups, published 2011-2026, overwhelmingly at CS conferences using numeric-bracket citation.
Every gap below traces to that shape.

---

### A

Nothing on the title at all — no pattern about what a title promises or whether the abstract discharges it, though the rubric opens with that contract. Nothing on the abstract's move sequence or its sentence budget per move: two entries cover only the last sentence and the content type. And section inventory (the job each section is asked to do) is unmeasurable here, since pdftotext does not isolate headings — best recovery was 7/119 papers. A future pass should hand-code 12-15 abstracts move by move with sentence counts, and hand-code the title/abstract/first-contribution triple, since neither can be greped.

---

### B

Discussion and limitations are thin, and the corpus is probably the reason: CS conference papers mostly have no discussion section, so nothing was found on raising alternative interpretations, on hedging calibration sustained across a discussion, or on what a discussion adds that results do not. The three surviving entries near this territory (concession placement, conclusion residue, named open problems) are all short-range. A future pass should either mark this dimension as not evidenced by this corpus or extend the corpus with journal-format papers rather than manufacture patterns from four instances.

---

### C

The transition inventory is measured but unexploited. The digest has per-paper counts for however (117/118), note that (99/118), therefore, thus, hence, instead, that is, for example — and only "note that" became a pattern. Nothing says which connective does which job, or what the corpus's ratio of contrastive to additive connectives is, though that ratio is exactly what distinguishes the defect-chain paragraph from the catalogue paragraph. This is the single most tractable gap: the counts already exist and only need a reading pass to attach function to form.

---

### C/E

Demonstrative cohesion has no entry. A verifier noticed that p2307-wheatman opens interpretive sentences with "These results …" ten times and never varies it to "These findings" or "These observations", and explicitly deferred it as needing its own exemplars. The rubric asks for antecedent clarity for pronouns and demonstratives ("this" + noun) and nothing in the 71 covers it. The detector is ready-made — find every sentence-initial bare "this"/"these" and check for a category noun — and it is one of the highest-frequency defects in weak drafts.

---

### D

Sentence openings other than fronted purpose clauses are uncharacterised: nothing on how often sentences open with an adverbial frame, a connective, or the bare subject, though this is measurable and shapes rhythm as much as length does. Embedded-clause depth is covered only negatively, by the subject-verb-proximity rule. Otherwise this dimension is the best covered of the eight.

---

### E

When a symbol should replace a word — the rubric's notation-conventions bullet — is touched only obliquely by the shorthand and scope-stamp entries. Nothing addresses the choice between prose and notation for the same content, which is a live decision in any quantitative field and portable to statistics-heavy work in any discipline.

---

### F

Everything rests on numeric-bracket style, at a corpus-wide bracket-to-integral ratio of about 22:1. Author-date venues (APA, Chicago) receive only a do_not_apply_when clause, and the bracket-placement entry — the highest-ranked in the dimension — does not transfer cleanly at all, since an author-date citation always contains a name. Also missing: how self-citation is handled, and how the boundary of a long borrowed passage (more than one sentence) is marked. A future pass needs a non-bracket corpus to say anything reliable to those venues.

---

### G

No pattern on uncertainty, though the rubric asks for it explicitly. The corpus reports spread across instances but essentially nothing on run-to-run variance, repeated trials, error bars, or significance, because a systems corpus does not need them — so the library currently has nothing to say to a field where uncertainty reporting is the norm, and worse, its ranges-across-instances advice could be mistaken for it. Two of the nine G entries also survive only as variants (ceiling statements at 3/119; the losing-variant exhibit at 3 papers), so the dimension is thinner than its entry count suggests.

---

### H

Signposting density has no measured norm, unlike paragraph length in dimension C, so "signpost more" has no calibration number and a reviser cannot tell over- from under-signposting. A future pass should count signposting phrases per 1000 words per paper and report the distribution, exactly as was done for sentence and paragraph length. Also nothing on how the assumed-knowledge boundary shifts between the introduction and the technical core, though one entry (prerequisites) touches its edge.

---

### cross-cutting (method)

Two systemic weaknesses a future pass must fix before ranking. (1) papers_seen_in counts are out of the 12 papers each dimension agent read, not out of 119; a pattern at 8/12 and a pattern at 8/119 currently look alike in the JSON, which is why every entry here carries an explicit papers_note. Only 8 claims were re-validated corpus-wide. (2) Numeric claims inside "why" fields were wrong twice out of the handful checked (span/depth counts in two papers, possessive back-reference counts in two more) and one detector regex was off by 14× on first writing. Validate mechanically before ranking, and re-measure every number that appears inside a pattern's prose, not only the quotes.
