# ChaosEvidence: Failure-Injection Recovery with Evidence Replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `chaosevidence-failure-injection-recovery-with-evidence-replay-27456324fa63`
Run ID: `chaosevidence-failure-injection-recovery-with-evidence-replay-27456324fa63-20260609T232358091727+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4c3df127b157

## What looked useful

Across 13,000 trials per strategy, evidence replay achieved 1.0 success rate and zero duplicates; checkpoint-only recovery failed every after_call_before_checkpoint window and naive retry duplicated earlier side effects in most crash scenarios.

## Boundaries and scale limits

Single-process CPU-only simulation; no real process kills, durable database, network partitions, concurrent recovery, stale reads, production workflow engine, or high-throughput service workload was tested.

## Claim scope

In a deterministic synthetic three-step workflow with idempotent/queryable external side-effect ledgers, evidence replay using stable operation keys prevents duplicate side effects across injected crash windows that break naive retry and checkpoint-only recovery.

## Why it stopped

No-paper useful signal: the current evidence is synthetic/proxy evidence that supports the mechanism but is not direct production-grade validation.

## Recommended next action

Run a bounded durable-process follow-up with a file-backed evidence store, actual worker kills, and an HTTP service exposing idempotency-key reconciliation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Durable Process-Kill Evidence Replay for Idempotent HTTP Side Effects
- Success threshold: Evidence replay has zero duplicate and zero missing side effects across at least 100 process-kill trials per crash window, while checkpoint-only recovery duplicates at least one after-call-before-checkpoint side effect.
- Stop condition: Stop if evidence replay produces any duplicate side effect under reliable idempotency-key reconciliation, or if the durable harness cannot inject and verify process-kill windows reproducibly.

## Evidence references

- Artifact root: `<local-path>/projects/chaosevidence-failure-injection-recovery-with-evidence-replay-27456324fa63`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
