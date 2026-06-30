# Multi-trace downstream validation of semantic compressed memory for agent task reuse

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `multi-trace-downstream-validation-of-semantic-compressed-m-c88440dd9d`
Run ID: `multi-trace-downstream-validation-of-semantic-compressed-m-c88440dd9d-20260612T220101073701+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Semantic Compression Memory on Real Agent Task Reuse Traces: enoch://control-plane/projects/semantic-compression-memory-on-real-agent-task-reuse-trace-5fe88edad7/runs/semantic-compression-memory-on-real-agent-task-reuse-trace-5fe88edad7-20260612T213510390091+0000
- Parent run decision: Semantic compression memory store vs flat vector retrieval for small agent task reuse: enoch://control-plane/projects/semantic-compression-memory-store-vs-flat-vector-retrieval-for-small-agent-task-reuse-c3750752a5fe/runs/semantic-compression-memory-store-vs-flat-vector-retrieval-for-small-agent-task-reuse-c3750752a5fe-20260612T210901664344+0000

## What looked useful

Semantic aggregation is a real mechanism relative to ablations, but compression at 44.5% fewer emitted tokens reduced ordered F1 by 0.0469 and execution score by 0.1607 versus the semantic full-trace baseline. A recall-heavy sensitivity setting improved execution score by 0.0763 but used 13.09 more tokens than full trace, so it is not evidence for compressed memory.

## Boundaries and scale limits

Synthetic workflow traces only; 10 seeds, 60 workflow families per seed, 720 train traces and 360 held-out tasks per seed. No real agent logs, no LLM execution traces, no human tasks, and no long-horizon tool execution.

## Claim scope

On a fixed-seed synthetic multi-trace agent workflow benchmark, semantic multi-trace aggregation improves over lexical, no-semantics, random, no-memory, and single-trace compression controls, but a memory-saving compressed configuration does not beat a semantic nearest full-trace baseline on downstream plan reuse.

## Why it stopped

Tier 2 fixed-seed validation did not show compressed semantic memory outperforming the same-representation full-trace baseline under a memory-saving configuration.

## Recommended next action

Stop paper escalation for this run; if continuing locally, run a Pareto-constrained compression sweep on a real or higher-fidelity trace corpus and require memory <= full trace before counting any execution-score gain.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pareto-budgeted semantic compression on real agent traces
- Success threshold: At memory tokens <= full_trace_semantic, compressed semantic memory improves execution score by at least 0.03 absolute without lowering ordered F1 by more than 0.01 across at least 10 fixed seeds or bootstrap-equivalent splits.
- Stop condition: Stop if no configuration on the Pareto frontier meets the memory constraint and execution/F1 thresholds, or if gains only appear when emitted memory exceeds the full-trace baseline.

## Evidence references

- Artifact root: `<local-path>/projects/multi-trace-downstream-validation-of-semantic-compressed-m-c88440dd9d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
