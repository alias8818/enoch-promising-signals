# Crash-Injection Baseline Test for Anchored Tool-Agent Evidence Ledgers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `crash-injection-baseline-test-for-anchored-tool-agent-evid-310b91fea5`
Run ID: `crash-injection-baseline-test-for-anchored-tool-agent-evid-310b91fea5-20260529T111421469984+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Tamper-Evident Evidence Ledger for Small Tool Agents: enoch://control-plane/projects/tamper-evident-evidence-ledger-for-small-tool-agents-ea814a10fc40/runs/tamper-evident-evidence-ledger-for-small-tool-agents-ea814a10fc40-20260529T040413314394+0000
- Parent run decision: Real Trace Persistence Test for Anchored Tool-Agent Evidence Ledgers: enoch://control-plane/projects/real-trace-persistence-test-for-anchored-tool-agent-eviden-08de1668ec/runs/real-trace-persistence-test-for-anchored-tool-agent-eviden-08de1668ec-20260529T081203923377+0000

## What looked useful

Anchoring supports a verifiable recovered-prefix mechanism, but it is not a raw crash-recovery improvement over SQLite WAL or fsynced JSONL under process-crash semantics. The no-fsync ablation matched fsync, showing this run cannot validate power-loss durability.

## Boundaries and scale limits

This tested process crashes only, not power loss, kernel writeback loss, torn storage writes, concurrent writers, external timestamping, real LLM/tool traces, or production-scale agent sessions. Raw recovered event count was identical across strategies in this model.

## Claim scope

In a local deterministic child-process crash-injection harness with 2,000 trials, an anchored hash-chain ledger certified a recovered prefix after crashes, averaging 61.68 certified events out of 65.31 recovered events, while JSONL, SQLite WAL, and hash-chain-without-anchor baselines certified 0 events.

## Why it stopped

Tier-2 fixed-seed crash injection produced a useful mixed result but no paper-ready advantage over the real SQLite WAL baseline on raw recovery; the positive mechanism evidence is limited to certified-prefix accounting.

## Recommended next action

Run a bounded storage-fault or tamper-after-crash follow-up that can distinguish fsynced anchors from no-fsync anchors and measure post-crash evidence manipulation detection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Storage-Fault and Tamper Test for Anchored Evidence Ledger Certification
- Success threshold: Anchored fsync must have false_accept_rate 0, tamper_detection_rate at least 99%, and a materially larger certified_count than no-fsync and no-anchor ablations across at least 1,000 fixed-seed trials.
- Stop condition: Stop if fsynced anchoring is not distinguishable from no-fsync/no-anchor controls on certified prefix survival or tamper detection, or if the storage-fault harness cannot validly model dropped unfsynced writes.

## Evidence references

- Artifact root: `<local-path>/projects/crash-injection-baseline-test-for-anchored-tool-agent-evid-310b91fea5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
