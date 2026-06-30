# Hash-Chain Data Commitment and Spot Audit for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chain-data-commitment-and-spot-audit-for-volunteer-training-a91af41b2e23`
Run ID: `hash-chain-data-commitment-and-spot-audit-for-volunteer-training-a91af41b2e23-20260611T084037049300+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cb0b9780d491

## What looked useful

Commitment overhead was about 227k-231k records/sec for 100k synthetic records. Detection is budgetable: 0.1% tampering with 5% audits has about 0.59% expected miss probability, while 0.1% tampering with 0.1% audits misses about 90.5%. Hash-chain proof size was 1.62x mean Merkle reference at checkpoint interval 64, 5.46x at 256, and 20.77x at 1024.

## Boundaries and scale limits

Synthetic fixed-size records only; no real training loop, volunteer network, privacy-preserving reveal flow, adaptive adversary, collusion model, or implemented Merkle/vector-commitment baseline. The result is bounded local evidence, not full-scale volunteer-training validation.

## Claim scope

On a local CPU worker with 100,000 synthetic 256-byte records, sparse-checkpointed SHA-256 hash-chain commitments build quickly and random spot-audit detection matches the exact hypergeometric sampling model, but random-access audit proof bandwidth is materially worse than a Merkle proof-size reference unless checkpoints are frequent.

## Why it stopped

The local synthetic evidence supports the mechanism only as a probabilistic integrity check with a significant proof-size tradeoff; it is insufficient for paper-positive claims about volunteer training systems.

## Recommended next action

Stop this run as no-paper useful signal; next, build a bounded real-shard prototype that compares hash-chain checkpoints against an implemented Merkle baseline during a toy volunteer training loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-shard hash-chain versus Merkle spot-audit prototype for volunteer training
- Success threshold: For 100k or more real records, checkpointed hash-chain audits must stay within 2x Merkle audit bandwidth and within 5% training wall-clock overhead while observed detection matches the hypergeometric target within 0.03 absolute error.
- Stop condition: Stop if hash-chain audit bandwidth exceeds 2x Merkle at the checkpoint interval needed for latency, or if audit/reveal handling adds more than 5% wall-clock overhead in the toy training loop.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chain-data-commitment-and-spot-audit-for-volunteer-training-a91af41b2e23`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
