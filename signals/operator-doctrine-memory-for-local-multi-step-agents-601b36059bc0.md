# Operator-Doctrine Memory for Local Multi-Step Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-for-local-multi-step-agents-601b36059bc0`
Run ID: `operator-doctrine-memory-for-local-multi-step-agents-601b36059bc0-20260630T113654057445+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/98942fa828f9

## What looked useful

Doctrine memory reached 77.5% accuracy versus 40.8% no-memory and 47.5% recent-context over 120 paired episodes, with 44 paired wins/0 losses against no-memory and 36 paired wins/0 losses against recent-context. Full doctrine remained better at 90.0%, and secret-protection remained weak at 35% under compact memory.

## Boundaries and scale limits

Synthetic episodes only; no real tool execution, no real autonomous coding-agent traces, no learned memory extraction, no retrieval failures, one small local instruction model, and compact doctrine memory underperformed full original doctrine, especially on secret-protection cases.

## Claim scope

On a synthetic multiple-choice benchmark using Qwen/Qwen2.5-0.5B-Instruct, injecting a compact persistent operator-doctrine memory after context truncation improved final action-choice accuracy versus no-memory and recent-context controls across 120 paired episodes.

## Why it stopped

Bounded synthetic useful signal obtained, but evidence is not paper-ready because the benchmark is proxy-only and uses hand-authored memory rather than a real agent memory pipeline.

## Recommended next action

Run a deepen follow-up in a real tool-using local agent harness with automatic doctrine extraction/retrieval and held-out multi-step tasks; require at least +15 percentage points over recent-context and no secret-protection regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Automatic Doctrine Memory in a Real Local Tool-Using Agent Harness
- Success threshold: At least +15 percentage points accuracy over recent-context on held-out tool-use tasks, paired losses not exceeding paired wins in any safety category, and secret-protection accuracy at least matching full-doctrine within 10 percentage points.
- Stop condition: Stop as negative if automatic doctrine memory fails to beat recent-context by 10 percentage points overall or causes any secret-protection regression versus recent-context.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-for-local-multi-step-agents-601b36059bc0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
