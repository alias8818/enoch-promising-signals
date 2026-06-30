# Non-oracle anchor selection for dual-resolution memory on a small language-memory task

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `non-oracle-anchor-selection-for-dual-resolution-memory-on-f2f015adbc`
Run ID: `non-oracle-anchor-selection-for-dual-resolution-memory-on-f2f015adbc-20260526T224821224272+0000`

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

- Parent run decision: Dual-Resolution Memory with Exact Anchor Bank: enoch://control-plane/projects/dual-resolution-memory-with-exact-anchor-bank-f00a8134b242/runs/dual-resolution-memory-with-exact-anchor-bank-f00a8134b242-20260525T033811119411+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/94d9ebb9dd35

## What looked useful

Across 1000 episodes, salience_nonoracle exact accuracy was 0.5248 versus random 0.2506 in salience_aligned demand, but only 0.2548 versus random 0.2508 under uniform demand and 0.1350 versus random 0.2494 under anti-salience demand. The effect depends on salience-query alignment.

## Boundaries and scale limits

Synthetic data only; deterministic selector only; no learned model, transformer integration, naturalistic corpus, dense/full-context baseline, or long-context benchmark.

## Claim scope

On a synthetic language-formatted key/value memory task with 96 facts, 48 queries, 16 exact high-resolution anchors, and coarse low-resolution buckets, a hand-coded non-oracle salience selector improves exact recall when future queries correlate with observable importance/repetition signals.

## Why it stopped

No-paper useful signal: Tier 1 direct evidence supports a narrow mechanism, but the experiment is synthetic and hand-coded rather than publication-grade model evidence.

## Recommended next action

Run a bounded deepen follow-up that integrates the selector into a small learned language-memory or retrieval-augmented model and evaluates held-out naturalistic query distributions against equal-memory random, recency, and oracle controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned small-model validation of non-oracle anchors for dual-resolution memory
- Success threshold: On at least one held-out aligned task, non-oracle anchors improve exact recall by at least 10 percentage points over random/recency equal-memory baselines while remaining clearly below oracle; on uniform controls the gain should shrink to less than 3 percentage points.
- Stop condition: Stop as negative if non-oracle anchors fail to beat random/recency by 5 percentage points on aligned held-out tasks, or if gains persist equally on uniform controls, indicating a confound rather than anchor-selection mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/non-oracle-anchor-selection-for-dual-resolution-memory-on-f2f015adbc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
