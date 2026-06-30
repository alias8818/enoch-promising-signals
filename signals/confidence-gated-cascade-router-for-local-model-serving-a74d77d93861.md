# Confidence-Gated Cascade Router for Local Model Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-cascade-router-for-local-model-serving-a74d77d93861`
Run ID: `confidence-gated-cascade-router-for-local-model-serving-a74d77d93861-20260523T040934483904+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2d6e729e5612

## What looked useful

Across four proxy configurations, confidence routing beat random routing at matched strong-call rates. Under a strict within-0.5pp validation target, savings ranged from 1.7% to 47.3%; the best case retained 96.94% accuracy versus 97.50% strong-only while escalating 51.67% of requests.

## Boundaries and scale limits

No local LLMs, token generation, KV-cache behavior, batching, concurrency, GPU residency, model-server queueing, or real production request traces were tested. Serving cost is estimated from single-process sklearn prediction latency.

## Claim scope

In small sklearn classification proxies, confidence-gated cascades can beat random routing at the same escalation rate and can materially reduce estimated serving cost when the cheap model is moderately competent; strict strong-model accuracy targets provide little savings when the cheap model is weak.

## Why it stopped

Proxy evidence supports the mechanism but does not directly validate local LLM serving behavior or server-level cost/quality tradeoffs.

## Recommended next action

Stop this run as no-paper useful signal; deepen with actual local LLM serving traces and confidence metrics before making any publication claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-Gated Cascade on Actual Local LLM Serving Traces
- Success threshold: At least 25% fewer strong-model calls than strong-only with accuracy within 1 percentage point of strong-only and statistically better than random routing at the same strong-call rate.
- Stop condition: Stop if no confidence signal beats random routing at matched strong-call rate or if maintaining the accuracy target requires more than 90% strong-model calls on all tested tasks.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-cascade-router-for-local-model-serving-a74d77d93861`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
