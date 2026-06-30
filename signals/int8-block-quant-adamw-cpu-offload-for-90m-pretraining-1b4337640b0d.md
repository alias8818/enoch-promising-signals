# INT8 Block-Quant AdamW CPU-Offload for 90M Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-block-quant-adamw-cpu-offload-for-90m-pretraining-1b4337640b0d`
Run ID: `int8-block-quant-adamw-cpu-offload-for-90m-pretraining-1b4337640b0d-20260604T061826818190+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e7d4d3256a42

## What looked useful

INT8 block quantization gave about 4x optimizer-state reduction at 90M parameters: 686.65 MiB to 172.33 MiB in the optimizer-only benchmark, and 696.79 MiB to 174.88 MiB in the GPT-style benchmark. Peak GPU memory fell from 1855.25 MiB to 1055.46 MiB in the 91.3M GPT-style run. Warm optimizer time increased from 0.0353 s to 0.1550 s, and warm total step time increased from 0.0604 s to 0.1802 s. A 1M-parameter 100-step drift check showed about 0.10 parameter relative RMSE and max absolute parameter difference about 1.15 versus fp32 AdamW.

## Boundaries and scale limits

Evidence is synthetic and local: 90M optimizer-step benchmark, 91.3M GPT-style random-token three-step throughput benchmark, and 1M-parameter 100-step drift check. It is not a real corpus convergence run, not multi-seed, and not a publication-grade optimizer study.

## Claim scope

On this GB10 worker, a naive CPU-resident INT8 block-quantized AdamW prototype for a 90M-class GPT-style synthetic pretraining step reduces optimizer-state and peak GPU memory substantially, but it slows the optimizer step and fails a fixed-gradient numerical drift check because quantized second-moment values can dequantize near zero.

## Why it stopped

Proxy and direct local tests found useful memory savings but early numerical falsification for naive INT8 block-quantized AdamW state; this is not a full validation, and the observed drift is enough to avoid scaling this exact variant.

## Recommended next action

Stop this naive signed-INT8 m/v CPU-offload variant as no-paper evidence; the next bounded test should replace second-moment quantization with a positive-domain or floor-clamped representation before any longer pretraining run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Positive-domain second-moment quantization for CPU-offloaded AdamW
- Success threshold: At least 2x optimizer-state memory reduction versus fp32 AdamW, no more than 3x warm optimizer-step slowdown in the 90M GPT-style benchmark, and parameter relative RMSE below 1e-3 after 100 fixed-gradient AdamW steps.
- Stop condition: Stop if the corrected second-moment representation still exceeds 1e-2 parameter relative RMSE after 100 steps or makes warm total step time more than 4x slower than GPU AdamW at 90M-class scale.

## Evidence references

- Artifact root: `<local-path>/projects/int8-block-quant-adamw-cpu-offload-for-90m-pretraining-1b4337640b0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
