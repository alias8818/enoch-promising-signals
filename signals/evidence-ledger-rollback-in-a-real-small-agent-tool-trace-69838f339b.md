# Evidence-ledger rollback in a real small-agent tool-trace harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-in-a-real-small-agent-tool-trace-69838f339b`
Run ID: `evidence-ledger-rollback-in-a-real-small-agent-tool-trace-69838f339b-20260529T101322478201+0000`

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

- Parent run decision: Evidence-ledger rollback for tool-use small agents: enoch://control-plane/projects/evidence-ledger-rollback-for-tool-use-small-agents-d0951e0665b3/runs/evidence-ledger-rollback-for-tool-use-small-agents-d0951e0665b3-20260529T065032674876+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2ce92ee43bde

## What looked useful

Rollback mode leaked 0 of 23 rolled-back observations across four deterministic scenarios plus a 48-step randomized trace; naive append-only mode leaked 23 of 23.

## Boundaries and scale limits

Tested only local deterministic and randomized small traces with Python tools; not tested in LangGraph runtime, LLM-driven planning, concurrent branches, durable checkpoint replay, distributed traces, or production evidence stores.

## Claim scope

In a controlled local small-agent Python tool-trace harness, rollback-aware evidence ledger semantics prevented all observations from failed speculative branches from being visible to final answers, unlike an append-only naive baseline.

## Why it stopped

Tier 1 direct small-harness threshold was met, but evidence is too narrow for publication-grade claims.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is to reproduce the same rollback invariant inside an actual LangGraph checkpoint/replay small-agent harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LangGraph checkpoint/replay evidence-ledger rollback test
- Success threshold: Rollback-integrated framework harness has 0 visible rolled-back observations after checkpoint restore across at least three deterministic traces and one randomized trace; naive baseline leaks at least one rolled-back observation.
- Stop condition: Stop as unsupported if any rolled-back observation remains visible after restore in rollback mode, or if framework callback ordering prevents implementing branch-scoped rollback without external/private changes.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-in-a-real-small-agent-tool-trace-69838f339b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
