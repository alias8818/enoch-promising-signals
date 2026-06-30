# Local validation set as Byzantine gradient filter for volunteer training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-validation-set-as-byzantine-gradient-filter-for-volunteer-training-19226b2af38a`
Run ID: `local-validation-set-as-byzantine-gradient-filter-for-volunteer-training-19226b2af38a-20260528T031833257619+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d89cab63ee6d

## What looked useful

Validation gating showed a real mechanism but strong validation-size dependence. Across attacked conditions, 256 validation examples yielded 92.0% benign acceptance and 0.47% Byzantine acceptance, while 16 examples yielded only 54.0% benign acceptance and lost badly to coordinate median at 20-40% Byzantine rates. The method is promising as an additional robust aggregation signal but unsafe to claim broadly without larger trusted validation sets and nonconvex tests.

## Boundaries and scale limits

Evidence is limited to a convex synthetic binary-classification task with simple feature-shift non-IID clients. It does not validate large neural-network training, real volunteer data, privacy constraints, communication limits, secure aggregation compatibility, or adaptive attackers that optimize against the validation gate.

## Claim scope

In a synthetic federated logistic-regression benchmark with 40 clients, 80 rounds, three Byzantine attack types, and up to 60% Byzantine clients, server-side validation-loss gating can filter malicious volunteer gradients when the trusted validation set is moderately sized; 256 validation examples produced high benign acceptance, near-zero Byzantine acceptance, and competitive or better final accuracy than non-validation baselines.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/convex and mixed by validation-set size; it supports a mechanism but not a full volunteer-training validation.

## Recommended next action

Run a bounded nonconvex follow-up on a small real dataset with non-IID clients and adaptive attacks before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validation-gated Byzantine filtering on nonconvex non-IID volunteer training
- Success threshold: With 256-1024 trusted validation examples, validation gating should match the best robust non-validation baseline within 1 percentage point at 20-40% Byzantine clients and exceed it by at least 5 percentage points in a majority-Byzantine condition where median-style aggregation fails, while accepting under 10% of Byzantine gradients.
- Stop condition: Stop if validation gating underperforms the best robust baseline by more than 3 percentage points at 20-40% Byzantine clients or accepts more than 25% of adaptive Byzantine gradients despite enough trusted validation data.

## Evidence references

- Artifact root: `<local-path>/projects/local-validation-set-as-byzantine-gradient-filter-for-volunteer-training-19226b2af38a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
