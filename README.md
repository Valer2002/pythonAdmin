# Python course – teacher kit

Each student gets their own **private repo** (`py-hw-<username>`) on your GitHub account.
Students hand in work as **Pull Requests**. GitHub Actions runs the tests and posts a feedback
comment with a score table. You then review the PR and approve it or request changes.

```
python-course/
├── students.txt              # GitHub usernames, one per line
├── published_lessons.txt     # lessons new student repos start with
├── template/                 # what every student repo contains
│   ├── .github/workflows/check.yml   # CI: runs tests + ruff, comments on the PR
│   ├── .github/scripts/grade.py      # builds the feedback report
│   ├── .github/pull_request_template.md
│   ├── README.md                     # instructions for students
│   └── lessons/lessonNN/             # README.md (task), solution.py (stub), test_solution.py
└── scripts/
    ├── create_student_repos.sh   # create repos + invite students (safe to re-run)
    ├── publish_lesson.sh         # push a new lesson folder to all students
    ├── status.sh                 # table of PRs: CI result + review state
    └── clone_all.sh              # clone/update all repos into submissions/
```

## One-time setup

1. Install the [GitHub CLI](https://cli.github.com) and run `gh auth login`.
2. Add student GitHub usernames to `students.txt`.
3. Run `scripts/create_student_repos.sh`. Each student gets an email invitation to their repo.
4. Ask the students to follow `README.md` in their repo (clone, venv, `pip install -r requirements.txt`).

To add students later, add them to `students.txt` and run the script again. Existing repos are skipped.

## Every lesson

1. Create `template/lessons/lesson03/` with:
   - `README.md` – the task
   - `solution.py` – function stubs (`raise NotImplementedError`)
   - `test_solution.py` – tests. **Add a message to every assert**, because the student sees it in the feedback.
2. Check your tests against a real solution: `cd template/lessons/lesson03 && pytest`, then put the stubs back.
3. Run `scripts/publish_lesson.sh lesson03`.
4. Students make a branch, write code, push and open a PR. CI comments with the results.
5. Run `scripts/status.sh` (or `status.sh all`) to see who submitted and what passed.
6. Review each PR on GitHub. Leave line comments, then **Approve** or **Request changes**.
   Optionally add a label as a grade, e.g. `grade: 9/10`.

## Notes

- To change the CI or other shared files later, edit `template/` and copy the changed files
  into the student repos (`clone_all.sh`, then commit and push in each repo).
- On a free personal account, branch protection doesn't work on private repos, so students *can*
  push directly to `main`. The workflow still runs on `main` pushes and shows results under the
  **Actions** tab. If you need to enforce PRs, get GitHub Pro or move to a free organization.
- Students can see and edit the tests. Before grading, run `git diff` on `test_*.py`
  in their PR (or check the "Files changed" tab).
- Rename the repo prefix with `PREFIX=...` in `scripts/config.sh` before creating repos.
