# 2-bit Weight Quantization with Orthogonal Residual Channels on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-weight-quantization-with-orthogonal-residual-channels-on-gb10-db87a1ba6ff6`
Run ID: `2-bit-weight-quantization-with-orthogonal-residual-channels-on-gb10-db87a1ba6ff6-20260621T114742004252+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2f909791b33b

## What looked useful

Orthogonal residual channels are a real residual-recovery mechanism: at 128 channels, mean output relative MSE was 1.023 for SVD channels versus 1.239 for random channels, a 0.826 SVD/random ratio, with 1.32x emulated latency over the plain base. Heavy-tail weights remained poor at about 2.25-2.28 relative MSE after correction.

## Boundaries and scale limits

Synthetic isolated linear layers only; no packed 2-bit CUDA kernel, no real transformer perplexity/task metric, no GPT-2-small-class baseline, and no production memory-bandwidth measurement.

## Claim scope

On synthetic 2048x2048 linear layers on GB10, SVD-derived orthogonal residual channels reduce 2-bit quantization output error versus random orthogonal residual channels at the same channel budget, but do not recover enough accuracy for a strong practical quantization claim.

## Why it stopped

Proxy/early falsification: the mechanism beats random controls, but the simple 2-bit plus orthogonal residual design leaves high isolated-layer output error and material emulated latency overhead, so it is not paper-ready or practically validated.

## Recommended next action

Stop this run as a proxy/early falsification of the strong practical claim; next, run a bounded GPT-2-small-class perplexity probe with real weights, storage-faithful 2-bit quantization, and a parameter-matched low-rank residual control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small bounded perplexity probe for orthogonal residual 2-bit weights
- Success threshold: At equal residual parameter budget, orthogonal residual channels improve perplexity degradation by at least 20% versus plain 2-bit and outperform the parameter-matched low-rank/control residual without more than 1.25x measured inference latency over the quantized baseline.
- Stop condition: Stop if orthogonal residual channels fail to beat the parameter-matched low-rank/control residual on perplexity or if measured latency/memory overhead erases the benefit.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-weight-quantization-with-orthogonal-residual-channels-on-gb10-db87a1ba6ff6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
