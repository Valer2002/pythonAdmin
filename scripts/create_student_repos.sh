#!/usr/bin/env bash
# Create a private repo for every student in students.txt (skips existing ones)
# and invite the student as a collaborator. New repos get all published lessons.
set -euo pipefail
source "$(dirname "$0")/config.sh"

touch "$PUBLISHED_FILE"

for user in $(students); do
  repo="$(repo_of "$user")"
  if gh repo view "$repo" >/dev/null 2>&1; then
    echo "• $repo already exists, skipping"
    continue
  fi

  tmp="$(mktemp -d)"
  rsync -a --exclude lessons/ "$TEMPLATE_DIR/" "$tmp/"
  mkdir -p "$tmp/lessons"
  while read -r lesson; do
    [ -n "$lesson" ] && cp -r "$TEMPLATE_DIR/lessons/$lesson" "$tmp/lessons/"
  done < "$PUBLISHED_FILE"
  touch "$tmp/lessons/.gitkeep"

  git -C "$tmp" init -q -b main
  git -C "$tmp" add -A
  git -C "$tmp" commit -q -m "Course setup"
  gh repo create "$repo" --private --source "$tmp" --push >/dev/null
  gh api -X PUT "repos/$repo/collaborators/$user" --silent
  rm -rf "$tmp"
  echo "✔ $repo created, invitation sent to @$user"
done
