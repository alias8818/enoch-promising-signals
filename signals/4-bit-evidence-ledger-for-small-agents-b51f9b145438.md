# 4-Bit Evidence Ledger for Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `4-bit-evidence-ledger-for-small-agents-b51f9b145438`
Run ID: `4-bit-evidence-ledger-for-small-agents-b51f9b145438-20260608T051911922376+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4244dd767c13

## What looked useful

The naive signed-nibble delta ledger was too lossy, but a 4-bit quantized log-odds state with 0.5 step size achieved 0.4-1.25 percentage point accuracy gaps versus 32-bit float log-odds while using 12.5% of the per-claim state and beating 2-bit by 4.6-12.6 points.

## Boundaries and scale limits

No live LLM-agent loop, natural-language evidence extraction, retrieval noise, tool-use trajectory, or end-to-end token-budget evaluation was tested. Claims are limited to compact belief-state accumulation after evidence events and reliability scores are available.

## Claim scope

In a synthetic binary-claim evidence accumulation task with known evidence reliabilities, a signed 4-bit quantized log-odds ledger preserved most float log-odds decision accuracy and beat 2-bit and last-evidence compact baselines across four bounded regimes.

## Why it stopped

Closed as no-paper useful signal because the supporting evidence is synthetic and mechanism-level rather than direct end-to-end evidence from real small agents.

## Recommended next action

Run a bounded real small-agent retrieval/QA follow-up that compares the 4-bit quantized log-odds ledger against uncompressed notes, no-ledger, and 2-bit baselines on final answer correctness and token/memory cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: 4-bit quantized log-odds ledger in a real small-agent retrieval QA loop
- Success threshold: Across at least 200 labeled QA traces, the 4-bit ledger improves accuracy per token over no-ledger and 2-bit baselines and remains within 2 percentage points of the uncompressed evidence-memory baseline.
- Stop condition: Stop if the 4-bit ledger fails to beat both no-ledger and 2-bit baselines on accuracy per token, or if evidence extraction noise makes ledger updates unreliable in more than 20% of inspected traces.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-evidence-ledger-for-small-agents-b51f9b145438`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
