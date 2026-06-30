# Exact-Anchor Compressed State for Long-Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-compressed-state-for-long-context-cb11ba3622c1`
Run ID: `exact-anchor-compressed-state-for-long-context-cb11ba3622c1-20260613T223124301803+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1cec187828d5

## What looked useful

At 32768 context length, sketch-only salient retrieval was about 0.05-0.06 accuracy, while exact-anchor variants reached 1.00 accuracy whenever anchor capacity covered the 8, 32, or 128 salient facts, using roughly 14.5x-15.9x less memory than a full key-value stream under the simple byte model. When capacity was below salient count, accuracy increased roughly in proportion to exact-hit coverage rather than solving overflowed facts.

## Boundaries and scale limits

No learned anchor selection, no transformer/SSM training, no natural-language benchmark, and no full-attention baseline were tested. The largest synthetic context was 32768 updates with 96 trials per condition.

## Claim scope

Synthetic key-value retrieval with oracle-salient exact anchors: a fixed-size lossy compressed state plus exact anchors preserves flagged long-range facts when anchor capacity covers the salient set, while the same sketch alone loses those facts under long distractor streams.

## Why it stopped

Closed as no-paper useful signal: the mechanism is supported in an oracle synthetic probe, but the result is not a direct validation of a trainable long-context architecture.

## Recommended next action

Run a bounded learned-selector follow-up on a small transformer or recurrent model with a causal anchor budget and compare against full attention, sliding-window, and sketch-only baselines on the same synthetic retrieval task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Causal Anchor Selection for Compressed Long-Context Retrieval
- Success threshold: At 8192 or longer context, learned anchors recover at least 80% of oracle-anchor gain over sketch-only while using at least 2x less memory than full key-value storage.
- Stop condition: Stop if learned selection fails to beat sketch-only by at least 10 percentage points after a calibrated small-model run, or if anchor choices collapse to non-salient tokens across multiple seeds.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-compressed-state-for-long-context-cb11ba3622c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
