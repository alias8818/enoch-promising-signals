# Federated Benchmark Validation of Canary Gradient Poison Detection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `federated-benchmark-validation-of-canary-gradient-poison-d-c5c1583fba`
Run ID: `federated-benchmark-validation-of-canary-gradient-poison-d-c5c1583fba-20260526T171251132360+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Canary Data Gradients for Volunteer Poison Detection: enoch://control-plane/projects/canary-data-gradients-for-volunteer-poison-detection-2192ff8b3e68/runs/canary-data-gradients-for-volunteer-poison-detection-2192ff8b3e68-20260525T212441474414+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e560ee96bbc0

## What looked useful

Zero-strength controls were random (canary AUROC mean 0.4932), while all 24 positive-strength condition summaries passed the preset threshold (AUROC >= 0.90 and TPR@5%FPR >= 0.60). Positive-strength canary AUROC mean was 0.9790 with minimum 0.9157; TPR@5%FPR mean was 0.9070 with minimum 0.6333. Norm-only detection was weaker and unreliable at low strengths.

## Boundaries and scale limits

Tier 1 small direct test only: synthetic binary classification, 40 clients, 30 rounds, 64-dimensional model, five seeds, no secure aggregation, no deep models, no real FL datasets, and no adaptive attacker.

## Claim scope

In a controlled synthetic federated logistic-regression benchmark where individual client updates are observable and malicious clients add a known fixed canary-direction component, projection onto the canary direction detects poisoned clients across IID and synthetic non-IID conditions at poison strengths >= 0.25x median honest update norm.

## Why it stopped

Tier 1 controlled direct validation completed; evidence supports the mechanism but remains synthetic and too small for publication readiness.

## Recommended next action

Run a bounded medium deepen test on a real federated dataset or neural FL benchmark, including adaptive canary-masking attackers and utility impact after filtering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Data Neural FL Validation of Canary Gradient Poison Detection
- Success threshold: Across at least three seeds, canary projection achieves AUROC >= 0.90 and TPR@5%FPR >= 0.60 at <=0.5x median honest update-norm poison strength while post-filter accuracy drops by less than 2 percentage points relative to the clean baseline.
- Stop condition: Stop if canary projection falls below AUROC 0.80 or TPR@5%FPR 0.40 on the real-data neural benchmark, or if secure aggregation assumptions prevent client-level scoring without a viable measurement path.

## Evidence references

- Artifact root: `<local-path>/projects/federated-benchmark-validation-of-canary-gradient-poison-d-c5c1583fba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
