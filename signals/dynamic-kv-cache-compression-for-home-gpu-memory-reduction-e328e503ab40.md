# Dynamic KV Cache Compression for Home GPU Memory Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-kv-cache-compression-for-home-gpu-memory-reduction-e328e503ab40`
Run ID: `dynamic-kv-cache-compression-for-home-gpu-memory-reduction-e328e503ab40-20260608T195217218696+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/69b8a2ecfe2c

## What looked useful

Int8 old-row KV quantization is promising but outlier-sensitive; adaptive preservation of 5% high-amplitude old rows restored sub-2% mean attention-output error in several outlier-heavy cases while retaining substantial memory savings. Simple int4 old-row quantization was consistently too lossy.

## Boundaries and scale limits

No full language model, perplexity, downstream task, long generation, or fused packed-KV kernel was tested. Latency measurements are from an unfused PyTorch prototype and are not representative of an optimized implementation.

## Claim scope

Synthetic single-token decode attention on GB10 shows that dynamic int8 KV cache compression, keeping recent rows and optionally a small high-amplitude old-row fraction in fp16, can reduce estimated packed KV memory by about 35-49% while keeping mean relative L2 attention-output error below 2% in normal/decay cases and selected outlier-heavy cases.

## Why it stopped

This worker run produced synthetic attention-output evidence only; it is a no-paper useful signal, not a full validation.

## Recommended next action

Run a bounded real-model follow-up with GPT-2-small-class cached generation, fp16 KV baseline, dynamic int8 packed KV, memory/throughput telemetry, and perplexity or task-quality deltas before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model validation of dynamic int8 KV compression with adaptive outlier retention
- Success threshold: At least 35% measured KV memory reduction, less than 1% perplexity regression or equivalent quality loss, and no more than 10% throughput loss versus fp16 KV on a real small decoder.
- Stop condition: Stop if dynamic int8 causes more than 2% perplexity regression at under 35% memory reduction, or if an optimized path cannot come within 25% throughput of fp16 baseline on GB10.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-kv-cache-compression-for-home-gpu-memory-reduction-e328e503ab40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
