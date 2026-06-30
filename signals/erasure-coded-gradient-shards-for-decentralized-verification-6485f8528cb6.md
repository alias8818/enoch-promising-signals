# Erasure-Coded Gradient Shards for Decentralized Verification

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `erasure-coded-gradient-shards-for-decentralized-verification-6485f8528cb6`
Run ID: `erasure-coded-gradient-shards-for-decentralized-verification-6485f8528cb6-20260522T135421763547+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/85a4b29ef1ec

## What looked useful

Pure erasure-coded shard consistency is not a low-bandwidth verifier by itself: every q <= k sample is always code-consistent, so detection is zero at <=1.0 gradient-equivalent bandwidth. The first detecting sample costs (k+1)/k gradient-equivalent bandwidth, and single-shard corruption can require 1.44x to 2.0x bandwidth for >=95% detection in the tested codes.

## Boundaries and scale limits

Tested finite-field encoded gradient blocks and random shard corruptions for small codes (12,8), (16,8), and (24,16) with 2,000 Monte Carlo trials per cell plus exact combinatorial detection probabilities. Did not test cryptographic commitments, adversarial valid-codeword substitutions, real model training, peer-to-peer networking, or large-scale distributed systems.

## Claim scope

For pure MDS/Reed-Solomon-style gradient shard consistency checks, decentralized verifiers cannot detect corrupted shards when sampling q <= k shards, and the first nonzero consistency check requires more than one full gradient-equivalent of shard bandwidth.

## Why it stopped

Proxy early falsification: the directly tested code-consistency verifier has a structural zero-detection region for q <= k and therefore fails the low-bandwidth decentralized verification claim without additional commitments or recomputation.

## Recommended next action

Stop this pure-consistency variant as a proxy early falsification; if continuing, test a commitment-assisted challenge protocol that can detect one corrupted shard with >=95% probability below 0.5x gradient-equivalent bandwidth on a toy training loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commitment-Assisted Erasure-Coded Gradient Shard Audits
- Success threshold: On at least one toy model training task, detect one corrupted shard with >=95% probability at <=0.5x gradient-equivalent verifier bandwidth, false accept rate <=1%, and final loss within 5% of the dense baseline.
- Stop condition: Stop if the commitment/challenge protocol still requires >=1.0x gradient-equivalent bandwidth for one-shard >=95% detection or degrades final loss by more than 5% versus the dense baseline.

## Evidence references

- Artifact root: `<local-path>/projects/erasure-coded-gradient-shards-for-decentralized-verification-6485f8528cb6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
