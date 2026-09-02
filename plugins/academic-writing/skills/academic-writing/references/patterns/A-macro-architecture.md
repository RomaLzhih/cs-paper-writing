# A. Macro-architecture

8 patterns, ordered by how much each would improve a weak draft.

---

## State the gap as a settleable proposition, and answer it in the next paragraph

**Move.** The last sentence before the thesis states the gap as a proposition in explicit epistemic form — "it remains open whether…", "there exists no X with both…", "we are unaware of…" — and the next paragraph opens with the sentence that settles exactly that proposition; where an author wants the reader's question voiced, it is converted to this declarative rather than posed as an interrogative, and the minority of papers that do pose a literal question answer it in the immediately following sentence.

**Why it works.** The gap becomes a yes/no question rather than a complaint about prior work's quality, so the contribution reads as an answer instead of an assertion of superiority; adjacency means the reader never carries the gap across intervening material; and the declarative asserts something checkable while an unanswered question spends credibility.

**Evidence.** 9 papers, union of the A and H samples (12 papers each). Corpus-wide: only 18/119 papers contain any rhetorical question of this shape in body prose.

**Exemplars.**

- "Hence, it remains open whether an efficient solution exists for incremental MST" — *am-tree*, 1 Introduction, end of gap paragraph
- "Unfortunately, there exists no parallel LIS algorithm with both work-efficiency and round-efficiency." — *lis*, 1 Introduction
- "It is therefore worth asking, whether we can adapt the simple join-based framework to also achieve I/O-efficiency with provable guarantees." — *pbtree*, 1 Introduction

**Violation signature.** The gap is only an evaluative complaint — "existing approaches are limited", "prior methods suffer from several drawbacks", "little attention has been paid to X" — with no proposition attached; or the gap paragraph and the contribution paragraph are separated by other material; or a run of two or more interrogatives with no answering sentence in the paragraph. Detector: try to rewrite the paper's gap as a yes/no question. If you cannot, the pattern is absent.

**Revision.**

- Before: Existing serological assays have well-documented limitations, and the literature on cross-reactivity remains fragmented. Why do these assays disagree? What should a surveillance programme use? We therefore developed a new multiplex assay.
- After: Existing assays have been validated only against single-antigen panels; it remains unknown whether they distinguish recent from historical exposure when antigens are assayed jointly. In this paper, we develop a multiplex assay that makes that distinction.

**Do not apply when.** The contribution is a synthesis, review, or dataset with no single open question behind it; or the question is the paper's actual unresolved problem, posed as such in the conclusion, where an unanswered question is content rather than device. Where a field treats first-person epistemic claims as overreach, scope it ("to our knowledge") but still end on the proposition.

---

## Attach every section pointer to the claim that creates the need for it, and delete the roadmap paragraph

**Move.** Every claim that will be discharged later carries its own inline or parenthetical pointer to the section that discharges it, spread across the introduction and body, in place of one enumerating roadmap block.

**Why it works.** A roadmap is read once and forgotten; a pointer attached to a claim is read at the moment the reader wants it, and doubles as a promise the author must keep, which keeps the section inventory honest.

**Evidence.** 15 papers across the A and H samples. Validated corpus-wide: an explicit roadmap paragraph appears in 17/119 (14%); the sampled papers carry 8-26 in-text section pointers each.

**Exemplars.**

- "We will refer to this approach as cluster-BFS (C-BFS), and present more details in Sec. 3." — *cbfs*, 1 Introduction
- "with constant-factor costs and amortization overheads that will likely render such designs inefficient in practice (see §2.2 for discussion)." — *pimzd*, 1 Introduction
- "The first contribution of this paper is to formally discuss (in Sec. 7) a wide range of temporal graph applications with different setting-problem combinations" — *am-tree*, 1 Introduction

**Violation signature.** A paragraph of the shape "Section 2 reviews… Section 3 presents… Section 4 evaluates…" at the end of the introduction, and no section number anywhere else in the introduction. Counting test: one roadmap paragraph plus fewer than about five in-text cross-references means the pattern is absent.

