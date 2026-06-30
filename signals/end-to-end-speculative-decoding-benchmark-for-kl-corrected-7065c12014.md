# End-to-end speculative decoding benchmark for KL-corrected layer-skipped drafts

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `end-to-end-speculative-decoding-benchmark-for-kl-corrected-7065c12014`
Run ID: `end-to-end-speculative-decoding-benchmark-for-kl-corrected-7065c12014-20260527T162615054855+0000`

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

- Parent run decision: Layer-Skipped Speculative Drafting with Residual Correction: enoch://control-plane/projects/layer-skipped-speculative-drafting-with-residual-correction-1b1160a49b41/runs/layer-skipped-speculative-drafting-with-residual-correction-1b1160a49b41-20260527T133743337710+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6b0b50c36b43

## What looked useful

Scalar KL-temperature correction reduced calibration KL but held-out draft acceptance stayed low (about 4.8% in the primary n_layer=6 gamma=4 run; 5.0-10.5% across the main ablation), so target forward-call reductions of 9.4-21.9% did not overcome draft overhead. All ablated configurations were slower than target-only decoding; best speedup was 0.655x.

## Boundaries and scale limits

Small Tier 1 direct test only: GPT-2 small, short prompts, short generations, no optimized paged KV cache, no learned correction head, no batched serving, and no large-model validation.

## Claim scope

On GPT-2 small with exact speculative sampling, 8 held-out prompts, 128 generated tokens per condition, top-k sampling, and scalar KL-temperature correction, layer-skipped same-model drafts did not improve end-to-end throughput over target-only decoding.

## Why it stopped

Controlled small direct benchmark falsified the local speedup threshold rather than merely proxying it: primary speedup was 0.407x and the best ablation point was 0.655x versus target-only decoding.

## Recommended next action

Stop this run as a no-paper useful negative result; a bounded deepen follow-up should test whether a learned lightweight correction head plus KV-aware implementation can raise acceptance above 50% and exceed 1.1x throughput on the same GPT-2-small harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned correction head for layer-skipped speculative drafts
- Success threshold: On GPT-2-small held-out prompts, learned correction must achieve at least 50% draft-token acceptance and at least 1.1x wall-clock tokens/sec versus target-only decoding while preserving exact speculative sampling.
- Stop condition: Stop if learned correction remains below 25% acceptance or below 1.0x throughput after one bounded training/calibration attempt and a gamma/depth sweep.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-speculative-decoding-benchmark-for-kl-corrected-7065c12014`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
