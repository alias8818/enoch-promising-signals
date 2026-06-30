# Confidence-Gated Local Model Cascade on Consumer GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-local-model-cascade-on-consumer-gpu-af60613809c1`
Run ID: `confidence-gated-local-model-cascade-on-consumer-gpu-af60613809c1-20260614T122522048407+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d3101b0c3e95

## What looked useful

Full SST-2 validation run found threshold 0.999 matched RoBERTa-only accuracy at 0.9404 with 38.5% fallback rate and estimated 0.812 ms/example versus 0.884 ms/example fallback-only. Lower thresholds were faster but lost accuracy; stricter threshold 0.9995 matched accuracy but became slower than fallback-only.

## Boundaries and scale limits

Classifier-only proxy, one public sentiment task, one model pair, batch-size 32, estimated sequential cascade latency from separate model timings rather than integrated production serving; not evidence for broad generative LLM cascades.

## Claim scope

On GLUE SST-2 validation using local CUDA inference on GB10, a DistilBERT first stage with a strict confidence threshold can match a RoBERTa fallback classifier's aggregate accuracy while reducing estimated sequential fallback-only latency by about 8.9%.

## Why it stopped

Proxy classifier evidence is useful but insufficient for a paper-level confidence-gated local LLM cascade claim; the result should not be presented as full validation.

## Recommended next action

Stop this run as no-paper useful signal; deepen with an integrated local generative-model cascade benchmark that measures actual wall-clock quality/latency with both models resident on GB10.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated GB10 Generative Cascade Wall-Clock Benchmark
- Success threshold: At least 15% end-to-end latency reduction versus fallback-only with no statistically meaningful quality drop on the selected benchmark and no unsafe memory pressure on swapless GB10.
- Stop condition: Stop if the integrated cascade cannot keep both models resident safely, if fallback-only is faster at quality-preserving thresholds, or if quality drops by more than the predefined tolerance.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-local-model-cascade-on-consumer-gpu-af60613809c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
