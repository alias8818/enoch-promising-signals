# Real Agent Tool-Call Ledger Integration With External Anchors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-tool-call-ledger-integration-with-external-anch-59ccac4e2d`
Run ID: `real-agent-tool-call-ledger-integration-with-external-anch-59ccac4e2d-20260610T174121244278+0000`

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

- Parent run decision: Tamper-Evident Evidence Ledger for Agent Tool Calls: enoch://control-plane/projects/tamper-evident-evidence-ledger-for-agent-tool-calls-0e7eb1d87a2c/runs/tamper-evident-evidence-ledger-for-agent-tool-calls-0e7eb1d87a2c-20260610T170322432710+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/74bbef087b46

## What looked useful

External root anchors closed the specific ledger-only gap: rewritten tampered ledgers passed internal hash-chain verification in 10/10 trials, while anchored verification rejected 10/10; clean ledgers were accepted in 10/10.

## Boundaries and scale limits

Small deterministic local agent, local JSONL anchor store, single process, no remote transparency log, no production model/tool runtime, no multi-writer concurrency, and no anchor compromise model.

## Claim scope

In a controlled local mini-agent with 600 real tool calls across 10 trials, a hash-chained tool-call ledger with independent root anchors detected 100% of post-hoc rewritten ledgers that were internally hash-consistent and accepted by ledger-only verification.

## Why it stopped

No-paper useful signal: the Tier 1 direct local mechanism test succeeded, but evidence is not broad or external enough for publication-grade claims.

## Recommended next action

Run a bounded deepen test using a real remote append-only anchor or transparency-log service and a production agent runtime, with the same rewrite-tamper threshold plus concurrency failure cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Remote Transparency Anchor Test for Agent Tool-Call Ledgers
- Success threshold: At least 99% clean-ledger acceptance, 100% rejection of internally consistent rewritten ledger attacks, 100% rejection of naive corruptions, and less than 5% mean wall-clock overhead versus unanchored ledger recording on the bounded workload.
- Stop condition: Stop as negative if rewritten tamper is accepted by anchored verification, clean-ledger false rejects exceed 1%, or mean overhead exceeds 5% after implementation-level fixes.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-tool-call-ledger-integration-with-external-anch-59ccac4e2d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
