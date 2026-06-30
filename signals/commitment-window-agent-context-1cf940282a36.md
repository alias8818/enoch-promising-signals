# Commitment-Window Agent Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `commitment-window-agent-context-1cf940282a36`
Run ID: `commitment-window-agent-context-1cf940282a36-20260619T021652117396+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/18122a9b386e

## What looked useful

Across 24,000 simulated episodes, commitment-window context beat recency-only in all 12 tested budget/reserve conditions. With a 96-token total budget and 72-token reserve, accuracy improved from 4.35% to 100%; zero-reserve and large-context controls showed no gain when the mechanism was disabled or context pressure was removed.

## Boundaries and scale limits

No LLM calls, no real agent traces, no natural-language extraction noise, and no comparison against rolling summary or retrieval baselines. The result validates a local mechanism, not production agent performance.

## Claim scope

In a deterministic synthetic trace simulator with explicit parseable commitments, reserving part of an equal token budget for compressed latest commitments substantially improves final requirement recovery under context pressure compared with recency-only truncation.

## Why it stopped

Closed as no-paper useful signal: the local synthetic mechanism is supported, but direct live-agent evidence is required before any paper claim.

## Recommended next action

Run a bounded live-agent benchmark with controlled context truncation and imperfect commitment extraction, comparing commitment windows against recency-only, rolling summaries, and retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-agent commitment-window context under controlled truncation
- Success threshold: Commitment-window policy improves requirement-fidelity by at least 10 percentage points over recency-only and is not worse than summary/retrieval baselines by more than 5 percentage points under matched budgets.
- Stop condition: Stop if commitment extraction precision falls below 90% or if improvement over recency-only is below 5 percentage points after the first 50 tasks.

## Evidence references

- Artifact root: `<local-path>/projects/commitment-window-agent-context-1cf940282a36`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
