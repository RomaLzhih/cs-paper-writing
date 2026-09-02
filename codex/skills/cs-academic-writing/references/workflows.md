# Task workflows

Read Shared preparation, the section matching the user's requested operation, the relevant Targeted section checks, and Final fidelity pass. Preserve the user's requested format and level of intervention.

## Shared preparation

Determine the passage type, intended audience, venue constraints if supplied, and requested scope. Infer these from the manuscript when safe; do not interrupt a focused edit for optional metadata.

Choose an intervention depth from `language-polishing.md`: copyedit, language polish, or deep prose edit. A request to “polish,” “improve the writing,” or “make this read naturally” defaults to language polish. Do not silently perform a deep reorganization when the user asked only for grammar correction.

Before rewriting, make a semantic ledger of details that must survive:

- defined terms, symbols, equations, and acronyms;
- assumptions, quantifiers, parameter ranges, and probability qualifiers;
- claim type and scope;
- citations and attribution;
- theorem, algorithm, figure, table, and section references;
- empirical numbers, units, baselines, datasets, and aggregation.

Use the ledger to compare the output with the source.

## Draft new prose

1. Identify the section's rhetorical contract and the facts/evidence available.
2. Arrange the necessary moves using the relevant corpus guide; do not invent missing moves.
3. Draft paragraphs with one main role each and explicit logical transitions.
4. Use exact technical terms and scoped claims from the author's material.
5. Run the complete language-polishing pass: sentence architecture, word precision, grammar, cohesion, concision, and rhythm.
6. Run the semantic and consistency checks in `SKILL.md`.

When information is missing, use a visible placeholder such as `[state the baseline and evaluation scope]` or list the missing author decision after the draft. Do not fill it with a plausible fact.

Unless the user requests commentary, return the draft first, followed by a short list of assumptions or unresolved placeholders.

## Paraphrase or revise supplied text

1. Record the semantic ledger.
2. Diagnose the passage at every requested language level: rhetorical order, paragraph cohesion, sentence architecture, reference and attachment, word choice, terminology, idiom, grammar, concision, and rhythm.
3. Rewrite at the smallest level that fully fixes the issues. Reorder clauses or sentences when needed; do not perform synonym substitution merely to sound different.
4. Read the revision once as continuous prose and repair choppy rhythm, repeated framing, abrupt transitions, and unnecessary sentence complexity.
5. Compare source and revision item by item against the ledger.
6. Flag any ambiguity that prevents a faithful rewrite instead of resolving it silently.

Preserve LaTeX commands, citation keys, labels, math delimiters, macros, and code identifiers unless asked to change them. Do not alter a formal statement's meaning for smoother prose.

Default output:

1. revised text;
2. a brief note only for material structural choices or unresolved ambiguities.

## Review a draft

For a full manuscript, first build a compact section-purpose outline and a map from each central claim or contribution to its mechanism, proof or evidence, and stated scope. Check for drift among the abstract, introduction, formal results, evaluation, and conclusion. Report systemic coherence issues before local prose findings. Skip this full-paper prepass for an isolated excerpt.

Use a mandatory fidelity screen for semantic inconsistencies, undefined terms, and altered or unsupported claims. Then make the writing review the primary assessment. Cover, at the requested scope:

1. wording or grammar that changes or obscures meaning, agency, comparison, reference, or logical scope;
2. sentence clarity, information order, and paragraph cohesion;
3. precise and idiomatic word choice, stable terminology, and calibrated claim verbs;
4. grammar, articles, number, tense, modifiers, parallelism, punctuation, and mechanics;
5. concision, transitions, academic tone, repetition, and rhythm;
6. section structure, argument flow, and contribution--evidence alignment when the supplied scope permits them.

Order reported findings by reader harm and recurrence, not by the list above. A systemic language pattern may deserve attention before an isolated structural preference.

For each substantive finding, give:

- **Location:** quoted phrase, paragraph purpose, section, theorem, or figure;
- **Issue:** the precise problem;
- **Why it matters:** effect on the stated contract, scope, reader inference, or evidence;
- **Repair:** a concrete structural change or example rewrite.

Do not report a generic preference as an error. Label findings using the Severity taxonomy below. Consolidate repeated instances under one pattern and include representative locations. State when a finding is excerpt-local or depends on unavailable context. If nothing substantive is wrong, say so and identify the residual verification limits.

Default output:

1. a one-sentence overall assessment;
2. prioritized findings, highest severity first;
3. optional concise strengths or a revised passage when it clarifies the repair;
4. remaining author checks, such as citation or theorem verification.

## Severity taxonomy

- **Must fix:** language permits a wrong technical reading or leaves the sentence incomplete; or the supplied text contains a semantic, consistency, attribution, support, or reproducibility presentation defect.
- **Should fix:** wording or organization substantially impairs clarity, idiom, sentence construction, cohesion, terminology, argument flow, concision, or rhythm.
- **Optional:** clear grammatical alternatives differ mainly in voice, rhythm, house style, or another preference with no material effect on readability.

Classify by reader consequence, not by the surface category. A misplaced modifier can be **Must fix**; a grammatical sentence rewrite can be **Should fix**; a comma or dialect choice can be **Optional**. Do not use a writing review to decide whether the underlying research method is valid.

## Give edit suggestions without rewriting

Honor “suggest only” requests. Recommend changes in the form:

> location → issue → consequence → proposed edit

Give exact replacement language for word-, phrase-, and sentence-level problems; explain the governing pattern when it is likely to recur. Do not provide a thesaurus-style synonym list without identifying the contextual distinction. For a structural problem, propose the smallest reordering that repairs the flow. Mark suggestions using the Severity taxonomy.

## Targeted section checks

For an abstract, verify problem, gap, response, mechanism/guarantee, and evidence without background sprawl.

For an introduction, verify a concrete gap, high-level answer, non-overlapping contributions, and a clear bridge to evidence.

For an algorithm or proof, review the exposition of the contract, invariant, pseudocode--prose agreement, stated correctness obligations, proof dependencies, and complete cost qualifiers. Do not validate the proof itself.

For an evaluation, verify that the prose states claim--evidence mapping, reproducibility details, comparison conditions and fairness caveats, exception-aware interpretation, any claimed mechanism test, and scope limitations. Do not judge methodology validity unless the user separately requests that task.

For related work, verify grouping by comparison axis, fair attribution, compatible semantics, and a precise novelty boundary.

For a conclusion, verify that it answers the motivation, introduces no new result, and preserves the paper's scope.

## Final fidelity pass

Read the revised text once only for meaning. Check every number, symbol, bound, condition, citation, referent, and novelty or causal verb against the source. Then use the final checklist in `language-polishing.md` and read the passage once as continuous prose for flow and rhythm. Meaning takes precedence over elegance, but the task is not complete until the requested language pass is also complete.
