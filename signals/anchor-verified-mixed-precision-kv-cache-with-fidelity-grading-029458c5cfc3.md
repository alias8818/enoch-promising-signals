# Anchor-Verified Mixed-Precision KV Cache with Fidelity Grading

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-verified-mixed-precision-kv-cache-with-fidelity-grading-029458c5cfc3`
Run ID: `anchor-verified-mixed-precision-kv-cache-with-fidelity-grading-029458c5cfc3-20260522T181051388232+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c41e0693cce5

## What looked useful

Adaptive fidelity grading was useful: on the long suite it selected int4/no-anchor, anchored int4, or int8 fallback candidates with 1.0 top-1 agreement, 6 B and 2 C grades, and mean estimated KV memory ratio 0.3678. The anchor mechanism was mixed: anchored variants helped some cases but did not consistently beat int4 no-anchor. Int2 was clearly non-viable under the grade threshold.

## Boundaries and scale limits

No packed cache kernel, no measured decode throughput or bandwidth, oracle attention used for attention-top anchors, small fixed prompt suite, one GPT-2-family model, next-token-only evaluation, and analytical rather than allocated compressed-cache memory estimates.

## Claim scope

On locally cached distilgpt2 with fp16 CUDA execution, synthetic quantize-dequantized KV caches, and 8 long plus 16 short prompts, fidelity grading can select mixed int4/int8 cache candidates that preserve long-suite top-1 agreement with an estimated 0.368 KV memory ratio, but full-precision anchor restoration alone is not a consistently reliable fidelity rescue.

## Why it stopped

No-paper useful signal: local evidence supports fidelity grading as a practical guardrail but does not support a publication-grade claim for anchor-verified mixed-precision KV caches.

## Recommended next action

Run a bounded deepen test with a non-oracle anchor predictor and a real packed int4/int8 KV cache path that measures decode throughput, bandwidth, and fidelity on GPT-2-small or a similarly available larger decoder.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle packed KV cache fidelity and throughput validation
- Success threshold: At least 0.98 top-1 agreement, reference token in candidate top-5 at least 0.995, p95 KL <= 0.02, and a measured throughput or bandwidth improvement over fp16 cache at comparable batch/context settings.
- Stop condition: Stop if non-oracle anchored int4 plus fallback fails to beat int8-only fidelity or fails to produce any measured throughput/bandwidth gain over fp16 packed-cache baseline.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-verified-mixed-precision-kv-cache-with-fidelity-grading-029458c5cfc3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
