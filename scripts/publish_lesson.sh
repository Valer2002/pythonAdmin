#!/usr/bin/env bash
# Copy template/lessons/<lesson> into every student's repo (main branch).
# Usage: ./publish_lesson.sh lesson02
set -euo pipefail
source "$(dirname "$0")/config.sh"

lesson="${1:?Usage: $0 <lesson-folder-name>}"
src="$TEMPLATE_DIR/lessons/$lesson"
[ -d "$src" ] || { echo "No such lesson: $src" >&2; exit 1; }

for user in $(students); do
  repo="$(repo_of "$user")"
  tmp="$(mktemp -d)"
  if ! gh repo clone "$repo" "$tmp" -- -q --depth 1 2>/dev/null; then
    echo "✘ $repo: cannot clone (run create_student_repos.sh?)"
    rm -rf "$tmp"; continue
  fi
  if [ -e "$tmp/lessons/$lesson" ]; then
    echo "• $repo already has $lesson"
  else
    mkdir -p "$tmp/lessons"
    cp -r "$src" "$tmp/lessons/"
    git -C "$tmp" add "lessons/$lesson"
    git -C "$tmp" commit -q -m "Add $lesson"
    git -C "$tmp" push -q origin HEAD:main
    echo "✔ $repo: $lesson published"
  fi
  rm -rf "$tmp"
done

grep -qx "$lesson" "$PUBLISHED_FILE" 2>/dev/null || echo "$lesson" >> "$PUBLISHED_FILE"
