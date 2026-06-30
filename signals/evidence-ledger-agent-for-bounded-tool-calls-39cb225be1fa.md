# Evidence-ledger agent for bounded tool calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-for-bounded-tool-calls-39cb225be1fa`
Run ID: `evidence-ledger-agent-for-bounded-tool-calls-39cb225be1fa-20260531T122952338069+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b3cd440f7980

## What looked useful

Across 1,000-task runs, the evidence-ledger policy achieved 100% success with 5 mean calls, versus greedy-quality success of 68.7% at budget 8, 30.8% at budget 6, and 59.6% under harder distractors; random baselines stayed below 4% success.

## Boundaries and scale limits

Evidence is synthetic and proxy-only: the ledger receives structured document claim IDs, no LLM is used, retrieval snippets are not noisy natural language, and answer/citation generation is not evaluated.

## Claim scope

In a deterministic synthetic multi-claim retrieval-control task, a policy that tracks claim-level evidence coverage uses a bounded retrieval-call budget more effectively than random selection or greedy standalone document-quality selection.

## Why it stopped

Proxy synthetic validation supports the mechanism but is not direct evidence for real bounded tool-call agents.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test a real LLM/tool agent where the ledger is populated from noisy extracted evidence states rather than oracle claim IDs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy evidence-ledger LLM agent under fixed tool budgets
- Success threshold: Evidence-ledger agent improves final answer correctness by at least 10 percentage points over the strongest non-ledger baseline while reducing unsupported claims or keeping them no worse under the same tool-call budget.
- Stop condition: Stop if the ledger advantage disappears under noisy extraction or if unsupported-claim rate increases by more than 5 percentage points versus the strongest baseline.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-for-bounded-tool-calls-39cb225be1fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
