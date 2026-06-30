# Implementation Gap: INT3 Quantization with Channel-wise Scaling Factors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `implementation-gap-int3-quantization-with-channel-wise-scaling-factors-25502e0ac67b`
Run ID: `implementation-gap-int3-quantization-with-channel-wise-scaling-factors-25502e0ac67b-20260605T115734463495+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/870c2e23d256

## What looked useful

INT3 channel-wise scaling reduced reconstruction error compared with tensor-wise INT3 and averaged -1.43 accuracy points versus FP32 across three stable seeds, while INT4 averaged -0.28 points. INT3 channel-wise storage with FP16 scales was 9.44% of FP32 and 75.14% of INT4 channel-wise storage. Signed INT3 packing roundtripped exactly.

## Boundaries and scale limits

Small 784-128-10 MLP on 10,000 MNIST training samples and 2,000 test samples; dequantized FP32 inference; no transformer, activation quantization, quantization-aware training, or fused INT3 kernel benchmark.

## Claim scope

A NumPy-only bounded post-training probe shows signed INT3 weight quantization with per-output-channel scaling can be implemented exactly at the packing layer and can preserve a small MNIST MLP within 0 to 3.5 accuracy points of FP32, but it is consistently higher-error than INT4 for only a 25% packed-weight storage reduction versus INT4.

## Why it stopped

Proxy/local evidence only: the implementation is feasible, but the small-task tradeoff versus INT4 is not strong enough for a paper without direct transformer and kernel evidence.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should evaluate INT3 channel-wise post-training quantization on a pretrained transformer with an INT4 control before investing in specialized INT3 kernels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: INT3 channel-wise post-training quantization on a pretrained transformer
- Success threshold: INT3 channel-wise must stay within 5% relative perplexity degradation of INT4 channel-wise while preserving the expected 25% packed-weight storage reduction versus INT4.
- Stop condition: Stop if INT3 channel-wise exceeds 10% relative perplexity degradation versus INT4 or if only dequantized inference is available and no storage/bandwidth argument distinguishes it from INT4.

## Evidence references

- Artifact root: `<local-path>/projects/implementation-gap-int3-quantization-with-channel-wise-scaling-factors-25502e0ac67b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
