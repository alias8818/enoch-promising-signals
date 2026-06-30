# Real-trace anchor-addressed memory validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-trace-anchor-addressed-memory-validation-b211a6a711`
Run ID: `real-trace-anchor-addressed-memory-validation-b211a6a711-20260629T053912805289+0000`

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

- Parent run decision: Anchor-Addressed Compressed Memory for Long-Context Agent Tasks: enoch://control-plane/projects/anchor-addressed-compressed-memory-for-long-context-agent-tasks-fdad5942473e/runs/anchor-addressed-compressed-memory-for-long-context-agent-tasks-fdad5942473e-20260629T051255721799+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/084f73bed7c6

## What looked useful

Anchor addressing is useful only if anchors are event-granular or revision-aware; mutable lifecycle ids such as item_N can conflate started/completed rows and produce wrong status or exit-code answers.

## Boundaries and scale limits

Single small project-local trace: 61 JSONL rows, 32 scored item rows, 110 generated structured retrieval tasks, no LLM generation, no multi-session corpus, and no private external trace validation.

## Claim scope

On one local real Codex JSONL trace with deterministic decoy noise, exact anchor lookup reduced retrieval work and beat anchor-stripped flat retrieval, but raw item ids were not reliable event-history addresses.

## Why it stopped

No-paper useful signal: the proxy-real local trace benchmark found a concrete anchor ambiguity failure mode, so this is not full validation or publication-grade evidence.

## Recommended next action

Run a bounded deepen test on a larger real multi-session trace using compound event anchors such as item_N@row_index and require anchor-addressed accuracy to match or beat transcript search while preserving candidate-scan savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Event-granular anchor addresses for real repeated-agent memory traces
- Success threshold: Compound event-anchor memory reaches at least 0.95 structured retrieval accuracy, is no worse than transcript search by more than 0.02 accuracy, and scans at least 50x fewer candidates than transcript search.
- Stop condition: Stop if compound anchors still conflate lifecycle revisions, fall more than 0.05 below transcript search accuracy, or require private labels unavailable to the worker.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-anchor-addressed-memory-validation-b211a6a711`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
