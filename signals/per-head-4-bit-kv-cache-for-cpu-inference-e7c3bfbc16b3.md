# Per-Head 4-Bit KV Cache for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-4-bit-kv-cache-for-cpu-inference-e7c3bfbc16b3`
Run ID: `per-head-4-bit-kv-cache-for-cpu-inference-e7c3bfbc16b3-20260529T130608336225+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6788e13f97b2

## What looked useful

4-bit KV cache produced long-context CPU speedups of about 1.37x to 5.13x and 7.1x to 8.0x KV compression, but relative L2 attention-output error was 0.249-0.302 for global per-head scaling, 0.165-0.170 for token/head scaling on clean synthetic tensors, and much worse under rare outliers.

## Boundaries and scale limits

Synthetic K/V tensors only; no real decoder model, perplexity, generation-quality, multi-threaded serving, or hand-vectorized int4 kernel validation. Largest case was 16 heads, head dim 128, 8192 cached tokens, single CPU worker.

## Claim scope

Single-threaded CPU microbenchmark of synthetic transformer-shaped single-token decode attention shows simple 4-bit K/V cache can reduce latency at 2048+ token contexts while compressing KV storage by roughly 7x to 8x, but naive per-head/global scaling has high attention-output error.

## Why it stopped

Proxy/direct microbenchmark evidence supports memory-latency mechanism but early-falsifies naive per-head 4-bit KV as paper-ready because output error is large and real-model quality is unvalidated.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should insert token/head 4-bit KV quantization into a small real decoder model and measure logit drift/perplexity before optimizing kernels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Quality Probe for Token/Head 4-Bit KV Cache
- Success threshold: At 2048-token context on a small real decoder model, achieve at least 4x KV memory reduction, no more than 1 percent relative perplexity degradation or at least 99 percent top-1 agreement on a fixed token set, and at least 1.2x decode-step speedup.
- Stop condition: Stop if perplexity degradation exceeds 5 percent, top-1 agreement falls below 95 percent, or quantized decode remains slower than baseline at 2048 tokens after a straightforward vectorized implementation.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-4-bit-kv-cache-for-cpu-inference-e7c3bfbc16b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
