# INT4 per-head KV cache for 4x context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-per-head-kv-cache-for-4x-context-on-cpu-6e3a7062b20d`
Run ID: `int4-per-head-kv-cache-for-4x-context-on-cpu-6e3a7062b20d-20260529T010331027809+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0c44e0cde6a7

## What looked useful

Per-head INT4 KV cache mechanically reaches about 4x effective packed compression versus FP16, but per-head scale granularity produced large attention-output errors (median output rel L2 0.4801, max 0.8554) and the vectorized dequantize-then-attend CPU path was slower than FP32 attention (median 3.52x).

## Boundaries and scale limits

No full LLM perplexity, task accuracy, real KV distributions, fused packed-INT4 CPU kernel, or end-to-end 4x context serving run was measured.

## Claim scope

Bounded synthetic CPU probe of single-token decode attention with generated Q/K/V tensors, 8 heads, head dim 64, contexts 1024-8192, comparing FP32 attention against symmetric INT4 KV quantization variants.

## Why it stopped

Proxy/local evidence is mixed and not paper-ready: memory compression is supported, but per-head INT4 attention fidelity and naive CPU latency are early negative signals rather than full validation.

## Recommended next action

Do not write a paper from this run; run a bounded deepen test on a small open model with real KV distributions and a fused or at least packed-aware CPU decode path before revisiting viability.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model packed-aware INT4 KV cache decode probe
- Success threshold: At context lengths at least 2x the FP16 memory-equivalent baseline, achieve >=3.5x effective KV memory reduction, <=5% relative perplexity increase or >=95% retrieval accuracy versus FP16, and <=1.25x FP16 decode latency.
- Stop condition: Stop if real-model quality degradation exceeds 10% relative perplexity or retrieval accuracy drops below 90%, or if packed-aware CPU decode remains >1.5x slower than FP16 at long context.

## Evidence references

- Artifact root: `<local-path>/projects/int4-per-head-kv-cache-for-4x-context-on-cpu-6e3a7062b20d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
