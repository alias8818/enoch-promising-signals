# Tiered memory: notes, project state, predictive operator updates

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiered-memory-notes-project-state-predictive-operator-updates-90fb1e1bac29`
Run ID: `tiered-memory-notes-project-state-predictive-operator-updates-90fb1e1bac29-20260613T120036325351+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3e5761862387

## What looked useful

Across budgets 150-400, tiered predictive memory improved mean state F1 by about +0.49 to +0.58 over flat logs. The predictive component improved over non-predictive tiered memory by about +0.003 to +0.006 state F1 in the sweep and +0.006 in the 100-seed medium run.

## Boundaries and scale limits

Synthetic events only; no real operator traces, natural-language note extraction, LLM context effects, human handoff tasks, or production workload diversity. CPU-only local runs: smoke, 100-seed medium run, and 50-seed budget sweep.

## Claim scope

In a deterministic synthetic project-event benchmark with fixed approximate token budgets, tiered project memory preserves current project state substantially better than flat chronological notes, and predictive refresh adds a small repeatable gain over non-predictive tiering.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a synthetic/proxy benchmark, not direct production trace or human/LLM handoff validation.

## Recommended next action

Run a bounded deepen test on real Enoch or agent project histories with natural-language notes and downstream handoff queries before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace tiered memory handoff benchmark
- Success threshold: At least +0.10 absolute handoff-answer F1 for tiered memory over flat logs and at least +0.02 targeted artifact/blocker recall from predictive refresh over non-predictive tiering at matched budgets.
- Stop condition: Stop if tiered memory fails to beat flat logs by +0.05 handoff-answer F1 on real traces, or if predictive refresh adds less than +0.01 targeted recall while increasing complexity.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-memory-notes-project-state-predictive-operator-updates-90fb1e1bac29`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
