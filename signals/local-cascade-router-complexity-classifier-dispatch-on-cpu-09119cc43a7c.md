# Local cascade router: complexity-classifier dispatch on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `local-cascade-router-complexity-classifier-dispatch-on-cpu-09119cc43a7c`
Run ID: `local-cascade-router-complexity-classifier-dispatch-on-cpu-09119cc43a7c-20260620T224413107748+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/08f267be815c

## What looked useful

Learned routing was materially better than brittle rules under lexical shift: learned NB reached 99.75% accuracy with 49.75% full calls, while the canonical rule router fell to 50.0% accuracy on shifted prompts.

## Boundaries and scale limits

Synthetic/proxy only: no real LLM inference, no natural prompt trace, no concurrent serving load, and full-path cost modeled with deterministic CPU work.

## Claim scope

On deterministic CPU proxy tasks, a tiny local complexity classifier routed about half of prompts to a cheap path while preserving 100.0% canonical accuracy and 99.75% lexical-shift accuracy versus an always-full solver.

## Why it stopped

Bounded proxy produced useful mechanism evidence but not direct model-serving evidence; no paper-positive closure.

## Recommended next action

Run the same harness against two real local CPU-served model paths on a labeled prompt trace before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real local CPU model cascade router validation
- Success threshold: Accuracy within 2 percentage points of always-strong and at least 30% fewer strong-model calls with lower p95 latency on the labeled trace.
- Stop condition: Stop if the router saves less than 20% strong-model calls at the 2 percentage point accuracy-loss bound or if real CPU inference overhead erases latency gains.

## Evidence references

- Artifact root: `<local-path>/projects/local-cascade-router-complexity-classifier-dispatch-on-cpu-09119cc43a7c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
