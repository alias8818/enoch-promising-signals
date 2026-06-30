# GPT-2-small-class ternary draft speculative decoding validation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gpt-2-small-class-ternary-draft-speculative-decoding-valid-2212a045c9`
Run ID: `gpt-2-small-class-ternary-draft-speculative-decoding-valid-2212a045c9-20260603T140922124540+0000`

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

- Parent run decision: 1.58-bit Draft Model for Speculative Decoding: enoch://control-plane/projects/1-58-bit-draft-model-for-speculative-decoding-6cd3a30fdb76/runs/1-58-bit-draft-model-for-speculative-decoding-6cd3a30fdb76-20260602T182701493241+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/878afbbb9b2b

## What looked useful

Naive post-training ternarization of GPT-2 block projections produced only 4.0% proposal acceptance and 1.04 generated tokens per target forward call, while dense self-draft control reached 100% acceptance and 4.57 generated tokens per target call.

## Boundaries and scale limits

Small direct CUDA run only: 24 prompts, 768 generated tokens per variant, gamma 4, top-k 50, temperature 0.8. No trained ternary draft, optimized ternary kernel, corpus-scale robustness, or long-context serving evaluation.

## Claim scope

A GPT-2-small target using a post-training ternarized Conv1D-copy draft, with dense embeddings and LM head, does not meet Tier 1 speculative-decoding mechanism thresholds on 24 short prompts.

## Why it stopped

Early direct falsification of the naive post-training ternary draft threshold, not a full validation or full impossibility result for trained ternary drafts.

## Recommended next action

Stop this no-paper run; a bounded deepen follow-up should train or distill a ternary GPT-2-small-class draft before retesting the same acceptance threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distilled ternary GPT-2 draft acceptance test
- Success threshold: Acceptance rate >= 0.45 and generated tokens per target forward call >= 1.30, with KL substantially below the post-training ternary result and no regression in exact speculative-decoding validity.
- Stop condition: Stop if trained/distilled ternary draft acceptance remains below 0.25 after a bounded local training budget or if validation KL remains near the post-training ternary baseline.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-ternary-draft-speculative-decoding-valid-2212a045c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
