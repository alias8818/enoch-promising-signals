# Evidence-ledger tool agent with local rollback

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-tool-agent-with-local-rollback-0348276a0352`
Run ID: `evidence-ledger-tool-agent-with-local-rollback-0348276a0352-20260525T111521496628+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/625d0a40f048

## What looked useful

Across 5,000 trials per policy with 2,448 injected failures, the no-rollback baseline restored 0.0 of failed plans and the ledger restored 1.0; both policies had 1.0 commit correctness on non-failed plans. The ledger cost averaged 10.266 entries and 3,721.38 evidence bytes per trial with a 15.77x relative latency slowdown, though absolute synthetic latency remained sub-millisecond.

## Boundaries and scale limits

Evidence is limited to local in-memory dictionary state, single-process execution, no concurrent transactions, no real LLM/tool traces, no external API side effects, no process-crash recovery, and no comparison against snapshot/checkpoint baselines.

## Claim scope

In a deterministic synthetic local-state tool environment with create, update, append, and delete operations, an evidence ledger recording per-operation pre-state can roll back failed single-transaction plans to their exact pre-plan state while preserving correct commits.

## Why it stopped

Synthetic local evidence supports the rollback mechanism but is insufficient for publication-grade claims about real tool agents.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same mechanism in a real agent harness with durable ledger persistence and a snapshot/checkpoint baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Durable evidence-ledger rollback in a real tool-agent harness
- Success threshold: Ledger restores at least 99% of failed recoverable tasks, preserves 100% commit correctness on non-failed tasks, and uses less storage than full snapshots at comparable recovery correctness.
- Stop condition: Stop if persisted ledger recovery fails to restore exact pre-plan state in more than 5% of recoverable failures or if storage/latency overhead exceeds full snapshots without a compensating recovery benefit.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-tool-agent-with-local-rollback-0348276a0352`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
