# Reversible tool-call ledger for home CPU agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `reversible-tool-call-ledger-for-home-cpu-agents-c9003b79fdcc`
Run ID: `reversible-tool-call-ledger-for-home-cpu-agents-c9003b79fdcc-20260527T201030942256+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0b5705bd13e5

## What looked useful

Mechanism supported locally: inverse-operation logging is storage-efficient and reversible; full-workspace hashing is the main naive CPU bottleneck; incremental state commitments are required for practical home-CPU agents.

## Boundaries and scale limits

Tested only on synthetic writes/deletes over 200 in-memory file paths for 5 trials of 5000 operations. Not tested with real agent traces, shell/network side effects, concurrency, partial-record crash recovery, encrypted/private data, or a production-grade Merkle commitment. The incremental XOR digest is a performance proxy, not a complete adversarial security design.

## Claim scope

In a deterministic synthetic local file-tool workload on one CPU process, a reversible append-only JSONL ledger with inverse operations supported replay, rollback, and tamper detection while using about 1.15% of snapshot logging bytes; an incremental state digest variant avoided the naive full-state-hash bottleneck and exceeded snapshot throughput.

## Why it stopped

No-paper closure: the synthetic benchmark provides a useful mechanism signal but not publication-grade direct evidence for production home CPU agents.

## Recommended next action

Run a bounded follow-up using real agent tool traces plus crash-fault injection and replace the XOR proxy with a Merkleized incremental state commitment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Merkleized reversible ledger on real local-agent tool traces
- Success threshold: Across the real traces, all correctness and crash-fault checks pass, ledger bytes per operation remain below 5% of snapshot logging, and append throughput is at least 5x snapshot logging on the same CPU host.
- Stop condition: Stop if Merkleized append throughput falls below snapshot throughput on two or more traces, if rollback cannot be made deterministic for common tool calls, or if crash recovery cannot reliably identify the last valid committed entry.

## Evidence references

- Artifact root: `<local-path>/projects/reversible-tool-call-ledger-for-home-cpu-agents-c9003b79fdcc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
