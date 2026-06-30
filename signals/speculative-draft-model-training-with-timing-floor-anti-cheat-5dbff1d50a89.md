# Speculative Draft Model Training with Timing-Floor Anti-Cheat

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `speculative-draft-model-training-with-timing-floor-anti-cheat-5dbff1d50a89`
Run ID: `speculative-draft-model-training-with-timing-floor-anti-cheat-5dbff1d50a89-20260610T230849650313+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e509d1003508

## What looked useful

Raw timing produced train timing AUC 0.9976, same-timing accuracy 0.9790, randomized-timing accuracy 0.5063, and inverted-timing accuracy 0.0374. A q=0.995 timing floor reduced train timing AUC to 0.5050 and kept randomized/inverted accuracy near 0.66. Adding independent jitter reduced learned timing weight from 0.2713 to 0.0508. Lower floors q=0.90 and q=0.95 left measurable residual timing leakage.

## Boundaries and scale limits

Synthetic binary accept/reject data, logistic draft policy, CPU-only short runs, no real LLM draft model, no real verifier traces, no throughput or acceptance-rate measurement.

## Claim scope

In a synthetic draft accept/reject training proxy, raw label-correlated latency creates a shortcut that fails under timing perturbation, while a high timing floor removes most timing-decodable label signal and preserves content-only counterfactual accuracy.

## Why it stopped

No-paper useful signal: the mechanism is supported only in a synthetic proxy, not by direct full draft-model training or real speculative decoding throughput evidence.

## Recommended next action

Run a bounded deepen follow-up using a tiny real transformer draft model and measured verifier traces to test whether the timing-floor mechanism survives realistic token and latency distributions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Speculative Draft Training with Measured Timing-Floor Anti-Cheat
- Success threshold: Timing-floor training should reduce timing-label AUC to <=0.53, keep counterfactual acceptance/quality within 2 percentage points of dropped-timing training, and outperform raw-timing training by at least 10 percentage points under inverted or randomized timing.
- Stop condition: Stop if raw timing does not create a measurable shortcut on real traces, or if timing-floor training cannot suppress timing-label AUC below 0.57 without unacceptable throughput or quality loss.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-draft-model-training-with-timing-floor-anti-cheat-5dbff1d50a89`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
