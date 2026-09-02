# Language polishing for CS papers

Use this reference for every drafting, paraphrasing, revision, line-editing, or writing-review task. It turns the corpus's strongest recurring habits—stable terminology, explicit logical relations, direct claims, and scoped comparisons—into an editing procedure. The corpus also contains awkward or ungrammatical sentences; correct those habits rather than treating publication as evidence that every surface form is desirable.

## Editing contract

Language polish should make the intended technical meaning easier to recover on the first reading. It is not synonym replacement and must not make the writing sound more ornate.

Preserve the semantic ledger from `workflows.md`. In particular, do not change:

- a defined term, symbol, routine name, mathematical relation, or code identifier;
- a quantifier, condition, probability qualifier, cost type, baseline, or evaluation scope;
- the strength of a claim, the source of evidence, or the distinction between observation and explanation;
- a citation's referent or an author's ownership of an idea.

When an original sentence has more than one plausible technical reading, do not silently choose the most convenient one. Provide the safest revision and flag the ambiguity, or ask for the intended meaning when no faithful revision is possible.

Do not silently recalibrate a substantive claim under the label of style. When the source itself exposes an evidence--verb mismatch—for example, experiments that “prove” a general property—use the strongest wording defensible from the supplied text and briefly flag the calibration. When the supplied context is insufficient to judge the intended claim, preserve it and flag the issue rather than either strengthening or weakening it silently.

## Choose the editing depth

Match the intervention to the request:

- **Copyedit:** Correct grammar, spelling, punctuation, articles, agreement, obvious idiom, and local ambiguity. Preserve sentence and paragraph order unless a sentence is not repairable in place.
- **Language polish:** This is the default for “polish,” “improve the writing,” “paraphrase,” or “make this natural.” Improve word choice, sentence architecture, cohesion, concision, and rhythm in addition to copyediting. Reorder clauses or nearby sentences when needed.
- **Deep prose edit:** Rebuild paragraphs and local section flow as well as polishing the language. Use when the user requests substantial revision or when local wording cannot repair the argument's presentation.

If the requested depth is clear, do not ask the user to choose a label. Preserve a consistent American or British variety when the manuscript already establishes one; do not impose a new variety for isolated edits.

## Run a complete language pass

Use these passes in order, combining them for a short excerpt:

1. **Purpose and cohesion:** Identify the rhetorical job of each paragraph and the logical relation between adjacent claims.
2. **Sentence architecture:** Put the principal claim or action in a recoverable main clause; repair attachment, reference, and information order.
3. **Word precision:** Stabilize technical terms; choose concrete nouns, exact verbs, calibrated modifiers, and idiomatic combinations.
4. **Grammar and mechanics:** Check agreement, articles, number, tense, modifiers, parallelism, comparisons, punctuation, and mathematical prose.
5. **Concision and rhythm:** Remove empty framing and unintended repetition; vary sentence shape enough to keep dense reasoning readable.
6. **Fidelity:** Compare the revision against the semantic ledger rather than relying on memory.

Do not stop after a grammar checker would stop. A grammatical sentence can still be vague, structurally overloaded, non-idiomatic, or disconnected from its paragraph.

## Choose words by function

### Keep technical vocabulary stable

Repeat a defined technical term even when a synonym would sound less repetitive. Variation is useful for ordinary prose, not for distinctions the paper relies on. Do not alternate among *method*, *algorithm*, *system*, *framework*, and *implementation* unless the referents genuinely differ.

Expand an acronym at first use in the relevant reading scope, then use the acronym consistently. Preserve capitalization and hyphenation of named models, data structures, datasets, and operations.

### Prefer exact nouns and visible agents

Replace vague stand-ins such as *it*, *this*, *that*, *the approach*, or *the result* when two or more antecedents are plausible. A small amount of noun repetition is better than referential ambiguity.

Name the actor when agency matters:

- the algorithm **partitions** the input;
- the data structure **maintains** the invariant;
- the theorem **guarantees** the bound;
- the experiment **measures** throughput;
- the result **suggests** an explanation.

Do not make an inanimate artifact “believe,” “want,” or “try.” Avoid passive voice when it hides who chose a parameter, implemented a baseline, or inferred a cause. Keep passive voice when the actor is irrelevant and the object should remain the topic.

### Use verbs that match the evidence

Choose the verb by claim type:

- **Author action:** *introduce, design, develop, implement, evaluate, compare*.
- **Formal result:** *prove, establish, guarantee, bound, imply*—only when the formal argument supplies that relation.
- **Definition or mechanism:** *define, maintain, invoke, partition, aggregate, encode*.
- **Measurement:** *measure, observe, achieve, reduce, outperform*—with metric, baseline, and scope.
- **Interpretation:** *indicate, suggest, is consistent with, may arise from*.

Experiments do not *prove* a general claim, and a theorem does not *demonstrate* empirical speed. Use *show* only when its evidence source is clear from context.

