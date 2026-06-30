# Counterexample-Rich Reliability Benchmark for Small Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-rich-reliability-benchmark-for-small-local-agents-b8824552a7dd`
Run ID: `counterexample-rich-reliability-benchmark-for-small-local-agents-b8824552a7dd-20260613T222035029921+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ffdbb53a6b0a

## What looked useful

The local benchmark met its predefined useful-signal threshold: counterexample-aware rules reached 1.000 accuracy while lure-copy reached 0.0167 accuracy with 1.000 lure-match rate across 60 tasks.

## Boundaries and scale limits

No real local LLM agents were evaluated; tasks are synthetic, prompt-only, exact-match, and limited to six generated families with one seed.

## Claim scope

A deterministic 60-task, six-family counterexample-rich benchmark can be generated and scored locally, and it separates shallow shortcut controls from a counterexample-aware rule control.

## Why it stopped

No-paper useful signal: benchmark construction and deterministic controls succeeded, but this is proxy/control evidence rather than direct small-local-agent reliability evidence.

## Recommended next action

Run a bounded deepen test on two real small local instruct models plus matched non-counterexample controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate counterexample-rich benchmark on small local instruct models with matched controls
- Success threshold: A follow-up is useful if at least one small model has a counterexample-vs-control accuracy gap of at least 0.20 and lure-match rate of at least 0.30 on counterexample tasks, with reproducible saved completions.
- Stop condition: Stop if both models score within 0.05 accuracy of matched controls and lure-match remains below 0.10 across all families, or if no small local model can be installed or run after ordinary dependency setup.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-rich-reliability-benchmark-for-small-local-agents-b8824552a7dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
