# Bounded Evidence Ledger for Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-evidence-ledger-for-agent-reliability-94bd73bc056a`
Run ID: `bounded-evidence-ledger-for-agent-reliability-94bd73bc056a-20260607T040905432796+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d189e1faa4bf

## What looked useful

Bounded provenance-aware retention produced consistent paired accuracy gains over naive recency of +5.13, +7.30, and +8.09 percentage points across low, medium, and high noise conditions, with stale-wrong-rate reductions of 24.7%, 17.4%, and 13.4%. It also beat a source-weighted recency control by about +2 percentage points in all conditions.

## Boundaries and scale limits

The run used synthetic observations, not real LLM agent traces or deployed tool logs. It used 3 noise regimes, 80 paired seeds per regime, 2000 stream steps per seed, 64 keys, and fixed ledger hyperparameters. It does not establish publication-grade general agent reliability.

## Claim scope

In a deterministic synthetic keyed-fact evidence stream with contradictions, stale facts, low-trust distractors, and a 128-entry memory budget, a small bounded evidence ledger improved end-to-end query accuracy and reduced stale-wrong answers relative to naive bounded recency memory.

## Why it stopped

Synthetic benchmark supports the mechanism but is proxy evidence, not direct deployment or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should replay real or recorded LLM-agent tool traces through the same ledger and controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Bounded Evidence Ledger on Real Agent Tool Traces
- Success threshold: At least +3 percentage points paired end-to-end accuracy over naive recency and at least 15% stale-claim reduction across two real trace domains, with no more than 2 percentage points coverage loss.
- Stop condition: Stop if gains disappear on real traces, if the ledger requires unavailable private labels, or if coverage loss exceeds 2 percentage points at capacities practical for agent context budgets.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-evidence-ledger-for-agent-reliability-94bd73bc056a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
