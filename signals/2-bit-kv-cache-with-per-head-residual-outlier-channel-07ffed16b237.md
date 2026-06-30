# 2-bit KV cache with per-head residual outlier channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-per-head-residual-outlier-channel-07ffed16b237`
Run ID: `2-bit-kv-cache-with-per-head-residual-outlier-channel-07ffed16b237-20260619T170422393745+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/38572eb15e20

## What looked useful

For persistent two-channel per-head outliers, int2/head relative MSE was 160.399676 while int2 plus r2 residual channels was 0.498970 at 15.23% of fp16 KV memory versus 12.5% for pure int2/head. The same r2 residual helped little for burst-token outliers, reducing relative MSE only from 26.450295 to 24.898961, and per-channel 2-bit quantization was a stronger reference on Gaussian and bursty cases.

## Boundaries and scale limits

No pretrained model, real KV trace, perplexity/task metric, multi-layer accumulation, packed-cache kernel, decode latency, or GPU memory-bandwidth measurement was run. Evidence is limited to 8 heads, 256 cache tokens, 64 query tokens, 64-d heads, 24 trials, and synthetic outlier distributions.

## Claim scope

Synthetic NumPy scaled-dot-product attention probe shows that keeping two calibrated per-head KV outlier channels exact while quantizing the remaining channels to 2 bits can sharply reduce attention-output error when outliers are persistent by channel.

## Why it stopped

This run produced a useful synthetic mechanism signal but not direct model-quality or serving evidence; finalize as no-paper proxy evidence rather than full validation.

## Recommended next action

Run a bounded real-trace follow-up on a small pretrained transformer, comparing fp16 KV, int2/head, int2/channel or int2/group, and int2/head plus calibrated residual channels using next-token KL or perplexity plus explicit memory accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model real KV trace validation for 2-bit residual outlier channels
- Success threshold: At equal or explicitly costed memory budget, r2 residual must reduce next-token KL or perplexity degradation by at least 25% versus pure int2/head on real traces without worse than 5% regression versus the best non-residual 2-bit baseline in non-outlier-heavy layers.
- Stop condition: Stop if real KV traces do not show persistent per-head channel outliers, or if r2 residual fails to improve next-token KL or perplexity degradation by at least 10% versus int2/head in an initial bounded trace run.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-per-head-residual-outlier-channel-07ffed16b237`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
