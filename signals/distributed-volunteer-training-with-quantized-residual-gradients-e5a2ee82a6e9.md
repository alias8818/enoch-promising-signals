# Distributed Volunteer Training with Quantized Residual Gradients

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `distributed-volunteer-training-with-quantized-residual-gradients-e5a2ee82a6e9`
Run ID: `distributed-volunteer-training-with-quantized-residual-gradients-e5a2ee82a6e9-20260608T203245896230+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/91e7721ea839

## What looked useful

Low-bit residual gradients are a plausible mechanism for bandwidth-limited volunteer training: 4-bit residuals matched dense in this bounded simulation while 4-bit no-residual lost 12.23 accuracy points; sign residuals reduced a 15.75-point no-residual loss to 0.82 points.

## Boundaries and scale limits

Synthetic teacher-labeled classification only; one process on one GB10; synchronous aggregation only; no real volunteer network, asynchronous staleness, adversarial clients, privacy/security layer, or GPT-2-small-class/real-data validation.

## Claim scope

In a single-host CUDA simulation with 8 intermittent non-IID workers and 35% per-step dropout, residual/error-feedback buffers make 4-bit gradient aggregation match dense validation accuracy within 0.03 percentage points at 12.5% of dense communication, and make 1-bit/sign aggregation recover most of the no-residual failure at 3.13% of dense communication.

## Why it stopped

Closed as no-paper useful signal because the evidence supports the optimizer mechanism only in a synthetic single-host proxy, not the full distributed volunteer-training system.

## Recommended next action

Run a bounded real-data asynchronous deepen test before any paper claim: multi-process simulated volunteers with stale gradients on a small standard dataset/model, comparing dense, q4 no-residual, q4 residual, sign no-residual, and sign residual under matched communication accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Asynchronous real-data residual-gradient volunteer simulation
- Success threshold: q4 residual reaches at least 98% of dense final accuracy with no more than 15% of dense transmitted bytes and clearly outperforms q4 no-residual across at least 3 seeds.
- Stop condition: Stop as negative if q4 residual is more than 2% relative accuracy below dense or does not outperform q4 no-residual under the same churn/staleness schedule.

## Evidence references

- Artifact root: `<local-path>/projects/distributed-volunteer-training-with-quantized-residual-gradients-e5a2ee82a6e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
