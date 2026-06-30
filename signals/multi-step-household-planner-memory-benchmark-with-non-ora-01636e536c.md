# Multi-step household planner memory benchmark with non-oracle memory updates

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-step-household-planner-memory-benchmark-with-non-ora-01636e536c`
Run ID: `multi-step-household-planner-memory-benchmark-with-non-ora-01636e536c-20260611T105658118561+0000`

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

- Parent run decision: LLM planner household-task memory comparison under fixed context budgets: enoch://control-plane/projects/llm-planner-household-task-memory-comparison-under-fixed-c-aa9258c61d/runs/llm-planner-household-task-memory-comparison-under-fixed-c-aa9258c61d-20260611T104029723645+0000
- Parent run decision: Agent memory architecture comparison on repeated home tasks with bounded VRAM: enoch://control-plane/projects/agent-memory-architecture-comparison-on-repeated-home-tasks-with-bounded-vram-b301314082b1/runs/agent-memory-architecture-comparison-on-repeated-home-tasks-with-bounded-vram-b301314082b1-20260611T101846784050+0000

## What looked useful

Across 8 fixed seeds, 500 households, 21 days, and 7 policies, the confidence/action memory policy achieved 0.6412 +/- 0.0054 success versus 0.3431 +/- 0.0025 stateless and 0.4727 +/- 0.0046 last-write. Missing units/day fell to 0.3834 versus 0.7866 stateless and 0.6052 last-write. Confidence weighting and action updates were supported by ablations; decay was not.

## Boundaries and scale limits

Synthetic simulator only; deterministic planner; simulated noisy observations; no real household traces, no human users, and no LLM-in-the-loop memory extraction or planning. The decay component was not supported because the no-decay ablation matched the full candidate.

## Claim scope

On a synthetic multi-step household-planning benchmark with noisy partial observations, confidence-weighted non-oracle memory updates with action updates improved planning success and missing-ingredient rates over stateless and last-write baselines across fixed seeds.

## Why it stopped

Tier 2 local validation target was met, but evidence remains synthetic-only and one mechanism component was unsupported, so it is useful signal rather than paper-positive evidence.

## Recommended next action

Stop this run as no-paper useful synthetic evidence; next run should replace simulated observations with an LLM-in-the-loop note-to-memory update benchmark using the same fixed tasks, baselines, ablations, and success/missing/waste metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop household note memory update benchmark
- Success threshold: Confidence/action memory improves success rate by at least 0.10 absolute over last-write with paired 95% CI excluding 0, reduces missing units/day, and keeps unnecessary units/day no higher than stateless by more than 0.05 units/day.
- Stop condition: Stop if the LLM-in-the-loop confidence/action policy fails to beat last-write by 0.05 absolute success on a 2-seed smoke subset, or after the full fixed-seed run if the 0.10 absolute success threshold is not met.

## Evidence references

- Artifact root: `<local-path>/projects/multi-step-household-planner-memory-benchmark-with-non-ora-01636e536c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
