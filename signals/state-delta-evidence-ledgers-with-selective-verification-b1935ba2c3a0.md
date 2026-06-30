# State-Delta Evidence Ledgers with Selective Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `state-delta-evidence-ledgers-with-selective-verification-b1935ba2c3a0`
Run ID: `state-delta-evidence-ledgers-with-selective-verification-b1935ba2c3a0-20260526T120811133266+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b0283eaa9379

## What looked useful

Selective verification is mechanically useful when query dependency metadata is complete, but read-set omissions are a first-order failure mode. Periodic checkpoints alone did not repair omissions; risk-aware verification recovered recall at a much smaller cost saving.

## Boundaries and scale limits

No production traces, no adaptive adversary, no concurrent multi-reader ledgers, no cryptographic proof implementation, no real evidence-source latency, and only 2,000 synthetic episodes per condition.

## Claim scope

Synthetic state-delta ledgers with hash-chain integrity, expensive per-delta evidence predicates, generated downstream query read-sets, and injected evidence/hash/actor faults. Exact read-set selective verification preserved query-relevant fault detection at about 53% weighted evidence cost; omitted read-set metadata caused substantial missed relevant faults.

## Why it stopped

No-paper useful signal: synthetic evidence supports the mechanism under exact read-set metadata but exposes a practical fragility under omitted dependencies; this is not a full validation.

## Recommended next action

Run a bounded trace-based follow-up using real or realistic agent workflow ledgers with independently extracted read/write sets and injected evidence faults; stop if selective policies cannot exceed 0.99 query-relevant fault recall below 0.70 full evidence cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-based selective verification with independent read-set extraction
- Success threshold: At least 0.99 query-relevant fault recall and at most 0.70 mean weighted evidence cost ratio across realistic traces, with all missed relevant faults categorized.
- Stop condition: Stop as negative if any selective policy below 0.70 cost ratio misses more than 1% of query-relevant faults or if read/write-set extraction cannot be made independent of the ledger policy.

## Evidence references

- Artifact root: `<local-path>/projects/state-delta-evidence-ledgers-with-selective-verification-b1935ba2c3a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
