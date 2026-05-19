# Process-Level Exact-Anchor Resume in a 1000-Step Tool-Using LangGraph Agent

Status: `useful_signal`
Project ID: `process-level-exact-anchor-resume-in-a-1000-step-tool-usin-38fce41f14`
Run ID: `process-level-exact-anchor-resume-in-a-1000-step-tool-usin-38fce41f14-20260515T150706856032+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Process-Level Exact-Anchor Resume in a 1000-Step Tool-Using LangGraph Agent: internal_generated:process-level-exact-anchor-resume-in-a-1000-step-tool-usin-38fce41f14

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 evidence supports per-step exact-anchor resume, including abrupt process exit, but a real LangGraph SQLite checkpoint baseline achieved the same exact trace metric on the 1000-step benchmark, so the broad claim is not paper-ready or clearly novel.

## Recommended next action

Stop the broad exact-resume paper path; if continuing, narrow to a bounded crash-atomicity and overhead comparison against LangGraph SQLite on production-like tool payloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-Atomic External Side Effects versus LangGraph SQLite Checkpoint Resume
- Success threshold: Process-level anchors must achieve 100% exact external side-effect trace recovery across all injected crash points and seeds, while LangGraph SQLite or interval baselines show a reproducible failure mode or the process-level method shows at least 2x lower mean overhead with no semantic regression.
- Stop condition: Stop if LangGraph SQLite also achieves 100% exact external side-effect recovery under the injected crash points and the process-level method does not show at least a 2x overhead advantage on production-like payloads.

## Evidence references

- Artifact root: `<local-path>/projects/process-level-exact-anchor-resume-in-a-1000-step-tool-usin-38fce41f14`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
