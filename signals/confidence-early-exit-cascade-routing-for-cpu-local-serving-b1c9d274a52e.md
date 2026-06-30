# Confidence-early-exit cascade routing for CPU local serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-early-exit-cascade-routing-for-cpu-local-serving-b1c9d274a52e`
Run ID: `confidence-early-exit-cascade-routing-for-cpu-local-serving-b1c9d274a52e-20260527T170401064199+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ba419e89fff0

## What looked useful

Centroid early exit failed because the cheap stage was too inaccurate, but a stronger cheap subset-kNN stage showed a repeatable speed/accuracy tradeoff. The strict predeclared rule of >=1.25x speedup with <=1 percentage point accuracy loss held on 3/5 random splits; at fixed threshold 0.61 all five splits achieved >=1.54x speedup and stayed within 1.25 percentage points accuracy loss.

## Boundaries and scale limits

This is a bounded CPU classification proxy, not local LLM serving. It uses one UCI dataset, simple exact-kNN models, measured single-request predictor latency composed into an estimated cascade latency, and no production server, batching, token generation, neural confidence, or multi-dataset validation.

## Claim scope

On UCI Letter Recognition with CPU single-request exact-kNN classification, a confidence early-exit cascade using a 2,000-example cheap kNN index and full 12,000-example kNN fallback can skip about 59% of fallback calls and produce about 1.58x estimated mean latency speedup at threshold 0.61, with mean accuracy loss under 1 percentage point across five splits but one split reaching 1.2 percentage points loss.

## Why it stopped

No-paper useful signal: the bounded proxy supports the mechanism but strict robustness is mixed and the experiment does not directly test local LLM serving or an end-to-end server.

## Recommended next action

Run a bounded deepen follow-up with validation-calibrated confidence thresholds on at least three datasets or local text-classification serving tasks, requiring the strict <=1 percentage point accuracy-loss rule to hold on every split before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validation-calibrated confidence cascades across multiple CPU serving tasks
- Success threshold: Every task/split must achieve >=1.25x measured mean latency speedup versus always-fallback with <=1 percentage point absolute accuracy loss, and no task may rely on a threshold chosen on the test set.
- Stop condition: Stop as negative if fewer than two tasks meet the speed/accuracy threshold or if validation-selected thresholds exceed 1 percentage point test accuracy loss on any task.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-early-exit-cascade-routing-for-cpu-local-serving-b1c9d274a52e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
