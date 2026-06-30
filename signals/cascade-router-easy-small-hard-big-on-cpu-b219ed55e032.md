# Cascade Router: Easy->Small, Hard->Big on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cascade-router-easy-small-hard-big-on-cpu-b219ed55e032`
Run ID: `cascade-router-easy-small-hard-big-on-cpu-b219ed55e032-20260621T083932857445+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/92728ff62b1b

## What looked useful

The cascade mechanism worked when competence boundaries were explicit: all-small was fast but only 65.00% accurate, all-big was 100.00% accurate but used 5.9180 CPU seconds, and the best cascade preserved 100.00% accuracy with 2.0612 CPU seconds on the same 600-task suite.

## Boundaries and scale limits

The small and big systems are deterministic solvers, not language models; task hardness is generated and feature-separable; the big-solver cost is simulated with deterministic CPU burn. Results should not be generalized to learned routers, real prompts, real model quality, or production CPU inference without direct model evidence.

## Claim scope

On a deterministic synthetic arithmetic CPU benchmark with 600 tasks, a cheap router sent easy cases to a strict small solver and hard cases to a slower full solver, matching all-big accuracy while reducing measured CPU time by 2.45x to 2.87x depending on router rule.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is proxy-only and not a full validation of real LLM routing.

## Recommended next action

Stop this run as a no-paper useful signal; next run should replace the deterministic solvers with two actual CPU-hosted models and keep the same all-small/all-big/cascade policy comparison.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU LLM cascade router with real small and larger local models
- Success threshold: Cascade accuracy is within 1 percentage point of all-big and wall-clock is at least 25% lower than all-big on the same task set.
- Stop condition: Stop early if the router sends more than 5% of hard tasks to the small model or if cascade accuracy drops more than 3 percentage points below all-big in the first 100 scored examples.

## Evidence references

- Artifact root: `<local-path>/projects/cascade-router-easy-small-hard-big-on-cpu-b219ed55e032`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
