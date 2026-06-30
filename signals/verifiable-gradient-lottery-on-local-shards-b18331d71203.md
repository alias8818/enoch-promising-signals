# Verifiable Gradient Lottery on Local Shards

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `verifiable-gradient-lottery-on-local-shards-b18331d71203`
Run ID: `verifiable-gradient-lottery-on-local-shards-b18331d71203-20260520T084201470811+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/080b78960275

## What looked useful

The lottery/commitment mechanism is useful for reproducible sampling and post-lottery tamper detection, but the broad verifiable-gradient claim fails without an additional correctness proof or audit: malicious clients can pre-commit false gradients and pass verification.

## Boundaries and scale limits

Single-process CPU-only NumPy simulation; no real federated training, no production non-IID data, no multi-round optimizer convergence test, and no cryptographic proof/audit mechanism beyond hash commitments and HMAC selection.

## Claim scope

On synthetic 64-dimensional logistic-regression gradients split across 40 clients and 640 local shards, a public HMAC lottery with hash pre-commitments reproducibly selects shard gradients, yields an empirically near-unbiased sampled aggregate over many lottery seeds, and detects post-commit mutation of revealed gradients. It does not verify that pre-committed gradients were honestly computed from private shard data.

## Why it stopped

Moderate proxy evidence supports the sampling mechanism but early-falsifies the broad verifiable-gradient interpretation because semantic false-gradient pre-commits pass all hash/HMAC lottery checks.

## Recommended next action

Stop this standalone run; the next bounded test should add an audit/recompute layer for sampled shards and measure whether it detects false pre-committed gradients at acceptable overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Audited Gradient Lottery With Shard Recompute Challenges
- Success threshold: Detect at least 95% of malicious false-gradient clients at 10% malicious participation while retaining at least 2x communication reduction versus full reveal and keeping final validation loss within 5% of honest full-gradient aggregation on the synthetic task.
- Stop condition: Stop if the audit cannot verify gradient correctness without revealing enough data/gradients to erase the communication advantage, or if detection stays below 80% at 10% malicious clients under the bounded synthetic setup.

## Evidence references

- Artifact root: `<local-path>/projects/verifiable-gradient-lottery-on-local-shards-b18331d71203`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
