#!/usr/bin/env bash
# Show open/merged homework PRs for every student with CI result and review state.
# Usage: ./status.sh [open|merged|all]
set -euo pipefail
source "$(dirname "$0")/config.sh"

state="${1:-open}"
printf "%-20s %-5s %-25s %-8s %-18s\n" STUDENT PR BRANCH CI REVIEW
for user in $(students); do
  gh pr list -R "$(repo_of "$user")" --state "$state" \
    --json number,headRefName,statusCheckRollup,reviewDecision \
    --jq '.[] | [
        (.number|tostring),
        .headRefName,
        ([.statusCheckRollup[]?.conclusion] | if length==0 then "pending"
           elif all(.=="SUCCESS") then "pass" elif any(.==null or .=="") then "running" else "FAIL" end),
        (.reviewDecision // "NEEDS REVIEW")
      ] | @tsv' 2>/dev/null |
  while IFS=$'\t' read -r num branch ci review; do
    printf "%-20s #%-4s %-25s %-8s %-18s\n" "$user" "$num" "$branch" "$ci" "$review"
  done
done
