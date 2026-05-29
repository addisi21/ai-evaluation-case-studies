# Search Relevance Golden Set Summary

Generated from `data/search_relevance_golden_set.json` with
`scripts/summarize_search_relevance.py`.

| Metric | Value |
| --- | ---: |
| Total items | 6 |
| Excellent or good | 4 |
| Fair or bad | 2 |

## Rating Distribution

- `excellent`: 2
- `good`: 2
- `fair`: 1
- `bad`: 1

## Issue Label Distribution

- `not_official`: 2
- `indirect_answer`: 1
- `possible_scam`: 1
- `privacy_risk`: 1
- `medical_context`: 1
- `developer_query`: 1

## Reviewer Notes

- **SR-001 (excellent)**: Official, task-completing result for the user's location and intent.
- **SR-002 (fair)**: Related to renewal but does not complete the user's task.
- **SR-003 (excellent)**: Official result path and matches the local education context.
- **SR-004 (bad)**: Likely unsafe and asks for personal data without official backing.
- **SR-005 (good)**: Useful overview, but evaluator should check authority and emergency framing.
- **SR-006 (good)**: Matches the developer intent and provides an implementation path.
