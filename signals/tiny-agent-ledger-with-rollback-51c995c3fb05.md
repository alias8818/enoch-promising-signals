# Tiny Agent Ledger with Rollback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-agent-ledger-with-rollback-51c995c3fb05`
Run ID: `tiny-agent-ledger-with-rollback-51c995c3fb05-20260528T133113364876+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/093bcd84ab6e

## What looked useful

Across 50 randomized trials with 10,312 injected failures, ledger rollback matched the atomic oracle in 50/50 trials while no rollback matched 0/50. In the 2,400-transaction benchmark, ledger rollback matched the oracle and had 0.197s median runtime versus 2.706s for snapshot rollback, but reached about 111 MB median peak traced allocation for 12,672 committed events.

## Boundaries and scale limits

The evidence is local and synthetic: no real LLM/tool agent, no durable storage, no concurrency, no external side-effect recovery, no nested transactions, and high in-memory event overhead in the prototype.

## Claim scope

In a toy dict-backed agent-state simulation with randomized injected mid-transaction failures, a tiny reversible mutation ledger preserved atomic rollback correctness and ran faster than full-state snapshot rollback.

## Why it stopped

No-paper useful signal: the mechanism is supported in a toy simulation, but memory overhead and missing real-agent durability/concurrency evidence make the result insufficient for paper writing.

## Recommended next action

Run a bounded deepen follow-up that implements compact or streamed event storage and reruns the same oracle-correctness and benchmark suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compact Tiny Agent Ledger Event Encoding
- Success threshold: 50/50 oracle correctness, peak traced allocation <= 11,137,792 bytes, and median runtime below snapshot rollback on the 2,400-transaction benchmark.
- Stop condition: Stop if compact or streamed ledger fails oracle correctness in any trial, or if peak memory remains above 25% of the current prototype after one implementation pass.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-ledger-with-rollback-51c995c3fb05`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
