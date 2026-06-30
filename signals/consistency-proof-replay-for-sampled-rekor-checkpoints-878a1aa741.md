# Consistency-Proof Replay for Sampled Rekor Checkpoints

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `28`
Project ID: `consistency-proof-replay-for-sampled-rekor-checkpoints-878a1aa741`
Run ID: `consistency-proof-replay-for-sampled-rekor-checkpoints-878a1aa741-20260527T075013469109+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `28`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Signed External Anchor Evidence Ledger Replay: enoch://control-plane/projects/signed-external-anchor-evidence-ledger-replay-dcd1bf37ca/runs/signed-external-anchor-evidence-ledger-replay-dcd1bf37ca-20260524T230201532570+0000
- Parent run decision: Real Transparency-Log Replay Test for Signed Evidence Ledgers: enoch://control-plane/projects/real-transparency-log-replay-test-for-signed-evidence-ledg-2a44970253/runs/real-transparency-log-replay-test-for-signed-evidence-ledg-2a44970253-20260524T231211311543+0000

## What looked useful

Inactive shard identity controls matched 2/2, confirming the endpoint can bind fixed roots. Active same-size identity checks mismatched 26/30 and active adjacent sampled-pair checks mismatched 28/29, while all sampled checkpoint rootHash fields matched their signedTreeHead roots. The proposed sampled active-checkpoint replay mechanism is therefore not reliably bindable with the current public API behavior.

## Boundaries and scale limits

Thirty active checkpoint samples over roughly 150 seconds against the public service, plus two inactive-shard identity controls. This is direct API behavior evidence, not a full independent cryptographic audit of Rekor or a private-deployment study.

## Claim scope

On the active public Rekor shard, sampled checkpoints from /api/v1/log?stable=true could not be reliably replayed later through /api/v1/log/proof because proof rootHash values usually did not bind to the sampled target checkpoint roots, including the firstSize == lastSize identity case.

## Why it stopped

Direct active-shard target checks failed the prerequisite root-binding identity condition at high rates, so the sampled-checkpoint replay threshold is unsupported rather than merely under-scaled.

## Recommended next action

Stop this follow-up as no-paper useful negative evidence; do not recommend another deepen/retry because controller follow-up depth is already 4.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/consistency-proof-replay-for-sampled-rekor-checkpoints-878a1aa741`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
