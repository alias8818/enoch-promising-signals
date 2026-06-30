# Residual-Channel 1.58bit CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-1-58bit-cpu-inference-48d18dbbe02b`
Run ID: `residual-channel-1-58bit-cpu-inference-48d18dbbe02b-20260528T142850949782+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/125b33f851bb

## What looked useful

At 1024x1024 single-thread, 2% residual channels reduced relative output MSE from 0.3962 to 0.1197 on outlier-channel weights, a 69.8% reduction, while running at 0.872x dense FP32 speed in the generic path. On Gaussian weights, 5% residual channels reduced MSE by only 5.6%.

## Boundaries and scale limits

Tested only synthetic 1024x1024 and 2048x2048 linear layers with batch 128. No real LLM checkpoints, perplexity, token loop, packed low-bit kernel, or production CPU serving stack were tested.

## Claim scope

Synthetic linear-layer mechanism test on CPU: ternary 1.58-bit row-scaled weights plus selected residual input-channel corrections reduce reconstruction error strongly for outlier-channel weight profiles but do not provide CPU speedup in a generic NumPy implementation.

## Why it stopped

Synthetic mechanism evidence is mixed: accuracy recovery is supported for outlier-channel structure, but CPU inference speed is unsupported in the generic NumPy path and full validation would require direct packed-kernel and model-level evidence.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test is a fused packed AVX-512 ternary-plus-residual kernel on real transformer layer traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed AVX-512 residual-channel ternary matmul on transformer traces
- Success threshold: At least 1.2x median speedup over optimized dense FP32 on transformer-like CPU layer shapes while keeping residual-channel relative MSE at least 50% lower than plain ternary on real outlier-structured layers.
- Stop condition: Stop if the packed kernel cannot beat dense FP32 by 1.0x at 2% residual channels, or if real transformer layers do not show at least 25% MSE reduction versus plain ternary.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-1-58bit-cpu-inference-48d18dbbe02b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
