#!/usr/bin/env bash
# Clone (or update) every student repo into ../submissions/<student>
set -euo pipefail
source "$(dirname "$0")/config.sh"

dest="$KIT_DIR/submissions"
mkdir -p "$dest"
for user in $(students); do
  dir="$dest/$user"
  if [ -d "$dir/.git" ]; then
    git -C "$dir" fetch -q --all && git -C "$dir" pull -q --ff-only || true
    echo "↻ $user"
  else
    gh repo clone "$(repo_of "$user")" "$dir" -- -q && echo "✔ $user"
  fi
done
