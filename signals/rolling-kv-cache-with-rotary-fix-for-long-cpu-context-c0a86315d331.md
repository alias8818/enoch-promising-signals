# Rolling KV cache with rotary fix for long CPU context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `rolling-kv-cache-with-rotary-fix-for-long-cpu-context-c0a86315d331`
Run ID: `rolling-kv-cache-with-rotary-fix-for-long-cpu-context-c0a86315d331-20260530T003820880017+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6d56167698b4

## What looked useful

The rotary fix is correctness-critical only for local-coordinate rolling caches that physically shift already-rotated keys. Absolute-position KV caching already preserves the correct RoPE geometry. A naive per-token re-rotation fix is correct but slower than absolute-position storage in the NumPy probe.

## Boundaries and scale limits

Synthetic single-layer attention only; no trained model, perplexity, multi-layer accumulation, quantized KV cache, production paging/block cache, SIMD kernel, or end-to-end long-context serving validation. The largest tested case was 4096 tokens, window 256, dimension 64.

## Claim scope

In a deterministic NumPy single-attention sliding-window RoPE harness up to 4096 tokens, a local-coordinate rolling KV cache that shifts keys without re-rotation diverges at the first roll, while applying the relative RoPE rotation R(-1) to surviving keys exactly matches an absolute-position sliding-window baseline to floating point precision.

## Why it stopped

No-paper closure: this run produced a reproducible synthetic mechanism result, but not direct model-serving or publication-grade evidence.

## Recommended next action

Run a bounded decoder-level follow-up that integrates the local re-rotation fix into a tiny real autoregressive model cache and compares logits plus throughput against an absolute-position KV baseline on long sliding-window prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Decoder-level validation of local RoPE re-rotation in a rolling KV cache
- Success threshold: For prompts at least 4x longer than the cache window, the re-rotation cache has max logit error below 1e-5 versus the absolute-position baseline, the no-fix cache diverges after the first roll, and runtime overhead is measured with enough repetitions to report median latency.
- Stop condition: Stop if the re-rotation cache cannot match absolute-position logits within 1e-5 in a controlled tiny decoder, or if implementation requires external/private model artifacts not available locally.

## Evidence references

- Artifact root: `<local-path>/projects/rolling-kv-cache-with-rotary-fix-for-long-cpu-context-c0a86315d331`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
