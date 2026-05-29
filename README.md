# AI Evaluation Case Studies

Anonymized case studies based on real AI data quality, RLHF, annotation QA, HR AI, and operations experience. These examples are rewritten for public portfolio use and do not expose client-private task content, proprietary rubrics, screenshots, or platform-specific instructions.

## Case Studies

| Case Study | Evaluation Focus | Domain |
| --- | --- | --- |
| Finance and insurance AI output QA | Accuracy, risk, compliance markers, hallucination detection | Finance / Insurance |
| Customer-support chatbot evaluation | Helpfulness, tone, resolution quality, escalation handling | SaaS / E-commerce |
| HR AI platform testing | Policy fit, workflow adoption, compliance mismatches | HR Tech |
| Voice AI response review | Phonetic accuracy, natural flow, UX quality | Voice AI |
| Video and generative media QA | Prompt adherence, coherence, safety | Generative Media |

## Proof Pack

See [proof-pack.md](proof-pack.md) for public, experience-derived evaluation examples with scenarios, model-output issues, scorecards, error labels, and reviewer feedback.

## Runnable Artifact

This repo now includes a small, runnable QA scoring artifact:

- [data/case_scores.json](data/case_scores.json): structured case-study scores and error labels
- [scripts/summarize_case_scores.py](scripts/summarize_case_scores.py): dependency-free Python summary script
- [outputs/score-summary.md](outputs/score-summary.md): generated-style score summary for reviewer scanning

Run locally:

```bash
python scripts/summarize_case_scores.py
```

## Evaluation Method

1. Define the user intent, business context, and risk level.
2. Score outputs against rubric dimensions such as instruction adherence, factual accuracy, safety, helpfulness, formatting, verbosity, and UX quality.
3. Classify failures using a consistent error taxonomy.
4. Write actionable feedback for model trainers, QA leads, or product owners.
5. Track recurring failure patterns to support calibration.

## Confidentiality Standard

These case studies are experience-derived. They are not copied from platform tasks or client projects, and they intentionally avoid identifying sensitive clients, prompts, datasets, internal rubrics, and task screenshots.
