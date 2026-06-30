# CheckpointChain: Incremental Hash-Chain Proof-of-Contribution for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `checkpointchain-incremental-hash-chain-proof-of-contribution-for-volunteer-training-c9ff9fbed9af`
Run ID: `checkpointchain-incremental-hash-chain-proof-of-contribution-for-volunteer-training-c9ff9fbed9af-20260610T015716117998+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7d69054757c

## What looked useful

Mutation, deletion, and reordering were detected by the chain verifier, and sparse Merkle updates were faster than full checkpoint hashing. However, random and sign-flipped workers also produced valid chains while damaging validation loss, so the chain proves artifact continuity rather than contribution usefulness.

## Boundaries and scale limits

Tested with toy logistic regression, four random seeds, synthetic checkpoint buffers up to 32 MB, and a pure-Python SHA-256/Merkle prototype. No large neural network, multi-worker network transport, secure data assignment, or adversarial cryptographic protocol analysis was performed.

## Claim scope

Bounded local evidence shows that an incremental hash-chain checkpoint log can make volunteer training artifacts tamper-evident, but cannot by itself prove useful training contribution.

## Why it stopped

Proxy/local falsification of the standalone proof-of-contribution claim: valid chains accepted harmful updates, so this is not full validation and not paper-ready.

## Recommended next action

Stop treating the standalone hash chain as proof-of-contribution; any next design should add an explicit contribution-quality verifier and test adversarial workers before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CheckpointChain with validation-gated contribution credit
- Success threshold: Reject at least 95% of harmful/adversarial updates while accepting at least 90% of honest useful updates and adding less than 5% wall-clock overhead on the bounded workload.
- Stop condition: Stop if the validation-gated protocol still accepts more than 10% of harmful updates or requires trusted private evidence that cannot be reproduced locally.

## Evidence references

- Artifact root: `<local-path>/projects/checkpointchain-incremental-hash-chain-proof-of-contribution-for-volunteer-training-c9ff9fbed9af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
