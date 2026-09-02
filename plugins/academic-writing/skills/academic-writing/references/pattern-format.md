# Pattern entry format

A pattern earns a place in the library only if it is **portable** (would transfer to a paper
on an unrelated topic), **observed** (seen in named papers, not assumed), and **actionable**
(tells a reviser what to change, not merely what good writing feels like).

Each entry:

    ### <imperative name — the move, not the virtue>

    **Dimension:** <A-H from rubric.md>
    **Observed in:** <n>/<N> papers — <short keys>
    **Move:** One sentence. What the author actually does to the prose.
    **Why it works:** One or two sentences. The effect on the reader, not praise.

    **Exemplars:**
    - "<verbatim quote, <=40 words>" — <paper key>, <section>
    - "<verbatim quote>" — <paper key>, <section>

    **Violation signature:** What the draft looks like when this pattern is absent.
    This is the detector the review mode greps for.

    **Revision:** Before -> after, on a neutral invented example, not on corpus text.

    **Do not apply when:** The condition under which the pattern is wrong.
    Every entry needs one. A pattern with no boundary is a platitude.

## Rules that keep the library honest

1. **Count, don't assert.** "Observed in 9/12" is a fact. "Papers usually..." is not.
   A pattern seen in fewer than a third of the corpus is recorded as a *variant*, not a rule.

2. **Name the move in the imperative.** "Open the paragraph with its claim" beats
   "Topic sentence usage." The name has to survive being read as an instruction.

3. **Quote verbatim and short.** Exemplars are evidence. Paraphrased exemplars are opinion.
   Keep quotes under 40 words and always attribute to paper and section.

4. **Every pattern carries its own falsifier.** The `Violation signature` is what makes
   review mode possible: it converts a description into something detectable in a draft.

5. **Record contested patterns as contested.** When papers split on a choice (integral vs
   non-integral citation, first person vs passive), the entry documents the split and the
   conditions each side tracks. Do not resolve a genuine disagreement by majority vote.

6. **Separate discipline-specific from general.** A convention driven by venue or field
   is tagged as such, so paraphrase mode does not impose one field's habit on another.

## What licenses rule 1

Counting only works because this corpus is **curated exemplars** — papers the user selected
as well-written. Frequency across it can therefore be read as endorsement. Were the corpus a
representative sample of a field, a common move might be a common flaw, and every pattern
would need judging on its merits instead of counting. If the corpus composition ever changes,
rule 1 is the first thing that must change with it.
