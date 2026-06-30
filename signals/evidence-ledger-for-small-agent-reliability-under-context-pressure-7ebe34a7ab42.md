# Evidence ledger for small agent reliability under context pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-agent-reliability-under-context-pressure-7ebe34a7ab42`
Run ID: `evidence-ledger-for-small-agent-reliability-under-context-pressure-7ebe34a7ab42-20260605T195318368531+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/92f395025fa0

## What looked useful

Across 200 episodes and four budgets, the evidence ledger reached 0.728 mean accuracy versus 0.260 for a recent-window baseline and 0.408 for an append-only ledger. The superseding ledger eliminated stale errors in this setup while the append-only ledger had 0.254 stale-error rate.

## Boundaries and scale limits

Synthetic structured observations only; whitespace token proxy; deterministic retrieval policies; no real LLM extraction, tokenizer-accurate context accounting, tool-use latency, adversarial natural language, or deployed agent traces.

## Claim scope

In deterministic synthetic multi-step traces with distractors and factual updates, a compact superseding evidence ledger preserves final-state query accuracy better than recent-window memory and append-only ledger baselines under the same token-like budgets.

## Why it stopped

The result is a synthetic deterministic mechanism test, not full validation of LLM-agent reliability under real context pressure.

## Recommended next action

Run a bounded real small-LLM agent follow-up with tokenizer-accurate budgets and natural-language traces; stop this run as no-paper useful-signal evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-accurate small-LLM evidence ledger under natural-language trace pressure
- Success threshold: Evidence-ledger agent improves paired final-state query accuracy by at least 10 percentage points over recent-window memory at two or more constrained budgets without increasing invalid citations above 2%.
- Stop condition: Stop if ledger extraction or querying fails to beat recent-window accuracy at the smallest two budgets, or if invalid citations exceed 5% in both ledger settings.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-agent-reliability-under-context-pressure-7ebe34a7ab42`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
