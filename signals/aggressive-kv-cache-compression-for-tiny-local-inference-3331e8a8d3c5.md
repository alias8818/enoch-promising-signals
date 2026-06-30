# Aggressive KV Cache Compression for Tiny Local Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `aggressive-kv-cache-compression-for-tiny-local-inference-3331e8a8d3c5`
Run ID: `aggressive-kv-cache-compression-for-tiny-local-inference-3331e8a8d3c5-20260628T034154303084+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/de30b90b0dd7

## What looked useful

4-bit KV quantization is worth a bounded deeper implementation test for tiny local inference; 2-bit KV and naive truncation should not be prioritized without a compensating method such as residual recent fp16 tokens or learned/adaptive selection.

## Boundaries and scale limits

Short prompts, 8 fixed prompts, 88 decode rows per quantization method, one tiny causal LM, synthetic random-attention truncation proxy only, no packed-cache kernel, no latency/memory-bandwidth measurement, no corpus perplexity or long-context retrieval evaluation.

## Claim scope

On a bounded local distilgpt2 next-token probe, same-shape per-token int4 KV-cache quantization preserved top-1 predictions with low KL/NLL perturbation, while int2 KV and naive recent-window truncation were too lossy in direct/proxy tests.

## Why it stopped

Bounded proxy/direct worker evidence is useful but not paper-grade; the run supports a focused 4-bit follow-up and early-falsifies more aggressive 2-bit/truncation variants at this scope.

## Recommended next action

Run a direct packed-int4 KV-cache inference-engine follow-up on distilgpt2/GPT-2-small with corpus perplexity, long-context probes, actual cache memory, and decode latency versus fp16 baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed int4 KV cache validation for tiny local causal LM inference
- Success threshold: At least 3x measured KV-memory reduction, no more than 2 percent perplexity/NLL degradation, top-1 agreement above 95 percent on teacher-forced decode, and no decode latency regression over fp16 for single-batch local inference.
- Stop condition: Stop if packed int4 KV exceeds 2 percent perplexity/NLL degradation or fails to reduce measured memory by at least 3x after a correct implementation and one quantization-scaling ablation.

## Evidence references

- Artifact root: `<local-path>/projects/aggressive-kv-cache-compression-for-tiny-local-inference-3331e8a8d3c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
