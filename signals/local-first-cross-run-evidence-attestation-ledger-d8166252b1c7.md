# Local-First Cross-Run Evidence Attestation Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `local-first-cross-run-evidence-attestation-ledger-d8166252b1c7`
Run ID: `local-first-cross-run-evidence-attestation-ledger-d8166252b1c7-20260611T143030211369+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd9129181108

## What looked useful

The mechanism is viable as a low-overhead local-first evidence attestation layer in bounded tests: 250-event cases verified cleanly, rejected all tested tamper cases, and reached roughly 2.2k-2.4k appends/s and 9.5k-13.3k verifies/s in this Python prototype.

## Boundaries and scale limits

Synthetic local artifacts only; no production Enoch run corpus, remote sync protocol, key rotation, crash recovery, many-replica merge, long-lived storage, malicious signer, or baseline comparison against signed manifests/Git signing was tested.

## Claim scope

A small single-host Python prototype showed that local content-addressed artifacts plus Ed25519-signed hash-chain events can verify clean cross-run evidence ledgers and detect body mutation, artifact mutation, middle-event deletion, and conflicting replay across two local replicas.

## Why it stopped

No-paper closure: bounded synthetic evidence supports the mechanism, but the result is not publication-grade without real traces, baseline comparison, and broader failure-mode testing.

## Recommended next action

Run a bounded deepen follow-up comparing this ledger to signed manifest and Git signing baselines on real Enoch run directories with crash/restart and partial-sync scenarios.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Baseline and Crash-Recovery Evaluation for Local-First Evidence Attestation
- Success threshold: The ledger must detect every injected tamper/conflict case caught by baselines, recover cleanly after interrupted appends, and stay within 2x storage overhead and 5x verification time of the strongest simple baseline on real run data.
- Stop condition: Stop if a simple signed-manifest or Git-signing baseline provides equal tamper detection and recovery semantics with materially lower overhead or complexity.

## Evidence references

- Artifact root: `<local-path>/projects/local-first-cross-run-evidence-attestation-ledger-d8166252b1c7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
