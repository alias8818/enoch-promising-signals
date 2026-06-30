# Agent Ledger: Exact Anchor Buffer plus Compressed Summary

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-ledger-exact-anchor-buffer-plus-compressed-summary-00d19bdc6bfa`
Run ID: `agent-ledger-exact-anchor-buffer-plus-compressed-summary-00d19bdc6bfa-20260528T222053649038+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/dcdcd6c75d7c

## What looked useful

At 45% anchor reserve, hybrid anchor-buffer-plus-summary improved old-anchor recall by +0.096 versus summary-only while reducing ordinary recall by -0.018. Reserve sweep showed a monotonic tradeoff: 0.35 reserve gave small gains, while 0.60 and 0.75 reserves gave larger anchor gains with larger ordinary-context losses.

## Boundaries and scale limits

Synthetic fact streams only; no live LLM summarization, tokenizer-level prompt packing, retrieval model, or downstream agent task-success measurement. Main run used 128 trials, 420 steps per trial, 4 facts per step, 12% anchor rate, and budget 900 weighted units.

## Claim scope

In a deterministic synthetic oracle benchmark of long agent-like fact streams, reserving part of a fixed memory budget for exact anchor facts improved long-horizon anchor retention versus summary-only and recent-buffer controls, with a measurable ordinary-context retention tradeoff.

## Why it stopped

Closed as no-paper useful signal: the mechanism is supported by synthetic oracle retention evidence, but the result is not direct LLM-agent evidence and should not be treated as publication-grade validation.

## Recommended next action

Run a bounded live-agent validation using real tokenizer budgets, model-generated summaries, and exact-value query/task success metrics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM Agent Anchor Ledger Validation
- Success threshold: Hybrid improves exact-value accuracy by at least 10 percentage points over summary-only with no more than 5 percentage points loss in downstream task success or ordinary-context question accuracy.
- Stop condition: Stop if tokenizer-measured hybrid memory fails to improve exact-value accuracy by at least 5 percentage points over summary-only on a 30-trace pilot, or if ordinary-context/task-success loss exceeds 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/agent-ledger-exact-anchor-buffer-plus-compressed-summary-00d19bdc6bfa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
