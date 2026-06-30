# Exact-anchor compressed memory on real or LLM-generated repeated-agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-compressed-memory-on-real-or-llm-generated-re-ac330ec9fa`
Run ID: `exact-anchor-compressed-memory-on-real-or-llm-generated-re-ac330ec9fa-20260614T121020689869+0000`

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

- Parent run decision: Compressed-State Agent Memory with Exact Anchors: enoch://control-plane/projects/compressed-state-agent-memory-with-exact-anchors-dc9601f4b701/runs/compressed-state-agent-memory-with-exact-anchors-dc9601f4b701-20260614T114343910552+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/293290b77429

## What looked useful

At 25% memory budget, layered_doctrine_memory recovered 288/288 anchor values while flat_retrieval recovered 48/288 with similar mean memory tokens per session. This supports the exact-anchor preservation mechanism but is not paper-ready.

## Boundaries and scale limits

Synthetic traces only; exact string evaluator only; no real operator traces, no independent LLM-generated traces, no trained summarizer, no LLM answer-generation loop, and no robustness tests beyond the seeded controlled setup.

## Claim scope

In a deterministic Tier 1 synthetic repeated-agent benchmark with 24 sessions, 288 exact-anchor replay queries, and 10-35% memory budgets, compact exact-anchor records preserved anchor-value recall under compression better than budget-matched flat recency memory.

## Why it stopped

Tier 1 controlled direct test passed its mechanism threshold, but evidence remains synthetic and hand-scored, so this is useful no-paper signal rather than publication-grade validation.

## Recommended next action

Run a bounded deepen test on held-out real or independently LLM-generated repeated-agent traces with an LLM answer-generation loop and a stronger compressed-memory baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-anchor compressed memory on held-out LLM-generated repeated-agent traces
- Success threshold: At 25% memory budget, exact-anchor memory reaches at least 0.90 answer accuracy and at least +0.25 absolute accuracy over the strongest compressed baseline with non-overlapping bootstrap 95% confidence intervals.
- Stop condition: Stop as negative if exact-anchor memory is below 0.80 accuracy or its gain over the strongest compressed baseline is below +0.10 absolute on the first 100 held-out traces.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-compressed-memory-on-real-or-llm-generated-re-ac330ec9fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
