# Semantic Memory Cascade for Agent Reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `semantic-memory-cascade-for-agent-reliability-efa63d803088`
Run ID: `semantic-memory-cascade-for-agent-reliability-efa63d803088-20260630T012504306217+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/3ca416d3c523

## What looked useful

Learned memory strongly beat a stateless heuristic, but the semantic cascade did not consistently beat a simpler flat-memory baseline. It was worse by 4.06% failures/1k in stable recurrence, approximately tied under noise and exception stress, and better under drift by converting stale-rule failures into 276.77 escalations/1k.

## Boundaries and scale limits

No real LLM, real embeddings, real tool traces, human escalation cost, long-horizon memory compaction, or model-scale evaluation was run. Each regime used 20 seeds x 10000 synthetic episodes per agent.

## Claim scope

Synthetic mechanism probe of a semantic-rule, exception-memory, and confidence-gate cascade for recurrent agent action selection under noise, exceptions, and drift.

## Why it stopped

Moderate synthetic evidence is mixed and not paper-ready: cascade adds drift robustness through escalation but does not consistently improve over flat memory.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should replay real or generated LLM tool-use traces with embedding retrieval and cost-normalized escalation against a memory-budget-matched flat baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-based semantic memory cascade with cost-normalized escalation
- Success threshold: At least 10% lower cost-weighted unrecovered failure rate than flat memory in three of four regimes, with no regime worse by more than 3%.
- Stop condition: Stop if cascade fails to beat flat memory on cost-weighted failures in at least two regimes or if gains come only from excessive escalation cost.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-memory-cascade-for-agent-reliability-efa63d803088`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
