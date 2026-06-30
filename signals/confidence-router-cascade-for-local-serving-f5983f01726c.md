# Confidence Router Cascade for Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-router-cascade-for-local-serving-f5983f01726c`
Run ID: `confidence-router-cascade-for-local-serving-f5983f01726c-20260525T234651418978+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b4b0386b97fe

## What looked useful

Five-seed means: digits matched strong-model accuracy with 87.3% cheap-served and 8.45x estimated mean-latency speedup; wine matched strong accuracy with 99.6% cheap-served but mostly collapsed to all-cheap; breast_cancer averaged -0.234 percentage-point accuracy delta with 74.4% cheap-served and 35.83x speedup, but thresholds were unstable. The mechanism is promising only when calibration finds a high-coverage, high-precision cheap-served subset.

## Boundaries and scale limits

Evidence is limited to toy/medium tabular and digit classification datasets, local CPU predict_proba latency, one cheap linear model, one random-forest strong model, and five train/calibration/test seeds. It does not directly validate LLM local serving, token-level confidence, request batching, queueing, or semantic answer quality.

## Claim scope

On three small local scikit-learn classification tasks, a max-probability confidence router sometimes preserved always-strong accuracy while reducing estimated CPU inference latency, but it also degenerated to all-cheap or all-strong policies depending on calibration and dataset.

## Why it stopped

The result is a small local proxy with mixed behavior and explicit failure modes, not a publication-grade validation of confidence-router cascades for local LLM serving.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded direct local-LLM follow-up with real prompts, cheap/strong local models, confidence features, quality labels, and end-to-end latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Local LLM Confidence Router with Prompt-Level Quality Labels
- Success threshold: On held-out prompts, reduce strong-model calls by at least 30% and mean end-to-end latency by at least 20% while keeping answer quality within 1 percentage point of always-strong.
- Stop condition: Stop as negative if calibrated routing saves under 20% mean latency, reduces strong calls under 30%, or loses more than 1 percentage point quality on held-out prompts.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-router-cascade-for-local-serving-f5983f01726c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
