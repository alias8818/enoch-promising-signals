# Evidence-ledger rollback on real file-system CPU-agent tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-on-real-file-system-cpu-agent-tas-b975726856`
Run ID: `evidence-ledger-rollback-on-real-file-system-cpu-agent-tas-b975726856-20260525T063051455691+0000`

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

- Parent run decision: Evidence-Ledger Rollback for Safer CPU Agents: enoch://control-plane/projects/evidence-ledger-rollback-for-safer-cpu-agents-dd0fef2a67f7/runs/evidence-ledger-rollback-for-safer-cpu-agents-dd0fef2a67f7-20260525T061031013499+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4f14132308e8

## What looked useful

The mechanism works when all filesystem effects pass through the ledgered tool API, and the uninstrumented shell control failed to restore in 20/20 cases, identifying tool gating or OS-level interception as the key boundary for real agents.

## Boundaries and scale limits

Small temporary workspaces only; no live LLM agent, arbitrary shell capture, concurrency, crash recovery, large repository workload, hard links, extended attributes, sparse files, or OS-level bypass prevention was tested.

## Claim scope

A prototype append-only evidence ledger attached to an instrumented CPU-agent filesystem tool layer restored real local filesystem task workspaces exactly after destructive edits, creates, deletes, renames, binary rewrites, permission changes, and symlink retargeting in 60/60 Tier 1 controlled cases.

## Why it stopped

Tier 1 direct mechanism evidence is useful but not paper-ready; the run does not validate live-agent behavior, arbitrary shell operations, crash consistency, or repository-scale robustness.

## Recommended next action

Run a deepen follow-up that replays real or recorded CPU-agent edit sessions through a hardened ledger wrapper with crash injection and shell-bypass prevention, using manifest equality as the success metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-safe and bypass-hardened evidence-ledger rollback for recorded CPU-agent edit sessions
- Success threshold: >=95% exact restore on mediated real-agent sessions, 100% safe recovery or safe abort for injected crash points, and 100% capture/block for defined shell bypass attempts.
- Stop condition: Stop if any mediated session cannot be restored to manifest equality and the failure requires unbounded manual repair, or if shell bypass cannot be captured or blocked without changing the agent execution model.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-on-real-file-system-cpu-agent-tas-b975726856`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
