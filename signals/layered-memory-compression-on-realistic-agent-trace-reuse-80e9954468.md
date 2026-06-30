# Layered Memory Compression on Realistic Agent Trace Reuse

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layered-memory-compression-on-realistic-agent-trace-reuse-80e9954468`
Run ID: `layered-memory-compression-on-realistic-agent-trace-reuse-80e9954468-20260610T201649545438+0000`

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

- Parent run decision: Layered Memory Compression vs Flat Retrieval for Agent Task Reuse: enoch://control-plane/projects/layered-memory-compression-vs-flat-retrieval-for-agent-task-reuse-f0e90d68946c/runs/layered-memory-compression-vs-flat-retrieval-for-agent-task-reuse-f0e90d68946c-20260610T200243099877+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7baa2397cd09

## What looked useful

The current top-term layered compression heuristic is not sufficient for paper claims: at 160 words per trace, scrubbed Hit@1 was 0.3021 for layered vs 0.3125 for flat_recent, and raw Hit@1 was 0.3021 vs 0.3403. Full-oracle memory reached scrubbed Hit@1 0.5382, showing recoverable signal exists but this compressor does not retain enough of it. At 80-120 words, scrubbed layered Hit@1 exceeded flat_recent by only 0.010-0.014.

## Boundaries and scale limits

Small local retrieval benchmark only; no LLM generation, no end-to-end agent task execution, no learned compressor, and no large multi-corpus validation. The trace corpus was sampled from local Enoch project logs and the task was correct-session retrieval, not answer-quality evaluation.

## Claim scope

On a 36-trace real Codex/Enoch held-out trace-reuse retrieval benchmark, the tested heuristic layered compressor did not beat an equal-budget flat_recent baseline on Hit@1 at the main 160-word budget, but it produced a small scrubbed Hit@3/MRR gain and slight Hit@1 gains only at very tight 80-120 word budgets.

## Why it stopped

Tier 1 controlled direct test completed; the pre-set success threshold was not met, so this is no-paper useful signal rather than paper-positive evidence.

## Recommended next action

Run one bounded deepen follow-up replacing the top-term heuristic with a structure-aware compressor that preserves objectives, files, commands, failures, and decisions, then require at least +0.10 scrubbed Hit@1 over flat_recent on the same 36-trace reuse benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Structure-aware layered compressor for real agent trace reuse
- Success threshold: At 160 words per trace on the scrubbed 36-trace benchmark, structure-aware layered compression must improve Hit@1 by at least +0.10 over flat_recent with a bootstrap CI whose lower bound is above 0, or stop as unsupported.
- Stop condition: Stop if the structure-aware compressor fails to beat flat_recent by +0.05 Hit@1 in a 10-trace smoke run or fails to reach the +0.10 Hit@1 threshold in the 36-trace run.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-compression-on-realistic-agent-trace-reuse-80e9954468`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
