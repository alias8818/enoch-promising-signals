# Structured Evidence Ledger for Tiny Tool Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structured-evidence-ledger-for-tiny-tool-agents-eb020c87ce0a`
Run ID: `structured-evidence-ledger-for-tiny-tool-agents-eb020c87ce0a-20260608T091711310885+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48a4ed233ae9

## What looked useful

Across 40 seeds, compact ledger accuracy exceeded filtered transcript accuracy by 2.69, 5.81, 12.75, and 24.69 percentage points at 512, 1024, 2048, and 4096 bytes respectively; raw transcript accuracy was much lower. Conflict metadata slightly reduced accuracy under the same byte budgets.

## Boundaries and scale limits

No real LLM agent, natural-language extraction, deployed tool environment, adversarial evidence, or long-horizon planning was tested. The benchmark isolates memory retention and latest-value lookup only.

## Claim scope

In a deterministic synthetic tool-observation memory benchmark with extractable typed claims, a compact structured evidence ledger improves final-value and provenance accuracy over raw and filtered transcript memories under 512-4096 byte budgets.

## Why it stopped

No-paper useful signal: local synthetic evidence supports the memory mechanism but does not directly validate tiny LLM tool agents or publication-grade robustness.

## Recommended next action

Run a bounded real-agent deepen test with a small local model or fixed tool-agent harness, comparing transcript, filtered transcript, compact ledger, and conflict-aware ledger on end-to-end task success and provenance correctness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Tiny Tool-Agent Evidence Ledger Harness
- Success threshold: Compact ledger improves final task accuracy by at least 10 percentage points over filtered transcript and does not reduce provenance correctness, averaged over at least 100 held-out tasks.
- Stop condition: Stop if the compact ledger fails to beat filtered transcript by 5 percentage points or if extraction errors erase the synthetic retention advantage.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-for-tiny-tool-agents-eb020c87ce0a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
