#!/usr/bin/env bash
# Install the academic-writing (Claude) and cs-academic-writing (Codex) skills
# into the agent's personal skill directory.
#
#   ./install.sh                 both skills, as symlinks (git pull then updates them)
#   ./install.sh --claude        Claude Code only  -> ~/.claude/skills/academic-writing
#   ./install.sh --codex         Codex only        -> ~/.codex/skills/cs-academic-writing
#   ./install.sh --copy          copy instead of symlink (for machines without this clone)
#   ./install.sh --force         replace a real directory already at the target
#   ./install.sh --uninstall     remove what this script installed
#
# Claude Code users can skip this entirely and use the plugin instead:
#   /plugin marketplace add RomaLzhih/cs-paper-writing
#   /plugin install academic-writing@cs-paper-writing

set -euo pipefail

SRC_ROOT=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)

CLAUDE_SRC="$SRC_ROOT/plugins/academic-writing/skills/academic-writing"
CLAUDE_DST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}/academic-writing"
CODEX_SRC="$SRC_ROOT/codex/skills/cs-academic-writing"
CODEX_DST="${CODEX_SKILLS_DIR:-$HOME/.codex/skills}/cs-academic-writing"

do_claude=0 do_codex=0 mode=symlink force=0 uninstall=0

for arg in "$@"; do
  case "$arg" in
    --claude)    do_claude=1 ;;
    --codex)     do_codex=1 ;;
    --all)       do_claude=1; do_codex=1 ;;
    --copy)      mode=copy ;;
    --force|-f)  force=1 ;;
    --uninstall) uninstall=1 ;;
    -h|--help)   sed -n '2,20p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *)           echo "install.sh: unknown option '$arg' (try --help)" >&2; exit 2 ;;
  esac
done
if [ "$do_claude" -eq 0 ] && [ "$do_codex" -eq 0 ]; then do_claude=1; do_codex=1; fi

remove_target() {
  local dst=$1 label=$2
  if [ -L "$dst" ]; then
    rm -f "$dst"; echo "  removed symlink $dst"
  elif [ -d "$dst" ]; then
    if [ "$force" -eq 1 ] || [ "$uninstall" -eq 1 ]; then
      rm -rf "$dst"; echo "  removed directory $dst"
    else
      echo "  SKIPPED $label: $dst exists and is a real directory." >&2
      echo "          Move it aside, or re-run with --force to replace it." >&2
      return 1
    fi
  fi
  return 0
}

install_one() {
  local src=$1 dst=$2 label=$3
  if [ ! -f "$src/SKILL.md" ]; then
    echo "  ERROR $label: no SKILL.md under $src" >&2; return 1
  fi
  mkdir -p "$(dirname "$dst")"
  remove_target "$dst" "$label" || return 1
  if [ "$mode" = copy ]; then
    cp -r "$src" "$dst"; echo "  copied   $label -> $dst"
  else
    ln -s "$src" "$dst"; echo "  linked   $label -> $dst"
  fi
}

rc=0
if [ "$uninstall" -eq 1 ]; then
  echo "Uninstalling:"
  [ "$do_claude" -eq 1 ] && { remove_target "$CLAUDE_DST" academic-writing || rc=1; }
  [ "$do_codex"  -eq 1 ] && { remove_target "$CODEX_DST" cs-academic-writing || rc=1; }
  echo "Done."
  exit $rc
fi

echo "Installing from $SRC_ROOT ($mode):"
[ "$do_claude" -eq 1 ] && { install_one "$CLAUDE_SRC" "$CLAUDE_DST" academic-writing    || rc=1; }
[ "$do_codex"  -eq 1 ] && { install_one "$CODEX_SRC"  "$CODEX_DST"  cs-academic-writing || rc=1; }

if [ $rc -eq 0 ]; then
  echo
  echo "Done. Restart Claude Code / Codex so it rescans the skills directory."
  [ "$mode" = symlink ] && echo "These are symlinks into this clone -- do not delete or move it."
fi
exit $rc
