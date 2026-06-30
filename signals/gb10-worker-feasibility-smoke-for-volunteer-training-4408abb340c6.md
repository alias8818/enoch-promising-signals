# GB10 Worker Feasibility Smoke for Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gb10-worker-feasibility-smoke-for-volunteer-training-4408abb340c6`
Run ID: `gb10-worker-feasibility-smoke-for-volunteer-training-4408abb340c6-20260610T055344505306+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9adcfa60010b

## What looked useful

GB10 worker feasibility for a small volunteer-training smoke is supported: CUDA/PyTorch/BF16 training works, resource telemetry is capturable, swap is disabled as expected, earlyoom is active, and memory stayed within the local envelope. The signal is useful for designing the next bounded volunteer recipe but is not paper-ready.

## Boundaries and scale limits

This was a synthetic single-worker smoke only. It did not test real datasets, model quality, checkpoint/restart, artifact upload, multi-worker coordination, volunteer churn, network reliability, or multi-hour stability.

## Claim scope

On this GB10 worker, a bounded synthetic PyTorch transformer training smoke can run on CUDA with BF16 autocast, backward pass, fused AdamW, no swap, active earlyoom posture, and reproducible JSON/log telemetry. The sustained 69.7M-parameter synthetic run completed 40 measured optimizer steps at 40,430 tokens/s with finite loss, 3.435 GiB peak CUDA allocation, and GPU utilization peaking at 96%.

## Why it stopped

Smoke/proxy feasibility result only; it supports the worker training path but does not provide full volunteer-training validation or publication-grade evidence.

## Recommended next action

Stop this run as a no-paper useful signal; next run should validate a bounded real-data volunteer training recipe with checkpoint/resume and artifact upload on the same GB10 worker.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 Volunteer Training Recipe With Checkpoint Resume
- Success threshold: Complete at least 30 minutes or a fixed useful step budget of real-data GPU training with one checkpoint/resume cycle, finite loss, no earlyoom/CUDA failures, and durable metrics/artifacts.
- Stop condition: Stop on earlyoom kill, CUDA/runtime failure, non-finite loss, checkpoint/resume failure, artifact integrity failure, or projected runtime/resource use beyond the bounded volunteer recipe budget.

## Evidence references

- Artifact root: `<local-path>/projects/gb10-worker-feasibility-smoke-for-volunteer-training-4408abb340c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
