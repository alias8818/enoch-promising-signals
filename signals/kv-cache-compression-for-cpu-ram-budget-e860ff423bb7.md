# KV Cache Compression for CPU RAM Budget

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-for-cpu-ram-budget-e860ff423bb7`
Run ID: `kv-cache-compression-for-cpu-ram-budget-e860ff423bb7-20260611T002329241364+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1c2cf98124c5

## What looked useful

Int8 groupwise KV compression is a plausible CPU RAM-budget mechanism worth direct model testing; naive int4 compression appears too lossy in this proxy despite higher memory savings.

## Boundaries and scale limits

Synthetic single-layer attention proxy only; no real transformer perplexity, downstream quality, production serving latency, optimized kernels, real prompt distributions, or multi-layer error accumulation were tested.

## Claim scope

On synthetic KV tensors with direct attention-output comparison at sequence length 2048, per-32-value symmetric int8 KV-cache quantization nearly doubles an FP16 CPU RAM budget while preserving sub-0.75% relative L2 attention-output error across four seeds; simple int4 variants produce much larger 12-13% relative error.

## Why it stopped

The local synthetic/proxy experiment completed and produced useful evidence, but it is not publication-grade direct model or serving evidence.

## Recommended next action

Run a bounded direct transformer decode experiment comparing FP16 KV against int8_g32 on real prompts, measuring perplexity or next-token KL, CPU tokens/s, and RSS at long context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model int8 KV cache CPU decode validation
- Success threshold: At least 1.7x measured KV/RSS reduction with <=1% perplexity increase or <=0.01 mean next-token KL increase and <=15% CPU decode throughput loss versus FP16 KV.
- Stop condition: Stop if int8_g32 exceeds the quality threshold or loses more than 15% CPU decode throughput on the bounded real-model test.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-for-cpu-ram-budget-e860ff423bb7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
