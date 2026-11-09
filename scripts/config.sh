# Shared settings for the helper scripts.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
KIT_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATE_DIR="$KIT_DIR/template"
STUDENTS_FILE="$KIT_DIR/students.txt"
PUBLISHED_FILE="$KIT_DIR/published_lessons.txt"

# Your GitHub username (auto-detected from `gh` if empty)
OWNER="${OWNER:-}"
# Student repos are named <PREFIX><github-username>, e.g. hw-alice
PREFIX="${PREFIX:-py-hw-}"

command -v gh >/dev/null || { echo "Install GitHub CLI: https://cli.github.com" >&2; exit 1; }
[ -n "$OWNER" ] || OWNER="$(gh api user --jq .login)"

students() {
  [ -f "$STUDENTS_FILE" ] || { echo "Missing $STUDENTS_FILE" >&2; exit 1; }
  sed -e 's/#.*//' -e 's/[[:space:]@]//g' "$STUDENTS_FILE" | grep -v '^$' || true
}

repo_of() { echo "$OWNER/$PREFIX$1"; }
