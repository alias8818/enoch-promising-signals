# Volunteer Training Gradient Verification via Sampling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-training-gradient-verification-via-sampling-136920969d26`
Run ID: `volunteer-training-gradient-verification-via-sampling-136920969d26-20260605T061350823701+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e8e619eb5e79

## What looked useful

Random coordinate recomputation is a practical cheap guardrail for dense or moderately sparse incorrect gradients, but it is not a complete verifier for sparse tampering unless sample sizes rise with the inverse tamper fraction or another orthogonal check is added.

## Boundaries and scale limits

No transformer-scale training, no real volunteer network, no adaptive pre-sampling adversary, no non-IID volunteer data, no cryptographic commitment layer, and no multi-step training dynamics were tested.

## Claim scope

In a synthetic logistic-regression verifier-batch probe with 4,096 parameters and 2,048 examples, random coordinate gradient verification caught dense volunteer gradient corruptions with k=32 sampled coordinates and no honest false positives, but detection of 1% sparse tampering followed coordinate-hit probability and required k=256 for about 93.5% detection.

## Why it stopped

Bounded synthetic evidence supports the mechanism for dense errors but also exposes a predictable sparse-tamper weakness; this is useful but not sufficient for a publication-grade claim.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded work should test the same verifier inside a multi-step toy volunteer-training loop with hidden per-step samples and adaptive sparse adversaries.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-step hidden-sample verifier against adaptive sparse volunteer gradients
- Success threshold: At verifier recomputation fraction <=5%, detect dense and 5% sparse corruptions within 3 training steps in >=95% of runs, maintain honest false-positive rate <=1%, and quantify any undetected 1% sparse attack impact on validation loss.
- Stop condition: Stop if hidden sampling cannot keep honest false positives <=1%, or if 5% sparse corruption detection remains below 90% within 3 steps at <=5% recomputation.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-training-gradient-verification-via-sampling-136920969d26`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