**Revision.**

- Before: The remainder of this paper is organized as follows. Section 2 reviews the corpus. Section 3 describes the annotation scheme. Section 4 reports agreement. Section 5 concludes.
- After: [Roadmap deleted.] …we annotate every clause for evidential marking using a three-way scheme (described in Section 3). Two annotators coded a 10% sample; agreement was substantial (Section 4 reports the figures and the disagreement classes).

**Do not apply when.** Theses, technical reports and long journal articles where a reader needs one map, or a template that mandates a roadmap. Even then keep the per-claim pointers: the roadmap replaces none of them.

---

## Close the abstract on a checkable claim: a number with its comparator and its scope

**Move.** The abstract's final evidence sentence gives a quantified comparison whose comparator is named and whose scope is stated ("on each graph", "on all the 18 tested graphs", "over the best sequential baseline"), instead of restating the contribution or promising findings.

**Why it works.** The last sentence is what a skimming reader retains; a number with a named comparator and a stated scope is checkable, while "demonstrates effectiveness" carries no information and a bare ratio carries almost none.

**Evidence.** 8 of the 12 papers read for dimension A.

**Exemplars.**

- "FAST-BCC is 3.1× faster than the best existing baseline on each graph." — *fastbcc*, Abstract, final sentence
- "Under the same memory budget, our new solution improves accuracy and/or time on all the 18 tested graphs." — *cbfs*, Abstract, final sentence
- "Our algorithm shows speedups of up to 315× over ParK, 33.4× over PKC, and 52.5× over Julienne." — *kcore*, Abstract, final sentence

**Violation signature.** The abstract's last sentence is a restatement of the contribution, a promise ("experiments demonstrate the effectiveness of the proposed approach", "we report our findings in Section 5"), or a bare figure. Detector: read only that sentence and ask "better than what, and over what set of cases?" If either answer is missing, the pattern is absent.

**Revision.**

- Before: Experiments on several datasets demonstrate the effectiveness of the proposed classifier.
- After: Across all six benchmark corpora, the classifier reduces error by 18-24% relative to the best published baseline, and by 31% on the two low-resource corpora.

**Do not apply when.** Purely theoretical papers with no evaluation — there the closing claim is the bound together with the prior result it improves on; or a venue mandating a structured abstract with a fixed final field. A comparative study whose findings do not reduce to one ratio may legitimately close on a pointer to its findings section (psi does).

---

## Write one thesis sentence and reuse it near-verbatim at the abstract pivot, the introduction hinge, and the conclusion's first line

**Move.** One sentence of the form "In this paper, we <verb> <object>, with <scope>" is planted, with the same head nouns and the same scope clause, where the abstract turns from problem to work, where the introduction stops describing the field, and as the conclusion's opening sentence.

**Why it works.** A reader entering at any of the three usual entry points gets the identical claim in identical words, so no reconciliation is needed and the paper's scope cannot drift between sections.

**Evidence.** 8 of the 12 papers read for dimension A. Corpus-wide "in this paper" appears in 111/119.

**Exemplars.**

- "In this paper, we systematically study parallel spatial indexes, with a special focus on achieving high-performance update performance for highly dynamic workloads." — *psi*, Abstract
- "In this paper, we systematically study parallel spatial indexes, with a special focus on achieving high-performance updates in highly dynamic workloads." — *psi*, Conclusion
- "In this paper, we propose the FAST-BCC (Fencing on Arbitrary Spanning Tree) algorithm for parallel biconnectivity." — *fastbcc*, Conclusion, opening sentence

**Violation signature.** Extract the abstract sentence that first says what the authors did, and the conclusion's first sentence. If they share fewer than half their content words, or one names a broader object than the other, the anchor is missing. Also flags: the conclusion opens "We have shown that…" with a claim the abstract never made.

**Revision.**

