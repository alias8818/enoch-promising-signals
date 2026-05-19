# Local Agent Evidence Ledger with Cryptographic Task Provenance

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-agent-evidence-ledger-with-cryptographic-task-provenance-f5ba7e47f3f2`
Run ID: `local-agent-evidence-ledger-with-cryptographic-task-provenance-f5ba7e47f3f2-20260513T214006726981+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9dfb8883a5d0

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic prototype evidence supports local tamper detection but is not direct publication-grade validation and does not demonstrate novelty beyond standard hash-chain/HMAC audit logging.

## Recommended next action

Stop this run as a proxy/synthetic negative for paper readiness; a bounded follow-up should integrate the ledger with real agent traces and test crash/concurrency/key-rotation behavior.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent provenance ledger integration and robustness benchmark
- Success threshold: All provenance events are captured and verified, all tamper/crash/concurrency tests pass, and median end-to-end runtime overhead is below 5% with documented storage overhead.
- Stop condition: Stop if real-agent integration misses required event classes, verification fails after crash/concurrency tests, or median runtime overhead exceeds 5% without a clear mitigation.

## Evidence references

- Artifact root: `<local-path>/projects/local-agent-evidence-ledger-with-cryptographic-task-provenance-f5ba7e47f3f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
