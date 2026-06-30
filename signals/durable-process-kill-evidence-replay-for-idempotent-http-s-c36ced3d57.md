# Durable Process-Kill Evidence Replay for Idempotent HTTP Side Effects

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `durable-process-kill-evidence-replay-for-idempotent-http-s-c36ced3d57`
Run ID: `durable-process-kill-evidence-replay-for-idempotent-http-s-c36ced3d57-20260610T042921989528+0000`

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

- Parent run decision: ChaosEvidence: Failure-Injection Recovery with Evidence Replay: enoch://control-plane/projects/chaosevidence-failure-injection-recovery-with-evidence-replay-27456324fa63/runs/chaosevidence-failure-injection-recovery-with-evidence-replay-27456324fa63-20260609T232358091727+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4c3df127b157

## What looked useful

Durable process-kill evidence replay is mechanistically supported for idempotent HTTP side effects in a controlled local direct test, but the evidence is not broad enough for publication readiness.

## Boundaries and scale limits

Single-host local HTTP only; SQLite row insert side effect only; no network partition, power loss, replicated server state, concurrent duplicate clients, server crash during commit, or real third-party API was tested.

## Claim scope

In a local Python HTTP service with persistent SQLite idempotency state, client-side fsynced intent/evidence replay using a stable idempotency key recovered from SIGKILL at three request/response cutpoints with exactly one persisted side effect in 30/30 durable trials; a naive fresh-key retry control duplicated the side effect in 10/10 trials.

## Why it stopped

Tier 1 direct local validation threshold was met, but this remains bounded mechanism evidence rather than full production or publication-grade validation.

## Recommended next action

Run a bounded deepen test that adds server crashpoints, concurrent recovery workers, and network timeout/reset injection before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash and Concurrency Fault Injection for Durable Idempotent HTTP Replay
- Success threshold: Across at least 100 direct fault-injection trials, stable-key durable replay has zero duplicate side effects and completes or reports a recoverable pending state; naive or fresh-key retry duplicates in the ambiguous post-commit cases.
- Stop condition: Stop if any stable-key durable replay trial creates more than one persisted side effect for the same logical operation, or if the harness cannot distinguish pending from completed operations after recovery.

## Evidence references

- Artifact root: `<local-path>/projects/durable-process-kill-evidence-replay-for-idempotent-http-s-c36ced3d57`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
