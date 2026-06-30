# INT2 KV Cache + Per-Head FP16 Residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-kv-cache-per-head-fp16-residual-ffb39a4ead0c`
Run ID: `int2-kv-cache-per-head-fp16-residual-ffb39a4ead0c-20260629T162915535699+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8d925090100d

## What looked useful

Per-head FP16 residual channels reduced mean output relative L2 from 1.233 at INT2-only to 0.794 at 25% residual channels and improved attention top-1 agreement from 0.313 to 0.445, but this is still too inaccurate while compression drops from 7.88x to 2.65x.

## Boundaries and scale limits

No CUDA/GPU path was available; no real model KV traces, perplexity, task accuracy, packed INT2 kernel, or serving throughput was measured. Largest tested synthetic case was 16 heads x 1024 tokens x 64 dim with 16 queries across three seeds.

## Claim scope

CPU synthetic proxy: INT2 per-head/per-channel quantized K/V tensors with exact FP16 residual channels selected per head by quantization residual energy improve attention reconstruction monotonically but remain high-error on tested shapes.

## Why it stopped

Proxy/early falsification: the tested per-head FP16 residual-channel mechanism improves synthetic attention metrics but remains far from acceptable fidelity, so it is not ready for paper or GPU-serving validation as-is.

## Recommended next action

Stop this design as no-paper proxy evidence; if continuing, run a bounded real-model KV-trace follow-up comparing INT2 plus residual against INT4/FP8 and recent-token residual baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace test for INT2 residual cache variants
- Success threshold: At least 3x compression versus FP16 with mean output relative L2 <= 0.15, attention top-1 agreement >= 0.90, and no worse than INT4/FP8 baselines on the same traces.
- Stop condition: Stop if all INT2 residual variants fail to reach output relative L2 <= 0.25 or top-1 agreement >= 0.80 at >= 3x compression on real traces.

## Evidence references

- Artifact root: `<local-path>/projects/int2-kv-cache-per-head-fp16-residual-ffb39a4ead0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