### Calibrate adjectives, adverbs, and claims

Replace or complete vague evaluations:

- *fast* → lower latency, higher throughput, or lower work under a named setting;
- *efficient* → specify work, span, space, communication, I/O, or measured resource use;
- *scalable* → state what increases and over what range;
- *large* → give a size, regime, or comparison when available;
- *simple* → name the reduced mechanism, interface, proof obligation, or implementation burden.

Scrutinize *very, significantly, substantially, dramatically, clearly, obviously,* and *straightforward*. Retain an intensifier only when a metric or visible argument supports it. Use *statistically significant* only for an appropriate statistical test.

Keep hedges that encode real uncertainty or scope. Do not delete *may, can, typically, in our experiments, with high probability,* or *to our knowledge* merely to sound decisive. Conversely, do not add *perhaps* or *seems* to a proved statement.

### Prefer idiomatic and compact combinations

Use established combinations consistently: *different from*, *independent of*, *proportional to*, *compatible with*, *based on*, *results in*, *consists of*, *allows X to do Y*, and *enables X*. Check a preposition as part of its full phrase rather than in isolation.

Prefer the direct form when meaning is unchanged:

| Wordy or indirect form | Usually prefer |
| --- | --- |
| *in order to* | *to* |
| *due to the fact that* | *because* |
| *has the ability to* | *can* |
| *conduct an evaluation of* | *evaluate* |
| *make use of* | *use* |
| *a large number of* | *many* or an exact count |
| *it is worth noting that X* | *X* |
| *the reason is because* | *the reason is that* |

Apply these as diagnoses, not blind replacements. For example, preserve *in order to* if it prevents a temporary ambiguity about purpose, and do not replace a scoped capability claim with an unconditional *can*.

## Build clear sentences

### Put the main action in the main clause

Keep the grammatical subject and its main verb close enough to recover easily. Avoid burying the contribution in a chain of introductory phrases, parentheticals, or nominalizations. Put central conditions where their scope is unmistakable, often at the start of the sentence or directly beside the claim they restrict.

Prefer a verb over a noun-plus-light-verb construction when no technical distinction is lost: *analyze* rather than *perform an analysis of*, and *reduces* rather than *provides a reduction in*. Retain a nominalization when it names a field concept or lets the sentence maintain a clear topic.

### Control information density

A sentence is overloaded when it asks the reader to track several of the following at once: setup, condition, algorithmic step, formal bound, comparison, exception, and interpretation. Split at a logical boundary. Keep a condition with its guarantee and a number with its metric, baseline, and scope.

Use a colon to introduce an explanation or list that completes a clause. Use a semicolon only when the two sides could stand as sentences and their relation is close. Do not connect independent clauses with a comma alone.

Integrate displayed mathematics into the surrounding grammar. The prose before a display should establish its role; punctuation after the display should reflect the sentence, not the visual layout. Follow a dense formula with a short interpretation when the consequence is not immediate.

### Make reference and attachment explicit

Check every *this, that, it, they, which,* and *respectively*. Replace *this* with *this bound*, *this reconstruction*, or another exact noun when the referent is not singular and immediate. Ensure a modifier sits beside what it modifies.

Place *only, also, even,* and *respectively* where their scope is intended. Rewrite dangling openers such as “Using the new representation, the running time decreases” when the grammatical subject cannot use the representation; name the actor instead.

Use *which* and *that* according to the manuscript's dialect and the intended restriction, but always punctuate nonrestrictive information as a parenthetical unit. Do not let a relative clause drift away from its antecedent.

### Order information for continuity

Within a sentence, begin with information already active in the paragraph and end with the new or consequential point when possible. Across adjacent sentences, carry forward a stable topic before introducing the next one. This given-to-new pattern is a default, not a rule that overrides emphasis or logical scope.

Use parallel grammatical forms for parallel ideas. Contribution bullets, theorem conditions, experimental questions, and comparison lists should align in voice and structure.

## Check grammar systematically

### Agreement and number

Find the head of the subject rather than matching the verb to the nearest noun: “A set of operations **is** supported,” but “The operations **are** supported.” Check agreement after long *of*-phrases, parentheticals, and mathematical subjects. With *there is/are*, match the following grammatical subject.

Keep singular and plural referents stable. Do not shift from *an algorithm* to *they* or from *data structures* to *it*. Treat collective and mass nouns consistently with the manuscript's dialect.

### Articles and countability

Use *a/an* for a new singular countable item, *the* for a specific or uniquely identified item, and no article for a generic plural or mass concept. Recheck articles before *algorithm, method, bound, model, experiment, baseline, implementation,* and *result*.

Do not pluralize mass nouns such as *evidence, information, software,* and *research* in their ordinary academic senses. *Work* is normally a mass noun for prior scholarship or computational cost, but it can be countable when it means distinct published works; choose the form that matches the intended sense.

### Tense and aspect

Use tense to mark the status of information, then follow the paper's established convention:

