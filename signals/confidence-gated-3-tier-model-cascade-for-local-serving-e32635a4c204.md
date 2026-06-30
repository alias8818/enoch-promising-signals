# Confidence-Gated 3-Tier Model Cascade for Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-3-tier-model-cascade-for-local-serving-e32635a4c204`
Run ID: `confidence-gated-3-tier-model-cascade-for-local-serving-e32635a4c204-20260524T232634349713+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/cd361cc01529

## What looked useful

Confidence gating reduced measured latency versus always running the largest tier when most examples exited early, but it failed the stronger practical control: in both full synthetic runs, always using the cheap tier was faster and at least as accurate as the selected cascade. Estimated route-cost speedups also overstated actual sequential speedups because gating overhead was material.

## Boundaries and scale limits

Not an LLM or production serving validation. The benchmark omits real token generation, KV-cache behavior, batching, quantization, model residency pressure, request distribution shift, and production scheduler overhead. Synthetic tiers did not provide a clean monotonic quality ladder in the stress setting.

## Claim scope

Self-contained PyTorch synthetic multiclass local-serving proxy with three neural tiers, confidence threshold routing, calibration-split threshold selection, held-out test evaluation, and measured batch-1 CUDA sequential cascade latency on GB10.

## Why it stopped

Early proxy result is mixed and not paper-ready: the cascade beats always-largest latency but does not beat the best cheap single-tier baseline, so it does not support the practical local-serving hypothesis as tested.

## Recommended next action

Stop this run as no-paper useful signal; run one bounded real-local-LM follow-up that requires the cascade to beat both always-largest and the best single smaller model on the same quality-latency Pareto target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Local-LM Confidence Cascade With Pareto Single-Tier Control
- Success threshold: At no more than 1 percentage point quality loss versus always-largest, the cascade must deliver at least 1.5x measured end-to-end latency speedup and must be Pareto-superior to every single-tier baseline at the same quality target.
- Stop condition: Stop negative if the cascade fails to beat the best single-tier baseline under the quality target, if confidence does not separate correct from incorrect lower-tier outputs, or if routing/model-residency overhead erases the always-largest speedup.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-3-tier-model-cascade-for-local-serving-e32635a4c204`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
