# Append-Only Evidence Ledger for Tool-Using CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `append-only-evidence-ledger-for-tool-using-cpu-agents-c63325ed93f0`
Run ID: `append-only-evidence-ledger-for-tool-using-cpu-agents-c63325ed93f0-20260603T235303994081+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/45d77e07dfa2

## What looked useful

A minimal ledger reached 25,959 ledger writes/s on 50,000-entry synthetic traces, 0.213x plain JSONL throughput, with 1.593x byte overhead. Mutation, middle deletion, and reorder were detected locally; tail truncation was detected only with a checkpointed expected count/final digest.

## Boundaries and scale limits

No real tool-using agent integration, concurrent writers, crash recovery, fsync durability, remote notarization, WORM storage, adversarial host controls, or distributed trace workloads were tested. Tail truncation is not detectable by local hash-chain verification alone; it requires an external expected count/final digest or equivalent checkpoint.

## Claim scope

Synthetic local benchmark of a single-process Python append-only evidence ledger for CPU-agent tool events: SHA-256 hash chaining plus per-entry HMAC produced replay-verifiable JSONL logs and detected payload mutation, middle deletion, adjacent reorder, and checkpointed tail truncation.

## Why it stopped

Synthetic/local evidence supports the mechanism but is not production or paper-grade validation; the key design limitation is that tail truncation needs external checkpoint evidence.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is to integrate the ledger into a real tool-using agent harness with periodic signed checkpoints and crash/concurrency tests.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Checkpointed evidence ledger in a live tool-agent harness
- Success threshold: On at least 10000 real or replayed tool calls, verification must pass after normal runs, detect mutation/deletion/reorder/checkpointed truncation, recover cleanly from interrupted runs under the chosen fsync policy, and keep median per-tool logging latency below 20 ms with storage overhead below 2x plain JSONL.
- Stop condition: Stop if checkpointed tail truncation cannot be detected, if crash recovery creates unverifiable ambiguous prefixes, or if median logging latency exceeds 20 ms per tool call on ordinary CPU-agent traces.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-evidence-ledger-for-tool-using-cpu-agents-c63325ed93f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
