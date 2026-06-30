# CPU-offloaded Adam states with fused GPU kernel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-adam-states-with-fused-gpu-kernel-87cd308abb97`
Run ID: `cpu-offloaded-adam-states-with-fused-gpu-kernel-87cd308abb97-20260608T103413540137+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b2be2b147e7d

## What looked useful

Mechanism works for memory relief: at 32M parameters CUDA max allocation fell from 512 MB to 264-320 MB depending on chunk size. Naive per-step migration of both Adam moment tensors costs about 3.0-3.2x wall time at that size.

## Boundaries and scale limits

No end-to-end model training, convergence, distributed optimizer, mixed precision, or overlap-with-backward validation was performed; the result is a bounded optimizer microbenchmark.

## Claim scope

On GB10 with synthetic fp32 vectors up to 32M parameters, chunked CPU-offloaded Adam moment states updated by a fused CUDA kernel reduce CUDA-resident memory but impose about a 3x optimizer-step slowdown versus GPU-resident moments.

## Why it stopped

No-paper useful signal: the proxy directly supports memory savings but also shows a large naive transfer penalty, so this is not a full validation or paper-positive result.

## Recommended next action

Run a bounded GPT-2-small-class training follow-up that measures end-to-end tokens/sec, max batch size, and time-to-loss with GPU-resident Adam versus chunked CPU-offloaded Adam with attempted copy/backward overlap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-transformer test for CPU-offloaded Adam moments
- Success threshold: Offloaded Adam saves at least 25% CUDA memory allocated to optimizer state while preserving at least 80% end-to-end tokens/sec or enabling a larger batch/model with better tokens/sec-per-GB at matched loss trend.
- Stop condition: Stop if end-to-end throughput drops below 70% of GPU-resident Adam without enabling a larger stable batch/model, or if loss curves diverge under matched hyperparameters.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-adam-states-with-fused-gpu-kernel-87cd308abb97`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
