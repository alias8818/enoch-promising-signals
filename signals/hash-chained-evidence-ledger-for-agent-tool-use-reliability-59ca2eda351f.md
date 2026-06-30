# Hash-Chained Evidence Ledger for Agent Tool-Use Reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chained-evidence-ledger-for-agent-tool-use-reliability-59ca2eda351f`
Run ID: `hash-chained-evidence-ledger-for-agent-tool-use-reliability-59ca2eda351f-20260621T211214367058+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd900f1ea238

## What looked useful

Anchored hash chains provide strong local tamper evidence for partial-compromise or post-hoc trace mutation assumptions at about 1.97x storage and 2.57x write-time overhead in this Python prototype, but the trust boundary around anchor/signing storage is decisive.

## Boundaries and scale limits

Synthetic traces only; no real agent framework integration, no concurrent append path, no crash recovery, no external write-once anchor, and no human audit usability test. Main run covered 1000 episodes, 12 events per episode, and 7000 total tamper trials.

## Claim scope

In a synthetic local agent tool-use trace model, an HMAC-anchored SHA-256 hash-chain ledger detected payload mutation, status flip, deletion, insertion, reorder, and chain recomputation without anchor update at 1000/1000 trials per condition, while ordinary structured JSON validation detected only adjacent reorder. The mechanism did not detect a privileged adversary that rewrote both chain and trusted anchor.

## Why it stopped

No-paper useful signal: the result is synthetic and mechanism-focused, and public context indicates hash-chained AI-agent audit ledgers are already an active known direction.

## Recommended next action

Run a bounded real-agent middleware follow-up that logs actual tool calls, stores anchors outside the log directory, and tests concurrent writes plus crash recovery.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent anchored evidence ledger with concurrent append and crash recovery
- Success threshold: Detect at least 99% of non-privileged tampering attempts, detect truncation/forking after crash through anchor mismatch, and keep median per-event logging overhead below 5 ms on local hardware.
- Stop condition: Stop if integration cannot preserve ordering under concurrent writes, if crash recovery silently accepts a truncated or forked ledger, or if median per-event overhead exceeds 25 ms after straightforward batching.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-evidence-ledger-for-agent-tool-use-reliability-59ca2eda351f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
