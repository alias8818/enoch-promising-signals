# Split-Residual: High/Low Precision Dual Path

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `split-residual-high-low-precision-dual-path-3566b349d167`
Run ID: `split-residual-high-low-precision-dual-path-3566b349d167-20260523T231954321489+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71075af61b6a

## What looked useful

Split precision reduced aligned-sparse output MSE to 0.3035x uniform int5 but was 1.2961x uniform int6. With misaligned variance/sensitivity, top-variance selection was 1.0493x uniform int5 while oracle selection was 0.8259x. On isotropic residuals, split precision was 3.9353x worse than uniform int5 and 16.6671x worse than uniform int6.

## Boundaries and scale limits

No trained Transformer, no real activation traces, no GPU kernels, no latency measurement, no learned selector, and no end-task accuracy or perplexity. The probe used 5 trials, 1024 samples, 128 residual dimensions, and 32 linear output dimensions on CPU.

## Claim scope

Dependency-free synthetic residual/readout probe: a 12.5% fp16 high-precision channel path plus int4 low-precision path helps versus uniform int5 only when residual variance and downstream sensitivity are sparse and aligned; it is not a robust general replacement for uniform quantization.

## Why it stopped

Closed as a no-paper useful signal: the local synthetic probe supports a conditional mechanism but falsifies the broad/general split-residual precision claim.

## Recommended next action

Run a bounded deepen experiment on real small-Transformer residual traces with matched average-bit and latency budgets before considering any larger model-training or serving claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transformer Residual Trace Split-Precision Probe
- Success threshold: Split precision must reduce downstream output error or task-loss delta by at least 20% versus the best matched-bit uniform quantization baseline in most tested layers without exceeding the matched bit budget or adding unbounded latency overhead.
- Stop condition: Stop if split precision fails to beat matched-bit uniform quantization on most layers, if high-channel selection is unstable across calibration batches, or if overhead erases the compression benefit.

## Evidence references

- Artifact root: `<local-path>/projects/split-residual-high-low-precision-dual-path-3566b349d167`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
