# F. Citation integration

6 patterns, ordered by how much each would improve a weak draft.

---

## Attach the bracket to the thing it names, not to the end of the sentence

**Move.** Place the reference immediately after the noun phrase naming the model, system, term, or parameter it identifies, and let the rest of the sentence carry the authors' own assertion unbracketed.

**Why it works.** The reader sees at a glance which span of text is borrowed and which is the paper's own claim; a terminal bracket leaves a whole sentence ambiguous between "they showed this" and "we assert this about their work".

**Evidence.** 12 of the 12 papers read for dimension F. Validated corpus-wide: 4,657 of 6,881 citations (68%) sit mid-sentence attached to what they name — a strong tendency, not a rule, since 32% are sentence-final.

**Exemplars.**

- "A main weakness of Packed Memory Arrays (PMAs) [6, 21] is their search cost." — *xu-spma-alenex-23*, Introduction
- "we borrow the concept of burdened span from Cilkview [37], a profiling tool for multicore programs" — *kcore*, 2 Preliminaries
- "we compare to an existing system Aspen [21] that represents graphs using trees" — *PacTree*, Introduction

**Violation signature.** Nearly every cited sentence ends "… [12]." Mechanical test: count brackets sitting immediately before a period as a share of all in-text references. Across the sampled papers only 22% do (13-42% per paper); a draft above ~40% is defaulting to sentence-final citation and has stopped marking what is borrowed.

**Revision.**

- Before: Speakers of the minority dialect show reduced vowel duration under stress, which is the standard measure of prosodic prominence [14].
- After: Speakers of the minority dialect show reduced duration on the stressed vowel, measured by the normalised-duration index [14]. The reduction is larger than any previously reported for this variable.

**Do not apply when.** The sentence's entire proposition really is the cited work's finding and none of it is yours. Then the terminal bracket is the honest placement, and moving it onto a noun would understate how much you are borrowing.

---

## Go integral only to credit an origin, a borrowed part, or an attributed opinion

**Move.** Use "X et al. [n]" in a syntactic slot only when naming the inventor of something the paper reuses or renames, the author of a component it directly borrows, the source of a position rather than a fact, or a work discussed across several sentences that needs a pronoun antecedent; everywhere else cite with a bracket alone.

**Why it works.** Because names are rare, each one signals that a person and not merely a result is at issue, so priority, credit and contestable stances stand out from ordinary grounding.

**Evidence.** 12 of the 12 papers read for dimension F. Corpus-wide the bracket-to-integral ratio is about 22:1; in the sampled papers integral citations run 0-9 per paper against 36-233 bracket-only.

**Exemplars.**

- "The idea of CH was proposed by Geisberger et al. [41], based on simplifying highway hierarchies [55, 68] and highway node routing [70]." — *ch*, Related Work
- "Regarding parallel cache complexity, Blelloch et al. [20] suggest that analyzing the span and sequential cache complexity of an algorithm is sufficient" — *DP*, Introduction
- "the finishing step uses the union-find structure by Jayanti et al. [57]" — *scc*, 5 Implementation

**Violation signature.** Related work reads as a roll call in which the grammatical subject of every sentence is a research team: "Smith et al. [3] show that… Jones et al. [4] found that…" No sentence's subject is the phenomenon. The opposite failure also counts: nobody is ever named, so a reader cannot tell who invented the method the paper builds on.

**Revision.**

- Before: Priming effects for morphologically complex words have been reported repeatedly. Ramirez et al. [7] report them, Okafor et al. [8] report them, and Lindqvist et al. [9] report them.
- After: Priming effects for morphologically complex words are well attested [7, 8, 9]. The decomposition account that explains them was introduced by Ramirez et al. [7], and our stimuli follow their design.

**Do not apply when.** The venue uses author-date style (APA, Chicago), where every citation contains a name and the choice is only whether the name occupies a syntactic slot. The underlying rule — name people when priority, borrowing, or stance is at issue — still holds; the 22:1 ratio does not transfer.

---

## Keep the contribution sentence free of other people's citations

**Move.** State what this paper does in a sentence containing no reference to anyone else's work; where a novelty claim must be made, mark it with a knowledge hedge rather than attempting to cite an absence.

**Why it works.** A bracket inside "we propose X" makes the reader stop to work out whether the claim is yours or the cited paper's.

**Evidence.** 12 of the 12 papers read for dimension F. Mechanical test across them: of 144 sentences matching "we propose/present/introduce/design/develop/show that/give/provide", only 12 contain a bracket, and 10 of those point at the authors' own full version or code repository rather than at prior work.

**Exemplars.**

- "To our knowledge, the Semi-External setting with asymmetric read-write costs has not been studied." — *ROSE*, Introduction
- "First, to the best of our knowledge, there exist no implementations given the sophistication of these algorithms." — *edit-distance*, Introduction

**Violation signature.** Contribution sentences carrying references to others — "We propose a method that outperforms [4, 9, 14]" — or bare novelty claims with neither hedge nor concession.

**Revision.**

- Before: We present the first corpus-based account of clitic doubling in heritage speakers, improving on [12, 17].
- After: Clitic doubling in heritage speakers has been described from elicited data [12, 17]. We present a corpus-based account, the first we are aware of.

**Do not apply when.** The contribution is explicitly an extension, adaptation, or replication of one named work the reader must see immediately. Then name it inside the contribution sentence and say in the same clause what you changed — edit-distance does exactly this.

