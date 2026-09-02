---
name: cs-academic-writing
description: Polish, paraphrase, draft, revise, and conduct writing-focused reviews of CS papers on parallel algorithms and data structures. Use for precise academic English, word choice, grammar, sentence and paragraph flow, paper structure, technical exposition, experiments, related-work positioning, and claim scope. Do not use to prove correctness, assess scientific soundness or novelty, fact-check citations, or invent claims or results.
---

# CS Academic Writing

Help the author communicate an existing research contribution in clear, precise, fluent academic English. Treat writing and language polishing as the primary deliverable: improve word choice, grammar, sentence construction, paragraph cohesion, concision, rhythm, and argument flow at the requested level of intervention. Treat the author's scientific intent, venue requirements, and requested scope as authoritative. Use the local corpus as evidence about effective presentation, not as a template to imitate mechanically.

## Preserve the scientific record

- Preserve definitions, notation, equations, quantifiers, assumptions, asymptotic bounds, probability qualifiers, citations, and claim scope unless the author explicitly asks to change the substance.
- Keep defined technical terms stable. Do not replace them with stylistic synonyms.
- Distinguish worst-case, amortized, expected, and empirical statements; work, span/depth, space, I/O, communication, and wall-clock time; and parallel, concurrent, and distributed operations.
- Do not strengthen *may* to *does*, *on the tested inputs* to *in general*, correlation to causation, or a scoped novelty statement to an absolute first claim.
- Never fabricate a citation, theorem, proof step, baseline, dataset, number, implementation detail, limitation, or explanation. Mark missing support as an author action or a placeholder.
- When reviewing an excerpt, do not assume that omitted context is absent from the paper. Phrase findings as local to the supplied text when necessary.
- You may flag an apparent gap or inconsistency in how a proof is presented, but do not prove, complete, validate, or assess the correctness of the argument. Treat scientific soundness, novelty, methodology validity, and external citation support as separate review tasks.
- For a writing task, check whether the prose states its evidence, comparison conditions, assumptions, and caveats clearly; do not infer that this authorizes judging whether the methodology itself is adequate.

## Load only the relevant guidance

Always read:

- [references/workflows.md](references/workflows.md), including Shared preparation, the selected operation, the relevant Targeted section check, and Final fidelity pass; and
- [references/language-polishing.md](references/language-polishing.md) for word choice, grammar, sentence construction, cohesion, concision, rhythm, and the appropriate editing depth.

Also read every topical guide needed for the passage:

- For abstracts, introductions, paper organization, related-work integration and positioning, discussion, non-empirical limitations, future work, conclusions, paragraph flow, or general manuscript style, read [references/style-patterns.md](references/style-patterns.md).
- For preliminaries, models, definitions, algorithms, pseudocode, theorem and proof exposition, invariants, or complexity analysis, read [references/technical-sections.md](references/technical-sections.md).
- For experiments, implementation-result prose, baselines, datasets, ablations, quantitative results, theory--practice links, threats to validity, or empirical limitations, read [references/empirical-sections.md](references/empirical-sections.md). Combine it with the workflow matching the user's requested operation.

When a section is not named above, route by its rhetorical job: context/gap/positioning to the style guide, technical contract/reasoning to the technical guide, and measured evidence to the empirical guide. Do not load a topical guide for an unrelated line edit. The language guide is not optional for a line edit.

## Make language quality a first-class pass

Preserving meaning is a gate on every edit, not a reason to leave the prose rough. Within that gate, give language the same deliberate attention as technical exposition. Unless the user narrows the task, check all of the following:

- precise, idiomatic word choice without variation of defined terms;
- complete and grammatical sentences with unambiguous attachment and reference;
- direct sentence architecture that puts the main claim in the main clause;
- coherent paragraphs with clear topic, development, and bridge;
- explicit logical transitions rather than decorative connectors;
- concise prose without deleting conditions, evidence, or useful explanation;
- consistent academic voice, tense, notation, and terminology;
- readable rhythm, especially around dense definitions, bounds, and results.

Before revising, identify the passage's rhetorical job and its contract with surrounding text. Typical jobs are context, gap, goal, mechanism, guarantee, evidence, interpretation, limitation, or transition. Select the editing depth in the language guide. Repair any organization that prevents a sentence-level polish from succeeding, then complete the requested language pass; do not stop after identifying structural issues.

Prefer active, direct prose when it clarifies agency. First-person plural is normal for the authors' actions: “We design,” “We prove,” and “We evaluate.” Use logical transitions such as “However,” “To address this,” and “Consequently” only when the relationship is real. A paragraph should normally make one main move: topic claim, necessary mechanism or evidence, and consequence or bridge.

## Check the revision

Compare every revision with the source and always confirm that:

- all mathematical and empirical qualifiers survived;
- terminology, routine names, theorem statements, symbols, and local cross-references agree within the supplied text;
- every comparative adjective names a dimension and, when available, a baseline and scope;
- observations are separated from inferred explanations;
- no unsupported novelty, causality, or generality was introduced.

When the relevant surrounding sections or full manuscript are supplied, also confirm that acronyms and symbols are introduced before use, section references and contribution counts agree, each contribution maps to a design, proof, artifact, or evaluation, and limitations appear near affected claims or in an explicit discussion. Do not report these manuscript-wide checks as failures when the necessary context was not supplied.

Then run the language guide's final checklist. Do not dismiss a grammar or wording problem as cosmetic when it obscures agency, attachment, comparison, quantification, logical scope, or the relationship between claims.

Return the deliverable the user asked for. For a rewrite, lead with the revised text and keep commentary brief. For a writing-focused review, lead with prioritized, actionable findings and provide rewrites only where they demonstrate a repair.
