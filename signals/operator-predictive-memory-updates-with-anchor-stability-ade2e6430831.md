# Operator-Predictive Memory Updates with Anchor Stability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operator-predictive-memory-updates-with-anchor-stability-ade2e6430831`
Run ID: `operator-predictive-memory-updates-with-anchor-stability-ade2e6430831-20260613T215440249359+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ffda7f9aacb9

## What looked useful

Anchor-stable predictive memory reached 0.9142 aggregate accuracy across 18,000 predictions versus 0.7544 for transcript search and 0.8564 for flat retrieval. It achieved perfect transient-noise accuracy in this labeled synthetic setup, but had 0.0000 true-update accuracy on update episodes because it deliberately waits for repeated durable evidence before changing an anchor.

## Boundaries and scale limits

Synthetic-only evidence; no real operator transcripts, LLM extraction errors, task execution outcomes, long-horizon compaction, or model-scale training were tested.

## Claim scope

On a deterministic synthetic replay with six operator preference anchors, transient contradictory signals, missing signals, and rare durable updates, anchor-stable predictive memory improved aggregate next-session anchor prediction accuracy over transcript-last-hit and flat decayed retrieval baselines.

## Why it stopped

Closed as no-paper useful synthetic mechanism evidence; the result is not a full validation because the replay uses generated labels and does not test real operator language or end-to-end agent behavior.

## Recommended next action

Run a bounded real-transcript or LLM-generated transcript follow-up that removes oracle signal labels and scores both anchor prediction and task outcome after true preference changes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle transcript replay for anchor-stable predictive memory
- Success threshold: At least 5 percentage point aggregate accuracy improvement over flat retrieval while keeping median durable-update recovery lag at or below two subsequent relevant anchor observations.
- Stop condition: Stop if the non-oracle extractor cannot distinguish transient overrides from durable updates above 0.70 F1 or if anchor-stable memory fails to beat flat retrieval by 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/operator-predictive-memory-updates-with-anchor-stability-ade2e6430831`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
