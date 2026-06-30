# Framework-level int16 gradient accumulation on a small real workload

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `framework-level-int16-gradient-accumulation-on-a-small-rea-c1d9e3732f`
Run ID: `framework-level-int16-gradient-accumulation-on-a-small-rea-c1d9e3732f-20260605T034453940411+0000`

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

- Parent run decision: Int16 gradient accumulation for micro-batches: enoch://control-plane/projects/int16-gradient-accumulation-for-micro-batches-fe025cfd5226/runs/int16-gradient-accumulation-for-micro-batches-fe025cfd5226-20260604T225620907497+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e621841cbccf

## What looked useful

Dynamic per-tensor scaled int16 accumulator buffers preserved fp32 accumulation behavior on a small real workload while using 0.5038x fp32 accumulator storage including scale metadata.

## Boundaries and scale limits

Single small tabular dataset, manual NumPy training loop, SGD-like updates, no framework autograd integration, no GPU kernels, no distributed training, no AMP/loss scaling, no optimizer moments, and no CNN/Transformer workloads.

## Claim scope

On UCI WDBC breast cancer classification with a NumPy 30-32-2 MLP, paired fp32 and int16 gradient accumulation produced identical test accuracies across five seeds at 8 and 32 accumulation steps, with max test-loss deltas below 4e-6 and no int16 saturation.

## Why it stopped

Tier 1 direct mechanism test passed, but evidence remains no-paper because it is one small real workload in a NumPy framework-like harness rather than a real framework implementation across workloads.

## Recommended next action

Run a bounded PyTorch optimizer-hook implementation on two small canonical workloads before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch-level int16 gradient accumulation on two small canonical workloads
- Success threshold: Both workloads stay within 0.5 percentage points accuracy or equivalent validation-loss tolerance versus fp32 accumulation, show zero saturation or an explicit safe rescale path, and retain at least 40% accumulator memory reduction including scale metadata.
- Stop condition: Stop if either workload shows reproducible degradation beyond threshold, saturation without recovery, or runtime/framework overhead that removes practical value.

## Evidence references

- Artifact root: `<local-path>/projects/framework-level-int16-gradient-accumulation-on-a-small-rea-c1d9e3732f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
