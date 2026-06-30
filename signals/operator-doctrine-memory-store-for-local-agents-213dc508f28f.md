# Operator-Doctrine Memory Store for Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-store-for-local-agents-213dc508f28f`
Run ID: `operator-doctrine-memory-store-for-local-agents-213dc508f28f-20260621T003712242542+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e2d03d5dbc0

## What looked useful

Metadata-aware local doctrine retrieval reached 1.000 mean recall@3, 0 forbidden retired docs in top 5, and 1.000 mean packed recall at 80 and 160 token budgets; static priority injection reached only 0.125 recall@3 and lexical overlap admitted 2 forbidden retired docs in top 5.

## Boundaries and scale limits

Synthetic doctrine corpus only: 20 short doctrine records, 12 task cases, no live LLM-agent A/B test, no production traces, no embedding or hybrid retrieval comparison.

## Claim scope

A local SQLite FTS5 memory store with priority, version, active filtering, and conflict-aware prompt packing can retrieve the correct operator-doctrine snippets on a 12-case deterministic local-agent probe better than static priority injection and with fewer retired-rule intrusions than lexical overlap.

## Why it stopped

No-paper useful signal: the mechanism passed a deterministic proxy probe, but publication-grade evidence would require live-agent task outcomes and a realistic labeled doctrine/task corpus.

## Recommended next action

Run a bounded live-agent A/B replay on 50-100 realistic local-agent tasks comparing static AGENTS injection, lexical retrieval, metadata FTS retrieval, and hybrid embedding retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-agent A/B replay for operator-doctrine memory retrieval
- Success threshold: Metadata FTS or hybrid retrieval improves instruction compliance by at least 10 percentage points or reduces prompt tokens by at least 40 percent at equal compliance, with no increase in forbidden doctrine injection over static injection.
- Stop condition: Stop if metadata-aware retrieval fails to outperform static injection on both compliance and token budget, or if forbidden doctrine injection exceeds the static baseline.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-store-for-local-agents-213dc508f28f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
