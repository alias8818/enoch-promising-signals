# Evidence-Ledger Agent with Cryptographic Claim Chain

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-with-cryptographic-claim-chain-f1c4aeeeea30`
Run ID: `evidence-ledger-agent-with-cryptographic-claim-chain-f1c4aeeeea30-20260622T004942338586+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/46b12fc240fc

## What looked useful

Hash-chain plus evidence Merkle roots and HMAC seals verified at about 63098 claims/s and appended at about 53615 claims/s on the 10000-claim run. Chain-only verification detected 5 of 6 tamper classes and missed tail truncation; adding a sealed head/count checkpoint detected all 6.

## Boundaries and scale limits

Tested only on synthetic JSONL ledgers up to 10000 claims with 3 evidence records per claim on one local CPU process. Did not test real LLM agents, real retrieval corpora, public-key signatures, external timestamping, multi-writer replication, key compromise, or human claim quality.

## Claim scope

A stdlib local prototype can cryptographically bind synthetic claim records to evidence payloads and prior ledger state with practical local throughput; completeness against tail truncation requires an anchored checkpoint or equivalent expected head/count evidence.

## Why it stopped

No-paper useful signal: the local prototype supports the integrity mechanism but the evidence is synthetic and shows that completeness claims need checkpoint anchoring.

## Recommended next action

Run a bounded deepen test by integrating the ledger into a real retrieval agent and requiring signed checkpoint anchoring plus replay verification over real evidence payloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Retrieval-agent evidence ledger with signed checkpoint anchoring
- Success threshold: On at least 100 realistic agent answers, replay verification succeeds for untampered runs, all defined tamper classes are detected with anchoring, and median end-to-end latency overhead remains below 2x versus the same agent without ledger writes.
- Stop condition: Stop if signed checkpoint anchoring cannot detect tail truncation, if replay cannot reconstruct claim evidence bindings, or if median latency overhead exceeds 2x on the 100-answer benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-with-cryptographic-claim-chain-f1c4aeeeea30`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