---

## Run the technical core citation-free, and pay for every borrowed part in an explicit provenance sentence

**Move.** Concentrate references in the framing sections and let the method and analysis run without them, except for one-sentence statements of the form "our X is based on / adapted from Y [n]" naming exactly which component came from where.

**Why it works.** A reader moving through the method knows that unattributed text is the paper's own, and the provenance sentences let them subtract prior work and see precisely what remains as new.

**Evidence.** 12 of the 12 papers read for dimension F.

**Exemplars.**

- "Our connectivity and spanning forest algorithms are based on the algorithm by Shun et al. [69], and our biconnectivity algorithm is from Dhulipala et al. [44]." — *ROSE*, Sec. 7
- "Our graph processing application is based on Aspen [21]." — *PacTree*, Applications
- "This idea is used in Landau and Vishkin [37] on parallel approximate string matching, and we adapt this idea to edit distance here." — *edit-distance*, Sec. 3

**Violation signature.** Two opposite failures, both detectable by counting brackets per thousand words through the body. Either the method section carries a bracket after every second sentence, so novelty is invisible; or it carries none while demonstrably reusing prior machinery, so borrowed material reads as original. In the sampled papers citation density is U-shaped: 8-15 references per thousand words in the opening tenth, 0-5 through the middle, 19-36 in the closing tenth. A flat profile is the symptom.

**Revision.**

- Before: We normalise the formant measurements and fit a mixed-effects model with random intercepts for speaker and item, then weight trials by response latency.
- After: We normalise formants with the Lobanov transform [11] and fit the mixed-effects specification of [19], with random intercepts for speaker and item. The latency weighting described below is new here.

**Do not apply when.** Formal sections whose content restates or extends a prior proof. There the citations belong inside the argument, at each borrowed step, so the reader can verify the chain — DP re-cites Hong and Kung at the proof it extends rather than once in the framing.

---

## Split a literature into labelled streams, one bracket bundle per label

**Move.** Summarise a body of work in one sentence by partitioning it into named sub-streams — by application, setting, platform, theory versus practice — and hang a separate reference bundle on each label.

**Why it works.** A flat pile of references tells the reader only that the area is crowded; labelled bundles tell them what it contains and let them jump to the branch they care about.

**Evidence.** 4 of the 12 papers read for dimension F.

**Exemplars.**

- "including social network analysis [12, 31, 41, 43, 55, 81], risk assessment [13, 30, 43, 55, 60, 83]," — *kcore*, Introduction
- "Examples include the time-dependent versions [12, 13], parallel and distributed versions [54, 76], on dynamic graphs [65], and more algorithmic optimizations [27, 42, 48]." — *ch*, Related Work
- "the PMA appears in many applications such as graph processing [15, 30, 35, 36], particle simulations [16], and computer graphics [34]." — *xu-spma-alenex-23*, Introduction

**Violation signature.** A sentence of the form "This problem has been widely studied [1-19]" — five or more references in one bundle with no noun distinguishing any of them. Every reference is interchangeable to the reader.

**Revision.**

- Before: Sleep deprivation has been linked to many adverse outcomes [2, 6, 9, 13, 18, 21, 24].
- After: Sleep deprivation has been linked to impaired memory consolidation [2, 9], elevated inflammatory markers [6, 21], and reduced sustained attention [13, 18, 24].

**Do not apply when.** The bundle is deliberately a non-exhaustive gesture rather than a survey — ch writes "A brief list of recent work … includes [44, 49, …]" and DP uses "(e.g., [...])" for the same purpose. Labelling a list you have not actually surveyed promises a taxonomy you did not do.

---

## Hand the neighbouring literature to a survey and say out loud where your coverage stops

**Move.** Where an adjacent area is too large to review, cite one or more surveys, tell the reader to go there, and state in the same passage which part of the area this paper does and does not cover.

**Why it works.** The reader gets both a route into the wider field and an explicit map of the paper's scope, instead of a paragraph of one-line summaries that serves neither purpose.

**Evidence.** 5 of the 12 papers read for dimension F.

**Exemplars.**

- "We refer the audience to the excellent surveys [9, 61, 74] for more background of the state-of-the-art techniques for route planning." — *ch*, Introduction
- "We refer the readers to the survey papers on static frameworks [60, 90] for a detailed explanation." — *xu-terrace-sigmod-21*, Related Work
- "recently, and we refer the audience to an excellent survey [24] for more background" — *am-tree*, Related Work

**Violation signature.** The related-work section attempts an adjacent field with a paragraph of "X et al. did A. Y et al. did B." at one line each, adding nothing a bibliography would not; or the adjacent field is omitted silently, so a reviewer from it reads the paper as unaware of them.

**Revision.**

- Before: Bilingual lexical access has also been studied extensively. Ito et al. examined cognate effects. Novak et al. examined switching costs. Ahmed et al. examined proficiency effects.
- After: Bilingual lexical access is a large field in its own right; we refer the reader to the surveys of [7, 15]. From it we take only the cognate-frequency control [9]. We do not model switching costs, and our design cannot speak to them.

**Do not apply when.** The adjacent work contains a direct rival a reviewer will expect you to engage. Delegating a competitor to a survey reads as evasion; that work has to be named, described, and differentiated in your own prose.
