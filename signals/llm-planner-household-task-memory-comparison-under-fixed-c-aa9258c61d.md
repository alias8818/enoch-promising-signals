# LLM planner household-task memory comparison under fixed context budgets

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-planner-household-task-memory-comparison-under-fixed-c-aa9258c61d`
Run ID: `llm-planner-household-task-memory-comparison-under-fixed-c-aa9258c61d-20260611T104029723645+0000`

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

- Parent run decision: Agent memory architecture comparison on repeated home tasks with bounded VRAM: enoch://control-plane/projects/agent-memory-architecture-comparison-on-repeated-home-tasks-with-bounded-vram-b301314082b1/runs/agent-memory-architecture-comparison-on-repeated-home-tasks-with-bounded-vram-b301314082b1-20260611T101846784050+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/29ac784301c8

## What looked useful

Under exactly equal 210-word prompts, recent-only context reached 53.125% accuracy, lexical retrieval reached 81.25%, and structured memory reached 100.0%; paired sign tests versus recent-only gave p=0.00390625 for lexical retrieval and p=0.00006103515625 for structured memory.

## Boundaries and scale limits

Single small instruction model, synthetic object-location episodes, approximate word budget rather than tokenizer-level budget, multiple-choice single-step planning only, oracle structured memory, no embodied simulator, no real household task distribution, and no multi-turn execution success metric.

## Claim scope

In a 32-episode synthetic household retrieval next-action benchmark using Qwen/Qwen2.5-0.5B-Instruct, compact explicit memory and lexical retrieval improved multiple-choice planner accuracy under an equal 210-prompt-word budget compared with a recent-only context baseline.

## Why it stopped

Tier 1 direct small test produced a useful mechanism signal but remains synthetic, single-model, and single-step, so it is no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded multi-step household-planning follow-up with non-oracle memory updates and execution success rate in a simulator or scripted environment before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-step household planner memory benchmark with non-oracle memory updates
- Success threshold: Memory condition improves task success over recent-only by at least 15 percentage points with no more than a 5 percentage-point increase in invalid actions.
- Stop condition: Stop if memory does not improve paired task success by at least 10 percentage points on the first 50 episodes or if non-oracle memory updates introduce more than 10 percentage points additional invalid actions.

## Evidence references

- Artifact root: `<local-path>/projects/llm-planner-household-task-memory-comparison-under-fixed-c-aa9258c61d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
