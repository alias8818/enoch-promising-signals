# Tiered Memory for Agent Task Reuse

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-memory-for-agent-task-reuse-5a9ab0e690e6`
Run ID: `tiered-memory-for-agent-task-reuse-5a9ab0e690e6-20260611T113759456854+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/867393ad498c

## What looked useful

Tiered task memory is not supported as a general replacement for flat episodic retrieval. The useful signal is a budget-dependent crossover: compact procedure memories can help when context is too tight for enough full examples, but they lose disambiguating detail and are overtaken by flat retrieval once context budget permits multiple episodes.

## Boundaries and scale limits

Synthetic proxy only; no real LLM agents, embedding model, production task traces, learned summarizer, long-horizon drift, or user-facing task success measurement. Sweep used 40 seeds, 240 train tasks, and 360 eval tasks per seed per budget.

## Claim scope

In a deterministic synthetic repeated-task benchmark with 16 latent procedures and fixed retrieval budgets, promoted tiered procedure memory slightly outperformed flat episodic retrieval only at very tight context budgets of 160-240 synthetic tokens, while flat episodic retrieval dominated from 320 tokens upward.

## Why it stopped

No-paper closure: synthetic evidence is mixed and contradicts the broad hypothesis outside very tight context budgets, but it gives a concrete bounded mechanism for a direct follow-up.

## Recommended next action

Run a bounded real-agent replay follow-up that tests adaptive routing between compact procedures and flat episodes on natural task traces under matched sequence-item budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Tiered-vs-Flat Memory Routing on Real Agent Task Replays
- Success threshold: Adaptive routing improves token cost by at least 20% at no more than 2 percentage points task-success loss versus flat-only retrieval, or improves task success at equal token budget, across at least 3 task families.
- Stop condition: Stop if adaptive routing fails to beat flat-only retrieval on either token cost at matched success or success at matched sequence-item budget in two representative task families.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-memory-for-agent-task-reuse-5a9ab0e690e6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
