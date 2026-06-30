# Memory That Learns Reusable Operator Doctrine

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-that-learns-reusable-operator-doctrine-863ce8198019`
Run ID: `memory-that-learns-reusable-operator-doctrine-863ce8198019-20260628T233632058055+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/aa15f41a92c5

## What looked useful

Across 10 motif seeds, learned-memory solve rate averaged 0.6425 versus 0.27125 primitive-only and 0.36875 random-macro control. In random/no-motif tasks, learned memory still averaged 0.55 versus 0.325 primitive-only and 0.4625 random macros, indicating part of the gain is generic compression rather than fully semantic doctrine reuse.

## Boundaries and scale limits

Synthetic symbolic tasks only; no neural training, no real operator doctrine traces, no natural-language transfer, and no production agent workflows. Training traces are obtained with a larger offline primitive search budget, and memory construction cost is not charged as part of test-time solving.

## Claim scope

In a toy modular-arithmetic compositional search benchmark with repeated hidden motifs, mining frequent operator subsequences from solved traces and reusing them as macros improves shallow-budget task solve rate versus primitive-only search and random macro controls.

## Why it stopped

No-paper useful signal: the mechanism is supported only in a toy/proxy benchmark and is not a full validation of reusable operator doctrine in real agents or neural memory systems.

## Recommended next action

Run a bounded deepen follow-up on a recognized compositional task suite or real agent trace DSL with explicit memory construction cost and matched action-space controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Reusable doctrine memory on realistic compositional agent traces
- Success threshold: Learned memory improves held-out solve rate by at least 15 percentage points over primitive-only and at least 10 percentage points over random/stale macro controls without increasing total accounted compute by more than 2x.
- Stop condition: Stop if learned memory does not beat random/stale macro controls on at least 8 of 10 seeds or if accounting for memory construction removes the advantage.

## Evidence references

- Artifact root: `<local-path>/projects/memory-that-learns-reusable-operator-doctrine-863ce8198019`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