- present tense commonly describes the paper, algorithms, definitions, figures, and enduring claims: “Section 3 defines …”; “Figure 4 shows …”;
- past tense commonly reports completed experimental procedures: “We ran five trials …”;
- present perfect connects prior work to the current state of knowledge: “Several studies have considered …”.

Do not switch tense merely because a sentence was paraphrased. Keep a result paragraph internally coherent, and distinguish what the experiment did from what the displayed evidence currently shows.

### Parallelism, comparisons, and coordination

Coordinate like forms: “reduces work, improves locality, and preserves determinism,” not a mixture of nouns, clauses, and infinitives. Make numbered contributions grammatically parallel.

A comparison must compare compatible entities and expose its dimension. Prefer “Our implementation has lower update latency than Baseline A” to “Our implementation is lower than Baseline A.” Check *than that of*, *than those of*, and omitted comparison terms for unambiguous reference. Keep *between* for two or explicitly paired items and *among* for a group when that distinction improves clarity.

### Modifiers, prepositions, and punctuation

Place introductory and trailing modifiers so they cannot attach to the wrong algorithm, result, or condition. Avoid long noun stacks; unpack the relation with a preposition or relative clause when readers must reverse-engineer which noun modifies which.

Hyphenate a multiword modifier before a noun when needed for grouping, such as *work-efficient algorithm*, *high-dimensional data*, or *state-of-the-art baseline*. Do not normally hyphenate an adverb ending in *-ly* with the adjective it modifies. Preserve established spelling of technical terms.

Use commas to expose structure, not breathing pauses. Set off genuinely parenthetical material, but do not put a comma between a subject and its verb. Make list punctuation consistent with the paper or venue style. Check that parentheses contain a qualification rather than a second argument the reader needs in the main line.

## Build cohesive paragraphs and transitions

Give each paragraph one dominant rhetorical job. Its opening should establish a usable topic or relation, not merely announce “In this section.” Develop the topic with mechanism, evidence, qualification, or consequence. End with the implication or the reason the next paragraph is needed when that bridge is not already obvious.

Use lexical continuity deliberately: repeat the key noun or a clearly defined short form across the topic chain. Avoid unnecessary renaming that makes readers wonder whether a new concept has appeared.

A connector must name a real relation:

- *however* marks contrast or violated expectation;
- *therefore/consequently* marks a supported consequence;
- *instead* marks replacement;
- *specifically* narrows or instantiates;
- *in addition* adds a parallel point;
- *for example* supplies an instance, not new evidence of a different kind.

Do not insert a connector merely because two sentences feel abrupt; repair the missing logical link. Likewise, do not begin every sentence with a transition. Sentence order and repeated topic terms should carry much of the cohesion.

## Improve concision and rhythm

Delete throat-clearing that delays the claim: *It should be noted that*, *It is important to mention that*, and generic statements about growing data or modern systems when they do not establish the paper's actual pressure.

Remove repeated meaning, not deliberate technical reinforcement. Keep a local restatement when it interprets a formula, reconnects a long proof to its obligation, or restates a result in the comparison terms readers need.

Avoid a paragraph made entirely of long, similarly shaped sentences. After a dense sentence containing a definition, bound, or multi-part result, use a shorter sentence to state its implication. Combine choppy sentences when they share one subject and logical action. Do not vary length or vocabulary merely for decoration.

Read the polished passage continuously, preferably aloud when practical. Repair unintended echoes, repeated sentence openings, long stretches without a finite verb, and abrupt alternation between formulas and fragments. Preserve the author's professional voice; fluency does not require inflated vocabulary or promotional tone.

## Report language edits usefully

For a rewrite, lead with clean revised prose. Do not annotate every correction unless the user requests tracked explanations. Briefly flag only a material ambiguity, a necessary structural change, or wording whose choice depends on scientific intent.

For a review or suggestions-only request, consolidate recurring language problems into patterns and include representative locations plus exact repairs. Apply the unified severity taxonomy in `workflows.md` by effect, not by error label: a grammar issue that permits a wrong technical reading can be **Must fix**, whereas a defensible dialect choice, house style, or personal preference is **Optional** at most.

## Final language checklist

Before returning polished prose, confirm that:

- each sentence has one recoverable grammatical spine;
- subjects, verbs, pronouns, articles, and number agree;
- modifiers, transitions, and comparison phrases have unambiguous scope;
- technical terms are stable and ordinary words are precise and idiomatic;
- verbs match the evidence source and claims retain every qualifier;
- paragraphs have a clear topic chain and adjacent sentences have a real logical relation;
- no empty framing, redundant wording, or avoidable noun stack remains;
- sentence length and structure support rather than obstruct the reasoning;
- spelling, capitalization, hyphenation, punctuation, and dialect are consistent;
- LaTeX, citations, cross-references, symbols, numbers, and technical meaning are unchanged unless the user authorized a substantive edit.
