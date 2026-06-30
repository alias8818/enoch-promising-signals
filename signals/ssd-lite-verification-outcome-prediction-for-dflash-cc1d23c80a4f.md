# SSD-lite Verification-Outcome Prediction for DFlash

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `ssd-lite-verification-outcome-prediction-for-dflash-cc1d23c80a4f`
Run ID: `ssd-lite-verification-outcome-prediction-for-dflash-cc1d23c80a4f-20260519T231446393478+0000`

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

- ChatGPT Pro speculative decoding research map 2026-05-19: file://new-chatgpt-pro-ideas-05-19.md
- Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals: file://new-chatgpt-pro-ideas-05-19.md

## What looked useful

Main run: SSD-lite AUC 0.9564, AP 0.8605, Brier 0.0711, best-F1 0.8051 on 7,200 held-out token labels; draft-probability baseline AUC 0.8366, AP 0.6425, Brier 0.1368, best-F1 0.6514. Five robustness seeds gave mean SSD-lite AUC 0.9564 versus 0.8342 for draft probability.

## Boundaries and scale limits

Evidence is from n-gram target and block drafter models on Tiny Shakespeare, not from neural DFlash, target-layer hidden states, GPU serving, or production latency measurements.

## Claim scope

In a reproducible word-level DFlash-lite proxy, a tiny logistic SSD-lite predictor using pre-verification block/draft features predicts speculative verification accept/reject outcomes substantially better than draft confidence alone.

## Why it stopped

Closed as no-paper useful signal: the proxy supports the mechanism, but real DFlash traces and intervention latency/quality measurements are required before any paper-positive claim.

## Recommended next action

Run a direct DFlash trace study using real neural draft blocks and target verifier outcomes, then test whether SSD-lite can safely drive adaptive draft length or early-stop policies without violating exactness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SSD-lite outcome prediction on real DFlash verification traces
- Success threshold: SSD-lite improves AUC by at least 0.05 and best-F1 by at least 0.08 over draft-confidence on real DFlash traces, and an adaptive policy improves latency or target calls by at least 5% without reducing exact-match verification correctness.
- Stop condition: Stop if real DFlash trace AUC gain is under 0.02 over draft confidence or if adaptive decisions cannot preserve exactness/quality under a clearly specified acceptance policy.

## Evidence references

- Artifact root: `<local-path>/projects/ssd-lite-verification-outcome-prediction-for-dflash-cc1d23c80a4f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
