# Signed evidence-ledger agent with replay falsification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `signed-evidence-ledger-agent-with-replay-falsification-2ff540ec2057`
Run ID: `signed-evidence-ledger-agent-with-replay-falsification-2ff540ec2057-20260609T173036246434+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/57caa9d46515

## What looked useful

Terminal anchoring is the critical requirement. Unanchored signed hash chains validate internally consistent prefixes and miss suffix truncation, while anchored signed ledgers detected all tested falsification classes at about 32k verified events/s with 3.21x storage versus the minimal unsigned JSON baseline.

## Boundaries and scale limits

Synthetic traces only; no production agent traffic, concurrent writers, key rotation, signer compromise, external witness service, distributed timestamping, or mature audit-log baseline. The unanchored signed hash chain failed suffix truncation detection.

## Claim scope

In a local synthetic 100-trace, 64-event-per-trace experiment, an Ed25519-signed SHA-256 hash-chain evidence ledger with a separately signed terminal receipt detected all tested replay, tamper, drop, reorder, splice, and suffix-truncation falsifications while accepting clean traces.

## Why it stopped

The result is a synthetic bounded mechanism confirmation, not direct production or publication-grade validation; unanchored ledgers have a demonstrated truncation failure mode.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded work should replay real agent traces through an anchored ledger with checkpoint loss and key-rotation adversary tests.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored signed evidence ledger on real agent traces with key rotation
- Success threshold: Across at least 1000 real trace replays, zero false accepts for the covered attacks, zero false rejects for clean traces, and sustained verification throughput above 10000 events/s with documented storage overhead.
- Stop condition: Stop if any covered attack is accepted under the stated trust model, or if key rotation/checkpoint handling requires a trusted component equivalent to an existing transparency-log system without simplifying benefit.

## Evidence references

- Artifact root: `<local-path>/projects/signed-evidence-ledger-agent-with-replay-falsification-2ff540ec2057`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
