# G. Evidence presentation

9 patterns, ordered by how much each would improve a weak draft.

---

## Cash the magnitude word, and complete the number: comparator, spread, instance set

**Move.** Two halves of one discipline. A magnitude word (significantly, much, greatly, negligible) applied to the paper's own measurements is discharged by a ratio, range, or percentage no later than the following sentence. And each performance number is written as a four-part unit — magnitude, direction word, the named thing compared against, and the instance set the aggregate covers — with a range across instances reported alongside or instead of the mean.

**Why it works.** The word supplies direction and emphasis, the number supplies size: separated, the reader either takes the adjective on faith or goes hunting, and the adjective silently absorbs whatever magnitude the reader already expected. A lone mean invites the reader to assume it holds on every instance.

**Evidence.** 11 papers, union of the E and G samples. The one-sentence version of the first half was falsified in verification — the corpus routinely puts the qualitative headline in one sentence and the ratio in the very next — so the unit is the adjacent sentence, and the rule applies only to the paper's own measured results.

**Exemplars.**

- "achieve speedups of 190–559x (325x on average) over CGAL for 2-dimensional convex hull" — *ParGeo*, 6.1 Convex Hull, results
- "which is from 4% slower (on WT) to 1.5× faster (on SB). On average across seven graphs, Lazy-Stitch is 1.2× faster." — *am-tree*, 8.2 Update Throughput
- "On average, Ours1 is 5.7× faster than InfuserMG and 18× faster than Ripples." — *im*, 5 Running Time

**Violation signature.** Two greps, both restricted to results sections. (1) Highlight every significantly / much / greatly / substantially / negligible; read one sentence further; if no ratio, range or percentage has arrived, the claim is unlicensed. (2) A percentage or factor with no comparator named in the same sentence ("we achieve a 30% improvement"), or a mean with no range, percentile or max and no statement of how many instances it averages over. Neither detector fires in related work, motivation, or mechanism prose, where the corpus uses bare magnitude words freely.

**Revision.**

- Before: The revised protocol substantially reduced processing time, our method improves accuracy by 12%, and it is substantially faster to train.
- After: The revised protocol cut processing time by 3.4× (41 minutes to 12). Our method is 8-19% more accurate (12% on average across the 14 test corpora) than the CRF baseline, and 1.4-3.1× faster to train.

**Do not apply when.** The comparison is over something that was not and could not be measured — simplicity of an argument, generality of a definition. Papers here write "significantly simpler" of a proof with no number and are right to: inventing one would be worse than the vague word. Also, a single measured constant (a dataset size, a participant count) needs units and precision, not a comparator, and a hard-capped abstract may let one aggregate with a named baseline stand in for the full spread.

---

## Report the unfavourable end of the comparison in the same sentence as the favourable one

**Move.** When a comparison spans wins and losses, both ends appear in the same sentence — the losing endpoint of a range, or the baseline that still beats you — rather than being deferred to a later paragraph or dropped.

**Why it works.** A reader who finds the loss themselves in the table discounts everything else in the paper; a reader handed it in the same breath as the win reads the whole comparison as trustworthy.

**Evidence.** 7 of the 12 papers read for dimension G. Two-endpoint ranges outnumber "up to X" phrasing in 7 of those 12 (kdtree 13 vs 2, ppcsr 7 vs 0, fastbcc 6 vs 3), and the terrace instance below is in the abstract, where a concession costs most.

**Exemplars.**

- "is between 1.7×–2.6× faster than Aspen and between 0.5×–1.3× as fast as Ligra" — *xu-terrace-sigmod-21*, Abstract
- "SPaC-H-tree is between 3.7× slower to 5.66× faster, with a geometric mean of 2.5× faster." — *psi*, 5.1 Operations on Synthetic Datasets
- "On average, our sequential time is 2.8× slower than SEQ, but is 10% faster than GBBS." — *fastbcc*, 6.1 Overall Performance

**Violation signature.** An abstract or summary in which every comparison points one way; ranges written only as "up to X×" with the lower endpoint suppressed; a baseline that appears in the tables and beats the method on some column but never appears in the prose summary. Detector: grep "up to" and diff the tables' losing cells against the prose.

**Revision.**

- Before: Our parser achieves up to 2.4× the throughput of prior systems.
- After: Our parser runs at 0.9-2.4× the throughput of Baseline A (1.6× on average) and remains 1.1-1.3× slower than the non-incremental Baseline B.

**Do not apply when.** There genuinely is no losing end inside the reported experiments — state the full range plainly rather than manufacturing a concession. Inapplicable to a proved bound, where "up to" names a real worst case, not a cherry-picked endpoint.

---

## Load the caption with the normalizer, the polarity, the aggregation, and where the full data lives

