# Real local-agent evidence ledger with nondeterministic tools

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-local-agent-evidence-ledger-with-nondeterministic-too-5629f0c008`
Run ID: `real-local-agent-evidence-ledger-with-nondeterministic-too-5629f0c008-20260604T003530948280+0000`

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
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae55cc497071

## What looked useful

Full raw evidence ledger replayed 1000/1000 nondeterministic decisions and rejected 1000/1000 tampered ledgers; summary-only and hash-only baselines replayed 0/1000 decisions.

## Boundaries and scale limits

Synthetic local tool only; no real browser/web/shell agent integration, no cross-process persistence test, no signing/key management, no hostile OS model, and no comparison against production provenance systems.

## Claim scope

In a controlled local Python simulator with nondeterministic tool outputs, an append-only ledger containing raw observations, payload hashes, tool identity, and hash-linked events enabled exact agent-decision replay and simple tamper detection across 1000 episodes.

## Why it stopped

Controlled Tier 1 evidence supports the mechanism but remains synthetic/local and is not paper-positive direct evidence for real local-agent tools.

## Recommended next action

Run a bounded deepen follow-up that instruments two real local tools, persists the ledger to disk, restarts the agent, and verifies replay/tamper detection from reloaded artifacts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent real-tool evidence ledger replay after agent restart
- Success threshold: Across at least 300 real-tool episodes, full ledger exact replay rate >= 0.99, tamper detection rate = 1.0 for all scripted cases, and both baselines fail exact replay materially more often than the full ledger.
- Stop condition: Stop negative if full ledger replay falls below 0.95, any scripted tamper class is not detected, or replay requires hidden in-memory state not present in the durable ledger.

## Evidence references

- Artifact root: `<local-path>/projects/real-local-agent-evidence-ledger-with-nondeterministic-too-5629f0c008`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
