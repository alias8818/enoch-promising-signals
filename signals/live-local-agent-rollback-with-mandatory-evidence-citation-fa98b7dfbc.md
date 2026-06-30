# Live local-agent rollback with mandatory evidence citations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-local-agent-rollback-with-mandatory-evidence-citation-fa98b7dfbc`
Run ID: `live-local-agent-rollback-with-mandatory-evidence-citation-fa98b7dfbc-20260527T190931120324+0000`

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

- Parent run decision: Evidence-Ledger Agent Rollback on CPU: enoch://control-plane/projects/evidence-ledger-agent-rollback-on-cpu-3e406a111087/runs/evidence-ledger-agent-rollback-on-cpu-3e406a111087-20260527T135143911097+0000
- Parent run decision: Evidence-ledger rollback on realistic agent traces: enoch://control-plane/projects/evidence-ledger-rollback-on-realistic-agent-traces-ae5a27b438/runs/evidence-ledger-rollback-on-realistic-agent-traces-ae5a27b438-20260527T171604050258+0000

## What looked useful

Evidence rollback achieved 0.605 exact success and 0.000 corruption rate versus unguarded baseline 0.070 exact success and 0.916 corruption rate; citation-audit-only did not improve corruption, and test-only rollback still had 0.760 corruption rate.

## Boundaries and scale limits

Synthetic compact key/value workspaces and heuristic seeded agent; no live LLM agent, full repository edits, real terminal evidence, or production trace replay. The result supports the control-flow mechanism but not external validity for deployed coding agents.

## Claim scope

In a deterministic seeded local-agent file-edit harness with 5 fixed seeds, 1,000 episodes, a real unguarded baseline, rollback-only and citation-audit-only ablations, mandatory evidence citations connected to live rollback eliminated persisted invariant corruption and improved exact task success versus controls.

## Why it stopped

Tier 2 synthetic harness supports the rollback-with-citations mechanism but does not provide publication-grade evidence over real agents or repositories.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is replaying the four-policy comparison on real local-agent traces with command-output citations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace replay validation for evidence-cited local-agent rollback
- Success threshold: Evidence-triggered rollback reduces persisted corruption by at least 50% versus unguarded and at least 25% versus test-only rollback, with task success no more than 10 percentage points below the best baseline/control.
- Stop condition: Stop if fewer than 30 usable traces can be collected locally, or if evidence rollback fails to reduce persisted corruption versus test-only rollback on the first 15 traces.

## Evidence references

- Artifact root: `<local-path>/projects/live-local-agent-rollback-with-mandatory-evidence-citation-fa98b7dfbc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
