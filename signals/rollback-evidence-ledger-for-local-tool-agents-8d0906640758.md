# Rollback Evidence Ledger for Local Tool Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `rollback-evidence-ledger-for-local-tool-agents-8d0906640758`
Run ID: `rollback-evidence-ledger-for-local-tool-agents-8d0906640758-20260520T051301386101+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d99004ef738a

## What looked useful

The mechanism is viable as a local rollback primitive for file-scoped tool side effects and appears much cheaper than full snapshots on edit-heavy workloads, but the evidence is bounded and not publication-grade.

## Boundaries and scale limits

Synthetic file create/edit/delete workloads only; no real LLM agent traces, shell side effects, package-manager mutations, symlinks, permissions, crash consistency, concurrent tools, or large binary repositories were tested.

## Claim scope

In deterministic synthetic filesystem-only local-agent workloads with hundreds of files and operations, a preimage-hash evidence ledger restored all non-tamper workspaces byte-for-byte, detected injected ledger-object corruption, and used 0.18% to 0.78% of full per-step snapshot storage.

## Why it stopped

Bounded proxy evidence supports the mechanism, but direct real-agent and crash-consistency evidence is required before a paper claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is replaying real local-agent traces with crash/fault injection around ledger commits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay real local-agent traces with crash-injected rollback ledger commits
- Success threshold: At least 95% successful rollback across non-destructive real-agent trace cases, 100% detection of injected ledger-object corruption, and median ledger storage below 10% of full per-step snapshots on file-scoped traces.
- Stop condition: Stop if any non-tamper rollback mismatch is reproducible without an identified unsupported side-effect class, or if ledger storage exceeds 50% of full snapshots on median real traces.

## Evidence references

- Artifact root: `<local-path>/projects/rollback-evidence-ledger-for-local-tool-agents-8d0906640758`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
