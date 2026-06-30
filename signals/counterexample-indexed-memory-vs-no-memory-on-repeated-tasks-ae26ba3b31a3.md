# Counterexample-Indexed Memory vs No-Memory on Repeated Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `counterexample-indexed-memory-vs-no-memory-on-repeated-tasks-ae26ba3b31a3`
Run ID: `counterexample-indexed-memory-vs-no-memory-on-repeated-tasks-ae26ba3b31a3-20260610T200242007705+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc2b9d07cee3

## What looked useful

Counterexample-indexed memory showed 62.87% mean aggregate test reduction across 30 medium matrix conditions and 16.62% mean reduction in a diffuse hot1000 stress probe, but diffuse recurrence caused majority per-task losses and negative median per-task savings.

## Boundaries and scale limits

Evidence is limited to deterministic synthetic Boolean tasks with 3,759 candidates, 8-bit domains, 1,500 tasks per condition, and three seeds per matrix cell. It does not validate real program synthesis, theorem proving, coding-agent, LLM memory, noisy verifier, or production retrieval settings.

## Claim scope

In a synthetic finite CEGIS benchmark with repeated Boolean concept-identification tasks, exact counterexample-set indexed memory reduced aggregate primitive solve cost versus a no-memory fixed-order candidate scan, especially when task recurrence was concentrated.

## Why it stopped

The result is useful but synthetic and mixed: aggregate gains are clear in repeated finite CEGIS tasks, while diffuse-recurrence conditions expose many misleading memory suggestions and majority per-task losses.

## Recommended next action

Stop this run as no-paper synthetic evidence; next run should test a guarded counterexample-memory policy against no-memory and ordinary recency/cache baselines on a real or more realistic repeated CEGIS/program-synthesis workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Guarded Counterexample Memory on Realistic Repeated CEGIS Tasks
- Success threshold: Guarded counterexample memory should reduce aggregate primitive solve cost by at least 25% versus no-memory while keeping per-task loss rate below 35% in diffuse-recurrence conditions.
- Stop condition: Stop if guarded memory fails to beat no-memory aggregate cost or still loses on more than 50% of tasks in two diffuse-recurrence settings.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-indexed-memory-vs-no-memory-on-repeated-tasks-ae26ba3b31a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
