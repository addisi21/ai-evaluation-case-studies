#!/usr/bin/env python3
"""Summarize a public search relevance golden set."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "search_relevance_golden_set.json"


def main() -> None:
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    items = payload["items"]
    ratings = Counter(item["rating"] for item in items)
    labels: Counter[str] = Counter()
    for item in items:
        labels.update(item["issue_labels"])

    print("# Search Relevance Golden Set Summary")
    print()
    print("| Metric | Value |")
    print("| --- | ---: |")
    print(f"| Total items | {len(items)} |")
    print(f"| Excellent or good | {ratings['excellent'] + ratings['good']} |")
    print(f"| Fair or bad | {ratings['fair'] + ratings['bad']} |")
    print()
    print("## Rating Distribution")
    print()
    for rating in ["excellent", "good", "fair", "bad"]:
        print(f"- `{rating}`: {ratings[rating]}")
    print()
    print("## Issue Label Distribution")
    print()
    for label, count in labels.most_common():
        print(f"- `{label}`: {count}")
    print()
    print("## Reviewer Notes")
    print()
    for item in items:
        print(f"- **{item['id']} ({item['rating']})**: {item['rationale']}")


if __name__ == "__main__":
    main()
