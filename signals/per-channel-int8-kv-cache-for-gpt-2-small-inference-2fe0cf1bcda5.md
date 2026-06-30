# Per-Channel INT8 KV Cache for GPT-2-Small Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-channel-int8-kv-cache-for-gpt-2-small-inference-2fe0cf1bcda5`
Run ID: `per-channel-int8-kv-cache-for-gpt-2-small-inference-2fe0cf1bcda5-20260528T190113323788+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/afdbd41a7a28

## What looked useful

Per-channel INT8 KV-cache storage appears numerically safe for this GPT-2-small probe, but memory savings alone do not yield speedup without an attention path that consumes quantized K/V directly.

## Boundaries and scale limits

Tested only GPT-2-small, batch sizes 1 and 4, prompt lengths 64/256/768, 8-64 decode steps, repeated prompt text, and a storage simulation rather than a fused INT8 attention kernel or production serving trace.

## Claim scope

On NVIDIA GB10 with Hugging Face GPT-2-small, simulated per-channel INT8 storage of KV cache tensors preserves teacher-forced next-token top-1 predictions over bounded local decode tests and reduces modeled KV-cache bytes by about 49-50%, but an unfused implementation that dequantizes the full cache before stock attention is 1.47-1.84x slower after warmup.

## Why it stopped

Bounded direct GPT-2-small evidence supports memory reduction and numerical stability but falsifies the practical speedup claim for the naive unfused implementation; this is not full production validation.

## Recommended next action

Stop this run as no-paper useful signal; next, test a fused or library-supported INT8-KV attention path that avoids full fp16 cache materialization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused INT8 KV Attention for GPT-2-Small Decode
- Success threshold: Cache bytes reduced by at least 45%, teacher-forced top-1 agreement at least 99%, mean KL below 1e-3, and mean decode latency no more than 5% slower than fp16 baseline.
- Stop condition: Stop if direct INT8-KV attention remains more than 20% slower than fp16 baseline or top-1 agreement falls below 99% on the bounded benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/per-channel-int8-kv-cache-for-gpt-2-small-inference-2fe0cf1bcda5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
