# cs-paper-writing

Two agent skills for writing CS papers on parallel algorithms and data structures — one for
**Claude Code**, one for **Codex / GPT**. Both were built by reading a corpus of 119
peer-reviewed papers (Yan Gu, Yihan Sun, Helen Xu; SPAA, PPoPP, SIGMOD, VLDB, ESA, ALENEX;
2011–2026) for craft rather than content.

| Skill | Agent | Path in this repo |
|---|---|---|
| `academic-writing` | Claude Code | `plugins/academic-writing/skills/academic-writing/` |
| `cs-academic-writing` | Codex / GPT | `codex/skills/cs-academic-writing/` |

They are independent, not two builds of the same thing. Installing both on one machine is fine.

## `academic-writing` (Claude Code)

Measurement-first. Every claim is backed by counts over all 52,006 sentences and 1.1M words of
the corpus, and patterns that measurement contradicted were narrowed or dropped.

- **Six ordered revision passes** (`references/polishing/PLAYBOOK.md`) — first position, names,
  reference, shape, action and weight, stance — each with a *do not touch* list so a later pass
  cannot re-break what an earlier one settled.
- **72 polishing patterns**, adversarially verified corpus-wide (11 kept as written, 61 narrowed
  or corrected, 2 rejected), plus a 15-check quick checklist and a 16-entry cut list.
- **59 structural patterns** across eight dimensions (`references/patterns/INDEX.md`).
- **`scripts/polish_lint.py`** — a mechanical pre-pass over a `.tex`/`.md` draft that flags only
  countable problems and cites the corpus rate for each. Stdlib only, no dependencies:

      python3 scripts/polish_lint.py draft.tex

  Calibration: 0.6–1.5 findings per 1,000 words is the corpus's own range.

## `cs-academic-writing` (Codex / GPT)

Workflow-first. Routes a request to the right guidance and gates every edit on preserving the
scientific record — quantifiers, asymptotic bounds, claim scope, and defined terminology survive
the rewrite, or the rewrite is wrong.

- Topical guides for style/positioning, technical sections (definitions, pseudocode, theorems,
  complexity) and empirical sections (baselines, ablations, threats to validity).
- A language-polishing guide with explicit editing depths, from a light line edit to a rewrite.
- A final fidelity pass that re-checks the revision against the source.

## Install

### Claude Code — as a plugin (recommended)

```
/plugin marketplace add RomaLzhih/cs-paper-writing
/plugin install academic-writing@cs-paper-writing
```

This repo is **private**, so the machine needs GitHub access first — an SSH key on the account,
or a token in a git credential helper. Verify with `ssh -T git@github.com`. If the `owner/repo`
shorthand fails to authenticate, pass the SSH URL instead:

```
/plugin marketplace add git@github.com:RomaLzhih/cs-paper-writing.git
```

Update later with `/plugin marketplace update cs-paper-writing`.

### Either agent — via `install.sh`

```bash
git clone git@github.com:RomaLzhih/cs-paper-writing.git
cd cs-paper-writing
./install.sh                # both skills, as symlinks into this clone
```

| Command | Effect |
|---|---|
| `./install.sh` | both → `~/.claude/skills/` and `~/.codex/skills/` |
| `./install.sh --claude` | Claude Code only |
| `./install.sh --codex` | Codex only |
| `./install.sh --copy` | copy instead of symlink (when the clone won't stay put) |
| `./install.sh --force` | replace a real directory already at the target |
| `./install.sh --uninstall` | remove what it installed |

Symlinks are the default so `git pull` updates the installed skills in place. `--copy` breaks
that link deliberately. Override the destinations with `CLAUDE_SKILLS_DIR` / `CODEX_SKILLS_DIR`.

Restart the agent afterwards so it rescans its skills directory.

### Per-project instead of global

Copy or symlink a skill directory into the project rather than into `$HOME`:

```bash
mkdir -p .claude/skills .agents/skills
ln -s /path/to/cs-paper-writing/plugins/academic-writing/skills/academic-writing .claude/skills/
ln -s /path/to/cs-paper-writing/codex/skills/cs-academic-writing              .agents/skills/
```

## Using them

Both skills load on their own when the request matches — "polish this paragraph", "review my
introduction", "does this gap statement land". To force one, name it: *"use the academic-writing
skill on Section 3."*

For the Claude skill the intended order is: run `polish_lint.py` first, read the structural
patterns (dimensions A and B) before the sentence-level passes, then work passes 1→6 in order.
Fixing word choice before sentence shape means rewriting the same words twice.

## What is not in this repo

The **corpus itself** — 119 PDFs and their extracted text, ~570 MB — is deliberately excluded:
it is third-party copyrighted material and far too large to distribute. The skills carry only
distilled patterns, measured counts, and short illustrative quotations. Neither skill reads the
corpus at runtime; both are self-contained. The build scripts that produced them
(`analysis/` in the source working directory) are likewise not included.

## Limits

Stated up front because they bite in practice:

- **One subfield, three research groups, one citation style.** Citation patterns assume numeric
  brackets (~22:1 over integral citation) and do not transfer to author-date fields.
- **Limitations and discussion sections are thin** in this corpus — "limitation" appears in 20 of
  118 papers. It is not a model for writing one.
- **Uncertainty reporting is largely absent**: spread across instances, but little on
  run-to-run variance, error bars, or significance.
- **Section structure was not measured mechanically** — raw PDF extraction does not isolate
  headings — so no claim about section ordering or naming rests on counts.

`plugins/academic-writing/skills/academic-writing/references/gaps.md` is the full list for the
Claude skill; read it before trusting the skill outside its range.
