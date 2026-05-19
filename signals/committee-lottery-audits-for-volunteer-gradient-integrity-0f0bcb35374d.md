# Committee Lottery Audits for Volunteer Gradient Integrity

Status: `useful_signal`
Project ID: `committee-lottery-audits-for-volunteer-gradient-integrity-0f0bcb35374d`
Run ID: `committee-lottery-audits-for-volunteer-gradient-integrity-0f0bcb35374d-20260517T045637057289+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/87ce680fc6cc

## What looked useful

Across 60 seeds with 25% malicious volunteers and 6 audits per 24 submitted gradients, lottery auditing achieved 0.1753 mean test loss and 0.9486 accuracy versus 0.2638/0.9143 for no audit and 0.2455/0.9246 for fixed auditing. Lottery detected all malicious volunteers in this setting with no observed honest false positives; stress-grid results showed predictable improvement with audit budget.

## Boundaries and scale limits

Evidence is limited to synthetic Gaussian binary classification, simple non-adaptive sign-flip attacks, small parameter vectors, and an assumed trusted audit oracle. It does not validate privacy-compatible reference-gradient construction, collusion resistance, identity churn, communication overhead, or neural-network-scale training.

## Claim scope

In a synthetic logistic-regression volunteer-gradient simulator with 80 volunteers, scaled sign-flip Byzantine clients, and a trusted noisy reference-gradient audit oracle, fresh per-round lottery auditing recovered near-clean accuracy and loss better than no audit or a fixed known audit set.

## Why it stopped

No paper now: the result is a synthetic/proxy mechanism signal and does not establish real volunteer-gradient integrity or solve trusted reference-gradient auditing.

## Recommended next action

Run a bounded deepen follow-up on a real federated-learning benchmark with non-IID clients, adaptive cosine-aware attackers, and a concrete privacy-compatible audit oracle.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Lottery Gradient Audits on Non-IID Federated Benchmarks
- Success threshold: Lottery auditing must improve final test loss by at least 50% of the no-audit clean-loss gap, keep honest false positives below 2%, and outperform fixed auditing under paired tests across at least 20 seeds.
- Stop condition: Stop as unsupported if adaptive attackers keep at least 90% inclusion while passing audits, if honest false positives exceed 5%, or if lottery does not significantly outperform fixed auditing on final loss.

## Evidence references

- Artifact root: `<local-path>/projects/committee-lottery-audits-for-volunteer-gradient-integrity-0f0bcb35374d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
