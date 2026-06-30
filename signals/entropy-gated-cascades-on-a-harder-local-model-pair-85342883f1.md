# Entropy-gated cascades on a harder local model pair

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-gated-cascades-on-a-harder-local-model-pair-85342883f1`
Run ID: `entropy-gated-cascades-on-a-harder-local-model-pair-85342883f1-20260520T171729907534+0000`

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

- Parent run decision: Entropy-Gated Local Model Cascades: enoch://control-plane/projects/entropy-gated-local-model-cascades-6a4ea0e74d7a/runs/entropy-gated-local-model-cascades-6a4ea0e74d7a-20260520T161922331865+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/964fde533235

## What looked useful

Entropy gating closed about 65.6% of the small-to-strong NLL gap at 59.1% strong-model calls, but the cascade was 3.71% worse than the strong model at that cost point. Staying within 2% relative NLL required more than 80% strong-model calls.

## Boundaries and scale limits

This was a Tier-1 CPU-only n-gram LM validation on 30,000 held-out tokens, not a neural transformer serving benchmark, not a multi-dataset robustness study, and not publication-grade evidence.

## Claim scope

In a controlled local word-level language-model cascade on tiny Shakespeare, a small-model entropy threshold produced a smooth quality/cost tradeoff but did not preserve five-gram-model validation NLL within 2% while using at most 60% strong-model calls.

## Why it stopped

Controlled Tier-1 direct validation failed the predeclared threshold: no swept entropy threshold achieved <=60% strong-model calls with <=2% relative NLL over the strong model.

## Recommended next action

Stop this entropy-only follow-up as a no-paper useful signal; the bounded next test is to compare entropy against calibrated learned or margin-based gates on the same local LM pair.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated gates versus entropy thresholds for local LM cascades
- Success threshold: At least one non-entropy-only gate achieves <=60% strong-model calls with <=2% relative NLL over the strong model on the 30,000-token validation split.
- Stop condition: Stop if all calibrated or margin-based gates exceed 2% relative NLL at <=60% strong-model calls, or if the learned gate only succeeds through validation leakage.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-gated-cascades-on-a-harder-local-model-pair-85342883f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
