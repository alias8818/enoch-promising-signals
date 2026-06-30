# Real-repository LLM evaluation of layered coding-task memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-repository-llm-evaluation-of-layered-coding-task-memo-1d67b4cf4f`
Run ID: `real-repository-llm-evaluation-of-layered-coding-task-memo-1d67b4cf4f-20260628T084805736691+0000`

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

- Parent run decision: Layered User/Project Memory for Repeated Coding Tasks: enoch://control-plane/projects/layered-user-project-memory-for-repeated-coding-tasks-f70571e098f3/runs/layered-user-project-memory-for-repeated-coding-tasks-f70571e098f3-20260628T083204352080+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/9f1b043331c8

## What looked useful

Layered task memory produced a +6/24 score improvement under a smaller memory-token budget, supporting the mechanism that structured task memory can help coding agents recover relevant implementation and test targets. The result is no-paper evidence because automatic memory construction and patch-level validation were not tested.

## Boundaries and scale limits

Single repository, one small local model, deterministic one-pass answers, manually curated memory, navigation-only scoring rather than patch generation or test-passing repair.

## Claim scope

In a six-task controlled MarkupSafe code-navigation benchmark using Qwen/Qwen2.5-Coder-1.5B-Instruct, a manually curated layered task-memory prompt improved objective file/symbol/test targeting from 13/24 to 19/24 versus a larger flat raw-context prompt.

## Why it stopped

Tier 1 direct test completed with useful mechanism support, but evidence is not publication-grade due to single-repo scope and manually curated memory.

## Recommended next action

Run a bounded deepen follow-up that automatically builds layered memory and evaluates patch generation with tests on 2-3 small real repositories.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Automatic layered-memory patch generation on small real repositories
- Success threshold: Layered automatic memory achieves at least a 20 percentage point higher test-pass rate than flat context, with no more than 10% higher mean generation latency, across at least 10 total tasks.
- Stop condition: Stop as negative if automatic layered memory fails to improve test-pass rate by at least 10 percentage points or introduces frequent wrong-file edits that make more than 30% of tasks fail before tests run.

## Evidence references

- Artifact root: `<local-path>/projects/real-repository-llm-evaluation-of-layered-coding-task-memo-1d67b4cf4f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
