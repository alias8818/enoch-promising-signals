# Persistent real-tool evidence ledger replay after agent restart

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `persistent-real-tool-evidence-ledger-replay-after-agent-re-e7cf00ba94`
Run ID: `persistent-real-tool-evidence-ledger-replay-after-agent-re-e7cf00ba94-20260604T022701707122+0000`

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

- Parent run decision: Evidence ledger for small local tool-calling agents: enoch://control-plane/projects/evidence-ledger-for-small-local-tool-calling-agents-91683b6de3d0/runs/evidence-ledger-for-small-local-tool-calling-agents-91683b6de3d0-20260603T210723697709+0000
- Parent run decision: Real local-agent evidence ledger with nondeterministic tools: enoch://control-plane/projects/real-local-agent-evidence-ledger-with-nondeterministic-too-5629f0c008/runs/real-local-agent-evidence-ledger-with-nondeterministic-too-5629f0c008-20260604T003530948280+0000

## What looked useful

Across 100 fixed seeds, four task families, and 2,400 total variant trials, verified ledger replay achieved 400/400 successes with zero post-restart tool calls; no-ledger, missing-ledger, verified-corrupt, and unverified-corrupt controls achieved 0/400 successes; rerunning tools also achieved 400/400 successes but required one post-restart discovery command per trial.

## Boundaries and scale limits

The validation used synthetic tasks, one key evidence item per task, scripted policies, local files/subprocesses, and simulated restart by discarding in-memory state. It did not test a live LLM agent, long multi-step trajectories, concurrent tool streams, production controller crashes, partial writes, schema migrations, or external services.

## Claim scope

In a deterministic local harness with real subprocess/file tools, synthetic workspaces, fixed seeds, and scripted agents, verified persistent evidence-ledger replay preserved task-relevant tool observations across a simulated hard restart and matched a rerun-tools baseline while using zero post-restart discovery calls.

## Why it stopped

No-paper closure: the mechanism is supported by medium deterministic local evidence, but the agents and tasks are synthetic and scripted, so this is not publication-grade direct evidence for real autonomous agents.

## Recommended next action

Run a bounded real-agent follow-up using an LLM or production Enoch worker trace with multi-step tool trajectories, forced process restart, partial-ledger ablations, and the same replay/no-ledger/rerun baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent evidence-ledger replay under forced restart
- Success threshold: Verified replay reaches at least 90% task success, is within 5 percentage points of rerun-tools success, reduces post-restart discovery calls by at least 50%, and detects 100% of intentionally corrupted ledger entries.
- Stop condition: Stop if verified replay success is below 80%, if replay cannot reliably reconstruct multi-step evidence after restart, or if integrity checks miss any intentionally corrupted target-evidence entry.

## Evidence references

- Artifact root: `<local-path>/projects/persistent-real-tool-evidence-ledger-replay-after-agent-re-e7cf00ba94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
