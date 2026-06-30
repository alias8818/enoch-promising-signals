# Real-logit calibration replay for confidence-thresholded local cascade routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-logit-calibration-replay-for-confidence-thresholded-l-6638298e39`
Run ID: `real-logit-calibration-replay-for-confidence-thresholded-l-6638298e39-20260621T042042275796+0000`

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

- Parent run decision: Confidence-thresholded local cascade router: enoch://control-plane/projects/confidence-thresholded-local-cascade-router-8657fb5a74d6/runs/confidence-thresholded-local-cascade-router-8657fb5a74d6-20260621T035544776196+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5f990dbbbaa

## What looked useful

Temperature calibration reduced test ECE from 0.2929 to 0.0623 and reduced unsafe accepts at threshold 0.90 from 0.2564 to 0.0121, but accepted-local accuracy was only 0.7927, below the required 0.90 threshold.

## Boundaries and scale limits

Not an LLM or production-traffic result; oracle route is represented by labels; replay distribution is controlled synthetic shifted classification; no latency or monetary cost measured.

## Claim scope

Controlled Tier 1 NumPy local-classifier replay with real held-out logits, scalar temperature calibration, and fixed 0.90 confidence-threshold local-or-oracle cascade routing.

## Why it stopped

Direct controlled fixed-threshold replay falsified the stated 0.90 accepted-local accuracy criterion for scalar real-logit temperature calibration; this is an early bounded falsification, not a full production validation.

## Recommended next action

Stop this run as a no-paper useful signal; deepen with a predeclared error/abstention head or vector/classwise calibration test that must reach at least 0.90 accepted-local accuracy at 0.05 or greater coverage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Error-aware calibration replay for fixed-threshold local cascade routing
- Success threshold: Accepted-local accuracy >= 0.90 with local coverage >= 0.05 at a predeclared threshold, while unsafe accept rate is lower than raw max-softmax and calibration error is not worse than scalar temperature.
- Stop condition: Stop negative if no method reaches 0.90 accepted-local accuracy at 0.05 coverage on the controlled replay, or if gains disappear on the natural-language replay.

## Evidence references

- Artifact root: `<local-path>/projects/real-logit-calibration-replay-for-confidence-thresholded-l-6638298e39`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
