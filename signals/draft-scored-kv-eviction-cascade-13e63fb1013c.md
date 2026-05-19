# Draft-Scored KV Eviction Cascade

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `draft-scored-kv-eviction-cascade-13e63fb1013c`
Run ID: `draft-scored-kv-eviction-cascade-13e63fb1013c-20260515T050213146244+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7250694f55c4

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy mechanism test supported draft-scored token selection, but no live KV eviction, generation quality, latency, or memory validation was performed.

## Recommended next action

Stop this worker run as proxy-only no-paper evidence; run a bounded direct KV-eviction generation follow-up before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct KV Eviction Generation Test for Draft-Scored Cascade
- Success threshold: At 12.5% and 25% KV budgets, draft-scored cascade should reduce quality loss versus recency/heavy-hitter controls by at least 20% relative while preserving a net throughput or peak-memory advantage over full-cache generation.
- Stop condition: Stop if draft-scored eviction is not better than recency or heavy-hitter controls at matched KV budget, or if draft scoring overhead removes the serving benefit.

## Evidence references

- Artifact root: `<local-path>/projects/draft-scored-kv-eviction-cascade-13e63fb1013c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
