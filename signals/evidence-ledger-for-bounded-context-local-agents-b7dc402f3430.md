# Evidence Ledger for Bounded-Context Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-bounded-context-local-agents-b7dc402f3430`
Run ID: `evidence-ledger-for-bounded-context-local-agents-b7dc402f3430-20260604T054103826787+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae31537fae7b

## What looked useful

Across 48,000 queries and five seeds, the window-only policy averaged 22.51% all-query accuracy and 0.00% outside-window accuracy, while the ledger policy achieved 100.00% answer-and-citation accuracy overall and on 37,196 outside-window queries.

## Boundaries and scale limits

Evidence is synthetic and proxy-only: no real LLM inference, natural-language ambiguity, semantic retrieval, adversarial conflicts, ledger corruption, compaction, multi-hop reasoning, or deployed local-agent traces were tested.

## Claim scope

In a deterministic synthetic exact-key event-stream benchmark, an append-only evidence ledger lets a bounded-context local-agent policy recover and cite latest supporting facts that have fallen outside a 128-event active window.

## Why it stopped

Synthetic exact-key evidence supports the mechanism but is proxy-only and insufficient for publication-grade validation of bounded-context local agents.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test the same ledger mechanism with real local LLM traces, semantic retrieval, paraphrased evidence, and citation faithfulness checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-Language Local-Agent Evidence Ledger Evaluation
- Success threshold: Ledger-backed agents improve outside-window answer-and-citation accuracy by at least 20 percentage points over both window-only and summary-only baselines without more than 2x median latency.
- Stop condition: Stop if the ledger improves outside-window accuracy by less than 5 percentage points over summary-only baselines or if citation correctness falls below 90% on conflict cases.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-bounded-context-local-agents-b7dc402f3430`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
