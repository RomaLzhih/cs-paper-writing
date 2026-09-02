# H. Reader management

4 patterns, ordered by how much each would improve a weak draft.

---

## Run the mechanism past the reader twice — gist pass, then detail pass — and mark the seam with its own sentence

**Move.** Describe the whole mechanism once in paraphrasable prose flagged as "high level" or "overview", then restart the same material at full detail, with an explicit sentence announcing the switch rather than letting the register drift.

**Why it works.** The reader builds a cheap mental skeleton first, so every later detail has a place to attach; the seam sentence tells them when they may stop skimming and start checking.

**Evidence.** 8 of the 12 papers read for dimension H.

**Exemplars.**

- "We first give a high-level overview of the algorithm." — *ParGeo*, 3 Convex Hull, Parallel Reservation-Based Algorithm
- "First, we will give a casual overview of how to do cache-adaptive analysis. This is meant to help guide the reader through the array of technical definitions that follow in this section" — *xu-ca-scan-hiding-full*, 2 Preliminaries, Cache-Adaptive Analysis
- "We first introduce this framework at a high level, and then elaborate on each function in Alg. 5." — *kcore*, 4.1.1 The Framework with Sampling

**Violation signature.** The section's first sentence about the method is already a full-detail sentence (a step, a parameter, a case split); searching the section for "at a high level", "overview", "in more detail", "we now" returns nothing; and the only summary of the mechanism anywhere is the abstract. A reader stopped after two paragraphs could not say in one sentence what the method does.

**Revision.**

- Before: The tagger assigns each token a weight computed from its three-word context window, normalises the weight by document length, thresholds at tau, admits the surviving tokens to a candidate set, and filters that set by the part-of-speech constraint of Section 2.
- After: At a high level, the tagger keeps the tokens whose context makes them surprising, then throws away the ones with the wrong part of speech. We now describe each step in detail. The tagger assigns each token a weight computed from its three-word context window…

**Do not apply when.** The mechanism is short enough that gist and detail would be the same two sentences — a one-paragraph procedure restated is padding, not scaffolding. Also skip when the venue's format already provides a separate overview section, since the seam is then structural.

---

## Attach the reason to the narrowing at the moment you narrow

**Move.** Whenever the paper restricts scope — one setting, one dimension, one baseline configuration, one language — the restricting sentence carries its justification in the same or next sentence, often enumerated ("due to the following reasons. First, … Second, …").

**Why it works.** An unexplained restriction reads as something being hidden; the same restriction with two concrete reasons reads as judgement, and adjacency means the reader never carries an open suspicion across several pages.

**Evidence.** 7 of the 12 papers read for dimension H.

**Exemplars.**

- "We mostly focus on one setting, the point-interval temporal connectivity, due to the following reasons. First, there exist fast baselines for this problem [47]" — *am-tree*, 8 Experiments
- "We evaluate all systems in an unweighted, undirected mode to enable the widest compatibility." — *p2307-wheatman*, 6 Experimental Evaluation
- "We will base our description in the context of R3 for the sake of clarity, but the algorithm can be extended to Rd for any constant integer d ≥ 2." — *ParGeo*, 3 Convex Hull

**Violation signature.** Scope restrictions as bare declaratives with no adjacent because-clause: "We consider only the binary case." "All experiments use the default configuration." "We report results on the English portion." Grep test: for each such sentence, is there a "because", "since", "to enable", "due to", or an enumerated reason within two sentences?

**Revision.**

- Before: We evaluate on English only. All models use the default hyperparameters.
- After: We evaluate on English only, for two reasons. First, it is the only language for which all four baselines have public implementations. Second, the annotation scheme we compare against is defined only for English. We use default hyperparameters throughout, since tuning per model would confound the comparison.

**Do not apply when.** The restriction is the paper's declared subject — a paper about one language does not defend being about that language, and justifying it implies a defensiveness the work does not need. Also skip when the only honest reason is "space", which adds nothing the reader had not assumed.

---

## Name the prerequisites you assume, and restate an imported result instead of citing and moving on

**Move.** State outright which background tools the reader needs, and re-present each borrowed result as a numbered Fact or Theorem carrying the exact interface the paper will use, rather than invoking it by citation number alone.

**Why it works.** The reader can decide up front whether they are equipped, and can then check every step without leaving the page; a bare citation forces a trip to another paper mid-argument, which most readers will not take and will instead skip.

**Evidence.** 7 of the 12 papers read for dimension H.

**Exemplars.**

- "The only mathematics tools we use are Chernoff bound and union bound." — *RWS*, 3 Simplified RWS Analysis
- "Fact 2.1. ([10]) The MST of a graph 𝐺 is PM-equivalent to 𝐺." — *am-tree*, 2.2 Temporal Graph and Path-Max Queries
- "Theorem 3.1. (Parallel Tournament Trees [14, 32]) A tournament tree can be constructed from 𝑛 elements in 𝑂 (𝑛) work and 𝑂 (log 𝑛)" — *lis*, 3 Longest Increasing Subsequence

**Violation signature.** A step licensed by a citation and nothing else — "by [12], the estimator is consistent", "following [7], this holds" — so the reader cannot verify the step or see which hypotheses it needs. And nowhere in the draft is there a sentence saying what the reader is assumed to know already.

**Revision.**

- Before: By [12], the estimator is consistent, so the residual term vanishes.
- After: We use the consistency result of [12] in the following form: if the noise has finite variance and the design matrix has full column rank, the estimator converges in probability to theta. Both hypotheses hold here, so the residual term vanishes. The only probabilistic tools we use are Chebyshev's inequality and the union bound.

**Do not apply when.** The result is genuinely standard for the venue and restating it pads the paper. Also do not restate when you need the general theorem and your paraphrase would quietly narrow it to the special case you happen to use; cite precisely instead.

---

## Introduce one small instance early and re-invoke it by name instead of inventing a fresh example each section

**Move.** Put a single tiny worked instance in a figure in the introduction or preliminaries, announce that it will recur, and in later figures and prose refer back to that same instance explicitly ("the input in Fig. 3") rather than constructing a new one.

**Why it works.** Each re-invocation costs the reader nothing because the objects, labels and numbers are already loaded; a fresh example per section makes them re-learn a cast of characters at every transition, which is where readers of long method sections are lost.

**Evidence.** 5 of the 12 papers read for dimension H.

**Exemplars.**

- "Throughout the section, we will use one specific problem to introduce the connection between temporal graphs and MST" — *am-tree*, 2.2 Temporal Graph and Path-Max Queries
- "We present an example in Fig. 4, which illustrates finding the first frontier for the input in Fig. 3." — *lis*, 3 Longest Increasing Subsequence
- "An example of this process, usually referred to as the “peeling” process, is given in Fig. 1." — *kcore*, 1 Introduction

**Violation signature.** Every figure uses a different instance, with different labels and sizes, and no caption refers to another figure's data; the prose says "for example" repeatedly and each time builds a new scenario; no sentence anywhere announces that an example will be reused.

**Revision.**

- Before: Figure 1 shows a three-word phrase parsed under the baseline. Figure 3 shows a nine-word sentence parsed under our method. Figure 5 gives a different sentence with the confidence scores.
- After: Figure 1 shows a five-word sentence we use as a running example throughout. Figure 3 repeats the sentence of Figure 1, now parsed under our method, and Figure 5 repeats it again with the confidence scores attached.

**Do not apply when.** The sections genuinely concern different objects, so one instance would have to be contorted to exhibit all of them. Also skip when the point being made is precisely about the diversity of inputs, where several contrasting instances are the evidence.
