# Concurrent Tiny-Agent Ledger Replay With Torn-Write Recovery

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `concurrent-tiny-agent-ledger-replay-with-torn-write-recove-756b84761b`
Run ID: `concurrent-tiny-agent-ledger-replay-with-torn-write-recove-756b84761b-20260529T120511580068+0000`

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

- Parent run decision: Real Tiny-Agent Ledger Replay and Crash-Recovery Test: enoch://control-plane/projects/real-tiny-agent-ledger-replay-and-crash-recovery-test-44461de71a/runs/real-tiny-agent-ledger-replay-and-crash-recovery-test-44461de71a-20260529T084206951705+0000
- Parent run decision: Tiny Agent Evidence Ledger: enoch://control-plane/projects/tiny-agent-evidence-ledger-a9d14b1b6ca9/runs/tiny-agent-evidence-ledger-a9d14b1b6ca9-20260528T145913291533+0000

## What looked useful

Framed CRC replay works for torn-tail recovery, but the no-CRC ablation and tolerant JSONL baseline also achieved 25/25 exact-prefix recovery; the active mechanism in this test is length-delimited stop-at-partial replay rather than CRC.

## Boundaries and scale limits

Synthetic records, shared userspace append lock, local filesystem, explicit partial-tail injection, no real power loss, no multi-process unlocked append race, no non-tail corruption, and no long production replay/compaction workload.

## Claim scope

On a local CPU-only fixed-seed filesystem harness with 16 concurrent logical agents, 128 records per agent, and injected partial final writes, length-delimited framed replay with CRC recovered exactly the committed prefix in 25/25 trials with zero false records.

## Why it stopped

Medium local evidence supports torn-tail prefix recovery but does not establish a novel or paper-ready advantage over tolerant JSONL or SQLite WAL, and the CRC mechanism was not necessary under the tested fault model.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up only if testing completed-frame corruption or process-kill filesystem crashes is desired.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CRC Framing Under Completed-Frame Corruption and Process-Kill Crashes
- Success threshold: CRC framing has zero false accepted records and at least 99% exact-prefix recovery across 100+ corruption/crash trials while length-only or tolerant JSONL shows a measurable false-accept or replay-failure rate.
- Stop condition: Stop if no-CRC framing and tolerant JSONL still match CRC framing on false-record and exact-prefix metrics across the completed-frame corruption and process-kill scenarios.

## Evidence references

- Artifact root: `<local-path>/projects/concurrent-tiny-agent-ledger-replay-with-torn-write-recove-756b84761b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
