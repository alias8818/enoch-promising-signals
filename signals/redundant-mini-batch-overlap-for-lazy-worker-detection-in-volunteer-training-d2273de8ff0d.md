# Redundant mini-batch overlap for lazy-worker detection in volunteer training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `redundant-mini-batch-overlap-for-lazy-worker-detection-in-volunteer-training-d2273de8ff0d`
Run ID: `redundant-mini-batch-overlap-for-lazy-worker-detection-in-volunteer-training-d2273de8ff0d-20260630T064415091111+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.2: enoch://research-facility/provider/hf:zai-org/GLM-5.2/b74f542df4db

## What looked useful

Overlap audit disagreement is a strong low-cost detector for non-adaptive lazy behavior, but visible audit channels are trivially special-cased. The next useful direction is hidden or embedded audits that workers cannot distinguish from ordinary training work.

## Boundaries and scale limits

40 seeds per detection condition, 12 workers, 80 rounds, 32-dimensional logistic regression, synthetic data, visible separate audit-gradient reporting; no large neural model, real volunteer hardware, network unreliability, hidden audit protocol, privacy mechanism, or adversarially robust commitment scheme was tested.

## Claim scope

In a bounded synthetic logistic-regression volunteer-training simulation, repeated visible overlapping audit mini-batches detect naive workers that skip, fake, stale-reuse, or subsample audit gradients, but do not detect adaptive workers that compute the visible audit batch honestly while skipping ordinary training work.

## Why it stopped

Proxy-scale synthetic experiment supports the naive-overlap mechanism but early-falsifies visible redundant mini-batch overlap as a complete lazy-worker detector because audit-only stale workers score near random.

## Recommended next action

Stop this run as no-paper useful signal; test an embedded/hidden audit protocol where audit examples are indistinguishable from ordinary mini-batch work and detection is evaluated against audit-only adaptive workers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hidden embedded overlap audits for adaptive lazy-worker detection
- Success threshold: For audit-only stale workers at 25% lazy fraction, achieve mean AUC >= 0.85 and TPR@5%FPR >= 0.70 without reducing honest-only validation accuracy by more than 1 percentage point.
- Stop condition: Stop as negative if embedded audits remain below mean AUC 0.70 or require per-example reporting overhead that exceeds 25% of baseline gradient payload in this bounded simulation.

## Evidence references

- Artifact root: `<local-path>/projects/redundant-mini-batch-overlap-for-lazy-worker-detection-in-volunteer-training-d2273de8ff0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
