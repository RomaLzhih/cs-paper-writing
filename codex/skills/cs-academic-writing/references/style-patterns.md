# Corpus-derived style patterns

## Scope and provenance

These patterns synthesize the repository's `AGENTS.md` and the writing in `corpus/`. The registry contains 119 PDFs across theory, algorithms, data structures, and systems, including duplicate versions, preprints, short announcements, and a few peripheral papers. The synthesis combines a broad structural scan with close reading of 27 distinct full papers spanning 2013--2026: `pimzd`, `kdtree`, `dp`, `parlayann`, `ED`, `PacTree`, `stepping`, `vcas`, `SAGE`, `pam`, `FRT`, `RadiusStepping`, `predictive`, `psi`, `pbtree`, `xu-cpma-ppopp-24`, `fastbcc`, `PIM`, `incremental`, `HPG13`, `semisort`, `DBSCAN`, `pam-snapshot`, `ParChain`, `xu-bptree-vldb-23`, `integer-sort`, and `kcore`. They were selected to span years, venues, and theory, data-structure, systems, and empirical styles; known alternate versions were excluded using `registry.tsv`.

The corpus is not balanced across authors or venues. Treat a pattern as a strong default only when it serves the paper's argument and target venue, and distinguish observed habits from recommendations here that deliberately improve on weak corpus habits.

Published papers also contain repetition, vague adjectives, incorrect cross-references, and awkward sentences. Follow the recurring logic and clarity, not every surface habit.

## The governing argument

The most stable pattern is an argument rather than a section template:

> important setting or task → concrete tension or gap → proposed response → mechanism and guarantees → evidence → scoped implication

The gap is testable. It names a missing capability, incompatible requirements, unexplained theory--practice mismatch, unsupported regime, or cost that prior approaches incur. Avoid motivations that say only that a problem is important or prior work is inefficient.

Theory and practice are paired without being conflated. State formal costs in their model and empirical outcomes in their measured setting. Explain how they inform one another only when the paper establishes the connection.

## Whole-paper architecture

A common full-paper backbone is:

1. abstract;
2. introduction;
3. background, model, or preliminaries;
4. overview, abstraction, or main design;
5. algorithm/data structure and analysis;
6. implementation, applications, or extensions when relevant;
7. evaluation when practical claims are made;
8. related work, early or late according to reader need;
9. conclusion and open directions.

Order sections by dependency: establish the contract before the construction, the construction before its proof, and the implementation before its measurement. Do not force separate sections when the content is clearer locally. Related work may be early, late, or integrated; limitations are often stated beside affected claims.

Use section openers to state the local goal, connect it to the previous result, and preview components only when the section is genuinely multi-stage. A transition should explain why the next material is needed, not merely announce that it exists.

## Abstract: problem--gap--answer--evidence

Strong abstracts usually make five moves in a compact order:

1. identify the task or setting and why it matters;
2. state the precise unresolved gap or tradeoff;
3. name the proposed algorithm, data structure, model, framework, or system;
4. give the central idea and strongest formal guarantee;
5. report the most informative empirical result or broader implication, if applicable.

Lead with content rather than “In recent years.” Define only indispensable terminology. Report bounds with their conditions and probability type. Report empirical numbers with the comparison and evaluation scope. If there is no evaluation, do not manufacture an evidence sentence.

A useful planning skeleton is:

> [Task and pressure.] Existing approaches [specific gap]. We present [artifact/approach]. The key idea is [mechanism]. We prove [scoped guarantee]. On [evaluation scope], [method] achieves [metric] relative to [baseline].

Use this as a checklist, not fixed prose.

## Introduction: narrow toward a checkable question

Introductions commonly proceed through these rhetorical moves:

1. establish the object and its applications or theoretical role;
2. define the problem and relevant evaluation dimensions;
3. present the strongest status quo fairly;
4. expose a concrete mismatch, tradeoff, or missing regime;
5. state the goal, challenge, or one or two research questions;
6. introduce the response at a high level;
7. explain why its key mechanism addresses the stated gap;
8. preview formal and empirical evidence;
9. summarize contributions in independently verifiable units.

Literal numbered research questions are optional. The reader must nevertheless be able to say what was unknown and what answer the paper supplies.

