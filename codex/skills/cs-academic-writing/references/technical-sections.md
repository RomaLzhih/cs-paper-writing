# Technical-section guidance

Use this reference for writing and reviewing preliminaries, models, definitions, algorithms, pseudocode, theorem and proof exposition, invariants, and complexity analysis. It does not establish that an algorithm or proof is correct.

## Establish the contract in dependency order

Introduce technical material in this order when applicable:

1. standard objects and notation;
2. computation, memory, or concurrency model;
3. black-box primitives and inherited results;
4. paper-specific states, definitions, assumptions, and invariants.

Introduce a symbol at its first conceptual layer, not merely one line before an equation. A notation table helps readers retrieve symbols but does not replace prose definitions. Define acronym, log base, index range, graph directionality, probability convention, and input parameters once and use them consistently.

## Models and assumptions

A model description should let the reader answer:

- What executes, and what may execute in parallel?
- Which operations, memory accesses, and synchronization primitives are allowed?
- What does the cost model charge?
- Which parameters and adversarial or probabilistic assumptions matter?
- How do work and span or other abstract costs translate to execution time?

Surface any assumption that changes a theorem's domain. If an assumption is made “for simplicity,” state whether the construction or analysis generalizes and what changes. Separate correctness assumptions from performance assumptions. When an algorithm is always correct but its cost is probabilistic, say so explicitly.

## Definitions

A definition can use the following layers when they help the reader:

> intuition → formal statement → example or plain-language paraphrase → immediate consequence

Use displayed mathematics for the formal contract and prose for why it matters. Contrast easily confused terms directly—for example, true versus tentative state, parallel versus concurrent operation, or abstract object versus implementation node. Do not vary a defined term for stylistic elegance.

## Algorithm and data-structure exposition

Many clear algorithm sections use these layers as applicable:

1. state the section's goal and promised result;
2. when it motivates the design, explain the relevant baseline or naive approach and its limitation;
3. give the new idea in one paragraph or a small number of named phases;
4. present pseudocode or a formal interface and explain its non-obvious parts.

Describe the algorithm well enough that a reader can predict the pseudocode's phases. Use a local roadmap when the construction has several dependent components. Figures should expose state, data movement, or phase relationships rather than decorate the section.

Pseudocode should specify inputs, outputs, maintained state, base cases, return behavior, and parallel semantics. Prose should use the exact routine, variable, and phase names. It should explain why a step exists, which invariant it preserves, how conflicts are handled, and which primitive supplies its cost. Do not translate every loop into English.

If the displayed algorithm is conceptual and the implementation differs, state the gap and its implications. Cross-check phase counts, parameter ranges, line references, and boundary cases after editing.

## Theorems and proof architecture

State a main result early enough to orient the reader. A complete theorem statement makes locally recoverable:

- the input and model;
- required assumptions and parameter ranges;
- the correctness or output guarantee;
- work, span/depth, space, I/O, or communication bounds as relevant;
- worst-case, amortized, or expected status;
- the probability qualifier and its parameter.

Before a long proof, identify the stated proof obligations and dependency order. A common exposition is:

1. structural or representation lemmas;
2. correctness, often split into soundness and completeness;
3. local phase costs;
4. global composition of work, span, and space.

Begin a proof or proof paragraph by naming its method or local goal—induction, contradiction, recurrence, charging, backward analysis, or case analysis. Label long cases. At the end, state how the lemmas combine to yield the theorem. If routine details move to an appendix or full version, retain the central invariant, proof skeleton, and non-obvious intuition in the main text.

Avoid “clearly” or “straightforward” in place of the missing argument. Use them only after the decisive fact is visible.

## Invariants and correctness

Tailor the invariant to the object:

- trees and indexes: ordering, balance, block size, layout, or version invariants;
- iterative algorithms: relation to a valid sequential execution;
- graph decompositions: both no false merge and no missed merge;
- concurrent objects: sequential specification, linearization points, helping, and progress;
- shortest paths or dynamic programming: which states are finalized or ready after a round.

A general correctness skeleton is:

1. state the representation or loop invariant;
2. establish initialization;
3. prove preservation for every operation, phase, or round;
4. establish progress and termination;
5. connect the final state to the required output.

Keep correctness separate from efficiency. A fast operation is not necessarily valid; a correct operation does not yet satisfy the promised bound.

## Complexity prose

Write the complete cost tuple in one recoverable statement:

> Under [conditions], [algorithm/operation] uses [work], [span], and [space/I/O/communication], [worst-case/amortized/expected], [probability qualifier].

Prove local costs before composition. Identify the dominant phase, recurrence, aggregation, charging argument, or critical path. When summing over subproblems, state why sizes or costs aggregate as claimed. Interpret important parameters after the formal statement: which term they affect and what tradeoff they induce.

Never silently switch among input-size symbols, logarithm bases, computational models, or probability conventions. Tables of bounds should define every symbol and mark amortized and probabilistic entries.

Associate each bound with its exact operation and interface: construction versus update or query, point versus batch operations, and preprocessing versus per-query cost. Identify output-sensitive parameters. For amortized claims, state the class or length of operation sequences over which the bound holds and, when relevant, the potential or accounting argument. For processor-time bounds, state the processor count, scheduler, and model assumptions that connect work/span to time.

## Citations and ownership

For every borrowed component, make clear whether it is used unchanged, adapted, reanalyzed, or only implemented. Do not describe an implementation optimization as a new algorithmic contribution unless the paper claims and supports that distinction. Compare results only under compatible interfaces, update semantics, models, and workload assumptions.

## Technical consistency audit

Before finalizing a revision, check:

- all symbols are defined before use and have one meaning;
- theorem restatements agree with the formal theorem;
- pseudocode, prose, figures, and proofs use the same names and phase order;
- correctness directions are not swapped in summaries;
- the exposition identifies how the listed lemmas combine, with no apparent omitted dependency; leave logical validity for author or formal verification;
- every bound has its conditions, bound type, and probability qualifier;
- cross-references point to the intended item;
- the exposition identifies how edge cases and base cases are treated, without treating this check as correctness validation;
- no paraphrase changes a quantifier, inequality, asymptotic term, or scope.
