# 4-bit KV-cache serving from CPU RAM for long context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-kv-cache-serving-from-cpu-ram-for-long-context-21c250305c6e`
Run ID: `4-bit-kv-cache-serving-from-cpu-ram-for-long-context-21c250305c6e-20260525T073140976951+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/48e5caa5378f

## What looked useful

At 262144 tokens the fp32 K+V pass took 0.217441 s for 2.0 GiB represented cache, while int4 took 0.978550 s for 0.28125 GiB represented cache; int4 relative RMSE was about 0.1076 on K and V. This early proxy falsifies scalar CPU-side 4-bit KV dequantization as a practical path, but leaves packed-transfer plus fused accelerator dequantization untested.

## Boundaries and scale limits

Tested synthetic K/V tensors only, up to 262144 tokens, 8 KV heads, 128 head dimension, group size 64, CPU RAM resident, scalar dequantization, and OpenMP CPU execution. Did not test real model quality, GPU fused kernels, host-to-device transfer overlap, batching, paged attention, or production serving.

## Claim scope

On this 8-thread CPU worker, a synthetic long-context KV-cache decode proxy with scalar CPU-side int4 unpack/dequantization is slower than fp32 streaming despite much smaller represented cache bytes.

## Why it stopped

Proxy/early falsification: local evidence shows scalar CPU-side int4 unpack/dequantization overwhelms cache-byte savings, so this run is not a full validation of CPU-RAM KV serving and is not paper-ready.

## Recommended next action

Stop this scalar CPU-side path; the concrete next bounded test is a fused GPU attention prototype that transfers packed int4 KV pages from host RAM and dequantizes on device.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed host-RAM int4 KV with fused GPU dequantization
- Success threshold: At least 1.5x end-to-end decode throughput improvement or equivalent context-length expansion at no more than 2% perplexity degradation versus the host-resident fp16/fp32 KV baseline.
- Stop condition: Stop if packed-transfer fused dequantization fails to beat the baseline by 20% in a 128k-context smoke test or quality degradation exceeds 2% perplexity before scheduler tuning.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-kv-cache-serving-from-cpu-ram-for-long-context-21c250305c6e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