- Before: Abstract: "We report an analysis of code-switching in bilingual classrooms." Conclusion: "This work has demonstrated that teacher-initiated language shifts serve several pedagogical functions."
- After: Abstract: "In this paper, we study teacher-initiated code-switching in bilingual classrooms, with a focus on its pedagogical functions." Conclusion: "In this paper, we studied teacher-initiated code-switching in bilingual classrooms, with a focus on its pedagogical functions. We identified three…"

**Do not apply when.** The conclusion is genuinely meant to reframe or generalise the contribution (a position piece, a discussion-heavy journal article), a style guide penalises cross-section repetition, or the repetition would eat a large fraction of a very short abstract.

---

## Give every contribution a label, and reuse that label verbatim where the contribution is delivered

**Move.** Each contribution gets a short handle — an ordinal, a bracketed tag, a bolded run-in heading, a named axis — and the same handle reappears where that contribution is worked out.

**Why it works.** Labels let the reader count the contributions, hold their place, and check at the end that each was delivered; they also let the author refer back without re-describing.

**Evidence.** 7 of the 12 papers read for dimension A.

**Exemplars.**

- "The second and the main contribution of this paper is a new, theoretically and practically efficient data structure for incremental MST, referred to as the Anti-Monopoly tree (the AM-tree)." — *am-tree*, 1 Introduction
- "The third axis studies the impact of different containers by fixing the algorithm using the BYO API and varying the container." — *p2307-wheatman*, 1 Introduction, Benchmark results
- "The algorithmic highlight in this paper is the Decomposable Property defined in Section 4." — *PIP*, 1 Introduction

**Violation signature.** Contributions are a run of "we also…" / "in addition, we…" sentences that cannot be counted; or a bulleted list whose items are never named again, so the reader cannot tell which section discharges which bullet. Detector: ask two readers how many contributions the paper claims. Different numbers mean the labels are missing.

**Revision.**

- Before: We introduce a new coding scheme and also validate it on a second corpus. In addition, we release the annotations, and we discuss implications for theories of evidentiality.
- After: This paper makes three contributions. (C1) a coding scheme for evidential marking (Section 3); (C2) a validation of C1 on an independent corpus (Section 5); (C3) a released annotation set (Section 6). …Section 5 then opens: "We now validate the scheme of C1 on…"

**Do not apply when.** Single-contribution papers and short notes, where labelling one item is ceremony; or where the contributions are genuinely inseparable aspects of one result — name the one result and stop.

---

## Give every omission a reason, a named item, a destination — and a one-line gist

**Move.** At the exact point of omission, one sentence gives the reason ("Due to the page limit"), the specific item, and the destination; the strongest instances add either what was retained and why, or the single idea being deferred, so the reader carries an idea forward rather than a hole.

**Why it works.** The reader learns immediately whether the missing piece is something they need and where to get it; the retained-or-gist clause converts an apology into an editorial decision the reader can evaluate.

**Evidence.** 12 papers across the A and H samples.

**Exemplars.**

- "the proofs for Fact 4.1 and 4.2 and Lem. 4.3 to 4.5 are given in the full version of the paper, and we mainly focus on the proofs that reflect some key ideas in our new algorithm." — *fastbcc*, 4 Correctness proofs
- "Hence, due to the space limit, we postpone the details of these two operations here in the appendix. The main difference lies in how subtrees are joined back." — *pbtree*, Appendix I, Additional Set Operations
- "Due to the page limit, we provide the full version of this paper [40] to present complete analysis and more experimental results." — *lis*, 1 Introduction, final sentence

**Violation signature.** A theorem stated with no proof and no note; a blanket "some details are omitted for space" naming neither item nor destination; a pointer with no address ("see the appendix", "available on request"). Detector: for each claim the paper does not support in-text, check that a nearby sentence names both the omitted item and where it went.

**Revision.**

- Before: Full regression tables are omitted here.
- After: Due to length limits, the full regression tables for all twelve specifications are in Appendix B; here we report the three that separate the competing hypotheses. The omitted ones differ only in the choice of control set.