**Move.** Captions state what is plotted and in what unit, what the values are normalized to and which direction is good, how values were aggregated, where the underlying per-instance numbers are, and — when the exhibit has a quirk or a colour code — what it means.

**Why it works.** A reader who skims by figure alone still reads the result correctly, and cannot mistake a ratio's direction or read plotting noise as a finding.

**Evidence.** 7 of the 12 papers read for dimension G, with six of six exemplars verbatim from six papers — the best-evidenced entry in the library. Polarity statements recur across cbfs, cpma, fastbcc and kdtree, so that clause is not one author's tic.

**Exemplars.**

- "The numbers followed by ‘×’ are speedups, higher is better. Others are running time, lower is better." — *cbfs*, Table 2 caption
- "Each point (𝑥, 𝑦) for a given graph container2 means that the container was at most 𝑥 times slower than CSR on 𝑦% of experiments." — *p2307-wheatman*, Figure 2 caption
- "Here we only run on one source vertex, since it has unclear meaning to compute the average of multiple runs on each step." — *stepping*, Figure 7 caption

**Violation signature.** A caption that is a bare noun phrase ("Figure 4: Error rates."); normalized or ratio-valued axes with no statement of the normalizer or which direction is better; a summary figure that never says how it aggregates or where the per-instance data is; visible oddities — missing bars, colour coding, bumpy curves — left unexplained.

**Revision.**

- Before: Figure 4: Error rates.
- After: Figure 4: Word error rate (%) on the held-out set; lower is better. Bars are means over the 12 speakers, per-speaker rates in Table 7. No bar for S9: that recording was unrecoverable.

**Do not apply when.** The venue enforces one-line captions or collects reading conventions in a shared notes block — then the instructions must live somewhere fixed and be pointed to, not duplicated per exhibit. A purely illustrative schematic needs a statement of what it depicts, not units and polarity.

---

## Count the exceptions and name the condition they share

**Move.** Cases that contradict the headline claim are counted rather than hedged ("except for three cases", "65 cases … 27 cases"), each given its magnitude, and then grouped by the property they share ("all in high-dimensional queries").

**Why it works.** Counted exceptions tell the reader the exact shape of the claim's boundary; a vague "in most cases" leaves them unable to tell whether three cells or thirty went the other way.

**Evidence.** 6 papers; beyond the quoted three, psi and am-tree both count-and-group their exceptions in prose.

**Exemplars.**

- "the Pkd-tree is the fastest except for three cases, all in highdimensional queries. It is within 1.1× slower than CGAL in two cases, and 1.32× slower than the BHL-tree in one case." — *kdtree*, 6.2 Overall Performance
- "The few cases where PIM-zd-tree does not outperform Pkd-tree in throughput occur for 𝑘NN queries with large 𝑘 values." — *pimzd*, 7.2 Main Results in Throughput
- "65 cases incurred negligible (less than 1.03×) slowdown, 27 cases incurred more than 1.1×" — *p2307-wheatman*, 6.3 API Microbenchmarks

**Violation signature.** Hedges standing in for counts — "in most cases", "with a few exceptions", "generally outperforms" — with no number of exceptions, no magnitude attached, and no shared property named. Also: cells in a table that favour the baseline which the prose never acknowledges.

**Revision.**

- Before: Our classifier outperforms the baseline on most categories, with a few exceptions.
- After: Our classifier outperforms the baseline on 17 of 20 categories. The three exceptions are all low-frequency categories (under 200 training examples), where it is 3-8 F1 points lower.

**Do not apply when.** The experiment has too few instances for a count to carry information (three runs), or the apparent exception is a known measurement failure that was excluded — an exclusion belongs in the setup section, not dressed up as a counted exception.

---

## Name the exhibit inside the sentence that states the number — as its subject in results, as a parenthetical earlier, never in the abstract

**Move.** Every sentence carrying a result number carries its exhibit reference too, but the grammatical form tracks location: in results sections the exhibit is the subject of the claim ("Table 8 shows that…"); in introduction and method it rides as a trailing parenthetical on a claim the authors own ("(see Tab. 1)"); in the abstract the numbers appear with no pointer at all.

**Why it works.** Coupling distance drops to zero — any number the reader doubts is one jump from its evidence — while the abstract stays readable standing alone, and a promise made in the introduction becomes a verifiable claim rather than a boast.

**Evidence.** 7 of the 12 papers read for dimension G. Verified for this pass: not one of the 12 sampled papers' abstracts contains a figure or table reference. Exhibit-as-subject dominates results sections (cpma 19, terrace 18, wheatman 13) while introductions lean parenthetical.

**Exemplars.**

