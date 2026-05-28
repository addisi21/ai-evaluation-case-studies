# AI Evaluation Proof Pack

Public, experience-derived examples. No client prompts, platform tasks, screenshots, proprietary rubrics, or private datasets are included.

## Case 1: Finance and Insurance Output QA

**Scenario:** A user asks whether they can delay payment after receiving an insurance premium notice.

**Sample model output:** "You can delay payment by 30 days. Coverage will remain active and late fees will not apply."

**Evaluator concern:** The answer invents grace-period, coverage, and fee terms that are not confirmed by the source. In insurance and finance contexts, unsupported certainty can cause customer harm and audit risk.

| Dimension | Score | Note |
| --- | ---: | --- |
| Instruction adherence | 4/5 | Answers the question but overreaches. |
| Factual accuracy | 2/5 | Key claims are unsupported. |
| Safety/risk | 2/5 | Could lead the user to miss a deadline. |
| Helpfulness | 3/5 | Useful framing, unreliable conclusion. |

**Error labels:** unsupported financial claim, missing caveat, sensitive-domain overconfidence.

**Reviewer feedback:** The response should summarize only visible policy facts, flag missing grace-period evidence, and advise the user to confirm with the insurer before delaying payment.

## Case 2: Customer-Support Chatbot QA

**Scenario:** A user says they cancelled yesterday but were charged today.

**Sample model output:** "Sorry about that. You are eligible for a refund. I have processed it and it will arrive in 5-7 business days."

**Evaluator concern:** The model sounds helpful but invents refund eligibility and account action. A support assistant should not claim a refund was processed unless the system confirms it.

| Dimension | Score | Note |
| --- | ---: | --- |
| Tone | 5/5 | Empathetic and calm. |
| Policy fit | 2/5 | Promises refund without evidence. |
| Resolution quality | 2/5 | Skips verification. |
| Escalation handling | 2/5 | No billing review path. |

**Error labels:** policy overreach, hallucinated account action, premature resolution.

**Reviewer feedback:** The safer answer should acknowledge the charge, verify cancellation timing, explain that refund eligibility depends on policy, and escalate to billing support if account review is needed.

## Case 3: Generative Media QA

**Scenario:** A prompt asks for a short product-style video showing a customer unboxing a device with the packaging label visible.

**Sample model output:** The video has polished lighting, but the device changes shape between frames and the requested packaging label is missing.

**Evaluator concern:** Visual polish masks prompt failure. Media QA should score instruction following separately from aesthetics.

| Dimension | Score | Note |
| --- | ---: | --- |
| Prompt adherence | 2/5 | Required label missing. |
| Visual coherence | 3/5 | Attractive scene, object drift. |
| Temporal consistency | 2/5 | Device shape changes. |
| Output usability | 3/5 | Needs regeneration. |

**Error labels:** missing prompt element, temporal artifact, object inconsistency.

**Reviewer feedback:** The output should be rated down despite strong visual style because it fails required product details.
