# Anchor-Conditioned Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-conditioned-speculative-decoding-5d6d618fee66`
Run ID: `anchor-conditioned-speculative-decoding-5d6d618fee66-20260529T173211064089+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a781bc0ef3e5

## What looked useful

Oracle anchor conditioning raised adjusted speed proxy from 2.516x to 5.129x and full-block acceptance from 8.4% to 67.1%. The benefit degraded with noisy anchors: 40% accuracy remained 8.3% above baseline, 35% was approximately break-even, and 30% was 7.2% below baseline.

## Boundaries and scale limits

Synthetic categorical process only; no transformer target, no trained anchor predictor, no natural-language corpus, no KV-cache or wall-clock serving measurement. Results are a mechanism and threshold proxy, not full LM validation.

## Claim scope

In a controlled synthetic target process with exact probabilities, an anchor-conditioned draft improves speculative-decoding acceptance when the anchor predictor is sufficiently accurate and the baseline drafter partially ignores the anchor signal.

## Why it stopped

Stopped as a no-paper useful-signal result because the evidence is synthetic/proxy and establishes a mechanism plus failure threshold, not publication-grade real-model performance.

## Recommended next action

Run a bounded real-LM deepen test using a small target/draft pair with an explicit anchor predictor, measuring acceptance, exact-output verification correctness, and wall-clock latency against standard speculative decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM Anchor Predictor Threshold for Speculative Decoding
- Success threshold: Anchor-conditioned decoding must improve measured wall-clock tokens/sec by at least 10% over standard speculative decoding at equal output distribution correctness, with confidence intervals over prompts and seeds.
- Stop condition: Stop if predictor accuracy is below the measured break-even threshold or if anchor overhead removes the acceptance gain on two independent prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-conditioned-speculative-decoding-5d6d618fee66`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
