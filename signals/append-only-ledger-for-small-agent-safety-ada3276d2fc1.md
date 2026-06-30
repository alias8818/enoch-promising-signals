# Append-Only Ledger for Small Agent Safety

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `append-only-ledger-for-small-agent-safety-ada3276d2fc1`
Run ID: `append-only-ledger-for-small-agent-safety-ada3276d2fc1-20260523T220344853686+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4550ade894df

## What looked useful

Append-only logging is not sufficient by itself. Public hash chains missed full chain rewrite and unanchored ledgers missed tail truncation; adding HMAC authentication plus an independent head/count anchor closed those tested gaps with about 19.4k appends/s in single-process Python.

## Boundaries and scale limits

Synthetic traces only; 10,000-action append/verify benchmark and 1,000-action attack matrix. No deployed agents, realistic prompt-injection behavior, concurrent writers, crash recovery, storage-layer append-only enforcement, external timestamping, or secret-management evaluation.

## Claim scope

In deterministic synthetic small-agent action traces on a CPU worker, an HMAC-authenticated hash-chain ledger with independently retained final head and event count detected all tested file-level tampering modes: payload mutation, interior deletion, tail truncation, forged insertion, and attacker-side public hash-chain rewrite.

## Why it stopped

Local synthetic evidence supports a narrower mechanism but is not direct enough for a paper or broad small-agent safety claim.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded work should test the anchored HMAC ledger on real agent traces with crash/restart and concurrent append conditions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-safe anchored HMAC ledger on real small-agent traces
- Success threshold: Detect 100% of the same tampering classes plus crash-induced partial-record corruption across at least 50 real or replayed agent runs, with anchored-ledger overhead below 5% of total agent wall-clock runtime.
- Stop condition: Stop if crash recovery or concurrency creates undetected ledger divergence, or if measured overhead exceeds 10% of total runtime in ordinary small-agent runs.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-ledger-for-small-agent-safety-ada3276d2fc1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
