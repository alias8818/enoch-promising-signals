# Medium Non-IID Neural Volunteer Gradient Spot-Check

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-non-iid-neural-volunteer-gradient-spot-check-6274317d16`
Run ID: `medium-non-iid-neural-volunteer-gradient-spot-check-6274317d16-20260613T004204235015+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Commitment-Based Gradient Spot-Check for Volunteer Training: enoch://control-plane/projects/commitment-based-gradient-spot-check-for-volunteer-training-30c0ac94b595/runs/commitment-based-gradient-spot-check-for-volunteer-training-30c0ac94b595-20260613T003014345835+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f8f9e63f7a3f

## What looked useful

The calibrated sign-flip run met the parent threshold: lottery loss 0.7427 versus no-audit 1.2191, fixed 1.1631, and clean 0.6004; lottery closed 77.0% of the no-audit clean-loss gap and beat fixed auditing in paired final loss with p=1.80e-05. The original scale-2 stress showed similar directional protection but heavy-tailed no-audit/fixed divergence. The adaptive near-threshold spot-check was mixed because the attack barely harmed no-audit training.

## Boundaries and scale limits

Evidence is limited to a small 784-64-10 MNIST MLP, 45 training rounds, label-shard non-IID partitions, an assumed trusted same-minibatch recomputation audit oracle, and non-adaptive sign-flip attackers for the primary threshold result. The tested cosine-aware adaptive attack was not harmful enough to validate adaptive robustness. This does not cover privacy-compatible reference-gradient construction, collusion, Sybil churn, network latency, CIFAR/language models, or production volunteer training.

## Claim scope

In a controlled MNIST MLP volunteer-gradient simulation with 60 non-IID clients, 25% sign-flip malicious clients, 12 participants per round, and 4 random audits per round, lottery auditing closed 77.0% of the no-audit clean-loss gap, beat fixed auditing in paired final loss across 20 seeds, detected 94% of malicious clients, and produced no honest false positives.

## Why it stopped

No paper now: this Tier 1 direct neural test supports lottery auditing against sign-flip Byzantine clients, but adaptive evasion and privacy-compatible reference-gradient auditing remain unresolved.

## Recommended next action

Run a bounded deepen test with a calibrated harmful adaptive attacker that passes the cosine audit at high rate, then compare lottery, fixed, and no-audit controls on MNIST or CIFAR with the same false-positive and paired-loss gates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harmful Cosine-Passing Adaptive Gradient Attacks Against Lottery Audits
- Success threshold: Lottery must improve final test loss by at least 50% of the no-audit clean-loss gap, beat fixed auditing in paired final loss at p<0.05, keep honest false positives below 2%, and handle attackers with at least 80% raw cosine pass rate.
- Stop condition: Stop as unsupported if a harmful cosine-passing attacker keeps at least 90% inclusion under lottery auditing, if honest false positives exceed 5%, or if lottery does not significantly beat fixed auditing on final loss.

## Evidence references

- Artifact root: `<local-path>/projects/medium-non-iid-neural-volunteer-gradient-spot-check-6274317d16`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
