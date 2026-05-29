#!/usr/bin/env python3
"""Summarize public AI evaluation case-study scores.

This script is intentionally dependency-free so a reviewer can run it with a
standard Python install. It reads the sample case data and prints a compact
markdown report showing average scores, verdicts, and recurring error labels.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "case_scores.json"


def average(values: list[int]) -> float:
    return round(sum(values) / len(values), 2)


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    cases = data["cases"]
    labels: Counter[str] = Counter()

    print("# AI Evaluation Case Score Summary")
    print()
    print("| Case | Domain | Risk | Avg Score | Verdict |")
    print("| --- | --- | --- | ---: | --- |")

    for case in cases:
        score = average(list(case["scores"].values()))
        labels.update(case["error_labels"])
        print(
            f"| {case['id']} | {case['domain']} | {case['risk_level']} | "
            f"{score} | {case['verdict']} |"
        )

    print()
    print("## Recurring Error Labels")
    print()
    for label, count in labels.most_common():
        print(f"- `{label}`: {count}")


if __name__ == "__main__":
    main()