- "Table 8 shows that Terrace is between 1.6×–1.9× slower than Ligra on SSSP." — *xu-terrace-sigmod-21*, 6.2 Results, SSSP
- "Figure 1 demonstrates that the throughput of parallel batch inserts in the CPMA is on average 3× faster than in compressed PaC-trees." — *xu-cpma-ppopp-24*, Evaluation, batch inserts
- "As shown in Figure 2, PPCSR is 2 − 5x faster than Aspen on small-batch updates but between 2 − 5x slower on batch sizes of at least 10 million." — *xu-ppcsr-alenex-21*, 1 Introduction, results summary

**Violation signature.** A results paragraph that runs several numeric sentences before naming the exhibit; an exhibit named once ("Table 3 shows our results.") with claims then accumulated around it; a table or figure referenced exactly once in the paper; an introduction previewing headline numbers with no pointer; conversely, an abstract cluttered with figure references.

**Revision.**

- Before: Recall improves markedly under the new sampling scheme, and precision holds steady. Table 4 shows our results.
- After: Table 4 shows that the new sampling scheme raises recall from 0.61 to 0.79 while precision stays within 0.02 of the baseline.

**Do not apply when.** The claim is qualitative or methodological, or the number was tied to its exhibit one or two sentences earlier — repeating the pointer in every sentence of a tight paragraph clutters it.

---

## Name the asymmetry where the numbers are given, and bound it only when it can be bounded

**Move.** Wherever the comparison is not like-for-like — extra work counted on one side, a different machine, a baseline missing or untuned, differently generated inputs — the paper names the asymmetry and its direction at the point the numbers appear (body, setup, footnote or caption), quantifying it when it is quantifiable and otherwise stating plainly why it cannot be closed, up to and including asking the baseline's authors and reporting their answer.

**Why it works.** Naming the flaw before the reader finds it converts a possible objection into a bounded caveat and shows the authors know how much of the reported gap is real; and an asymmetry you cannot close, named as such, is more credible than a manufactured bound.

**Evidence.** 5 of the 12 papers read for dimension G. Only fastbcc's instance quantifies; the others name the asymmetry and say why it stands — which is the corpus's actual and more transferable device.

**Exemplars.**

- "We include this step in FAST-BCC, although this postprocessing only takes at most 2% of the total running time in all our tests." — *fastbcc*, 6 Experiments, setup
- "Unlike the rest of this paper, this is not an apples-to-apples comparison because each system implements different algorithms and has been tuned for different graphs." — *p2307-wheatman*, Figure 6 caption
- "Julienne does not achieve satisfactory performance on road graphs. We have checked this with the authors, and the reason is that Julienne was not optimized on road graphs." — *stepping*, Table 4 caption, footnote

**Violation signature.** A setup section that lists baselines and hardware but never says what differs between the compared conditions; an unusually large win with no sentence on whether the losing side was configured competently; "for a fair comparison" asserted without naming what was equalized; a baseline named in related work but absent from the tables with no explanation; a cross-machine comparison whose differences appear nowhere near the numbers.

**Revision.**

- Before: We compare against System B on the same benchmark. Our method is 6× faster.
- After: We compare against System B on the same benchmark, but ran it on a 16-core machine because its released build does not support our 64-core node — so part of the 6× gap here is hardware, and we could not separate how much.

**Do not apply when.** The comparison really is like-for-like on identical inputs and hardware — say so once and move on. A paragraph of caveats about a clean comparison reads as anxious hedging and dilutes the caveats that matter elsewhere.

---

## Put the measured size of the cause next to the measured size of the effect

**Move.** When an explanation is load-bearing — it is the paper's account of why its headline result holds — the proposed cause is itself measured, and the two magnitudes are set side by side in one sentence and explicitly compared, sometimes with the verification narrated first ("To verify this, we further tested…").

**Why it works.** It converts an explanation from plausible storytelling into a second piece of evidence; a mechanism whose measured size matches the observed effect is far harder to dispute than one asserted from design reasoning.

**Evidence.** 4 of the 12 papers read for dimension G, and deliberately scoped: "this is because" appears in 62/119 corpus papers, but the large majority of those instances are structural reasoning with no second number, which is legitimate for secondary observations.

**Exemplars.**

- "Pkd-trees incur 6–12× less cache misses than BHL-trees or Log-trees, which is close to the speedup of Pkd-tree over BHL-tree or Log-tree in construction." — *kdtree*, 6.3 In-Depth Performance Study
- "OECForest is 1.8–2.9× deeper than AM-tree, making AM-tree 1.6– 2.5× faster than OEC-Forest for queries." — *am-tree*, 8.2 Query Throughput
- "To verify this, we further tested the average tree height for AM-tree and OEC-Forest, and present the results in the full version of this paper" — *am-tree*, 8.2 Query Throughput

