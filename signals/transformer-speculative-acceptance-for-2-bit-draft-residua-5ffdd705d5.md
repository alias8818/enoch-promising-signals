# Transformer Speculative Acceptance for 2-Bit Draft Residual Correction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `transformer-speculative-acceptance-for-2-bit-draft-residua-5ffdd705d5`
Run ID: `transformer-speculative-acceptance-for-2-bit-draft-residua-5ffdd705d5-20260605T040034388380+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Tiny 2-Bit Draft with Residual Logit Correction: enoch://control-plane/projects/tiny-2-bit-draft-with-residual-logit-correction-6f3f48822d24/runs/tiny-2-bit-draft-with-residual-logit-correction-6f3f48822d24-20260604T232815214164+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/bc4eb80e5e73

## What looked useful

2-bit residual correction improved expected acceptance over an uncorrected draft by +0.1818 to +0.4368 absolute and captured about 59-62% of the 4-bit correction gain. Shuffled 2-bit residuals also helped but less, so aligned residual information matters while same-family residual statistics may contribute.

## Boundaries and scale limits

Randomly initialized transformer-shaped model, byte-token local prompt stream, oracle residual h_target - h_draft, no learned residual predictor, no pretrained LM, no multi-token decode throughput measurement, and no GPU or serving-scale validation.

## Claim scope

In a NumPy controlled transformer-style causal attention stack, oracle aligned 2-bit hidden residual correction from a shallow draft state toward the full target state substantially improved exact expected one-token speculative acceptance across five seeds and four logit scales.

## Why it stopped

Tier 1 controlled mechanism test succeeded, but the residual was oracle-derived and the model was untrained, so the result is useful no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen test with a trained compact GPT-style target/draft pair and a target-free 2-bit residual predictor, measuring acceptance and decode wall-clock against uncorrected speculative decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned 2-bit residual predictor for compact GPT speculative decoding
- Success threshold: Learned 2-bit residual improves expected acceptance by at least +0.05 absolute over uncorrected draft, captures at least 50% of the oracle 2-bit gain, beats shuffled residual control, and does not reduce measured speculative decode throughput below the uncorrected draft baseline.
- Stop condition: Stop as unsupported if the learned 2-bit predictor fails to beat uncorrected acceptance by +0.05, fails to beat shuffled residual control, or erases decode speedup in the compact trained setting.

## Evidence references

- Artifact root: `<local-path>/projects/transformer-speculative-acceptance-for-2-bit-draft-residua-5ffdd705d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
