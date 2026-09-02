# Empirical-section guidance

Use this reference for experimental design prose, baselines, workloads, ablations, result narration, theory--practice links, and empirical limitations.

## Build the evaluation around claims

Frame the paper around a concrete tension—such as work efficiency versus parallelism, update versus query performance, speed versus space, or theory versus practice—and map each practical contribution to evidence. Literal research questions are optional, but the evaluation's purpose must be explicit.

At the start of an evaluation, preview the questions or claims and the order in which the experiments address them. A common progression is:

1. end-to-end comparison;
2. scalability;
3. component or ablation study;
4. parameter, input, or boundary sensitivity;
5. resource use or application study;
6. concise synthesis.

Use only the stages relevant to the claims. An evaluation should test the proposed mechanism, not just rank systems.

## Experimental contract

Before interpreting results, make the setting reproducible and the comparison legible. Report relevant items from the following list:

- processor model, sockets, physical cores, hyperthreads, frequency, memory, and cache;
- accelerator or PIM hardware and topology when relevant;
- operating system, compiler, runtime, libraries, versions, flags, scheduler, affinity, and NUMA policy;
- warmup, number of trials, aggregation statistic, variability, timeout, OOM, and failure policy;
- metric definitions, units, normalization, and whether higher or lower is better;
- dataset source, size, preprocessing, sampling, synthetic distribution, and parameter selection;
- baseline implementation source/version, modifications, tuning range, and execution mode.

Do not add irrelevant hardware trivia. Do disclose a detail when it can change parallel performance or comparison fairness.

## Workloads and baselines

Explain why each workload is present. Group inputs by the property that exercises the design: dense/sparse, uniform/skewed, low/high dimensional, short/long range, common/adversarial, or small/large output. State transformations and preprocessing near the dataset description.

Give each baseline a role. Useful roles include:

- the strongest comparable state-of-the-art method;
- a strong sequential baseline;
- a simpler or stripped-down variant;
- an established library or system used in practice;
- a practical lower-bound proxy when justified.

Discuss fairness explicitly. State API or semantic differences, unavailable operations, language and implementation provenance, source changes, I/O exclusions, machine differences, and tuning effort. Explain an omitted strong competitor rather than silently excluding it. Distinguish self-speedup from speedup over another implementation.

## Narrate each important result

Strong result paragraphs often use this sequence, omitting moves that are not supported or relevant:

> purpose → quantitative observation → important exception when present → mechanism when supported → scoped implication

For example, as a planning structure:

> To test [claim], we compare [methods] under [condition]. Figure X shows [precise observation and aggregate/range]. When present, the exception is [case], where [countervailing cost] dominates. This occurs because / likely arises because [mechanism]. Thus, the result supports [scoped implication].

Use “because” only when analysis or an ablation isolates the cause. Otherwise write “likely,” “a possible explanation is,” or “this suggests.” If the cause is unknown, say so.

Do not invent a losing case, exception, or mechanism to complete the sequence. If none appears in the supplied evidence, report the supported observation and scope only.

Report absolute time, throughput, memory, or work when it helps interpretation, alongside relative comparisons. Combine maxima with a typical statistic or coverage count: an “up to” speedup alone is weak evidence. Define geometric means, normalization, timeouts, and failure markings in captions or nearby prose.

When they are present and material in the supplied results, describe losing cases and crossovers. They often reveal the fixed overhead, locality effect, contention, insufficient parallelism, or regime boundary that makes the design understandable.

Do not use “significant” to mean merely “large” when no statistical significance test was performed.

## Ablation and sensitivity

When the paper attributes gains to a component or design choice, isolate it when feasible:

- remove or replace one component at a time;
- compare plain and optimized variants;
- vary block/node size, threshold, batch size, or another key parameter;
- test scale, skew, dimensionality, query/output size, and thread count;
- measure overhead when the target condition for an optimization is absent;
- include a boundary or adversarial input when making a robustness claim;
- test interactions when components target different regimes.

Explain how default parameters were chosen and avoid tuning on the reported test set when possible. A null or negative ablation result can increase credibility when reported and interpreted honestly.

## Connect theory to practice

Measure practical proxies predicted by the analysis: useful work, rounds or burdened span, bytes transferred, cache misses, contention, memory footprint, frontier size, or load balance. State why the proxy reflects the theoretical term, then test whether the trend matches. Explain crossovers and deviations rather than treating asymptotics as runtime predictions.

If the evaluated implementation differs from the analyzed algorithm, identify the difference, why it was made, and which formal guarantees still apply. Never imply that experiments validate a theorem or that a theorem guarantees observed speedup.

## Limitations and threats

The corpus often reports limitations locally but rarely synthesizes external-validity threats. Improve on that habit. Cover material concerns such as:

- dependence on one machine or architecture;
- dataset representativeness;
- tuning or selection bias;
- reimplementation and language effects;
- limited trial counts or unreported variability;
- unsupported operations or semantic mismatches;
- timeout, memory, and scale limits;
- differences between theoretical and implemented algorithms.

Place a limitation beside the affected result and add a compact limitations paragraph when the overall scope would otherwise be unclear. State condition, consequence, and mitigation or remaining uncertainty. Do not bury a comparison-changing caveat in a footnote.

## Empirical consistency audit

Before finalizing, verify that:

- every practical contribution has corresponding evidence;
- setup, metric, workload, and baseline definitions precede interpretation;
- numbers in prose match figures, tables, units, and aggregation rules;
- denominators and evaluation scope accompany quantitative claims;
- “average” identifies the statistic and population;
- every important figure has a purpose, main observation, any important observed exception, and implication;
- causal explanations are calibrated to the available evidence;
- any unfavorable regimes and failures present and material in the supplied results are visible;
- the conclusion preserves the evaluation's hardware, data, and workload scope.
