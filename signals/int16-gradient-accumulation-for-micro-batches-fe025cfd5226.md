# Int16 gradient accumulation for micro-batches

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int16-gradient-accumulation-for-micro-batches-fe025cfd5226`
Run ID: `int16-gradient-accumulation-for-micro-batches-fe025cfd5226-20260604T225620907497+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e621841cbccf

## What looked useful

Dynamic block-floating int16 accumulation matched fp32 mean test accuracy in both 16-step and 64-step accumulation probes, with mean relative accumulated-gradient error of 1.28e-4 and 2.50e-4 respectively, no saturation, and about 0.501x fp32 accumulator memory.

## Boundaries and scale limits

CPU-only synthetic MLP; no real dataset, autograd framework, GPU kernel, mixed-precision stack, Adam/AdamW optimizer state, distributed reduction, transformer architecture, or large-model validation was tested.

## Claim scope

In a deterministic NumPy two-layer MLP on a noisy synthetic multiclass task, per-tensor int16 gradient accumulators preserved fp32 accumulated-gradient training outcomes for 16 and 64 micro-batch accumulation while using about half the accumulator tensor storage.

## Why it stopped

Closed as no-paper useful signal: this run directly tested the accumulator mechanism in a small NumPy setting, but it is not full validation of production training usefulness.

## Recommended next action

Run one bounded framework-level follow-up that swaps only gradient accumulator storage in PyTorch or JAX on a small real workload and measures peak memory, convergence, and quality against fp32 and fp16/bf16 controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Framework-level int16 gradient accumulation on a small real workload
- Success threshold: At least 45% measured accumulator-memory reduction versus fp32 with final validation metric within 0.5 percentage points or comparable loss tolerance of fp32 across at least three seeds and no sustained saturation.
- Stop condition: Stop if int16 accumulation degrades validation quality beyond tolerance in two independent seeds, shows sustained saturation above 0.1%, or fails to reduce measured accumulator memory by at least 40%.

## Evidence references

- Artifact root: `<local-path>/projects/int16-gradient-accumulation-for-micro-batches-fe025cfd5226`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
