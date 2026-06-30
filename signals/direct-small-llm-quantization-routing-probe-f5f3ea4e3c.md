# Direct Small-LLM Quantization Routing Probe

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `direct-small-llm-quantization-routing-probe-f5f3ea4e3c`
Run ID: `direct-small-llm-quantization-routing-probe-f5f3ea4e3c-20260528T014313347976+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Per-Request Quantization Routing in Local Cascades: enoch://control-plane/projects/per-request-quantization-routing-in-local-cascades-5b7e63315676/runs/per-request-quantization-routing-in-local-cascades-5b7e63315676-20260527T220523347327+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3731a45b2210

## What looked useful

Dynamic int8 was 2.08x faster than FP32 on the timing subset and added 0.03428 NLL, but the entropy router recovered only 15.8% of that gap and was worse than same-budget random routing by 0.00439 NLL.

## Boundaries and scale limits

Single small causal LM, one dataset, 48 calibration sequences, 96 held-out eval sequences, CPU qnnpack dynamic int8, per-sequence routing, and mixed throughput estimated from separate FP32/int8 timing rather than a production router.

## Claim scope

On OPT-125M with PyTorch qnnpack dynamic int8 and WikiText-2 held-out likelihoods, a calibration-threshold router using quantized-model mean token entropy does not recover enough quantization harm to justify routing 30% of samples to FP32.

## Why it stopped

Tier 1 direct small-LM test failed the stated routing threshold: at 30% FP routing it recovered 15.8% of quantization loss instead of at least 50% and did not beat random same-budget routing.

## Recommended next action

Stop this entropy-router path as an early direct falsification; the only bounded next step worth running is a supervised quantization-harm router with an oracle ceiling and the same held-out controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Supervised Quantization-Harm Router With Oracle Ceiling
- Success threshold: Recover >=50% of the quantization-induced NLL gap at <=30% FP32 route fraction, beat random same-budget routing, reach at least 70% of the oracle top-harm route recovery, and preserve measured end-to-end speedup versus all-FP32.
- Stop condition: Stop if the oracle top-harm ceiling cannot recover >=50% of the gap at 30% FP routing, or if a cross-validated quantized-only supervised router fails to beat random routing on held-out data.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-llm-quantization-routing-probe-f5f3ea4e3c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
