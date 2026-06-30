# Bounded Multi-Session Memory Consolidation for Home Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-multi-session-memory-consolidation-for-home-agents-25a6283d139a`
Run ID: `bounded-multi-session-memory-consolidation-for-home-agents-25a6283d139a-20260619T025722207163+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/02d6a3a11c2b

## What looked useful

Canonical consolidation reached 1.000 preference and stable-fact accuracy at 69 slots, matching the max generated canonical fact universe, while recency reached 0.744/0.527 and lexical episodic retrieval reached 0.693/0.364. At 50 slots, consolidation still led but dropped to 0.802 preference accuracy, showing eviction policy is a real constraint below fact cardinality.

## Boundaries and scale limits

Synthetic only; no LLM extraction, no embedding retrieval, no Home Assistant integration, no real user data, and no action-taking evaluation. Tested 50 seeds, 120 sessions, 729 events per seed.

## Claim scope

In a deterministic synthetic home-agent memory benchmark with structured fact keys, canonical consolidation preserves current household facts better than bounded raw episodic stores when the slot budget approaches the canonical fact cardinality.

## Why it stopped

Closed as a no-paper useful signal because evidence is synthetic/proxy and not an integrated home-agent validation.

## Recommended next action

Run a bounded direct-evidence follow-up using an actual extractor/retriever on LongMemEval- or Home Assistant-style traces with stale-memory and action-quality metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Extractor-backed bounded consolidation on multi-session home-agent traces
- Success threshold: At equal memory budget, consolidation improves current-value accuracy by at least 10 percentage points and reduces obsolete-memory answers by at least 25% relative to bounded episodic retrieval on a held-out trace set.
- Stop condition: Stop if extractor noise prevents reliable canonical key updates or if consolidation fails to beat bounded episodic retrieval on current-value accuracy at two tested budgets.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-multi-session-memory-consolidation-for-home-agents-25a6283d139a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
