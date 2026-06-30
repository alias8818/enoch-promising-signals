# Tiny CPU Ring Distributed Training with 1-bit Adam

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-cpu-ring-distributed-training-with-1-bit-adam-a6a7855eedae`
Run ID: `tiny-cpu-ring-distributed-training-with-1-bit-adam-a6a7855eedae-20260527T162113220324+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/529125218837

## What looked useful

Error feedback recovered fp32-like convergence in the toy ring simulation, while sign compression without error feedback lagged. This supports the mechanism but is not enough for a paper.

## Boundaries and scale limits

Synthetic convex task only; no real network, no multiprocessing backend, no measured communication latency, no deep model, no transformer-scale validation, and no evidence of end-to-end wall-clock speedup in a real distributed system.

## Claim scope

In a single-process NumPy simulation of 4 ring workers training synthetic logistic regression with Adam, 1-bit sign compression with error feedback matched fp32 validation loss and accuracy within seed noise while reducing modeled per-worker ring payload by about 31.5x.

## Why it stopped

Current evidence is a bounded synthetic proxy, not a direct distributed-training validation or paper-ready result.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should implement a real local multi-process ring and measure actual wall-clock and byte transfer against fp32 on the same harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Local multi-process ring validation for 1-bit Adam
- Success threshold: sign_ef achieves at least 25x measured payload reduction versus fp32 and final validation loss within 1% relative of fp32 mean across 5 seeds, with no more than 20% wall-clock slowdown in the local CPU implementation.
- Stop condition: Stop if sign_ef diverges, trails fp32 by more than 3% relative validation loss across 3 preliminary seeds, or local multiprocessing overhead makes step time more than 2x fp32 despite lower payload.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-cpu-ring-distributed-training-with-1-bit-adam-a6a7855eedae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
