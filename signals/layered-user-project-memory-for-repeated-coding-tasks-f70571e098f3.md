# Layered User/Project Memory for Repeated Coding Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-user-project-memory-for-repeated-coding-tasks-f70571e098f3`
Run ID: `layered-user-project-memory-for-repeated-coding-tasks-f70571e098f3-20260628T083204352080+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/9f1b043331c8

## What looked useful

Layer separation eliminated synthetic cross-scope memory conflicts while project-only memory missed durable user preferences and flat retrieval frequently selected wrong-scope facts.

## Boundaries and scale limits

Synthetic memory facts and deterministic scoring only; no LLM patch generation, no real repository histories, no human preference logs, and no full-scale multi-session assistant evaluation.

## Claim scope

In a deterministic synthetic repeated-coding-task memory selector, a layered user-default plus project-override policy recovered all generated task constraints under a 12-memory budget and avoided project override conflicts that affected flat retrieval.

## Why it stopped

Evidence is a synthetic mechanism probe, not direct real-coding or LLM evidence, so it should not be treated as paper-ready validation.

## Recommended next action

Stop this run as a no-paper useful signal; next run should evaluate layered memory on real repository edit tasks with an LLM and tests/style checks as direct outcomes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-repository LLM evaluation of layered coding-task memory
- Success threshold: Layered memory should reduce convention/preference violations by at least 25% versus the best non-layered baseline while matching or improving test pass rate.
- Stop condition: Stop if layered memory fails to beat the best non-layered baseline on violation rate in two independent repositories or causes a test-pass regression greater than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/layered-user-project-memory-for-repeated-coding-tasks-f70571e098f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