**Violation signature.** The paper's central explanation of its main result rests only on design reasoning: "this is because" or "we hypothesize that" plus a mechanism measured nowhere and with no pointer to where it could be. Do not fire this on every causal clause — flag only the explanation the headline claim depends on, and the explanation an ablation or breakdown table exists to support.

**Revision.**

- Before: Our model is faster because it avoids re-encoding the context at every step.
- After: Our model is faster because it avoids re-encoding the context: it performs 5.4× fewer encoder passes per document (Table 6), close to the 4.8× end-to-end speedup we observe.

**Do not apply when.** The mechanism cannot be instrumented separately, or the explanation is deliberately a conjecture — then mark it as one ("we hypothesize", "one likely reason") rather than dressing an unmeasured guess in the grammar of a finding.

---

## Leave the variant that lost in the exhibit, and point at it by its label
> **Status:** variant

**Move.** A design the authors built and abandoned, or a component whose ablation shows no benefit, is named in the prose, kept as a labelled column or line in the figure beside the winner, pointed at by that label, and given a reason for losing; when the null is the paper's most surprising result it is promoted into the abstract rather than buried after the wins.

**Why it works.** It shows the design space was actually searched rather than asserted, and an ablation containing at least one null is evidence the ablation was run honestly.

**Evidence.** 3 papers, and a minority practice: only about 5 files corpus-wide match "we (implemented|tried|tested) … (but|however|slower)". Recorded as a variant.

**Exemplars.**

- "We implemented this straightforward design and, somewhat unexpectedly, found it much slower than P-Orth trees and Pkd-trees (see CPAM-H and CPAM-Z in Fig. 3)." — *psi*, 3 Preliminaries, Our SPaC-tree
- "All techniques provide substantial performance benefits, with the exception of Direct API." — *pimzd*, Evaluation, Sensitivity to Optimizations
- "The limited impact of Direct API arises from our use of large batch sizes to maximize performance, which falls outside the scenarios for which it is primarily optimized." — *pimzd*, Evaluation, Sensitivity to Optimizations

**Violation signature.** A method section in which every design choice was apparently right the first time; an ablation table where removing any component costs performance, with no null anywhere and no sentence flagging one; "we found that X works well" with no trace of what was tried and discarded; a discarded design described in prose but absent from every exhibit, so the reader cannot see how badly it lost.

**Revision.**

- Before: We adopt a hierarchical encoder, which gives the best results.
- After: We first tried a flat encoder with positional segment markers; it was 4 points worse on long documents (row 2, Table 3), because the markers are diluted past 512 tokens. We therefore adopt a hierarchical encoder.

**Do not apply when.** The failed variant was never actually measured — an unmeasured anecdote of failure adds narrative but no evidence. Also when the discarded variant is someone else's published method: reporting a version you tuned badly misrepresents their work rather than yours.

---

## State the ceiling next to the number
> **Status:** variant (3/119 papers)

**Move.** The sentence reporting a ratio or rate also names the maximum it could have reached — the count of available units, the hardware peak, or the value the design itself predicts — in the same sentence or the one adjacent.

**Why it works.** A bare "22.4×" is uninterpretable; against a stated ceiling of 64× the reader immediately knows how much headroom is left and how impressed to be.

**Evidence.** 3 papers of 119 corpus-wide — a variant by rule 1, kept because the move is portable and non-obvious (inter-annotator ceiling, human floor, Bayes error all transfer).

**Exemplars.**

- "Note that here, we have k = 64 sources, so the maximum speedup can be 64×." — *cbfs*, 5.1 Microbenchmarks on C-BFS
- "On our machine with a peak memory bandwidth of 443.78 GB/s, Pkd-tree has a 327–421 GB/s usage of bandwidth" — *kdtree*, 6.3 Cache Efficiency
- "By design, PPCSR should use about 2x the space of an unoptimized CSR representation to store the empty spaces of the PMA." — *xu-ppcsr-alenex-21*, 7.3 Memory usage

**Violation signature.** A ratio or rate whose scale is set by a known bound reported without that bound in view: a speedup with no source/thread count near it, a throughput with no stated peak, a measured overhead with no design-predicted value to check it against, an agreement score with no inter-annotator ceiling.

**Revision.**

- Before: The annotation pipeline reaches 0.78 agreement with the gold labels.
- After: The annotation pipeline reaches 0.78 agreement with the gold labels, against 0.85 inter-annotator agreement among the human coders — within 8% of the attainable ceiling.

**Do not apply when.** No meaningful ceiling exists for the measure, or the ceiling is a fixed constant every reader of the venue carries in their head, in which case restating it is padding.
