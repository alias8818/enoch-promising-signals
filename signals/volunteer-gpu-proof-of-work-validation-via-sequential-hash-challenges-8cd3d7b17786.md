# Volunteer GPU Proof-of-Work Validation via Sequential Hash Challenges

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-gpu-proof-of-work-validation-via-sequential-hash-challenges-8cd3d7b17786`
Run ID: `volunteer-gpu-proof-of-work-validation-via-sequential-hash-challenges-8cd3d7b17786-20260607T013744937945+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6a20286ef314

## What looked useful

Correctness matched CPU recomputation. For 4096 steps per chain, one chain ran at 0.665 GPU MHash/s versus 4.732 CPU MHash/s, making the GPU 7.11x slower. At 32768 independent chains the GPU reached 2990.47 MHash/s and 625.61x speedup over the simple CPU baseline, showing that GPU usefulness requires exposing many independent chains. Plain final-digest verification requires recomputing the checked chain, so the simple protocol is not succinct.

## Boundaries and scale limits

Local microbenchmark only: one GB10, one simple single-thread ARM CPU baseline, no optimized CPU SHA2 intrinsics, no multithreaded CPU baseline, no ASIC/FPGA baseline, no networked volunteer adversary model, and no production protocol implementation.

## Claim scope

On one GB10 CUDA GPU with a deterministic SHA-256 hash-chain benchmark, a single sequential chain underutilized the GPU and was slower than a single-thread CPU baseline, while many independent chains achieved high GPU throughput but changed the mechanism into a generic parallel hash benchmark rather than a GPU-specific sequential proof.

## Why it stopped

Bounded local mechanism evidence is enough to reject the simple sequential-hash challenge as paper-ready GPU proof-of-work validation, but it is not a full adversarial production-protocol validation.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should compare against optimized CPU SHA2/multithreaded and commodity hash-cracking baselines before considering protocol work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adversarial Baselines for Volunteer Sequential Hash Challenges
- Success threshold: Find a parameter regime where a volunteer GPU is at least 10x faster than optimized all-core CPU for prover work while full verification costs less than 5% of prover work, or clearly falsify that threshold.
- Stop condition: Stop if optimized CPU or generic hash tooling comes within 10x GPU throughput for practical challenge sizes, or if verifier recomputation remains above 5% of prover work without adding external succinct-proof machinery.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-gpu-proof-of-work-validation-via-sequential-hash-challenges-8cd3d7b17786`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
