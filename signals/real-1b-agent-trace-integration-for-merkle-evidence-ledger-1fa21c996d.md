# Real 1B-Agent Trace Integration for Merkle Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-1b-agent-trace-integration-for-merkle-evidence-ledger-1fa21c996d`
Run ID: `real-1b-agent-trace-integration-for-merkle-evidence-ledger-1fa21c996d-20260528T054643294794+0000`

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

- Parent run decision: Merkle Evidence Ledger for Local 1B Agents: enoch://control-plane/projects/merkle-evidence-ledger-for-local-1b-agents-3412c8832984/runs/merkle-evidence-ledger-for-local-1b-agents-3412c8832984-20260528T002253326962+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8e6317e9d84d

## What looked useful

Real 1B-class model trace integration worked mechanically: all 32 records verified, p95 proof verification was 0.0068 ms, storage overhead was 1.09x raw JSONL, and all four tested tamper modes changed the committed root.

## Boundaries and scale limits

Small single-process run only: 8 tasks, 32 records, harness-controlled tool selection, no crash/restart campaign, no externally signed checkpoint publication, no distributed storage, no human audit study, and no long heterogeneous production trace.

## Claim scope

In an eight-task controlled local TinyLlama 1.1B trace, a batched Merkle evidence ledger recorded model generations, tool observations, and final answers with zero inclusion-proof failures, zero observation-binding failures, and detection of mutation, deletion, reorder, and append-after-checkpoint tampering against a committed root.

## Why it stopped

No-paper useful signal: the Tier 1 controlled direct integration threshold was met, but the evidence is too small and harness-controlled for publication readiness.

## Recommended next action

Run a bounded deepen follow-up inside an agent framework with model-parsed tool calls, crash/restart injection, externally published signed roots, and hash-chain JSONL plus SQLite/WAL baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-Recovered Agent-Framework Merkle Ledger with Model-Parsed Tool Calls
- Success threshold: Zero proof failures and zero recovery-root mismatches after at least 10 injected crashes, all tested tamper cases detected against published roots, p95 proof verification below 1 ms, and storage overhead below 1.25x raw JSONL.
- Stop condition: Stop if model-parsed tool calls cannot produce at least 40 valid tasks, if any crash recovery loses committed records, or if Merkle storage overhead exceeds 1.5x raw JSONL in the bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/real-1b-agent-trace-integration-for-merkle-evidence-ledger-1fa21c996d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
