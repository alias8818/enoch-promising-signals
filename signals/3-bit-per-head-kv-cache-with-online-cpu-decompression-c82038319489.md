# 3-bit per-head KV cache with online CPU decompression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `3-bit-per-head-kv-cache-with-online-cpu-decompression-c82038319489`
Run ID: `3-bit-per-head-kv-cache-with-online-cpu-decompression-c82038319489-20260604T211913894247+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48518d91158f

## What looked useful

A compact 12-bit LUT is necessary for plausible performance and beat FP16 stream-read in the seq=4096 8-thread case, but the larger seq=16384 8-thread check fell to 15-24% of FP16 stream-read logical bandwidth; the broad online CPU decompression throughput hypothesis is not supported by this bounded evidence.

## Boundaries and scale limits

No GPU serving path, no attention kernel integration, no PCIe/UMA transfer measurement, no model quality measurement, synthetic values only, and CPU implementation limited to scalar plus LUT unpacking variants.

## Claim scope

CPU-only synthetic KV-cache benchmark for 3-bit per-head packed K/V unpacking and dequantization on an 8-online-CPU Intel Xeon Silver 4114 worker, comparing logical FP16-equivalent throughput against an FP16 stream-read baseline at seq=4096 and seq=16384.

## Why it stopped

Bounded CPU benchmark produced a mixed-to-negative proxy result rather than full validation: single-thread and larger-context 8-thread CPU decompression did not beat FP16 streaming, so the current evidence is not paper-positive.

## Recommended next action

Stop this run as a no-paper useful signal; only revisit with an end-to-end decode benchmark that overlaps CPU decompression with GPU attention and includes FP16/BF16 and GPU-side low-bit KV controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end overlapped CPU decompression for low-bit KV decode
- Success threshold: At seq>=16384, p50 and p95 decode latency improve by at least 10% over FP16/BF16 KV without unacceptable quality loss, and profiling shows CPU decompression is hidden or not the critical path.
- Stop condition: Stop if CPU decompression plus transfer accounts for more than 25% of decode step time or if end-to-end latency is not at least 5% better than FP16/BF16 KV after overlap and prefetch tuning.

## Evidence references

- Artifact root: `<local-path>/projects/3-bit-per-head-kv-cache-with-online-cpu-decompression-c82038319489`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
