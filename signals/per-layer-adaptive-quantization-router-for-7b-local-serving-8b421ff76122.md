# Per-layer adaptive quantization router for 7B local serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-layer-adaptive-quantization-router-for-7b-local-serving-8b421ff76122`
Run ID: `per-layer-adaptive-quantization-router-for-7b-local-serving-8b421ff76122-20260607T145250123101+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/14ba056c8bbc

## What looked useful

Adaptive routing reduced MSE versus static INT4 by 58.4%, but was 49.2% slower than fixed mixed precision, 49.6% slower than static INT8, required 50.2% more storage than static INT8, and had about 146x higher MSE than the fixed mixed-precision control. The mechanism improves over all-INT4 error but is dominated by simpler fixed policies in this proxy.

## Boundaries and scale limits

Not a real 7B model, not perplexity/task evaluation, and not production packed INT4/INT8 serving kernels. The benchmark uses pre-dequantized FP16 CUDA matmuls, so latency evidence mainly captures routing overhead and relative policy behavior rather than optimized quantized-kernel throughput.

## Claim scope

Synthetic CUDA transformer-like inference stack with 24 layers of 1024-wide feed-forward blocks, comparing FP16 teacher, static INT8, static INT4, fixed per-layer mixed precision, and activation-conditioned per-layer adaptive routing.

## Why it stopped

Bounded GPU proxy produced an early mixed/negative practical result: adaptive routing improved static INT4 error but failed the latency, storage, and fixed-mixed-control criteria, so it should not proceed to paper writing from this evidence.

## Recommended next action

Stop this activation-router variant as no-paper evidence; the only worthwhile deepen test is a direct packed-kernel 7B or 1-3B serving comparison against fixed mixed per-layer quantization with device-resident routing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed-kernel fixed mixed quantization versus device-resident adaptive routing on local LLM serving
- Success threshold: Adaptive routing must match or improve fixed mixed per-layer quantization quality while keeping decode throughput within 5% and storage no higher than static INT8.
- Stop condition: Stop if packed-kernel adaptive routing is still more than 5% slower than fixed mixed precision at matched quality, or if it requires dual full precision copies exceeding static INT8 storage.

## Evidence references

- Artifact root: `<local-path>/projects/per-layer-adaptive-quantization-router-for-7b-local-serving-8b421ff76122`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