Introduce the solution at two levels: first, one sentence saying what it is; second, a paragraph explaining its essential mechanism and why it resolves the stated gap. Discuss a naive alternative only when it genuinely motivates the design. Use a motivating figure or result table early only if it sharpens the problem or previews the evidence.

Contribution items should use parallel, active grammar and should not overlap:

- **Design:** “We design/develop a …”
- **Analysis:** “We prove/show that … under …”
- **Artifact:** “We implement/release …”
- **Evidence:** “We evaluate … against … on …”

Keep the primary contribution claims independently checkable. Tightly coupled design and guarantee statements may share an item, but avoid overlapping items or conflating a claim with evidence that does not establish it. Point to a section or theorem only after stating the takeaway. Avoid repeating the same contribution story in several lists.

## Paragraphs, sentences, and transitions

This section records the corpus-level pattern. Use `language-polishing.md` for the operational word-choice, grammar, sentence, cohesion, concision, and rhythm checks.

Give each paragraph one main rhetorical job. A reliable shape is:

> topic claim or purpose → mechanism/evidence → implication or bridge

Repeat exact technical nouns when a pronoun would be ambiguous. Put a central assumption in the main clause, not in a parenthesis. Use parentheses for short qualifications, not a second argument. Split a sentence that simultaneously carries a condition, algorithm, bound, comparison, and interpretation.

Prefer verbs that expose the role of a statement: *defines, maintains, guarantees, bounds, requires, measures,* or *suggests*. Pair vague adjectives such as *fast, efficient, scalable, simple,* or *large* with the relevant mechanism or metric.

Useful transition families include:

- backward link: “Recall that …” or “As established in Section …”;
- contrast: “However,” “In contrast,” or “Instead”;
- response: “To address this limitation, …”;
- refinement: “More formally,” or “Specifically,”;
- consequence: “Therefore,” or “Consequently,”;
- proof/algorithm sequence: “We first … Next … Combining …”;
- qualification: “This guarantee requires …” or “The exception is …”.

Do not use these phrases as decoration. Limit “Note that,” “At a high level,” “clearly,” and “straightforward” when they do not add a logical relation or explanation.

## Related work and citations

Organize related work by method family or comparison axis, such as work/span, memory layout, update semantics, interface, model, or supported workload. For each group:

1. state what the prior approach contributes or does well;
2. identify the relevant limitation or differing goal;
3. position the present work on the same dimension.

Distinguish an inherited primitive, an adaptation, and a new component. Comparative sentences must use compatible semantics and name the dimension of comparison. Avoid chronology-only surveys and paragraphs that end in a citation dump without synthesis.

Cite broad application claims, specific borrowed results, standard definitions when attribution matters, and factual comparisons. Never invent a citation or move one so far that its referent becomes unclear. Preserve uncertainty in novelty claims with language such as “to our knowledge” when that is what the evidence supports.

## Limitations and alternative interpretations

The corpus rarely uses a dedicated limitations section. Its stronger papers disclose scope locally: an assumption after a theorem, a losing regime beside a result, an implementation--analysis difference in the evaluation, or an open question in the conclusion. Preserve that local candor. For a new draft, add a compact synthesis when limitations would otherwise be scattered or easy to miss.

Write a limitation as:

> condition or boundary → consequence for the claim → mitigation, rationale, or remaining question

Do not invent a benign explanation for an anomaly. Separate measured observations from plausible mechanisms with calibrated language such as “likely,” “we believe,” or “this suggests” unless an ablation isolates the cause.

## Conclusion

A conclusion is short and claim-centered. It should answer the motivating question, restate the artifact and principal guarantees, summarize only supported evidence, preserve scope, and optionally identify a specific open direction. Do not introduce a new technical claim or experiment. A pure abstract replay is usually weaker than a synthesis of what the combined theoretical and empirical evidence establishes.

## Patterns to avoid

- a generic opening that delays the actual problem;
- “no prior work” or “first” without a carefully scoped novelty boundary;
- several overlapping contribution summaries;
- a section roadmap that lists headings but not dependencies;
- unexplained “better,” “efficient,” “non-trivial,” or “significant”;
- cross-references in place of a local takeaway;
- related work that acknowledges no strengths of prior approaches;
- result narration that reports only wins or only “up to” values;
- paraphrasing that removes conditions, probability qualifiers, citations, or terminology distinctions.