**Do not apply when.** There is no companion version or appendix to defer to — then include the material or cut the claim it supports. Never use a deferral to park a claim the paper depends on. And do not attach a gist to a genuinely routine omission; a one-line gist on an omitted arithmetic check over-advertises it.

---

## When the product is knowledge rather than an artifact, put the proposition in the abstract and in each contribution paragraph

**Move.** In studies whose contribution is what was learned, the abstract and each contribution paragraph state the proposition that came out, instead of describing the design or promising findings later.

**Why it works.** A reader deciding whether to read a study needs the conclusion, not the protocol; forcing each contribution paragraph to end in a proposition also exposes any axis of the study that produced no usable answer.

**Evidence.** 3 of the 12 papers read for dimension A — recorded as a variant by frequency, but it is the governing form for study-type papers, of which the sample contains few.

**Exemplars.**

- "Somewhat surprisingly, we find that the average algorithm running time does not differ much across containers, especially those that support dynamic updates." — *p2307-wheatman*, Abstract
- "Results: Our findings are as follows. MI-GRAAL’s NCF is superior to GHOST’s NCF, while the performance of the methods’ ASs is data-dependent." — *ppi-exp*, Abstract

**Violation signature.** The abstract and contribution paragraphs report activities and coverage — "we evaluate A against B on C datasets", "we compare four configurations" — and never state a proposition. Detector: strike every abstract sentence whose main verb is evaluate, compare, measure, investigate, study, or present. If nothing assertable is left, the pattern is absent.

**Revision.**

- Before: We compare three antibody assays across two cohorts and report sensitivity, specificity, and cross-reactivity, and we discuss implications for surveillance design.
- After: Across two cohorts the three assays differ little in sensitivity (all 91-94%), but cross-reactivity with the related serotype varies fourfold and drives the differences in specificity. Surveillance designs are therefore better served by choosing on cross-reactivity.

**Do not apply when.** The contribution is an artifact, where the introduction correctly delivers the artifact's property or bound. Also when a finding is genuinely conditional in a way one clause would distort — state the condition in the same sentence rather than deferring the whole finding.

---

## Put related work after the technical sections — unless prior work is the thing you are studying

**Move.** When the paper contributes a new artifact, the introduction names only the specific rivals and the survey is deferred to a section just before the conclusion; when the paper's object of study IS the prior work, related work comes second, before any method.

**Why it works.** In the first case the reader reaches the contribution without wading through a survey, and the late section serves someone who has already understood the result; in the second the prior work is the material, so the paper is unreadable until it is on the table.

**Evidence.** 9 of the 12 papers read for dimension A. Section order could not be verified mechanically — pdftotext does not isolate headings — so this rests on direct reading only.

**Exemplars.**

- "We review more related work in Sec. 7." — *lis*, 1 Introduction, deferring the survey after naming the rivals
- "More details about them were overviewed in Sec. 3.2." — *kcore*, 8 Related Work, back-reference to baselines introduced earlier
- "Despite the impressive body of existing work on dynamic-graph systems and containers, at present it is essentially impossible to answer the very basic question of which container is appropriate for a given graph application." — *p2307-wheatman*, 1 Introduction (a paper whose object of study is prior work; its Related Work is Section 2)

**Violation signature.** (a) A survey sits between the introduction and the contribution in an artifact paper, so the reader waits pages for the result. (b) Related work is late but the evaluated baselines are defined nowhere else. Detector: list every prior system named in the results section and check each is defined before the method section.

**Revision.**

- Before: [Section 2, four pages surveying every prior model of lexical access before the paper's own model appears in Section 5.]
- After: [Introduction names the two models the paper contests, one sentence each: "We compare against the cascaded model of Dell (1986) and the discrete model of Levelt (1999), reviewed against the wider literature in Section 7." The survey becomes Section 7.]

**Do not apply when.** A venue mandates a fixed order (many journals require Background second), or the contribution is only intelligible as a delta from one prior method that needs full exposition — then give that method an early background subsection and still defer the general survey.
