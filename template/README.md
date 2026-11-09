# Python homework

Each lesson's assignment lives in `lessons/lessonNN/`. Read its `README.md`, write your code in `solution.py`.

## One-time setup

```bash
git clone <your repo URL>
cd <repo>
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Submitting a lesson

```bash
git checkout main
git pull                          # get new lessons
git checkout -b lesson02          # one branch per lesson

# ... write your code in lessons/lesson02/solution.py ...
cd lessons/lesson02 && pytest     # check locally

git add lessons/lesson02
git commit -m "lesson02: solution"
git push -u origin lesson02
```

Then on GitHub open a **Pull Request** from `lesson02` to `main`.

- The automatic check posts a comment with your test results. Push fixes to the same branch and it updates.
- Your teacher reviews the code and leaves comments.
- After the teacher **approves**, click **Merge**.

## Rules

- Only change files inside the lesson you are working on.
- Do not edit `test_*.py` files.
