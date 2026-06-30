# Evidence-ledger agent loop for hallucinated tool-call reduction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-loop-for-hallucinated-tool-call-reduction-a83e899bdbdb`
Run ID: `evidence-ledger-agent-loop-for-hallucinated-tool-call-reduction-a83e899bdbdb-20260601T013322481245+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e56b47024e72

## What looked useful

Main run over 25,000 task/seed pairs per policy: ledger reduced executed hallucinated calls from 1.8739/task to 0.0000 versus baseline and from 1.2093/task to 0.0000 versus schema-only, with no success loss at noise 0.35. At high noise 0.55, ledger still eliminated executed hallucinations but success fell by 3.09 percentage points under a fixed step budget, showing a guardrail/recovery tradeoff.

## Boundaries and scale limits

No live LLM was used; proposal behavior, tools, facts, and ledger labels were synthetic. Results do not establish performance on real model tool-calling, real APIs, ambiguous language, latency, token cost, or human-authored tasks.

## Claim scope

In a synthetic closed-world support-tool benchmark with paired stochastic proposal streams, an evidence-ledger pre-execution guard eliminated executed hallucinated tool calls and outperformed schema-only validation on ungrounded reads and unsupported mutations.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy rather than direct live-LLM validation.

## Recommended next action

Run a bounded live-LLM follow-up using the same task generator and real function-calling proposals, comparing evidence-ledger, schema-only, and ReAct-style recovery on hallucinated executed calls, success, false blocks, latency, and token cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM evidence-ledger guardrail benchmark for tool-call hallucinations
- Success threshold: Evidence-ledger reduces executed hallucinated calls by at least 50% versus schema-only with success no more than 2 percentage points lower and false blocks below 1% of valid proposed calls.
- Stop condition: Stop as negative if ledger success is more than 2 percentage points below schema-only after retry-budget tuning, or if false blocks exceed 1% without a corresponding hallucination reduction above 50%.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-loop-for-hallucinated-tool-call-reduction-a83e899bdbdb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
