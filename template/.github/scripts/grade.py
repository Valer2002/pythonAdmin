"""Run each lesson's tests and write a Markdown feedback report.

Usage: python .github/scripts/grade.py [lesson01 lesson02 ...]
With no arguments, all lessons are checked and the exit code is always 0.
"""

import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LESSONS_DIR = ROOT / "lessons"
REPORT = ROOT / "report.md"


def run_tests(lesson: Path) -> dict:
    junit = lesson / ".junit.xml"
    # Each lesson runs in its own process so every lesson can have its own solution.py
    subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", f"--junitxml={junit}"],
        cwd=lesson,
        capture_output=True,
        text=True,
    )
    result = {"passed": 0, "total": 0, "failures": []}
    if not junit.exists():
        result["failures"].append(("pytest", "Tests could not run (syntax error?)"))
        return result
    for case in ET.parse(junit).getroot().iter("testcase"):
        result["total"] += 1
        problem = case.find("failure")
        if problem is None:
            problem = case.find("error")
        if problem is None:
            if case.find("skipped") is None:
                result["passed"] += 1
            continue
        message = (problem.get("message") or "").strip().splitlines()
        result["failures"].append((case.get("name"), message[0] if message else "failed"))
    junit.unlink()
    return result


def run_lint(lesson: Path) -> str:
    proc = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--output-format=concise", "."],
        cwd=lesson,
        capture_output=True,
        text=True,
    )
    return "" if proc.returncode == 0 else proc.stdout.strip()


def main() -> int:
    requested = sys.argv[1:]
    lessons = [LESSONS_DIR / name for name in requested] or sorted(
        p for p in LESSONS_DIR.iterdir() if p.is_dir()
    )

    lines = ["## 🤖 Homework check", "", "| Lesson | Tests | Result |", "|---|---|---|"]
    details = []
    all_passed = True

    for lesson in lessons:
        if not lesson.is_dir():
            continue
        tests = run_tests(lesson)
        lint = run_lint(lesson)
        ok = tests["total"] > 0 and tests["passed"] == tests["total"]
        all_passed &= ok
        icon = "✅" if ok else "❌"
        lines.append(f"| {lesson.name} | {tests['passed']}/{tests['total']} | {icon} |")

        if tests["failures"] or lint:
            details.append(f"<details><summary><b>{lesson.name}</b> – details</summary>\n")
            for name, msg in tests["failures"]:
                details.append(f"- ❌ `{name}`: {msg}")
            if lint:
                details.append("\n**Style hints (ruff):**\n```\n" + lint + "\n```")
            details.append("</details>\n")

    lines.append("")
    lines.extend(details)
    if all_passed:
        lines.append("🎉 All tests passed! Your teacher will review the code soon.")
    else:
        lines.append("Fix the failing tests, commit and push again – this comment will update.")

    report = "\n".join(lines) + "\n"
    REPORT.write_text(report, encoding="utf-8")
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary, "a", encoding="utf-8") as f:
            f.write(report)
    print(report)

    return 0 if (all_passed or not requested) else 1


if __name__ == "__main__":
    sys.exit(main())
