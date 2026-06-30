# Structured Evidence Ledger for Tiny Tool-Calling Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structured-evidence-ledger-for-tiny-tool-calling-agents-4e68b5afe514`
Run ID: `structured-evidence-ledger-for-tiny-tool-calling-agents-4e68b5afe514-20260608T155151540920+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9b056dfa36f3

## What looked useful

The mechanism appears to be relevance-protected evidence eviction rather than structure alone: the blind structured ledger matched transcript/notes, while the relevance-protected ledger won or tied all 20 tested conditions and had positive margin in 8 high-pressure conditions.

## Boundaries and scale limits

No real LLM policy, no real API tools, no noisy relevance-tag generation, and no long-horizon or multi-task serving workload were tested.

## Claim scope

In a deterministic synthetic tool-calling proxy with tiny memory budgets, a relevance-protected structured evidence ledger retained required tool facts and improved answer accuracy over FIFO transcript, deduplicated notes, and a blind structured ledger in high-distractor conditions.

## Why it stopped

Closed as a useful proxy signal, not full validation or paper-ready evidence, because the run isolates memory mechanics with deterministic synthetic agents rather than testing real tiny LLM tool-calling behavior.

## Recommended next action

Run a bounded real small-model tool-calling follow-up that measures whether the model can maintain accurate ledger relevance tags and whether the ledger improves task success over transcript summarization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model evidence-ledger tool-calling validation
- Success threshold: Relevance-ledger condition improves final accuracy by at least 10 percentage points over the best baseline while keeping malformed-ledger rate below 5% and relevance-tag F1 at or above 0.85.
- Stop condition: Stop if relevance-tag F1 is below 0.70 or final accuracy does not exceed the best baseline by at least 3 percentage points after the planned bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-for-tiny-tool-calling-agents-4e68b5afe514`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
