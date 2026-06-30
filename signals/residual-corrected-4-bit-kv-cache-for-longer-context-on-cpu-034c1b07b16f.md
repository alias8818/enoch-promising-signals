# Residual-corrected 4-bit KV cache for longer context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-corrected-4-bit-kv-cache-for-longer-context-on-cpu-034c1b07b16f`
Run ID: `residual-corrected-4-bit-kv-cache-for-longer-context-on-cpu-034c1b07b16f-20260629T084441958168+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/85c96a57ff49

## What looked useful

Error-aware residual correction improved median attention-output relative L2 by 5.6% on gaussian caches, 62.7% on 1% outlier caches, and 13.7% on drift caches at 5% residual rows; recent-only residual rows were weak and sometimes slightly harmful.

## Boundaries and scale limits

No packed int4 CPU kernel, no real transformer integration, no perplexity/retrieval benchmark, no decode throughput benchmark, and no validation beyond sequence length 16384 with 4 heads and head dimension 64. Top-error residual selection is simulated from available quantization-error scores.

## Claim scope

Synthetic NumPy single-step decode attention probe: grouped 4-bit K/V plus sparse fp16 residual rows can reduce relative L2 attention-output error versus naive grouped 4-bit K/V while remaining about 31.6% of fp16 KV memory at 5% residual rows. The signal is strongest when residual rows are selected by quantization error, especially for outlier-heavy K/V distributions.

## Why it stopped

Proxy-only synthetic evidence supports an error-aware residual-correction mechanism but does not provide direct model-quality or CPU-serving validation for a paper claim.

## Recommended next action

Implement a packed CPU KV-cache prototype in a small transformer decoder and test perplexity/retrieval quality plus decode throughput against fp16 and naive int4 baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed CPU residual-int4 KV cache in a small decoder
- Success threshold: At 5% to 10% residual rows, recover at least half of naive int4's quality loss versus fp16 while using no more than 40% of fp16 KV memory and losing no more than 20% CPU decode tokens/s versus naive int4.
- Stop condition: Stop if residual correction recovers less than 25% of naive int4 quality loss at 10% residual rows or if CPU decode throughput falls below 50% of naive int4.

## Evidence references

- Artifact root: `<local-path>/projects/residual-corrected-4-bit-kv-cache-for-longer-context-on-cpu-034c1b07b16f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
