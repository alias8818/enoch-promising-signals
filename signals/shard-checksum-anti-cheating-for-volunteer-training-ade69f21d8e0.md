# Shard-checksum anti-cheating for volunteer training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `shard-checksum-anti-cheating-for-volunteer-training-ade69f21d8e0`
Run ID: `shard-checksum-anti-cheating-for-volunteer-training-ade69f21d8e0-20260531T215053798135+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4c0f43dccae5

## What looked useful

Checksum-only validation accepted 100% of cheating submissions with zero checksum failures across random, zero, and sign-flipped update attacks. In the 50% sign-flip case, test accuracy fell from 0.8901 honest baseline to 0.4149. Recomputing audited gradients detected 100% of audited cheating submissions, showing that computation verification, not shard checksuming, is the missing anti-cheating mechanism.

## Boundaries and scale limits

Tested on toy binary classification with 4,096 training examples, 2,048 test examples, 64 dimensions, 16 shards, 80 rounds, and 50 seeds. It does not cover large models, real volunteer infrastructure, collusion, privacy-preserving training, or cryptographic proof systems.

## Claim scope

In a synthetic 16-shard volunteer logistic-regression setup, a checksum over assigned shard bytes detects data corruption but does not detect whether the submitted model update was computed from that shard.

## Why it stopped

Early direct falsification: the checksum proves shard identity/possession but not correct update computation, so legitimate shard holders can pass checksum validation while submitting arbitrary or poisoned gradients.

## Recommended next action

Stop pursuing checksum-only anti-cheating; evaluate computation-binding alternatives such as spot recomputation, redundant worker comparison, trusted execution, or verifiable computation with explicit overhead and threat-model measurements.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/shard-checksum-anti-cheating-for-volunteer-training-ade69f21d8e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
