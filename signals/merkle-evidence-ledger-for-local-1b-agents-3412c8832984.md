# Merkle Evidence Ledger for Local 1B Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `merkle-evidence-ledger-for-local-1b-agents-3412c8832984`
Run ID: `merkle-evidence-ledger-for-local-1b-agents-3412c8832984-20260528T002253326962+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8e6317e9d84d

## What looked useful

The mechanism is fast and correct enough in a bounded synthetic test to justify a real-agent integration follow-up, but the evidence is insufficient for a paper or deployment claim.

## Boundaries and scale limits

Synthetic records only; no real 1B model agent traces, no production persistence engine, no digital signatures or key management, no crash-recovery testing, no adversarial storage, no distributed replication, and no human audit study. CPU-only local benchmark, not a full-scale deployment validation.

## Claim scope

On synthetic local-agent evidence records, a dependency-free batched Merkle ledger with chained batch roots sustained at least 95643 appends/s across 50000-record CPU-only sweeps, verified 20000 sampled inclusion proofs with zero failures, detected 8000/8000 record mutations, and added about 9.6% to 11.0% storage overhead versus raw JSONL.

## Why it stopped

Bounded synthetic evidence supports feasibility but not novelty or real-agent deployment validity; this is not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the ledger into a real local 1B-agent tool loop and compare against hash-chain JSONL plus SQLite/WAL signed-checkpoint baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real 1B-Agent Trace Integration for Merkle Evidence Ledger
- Success threshold: Zero proof failures, zero tamper misses, successful crash recovery with no accepted corrupted batch roots, and less than 10% median end-to-end latency overhead versus the strongest baseline on at least 100 real tool tasks.
- Stop condition: Stop as negative if any baseline gives equivalent tamper localization with lower overhead, if crash recovery accepts corrupted state, or if median end-to-end latency overhead exceeds 25%.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-evidence-ledger-for-local-1b-agents-3412c8832984`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
