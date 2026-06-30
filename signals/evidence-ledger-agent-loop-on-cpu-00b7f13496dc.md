# Evidence-Ledger Agent Loop on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-agent-loop-on-cpu-00b7f13496dc`
Run ID: `evidence-ledger-agent-loop-on-cpu-00b7f13496dc-20260528T202911029086+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2f06b4594a63

## What looked useful

Evidence-ledger bookkeeping is viable and useful as an audit trail and guardrail against naive lexical retrieval failures, but it did not improve answer quality over a simple metadata filter in this controlled benchmark.

## Boundaries and scale limits

Synthetic tasks only; no LLM, no public QA benchmark, no human audit study, no real retriever logs, and no broad robustness validation.

## Claim scope

On 50,000 deterministic synthetic CPU retrieval tasks with stale and distractor evidence, an evidence-ledger loop matched a metadata-aware control and outperformed a naive lexical baseline, while producing replayable evidence traces.

## Why it stopped

Bounded synthetic evidence supports the audit/guardrail mechanism but the stronger metadata control matched answer quality, so this is not a paper-ready positive result.

## Recommended next action

Stop this run as no-paper useful evidence; deepen with a paired public RAG/QA trace benchmark where ledger and non-ledger agents receive identical retrieved passages.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger audit on public RAG traces
- Success threshold: At least 20% relative reduction in unsupported final answers versus the non-ledger structured-filter control with no more than 2 percentage points absolute accuracy loss and less than 2x CPU latency.
- Stop condition: Stop if the ledger fails to reduce unsupported answers, causes more than 2 percentage points accuracy loss, or exceeds 2x CPU latency on the paired public-trace benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-loop-on-cpu-00b7f13496dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
