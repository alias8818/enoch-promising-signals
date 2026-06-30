# Concurrent Replica Crash-Recovery Test for Local-First Evidence Attestation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `concurrent-replica-crash-recovery-test-for-local-first-evi-120d5ce617`
Run ID: `concurrent-replica-crash-recovery-test-for-local-first-evi-120d5ce617-20260612T101013987234+0000`

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

- Parent run decision: Local-First Cross-Run Evidence Attestation Ledger: enoch://control-plane/projects/local-first-cross-run-evidence-attestation-ledger-d8166252b1c7/runs/local-first-cross-run-evidence-attestation-ledger-d8166252b1c7-20260611T143030211369+0000
- Parent run decision: Baseline and Crash-Recovery Evaluation for Local-First Evidence Attestation: enoch://control-plane/projects/baseline-and-crash-recovery-evaluation-for-local-first-evi-ff2f17e0fe/runs/baseline-and-crash-recovery-evaluation-for-local-first-evi-ff2f17e0fe-20260612T100001059088+0000

## What looked useful

Attested recovery accepted 0 corrupt records and reached 100% oracle match over 40 medium seeds. The unauthenticated op-log baseline reached the same final LWW state but accepted 988 corrupt records, showing that final convergence can mask invalid evidence acceptance. The no_flush ablation failed oracle/intended matching and lost 1504.75 operations per run on average.

## Boundaries and scale limits

Synthetic simulator only; no real IndexedDB, SQLite, Automerge, Yjs, mobile storage, filesystem crash, or disk fault-injection validation. The no_chain ablation did not separate from full attestation, so predecessor-chain necessity is not established by this workload.

## Claim scope

In a deterministic in-process simulator of 5 local-first replicas with fixed-seed concurrent operations, crashes, replay, corrupt/torn-record injection, and final anti-entropy, signed per-operation evidence recovery rejected corrupt records and recovered the durable-operation oracle across 40 seeds.

## Why it stopped

Tier 2 simulator validation produced a useful mechanism signal but not publication-grade direct evidence; result is no-paper because evidence is synthetic and one ablation did not isolate hash-chain necessity.

## Recommended next action

Implement the same crash/corruption metric suite against a real SQLite or IndexedDB local-first persistence stack with process-kill crash injection before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Storage Crash-Recovery Attestation Test for Local-First Replicas
- Success threshold: Across at least 30 fixed seeds, attested recovery accepts 0 corrupt records, reaches at least 0.99 oracle match, and the baseline accepts corrupt records or diverges under the same injected faults; disabled durability must fail acknowledged-operation recall.
- Stop condition: Stop if the real storage implementation cannot reproduce any baseline corrupt-record acceptance or divergence under controlled injected faults, or if attested recovery accepts any corrupt record without a documented implementation bug fix and rerun.

## Evidence references

- Artifact root: `<local-path>/projects/concurrent-replica-crash-recovery-test-for-local-first-evi-120d5ce617`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
