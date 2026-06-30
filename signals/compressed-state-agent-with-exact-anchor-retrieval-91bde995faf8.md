# Compressed State Agent with Exact Anchor Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-state-agent-with-exact-anchor-retrieval-91bde995faf8`
Run ID: `compressed-state-agent-with-exact-anchor-retrieval-91bde995faf8-20260604T042835717297+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d1eff6718125

## What looked useful

Across 15 synthetic conditions, compressed-only exact recall averaged 0.0461 and fell to 0.0006 in the largest 16-slot condition; hybrid exact-anchor retrieval matched the full-state oracle at 1.0 accuracy in every condition while keeping live state bounded. Lossy anchor capture ablations averaged 0.5318 at 50% capture and 0.9034 at 90% capture, identifying extraction/indexing recall as the main practical risk.

## Boundaries and scale limits

Tested only deterministic synthetic streams up to 100000 events, 10000 possible anchors, 41989 latest keyed facts, and 16-256 live summary slots on one CPU process. No LLM, learned summarizer, natural-language extraction, semantic retrieval, or real agent task was tested.

## Claim scope

Synthetic keyed-event streams show that a fixed-size compressed live state loses exact anchored facts as stream length grows, while an external exact anchor index restores exact keyed-fact recall to full-state-oracle accuracy under perfect anchor capture.

## Why it stopped

Closed as a no-paper useful signal because the current evidence is synthetic mechanism isolation rather than full validation of an agent architecture.

## Recommended next action

Run a bounded end-to-end small-agent benchmark with natural-language anchor extraction and matched context budgets before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-agent exact-anchor memory benchmark
- Success threshold: Exact-anchor variant improves exact recall by at least 25 percentage points and task success by at least 10 percentage points over compressed-only memory at matched live-state budget, with anchor extraction recall >= 95% and stale-fact errors <= 2%.
- Stop condition: Stop if exact-anchor retrieval fails to improve exact recall by 10 percentage points, if extraction recall is below 90% without a clear fix, or if stale-fact errors exceed 5%.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-agent-with-exact-anchor-retrieval-91bde995faf8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
