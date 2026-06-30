# Agent memory architecture comparison on repeated home tasks with bounded VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-architecture-comparison-on-repeated-home-tasks-with-bounded-vram-b301314082b1`
Run ID: `agent-memory-architecture-comparison-on-repeated-home-tasks-with-bounded-vram-b301314082b1-20260611T101846784050+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/29ac784301c8

## What looked useful

Structured key-value state is a strong baseline for repeated home tasks when the task facts are stable keys with latest-value semantics; transcript or episodic recency buffers waste budget on redundant history and underperform at practical small budgets.

## Boundaries and scale limits

No LLM inference, embodied simulator, real household traces, GPU VRAM pressure, or multi-session human-agent evaluation was run. Memory was modeled as bytes in Python objects/text rather than actual transformer KV-cache or context-window VRAM.

## Claim scope

In a deterministic synthetic repeated-home-task benchmark with bounded byte budgets, structured latest-state memory outperformed sliding transcript memory on complete-task success across 384, 768, 1536, and 3072 byte budgets, with the largest tested delta at 768 bytes.

## Why it stopped

No-paper useful signal: the mechanism is supported in a synthetic proxy, but the original agent/home-task/VRAM claim needs direct LLM-agent evidence before paper writing.

## Recommended next action

Run a bounded direct follow-up using an LLM planner in a household-task simulator with fixed context/token budgets and compare structured-state memory against transcript recency on task success and token/VRAM use.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM planner household-task memory comparison under fixed context budgets
- Success threshold: Structured-state memory improves complete-task success by >=15 percentage points over sliding transcript at equal context budget, with paired confidence interval excluding zero and no unacceptable latency increase.
- Stop condition: Stop if the structured-state delta is <5 percentage points at all tested budgets or if LLM planner failures dominate memory-related failures.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-architecture-comparison-on-repeated-home-tasks-with-bounded-vram-b301314082b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
