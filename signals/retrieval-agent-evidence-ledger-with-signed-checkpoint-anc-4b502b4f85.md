# Retrieval-agent evidence ledger with signed checkpoint anchoring

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `retrieval-agent-evidence-ledger-with-signed-checkpoint-anc-4b502b4f85`
Run ID: `retrieval-agent-evidence-ledger-with-signed-checkpoint-anc-4b502b4f85-20260628T015109428490+0000`

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

- Parent run decision: Evidence-Ledger Agent with Cryptographic Claim Chain: enoch://control-plane/projects/evidence-ledger-agent-with-cryptographic-claim-chain-f1c4aeeeea30/runs/evidence-ledger-agent-with-cryptographic-claim-chain-f1c4aeeeea30-20260622T004942338586+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/46b12fc240fc

## What looked useful

Signed checkpoint anchoring produced a clean Tier 1 mechanism signal: 5/5 tamper cases detected versus 0/5 for the naive baseline, with median build and verify costs near 0.01 ms per event at 512 events.

## Boundaries and scale limits

Synthetic events only; local anchor manifest only; no real retrieval-agent integration, independent transparency service, concurrency, crash recovery, key rotation, key compromise, or long-running ledger growth tested.

## Claim scope

In a controlled local retrieval-agent simulation with 512 retrieval-shaped events, hash-chained evidence entries plus Ed25519-signed checkpoint anchors detected five post-hoc tampering modes that a naive JSONL-style event log accepted.

## Why it stopped

Tier 1 controlled direct test supports the mechanism but remains synthetic/local and is not paper-positive.

## Recommended next action

Run a bounded real-agent follow-up that instruments an actual retrieval QA loop, writes anchors to an independent append-only store, and repeats the same tamper matrix plus crash-recovery cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real retrieval-agent trace ledger with independent checkpoint anchoring
- Success threshold: Clean verification must pass; signed independent-anchor verifier must detect at least 6/6 tamper/crash cases; baseline must miss at least two cases; median append overhead must remain below 2 ms/event on at least 5000 real retrieval events.
- Stop condition: Stop if the verifier misses any post-anchor content modification, deletion, reorder, truncation, or unsigned checkpoint rewrite case, or if median append overhead exceeds 2 ms/event before 5000 events.

## Evidence references

- Artifact root: `<local-path>/projects/retrieval-agent-evidence-ledger-with-signed-checkpoint-anc-4b502b4f85`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
