# Tiny Model Volunteer Training Viability Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-model-volunteer-training-viability-baseline-ab5482c493b3`
Run ID: `tiny-model-volunteer-training-viability-baseline-ab5482c493b3-20260605T060635892667+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e8e619eb5e79

## What looked useful

Central and 4-shard volunteer aggregation matched validation-loss improvement (-0.9021 nats, delta difference 2.98e-08), confirming aggregation mechanics. The 843 KB gradient payload per volunteer would take 0.674 s to upload at 10 Mbps versus an estimated 0.0048 s parallel compute step, making naive every-step full-gradient synchronization about 140x communication-bound.

## Boundaries and scale limits

Single process CPU simulation; Tiny Shakespeare character LM; 120 training steps; no real network, heterogeneous devices, churn, stragglers, adversarial volunteers, privacy mechanism, large model, or long-horizon training.

## Claim scope

On a CPU-only worker, a 210,750-parameter NumPy character language model can learn under simulated 4-volunteer synchronous gradient aggregation, but naive per-step full-gradient upload is communication-bound relative to compute at ordinary residential uplinks.

## Why it stopped

Proxy early falsification of naive synchronous volunteer training: aggregation learns, but full-gradient per-step communication dominates tiny-model compute by one to three orders of magnitude, so this is not a full validation or paper-positive result.

## Recommended next action

Stop this naive full-gradient-per-step design; run a bounded follow-up testing local-SGD or compressed updates with a communication/compute ratio target below 1 while preserving validation-loss progress.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Local-SGD and Compression Baseline for Tiny Volunteer Training
- Success threshold: Communication/compute ratio below 1 at 10 Mbps uplink and final validation-loss improvement at least 90% of the synchronous baseline over a bounded run.
- Stop condition: Stop if no tested compression/local-step setting reaches communication/compute ratio below 1 without losing more than 10% of validation-loss improvement.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-model-volunteer-training-viability-baseline-ab5482c493b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
