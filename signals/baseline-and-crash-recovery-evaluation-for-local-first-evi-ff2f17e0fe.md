# Baseline and Crash-Recovery Evaluation for Local-First Evidence Attestation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `baseline-and-crash-recovery-evaluation-for-local-first-evi-ff2f17e0fe`
Run ID: `baseline-and-crash-recovery-evaluation-for-local-first-evi-ff2f17e0fe-20260612T100001059088+0000`

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
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd9129181108

## What looked useful

Tier 1 direct test supports the mechanism: staged atomic persistence improved crash-recovery behavior over direct append baselines at a small measured throughput cost. This is useful local evidence but not paper-positive.

## Boundaries and scale limits

Tested only process crashes on one local filesystem with deterministic 512-byte payloads, 40-record crash logs, and 1,000-record throughput benchmarks. Not tested: power loss, remount behavior, concurrent writers, replica synchronization, browser/mobile storage APIs, adversarial tampering beyond hash-chain validation, or production-scale event volume.

## Claim scope

In a minimal single-process local filesystem hash-chain attestation log, staged atomic persistence avoided corrupt main-log prefixes across six injected process-crash phases and replayed one fully staged record, while direct append baselines exposed one corrupt-tail case.

## Why it stopped

No-paper useful signal: direct Tier 1 evidence supports the mechanism, but the harness is minimal and does not validate broader local-first evidence attestation claims.

## Recommended next action

Run a bounded deepen follow-up using a realistic local-first workload with concurrent writers or replica sync, keeping the same explicit crash-injection and recovery metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent Replica Crash-Recovery Test for Local-First Evidence Attestation
- Success threshold: Across all injected crash phases, staged atomic mode has zero prefix-validity failures, recovers at least as many acknowledged records as baselines, and stays within 25% throughput overhead on a 1,000+ event local workload.
- Stop condition: Stop if staged mode shows any unrecoverable prefix corruption, loses more acknowledged records than append+fsync in two or more crash phases, or exceeds 25% throughput overhead without a compensating recovery advantage.

## Evidence references

- Artifact root: `<local-path>/projects/baseline-and-crash-recovery-evaluation-for-local-first-evi-ff2f17e0fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
