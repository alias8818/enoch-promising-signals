# Pre-action predicate gate for CPU agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pre-action-predicate-gate-for-cpu-agents-c270d142f500`
Run ID: `pre-action-predicate-gate-for-cpu-agents-c270d142f500-20260628T015542249425+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d7fccdab20de

## What looked useful

The gate avoided 105 invalid actions, reduced invalid action rate from 0.875 to 0.000, increased success rate from 0.250 to 0.875, and cost about 4.25 microseconds per gate invocation in the local overhead probe. It also produced 15 conservative false blocks in underspecified-policy cases.

## Boundaries and scale limits

No live LLM agent, production trace distribution, external tool executor, human-labeled corpus, or large-scale deployment was tested. The corpus intentionally stresses predicate-trap scenarios and should not be treated as representative production evidence.

## Claim scope

In a deterministic 120-task synthetic CPU-agent action-selection corpus with explicit preconditions, a pre-action predicate gate eliminated invalid action execution from the gated strategy and improved success rate versus ungated score argmax, with microsecond-scale CPU overhead.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and does not directly validate live CPU-agent behavior.

## Recommended next action

Run the same predicate gate on a bounded set of real or archived CPU-agent tool-call traces with oracle labels for invalid actions and false blocks; stop if false-conservative blocks exceed the invalid-action reduction benefit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay-trace validation of pre-action predicate gates for CPU agents
- Success threshold: At least 50% reduction in invalid or hazardous executions versus ungated argmax, false-conservative block rate below 10%, no more than 5% task completion loss versus the best baseline, and median gate overhead below 1 ms.
- Stop condition: Stop if replay traces are unavailable, labels cannot distinguish invalid actions from conservative halts, false-conservative blocks exceed 10%, or invalid-action reduction is below 25%.

## Evidence references

- Artifact root: `<local-path>/projects/pre-action-predicate-gate-for-cpu-agents-c270d142f500`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
