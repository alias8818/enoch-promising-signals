# Anchor-preserving per-head KV quant for CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-preserving-per-head-kv-quant-for-cpu-2a1becbe6088`
Run ID: `anchor-preserving-per-head-kv-quant-for-cpu-2a1becbe6088-20260601T000150863969+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/14e8254f30b8

## What looked useful

Per-head int8 KV quantization consistently improved fidelity over per-tensor int8 at the same 0.5x-fp16 storage ratio. Int4 per-head KV quantization remained high-error; query-top-K anchors restored top-1 attention agreement and reduced relative L2 error, but residual error stayed large, especially at 4096 and 8192 tokens. Recent anchors were not useful in this synthetic retrieval-like setup.

## Boundaries and scale limits

No real decoder model, perplexity, generated text quality, production traces, or fused low-bit CPU kernel. Timings include NumPy dequantization and should not be interpreted as optimized serving latency.

## Claim scope

Synthetic CPU NumPy decode-attention probe with 16 heads, head dimension 64, sequence lengths 1024/4096/8192, comparing per-tensor, per-head, and anchor-preserving KV quantization for output error, attention-probability drift, top-1 attention match, storage ratio, and unfused decode overhead.

## Why it stopped

Proxy/early falsification for int4 anchor-preserving KV as a high-fidelity CPU method: anchors helped but did not reduce synthetic attention-output error enough, and unfused NumPy dequantization did not show CPU speed benefits. This is not a full validation.

## Recommended next action

Stop this run as no-paper useful evidence; next run should test per-head int8 and int4 top-attention anchors on a real small decoder with perplexity and generation-quality metrics before optimizing kernels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model perplexity test for per-head KV quantization with top-attention anchors
- Success threshold: Per-head int8: <=1 percent perplexity/NLL regression at 0.5x fp16 KV storage. Int4 anchored: <=3 percent perplexity/NLL regression with <=0.35x fp16 KV storage and no severe generation-quality failures on sampled prompts.
- Stop condition: Stop if per-head int8 exceeds 2 percent perplexity/NLL regression or if all int4 anchored variants exceed 5 percent regression or show obvious generation failures, since the synthetic signal would not transfer.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserving-per-head-kv-quant-for-cpu-2a1becbe6088`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
