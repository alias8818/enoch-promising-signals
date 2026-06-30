# Evidence-Ledger Agent with Exact-Anchor State for Long-Horizon Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-with-exact-anchor-state-for-long-horizon-tasks-58bd207d354d`
Run ID: `evidence-ledger-agent-with-exact-anchor-state-for-long-horizon-tasks-58bd207d354d-20260609T222721065452+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a7be01676626

## What looked useful

Ledger maintained 1.000 exact value, exact anchor, and audit success for 1000+ age current queries and 1.000 audit success for 1000+ age historical anchors. Bounded 512-entry window/summary baselines fell to 0.000 on 1000+ age current and historical tasks. A 20,000-capacity current summary with anchors matched current queries but only reached 0.671 historical audit success for 1000+ age anchors.

## Boundaries and scale limits

Synthetic standard-library benchmark only; no LLM extraction, natural-language ambiguity, vector/RAG baseline, real task environment, token accounting, or multi-day deployment. Largest run used 8,000 events, 20 seeds, 30,000 current queries, and 30,000 historical audit probes.

## Claim scope

In deterministic synthetic long-horizon event streams, an append-only evidence ledger with exact current-state anchors preserves exact current anchors and arbitrary historical-anchor audit across 8,000 events, while bounded sliding-window and LRU current-summary baselines fail for old evidence. A high-capacity current summary can match current-fact recall, so the supported claim is specifically about bounded-state pressure and historical auditability, not universal superiority for current recall.

## Why it stopped

Closed as no-paper useful signal because the result is a deterministic synthetic proxy; it supports the mechanism but does not directly validate a long-horizon LLM agent.

## Recommended next action

Run a bounded LLM trace benchmark with natural-language event extraction, equal token/storage budgets, and a vector/RAG memory baseline; stop this run as synthetic useful signal rather than paper-ready evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM Trace Benchmark for Exact-Anchor Evidence Ledgers
- Success threshold: At least 95% exact citation/audit success for 1000+ step-old facts and statistically higher old/superseded evidence audit success than all matched-memory baselines, with no more than 5% relative loss in end-task answer accuracy.
- Stop condition: Stop if extraction noise or retrieval errors keep ledger citation/audit success below 80% on old facts, or if a matched vector/RAG or indexed-summary baseline reaches equivalent audit success with lower storage and latency.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-with-exact-anchor-state-for-long-horizon-tasks-58bd207d354d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
