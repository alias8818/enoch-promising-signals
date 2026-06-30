# Adaptive Cascade Router for Local Model Serving

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `adaptive-cascade-router-for-local-model-serving-26fdd3f69f67`
Run ID: `adaptive-cascade-router-for-local-model-serving-26fdd3f69f67-20260609T155926764666+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/31c16d638a15

## What looked useful

Adaptive thresholds improved over static calibration by 2.44 quality points but still missed target by 8.03 points and were slightly slower than always-large; an oracle cheapest-correct router showed exploitable structure remains.

## Boundaries and scale limits

Synthetic model correctness, confidence, and latency only; no real LLM prompts, evaluator, batching, concurrency, KV-cache behavior, GPU utilization, or production serving stack was tested.

## Claim scope

On a synthetic three-tier local-serving trace with drift, a simple delayed-audit adaptive confidence-threshold cascade failed to meet a 0.65 quality target and did not reduce latency versus always using the largest tier.

## Why it stopped

Proxy confirmation falsified the tested adaptive-threshold mechanism rather than providing full validation of local LLM routing.

## Recommended next action

Stop this run as no-paper evidence; run a bounded deepen follow-up that replaces threshold tuning with a learned correctness/escalation predictor on held-out drift traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Correctness Predictor for Drifted Local Cascade Routing
- Success threshold: Meet or exceed 0.65 quality with mean latency at least 5% below always-large and no phase-level target miss larger than always-large by more than 2 percentage points.
- Stop condition: Stop if the learned predictor misses overall target quality by more than 2 percentage points or has mean latency no better than always-large across held-out seeds.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-cascade-router-for-local-model-serving-26fdd3f69f67`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
