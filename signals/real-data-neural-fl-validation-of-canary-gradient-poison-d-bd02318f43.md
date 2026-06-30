# Real-Data Neural FL Validation of Canary Gradient Poison Detection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-data-neural-fl-validation-of-canary-gradient-poison-d-bd02318f43`
Run ID: `real-data-neural-fl-validation-of-canary-gradient-poison-d-bd02318f43-20260526T230841296856+0000`

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

- Parent run decision: Canary Data Gradients for Volunteer Poison Detection: enoch://control-plane/projects/canary-data-gradients-for-volunteer-poison-detection-2192ff8b3e68/runs/canary-data-gradients-for-volunteer-poison-detection-2192ff8b3e68-20260525T212441474414+0000
- Parent run decision: Federated Benchmark Validation of Canary Gradient Poison Detection: enoch://control-plane/projects/federated-benchmark-validation-of-canary-gradient-poison-d-c5c1583fba/runs/federated-benchmark-validation-of-canary-gradient-poison-d-c5c1583fba-20260526T171251132360+0000

## What looked useful

Canary-gradient cosine detection reached AUROC 1.000 on IID and 0.995-1.000 on non-IID across poison weights, while norm-baseline AUROC was 0.375 on IID and 0.445 on non-IID. No-poison controls were near chance, but independent wrong-canary controls were also high, so the signal is not specific to the exact canary batch.

## Boundaries and scale limits

MNIST MLP only; 24 simulated clients; one warmed global state and one local update pass per condition; no secure aggregation, adaptive attacker, multi-round persistence, larger models, or deployed FL telemetry.

## Claim scope

In a local MNIST neural FL simulation with 24 clients, 4 malicious clients, 5 fixed seeds, IID and label-skew non-IID partitions, and norm-stealth canary-loss poisoning, cosine scoring against a canary-gradient direction detects poisoned client updates substantially better than an update-norm anomaly baseline.

## Why it stopped

Tier 2 evidence supports detection of norm-stealth gradient poison, but the wrong-canary control also detects the attack, so the stronger exact-canary detection mechanism is mixed rather than paper-ready.

## Recommended next action

Stop paper escalation for this run; run a bounded deepen follow-up that tests canary specificity using orthogonal/random-label canary banks and adaptive cosine-penalized attackers before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Canary Specificity and Adaptive Evasion Test for Gradient Poison Detection
- Success threshold: Exact canary AUROC at least 0.90 and at least 0.20 absolute AUROC above independent canary/random-label controls under non-IID norm-stealth poisoning, with TPR@5%FPR at least 0.70 across 5 seeds.
- Stop condition: Stop if independent canary or random-label controls remain within 0.10 AUROC of the exact canary across two datasets or if adaptive cosine-penalized poisoning reduces exact-canary AUROC below 0.70 while preserving the poison objective.

## Evidence references

- Artifact root: `<local-path>/projects/real-data-neural-fl-validation-of-canary-gradient-poison-d-bd02318f43`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
