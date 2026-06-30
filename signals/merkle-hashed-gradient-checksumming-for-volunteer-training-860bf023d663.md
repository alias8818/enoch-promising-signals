# Merkle-Hashed Gradient Checksumming for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-hashed-gradient-checksumming-for-volunteer-training-860bf023d663`
Run ID: `merkle-hashed-gradient-checksumming-for-volunteer-training-860bf023d663-20260608T190100347549+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fc88751159c5

## What looked useful

BLAKE2s Merkle hashing reached 302.9-438.6 MB/s locally; a 20 MB, 5M-parameter gradient hashed in 0.0542 s with 4096-float leaves; 200/200 injected corruptions were detected and localized to one bucket. A self-consistent malicious worker remained undetected without reference evidence, while a two-honest-one-Byzantine replicated assignment flagged the mismatch.

## Boundaries and scale limits

Tested synthetic float32 gradients up to 5M parameters, an 8-worker local aggregation proxy, 200 random corruption trials, and one deterministic logistic-regression gradient probe. No real distributed coordinator, neural-model training loop, WAN volunteers, mixed precision, compression, signatures, or nondeterministic accelerator kernels were tested.

## Claim scope

Local CPU evidence shows Merkle-hashed gradient buckets can detect and localize byte-level gradient corruption after a prior commitment, and can support replicated-worker mismatch checks. It does not verify standalone volunteer gradient correctness.

## Why it stopped

Bounded local evidence supports Merkle checksums as a tamper-evident component but falsifies the stronger standalone volunteer-gradient correctness interpretation; this is not full distributed-training validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate signed Merkle roots with replicated deterministic minibatches in a small neural training loop and measure false positives, detection, and overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed Merkle Roots with Replicated Minibatch Audits in Small Neural Training
- Success threshold: Checksum-plus-replication detects at least 95% of injected Byzantine leaf attacks with no more than 1% honest false-positive rate and less than 15% end-to-end wall-clock overhead versus the no-checksum baseline on the small neural task.
- Stop condition: Stop if checksum-only remains unable to detect self-consistent Byzantine gradients and replication either exceeds 15% overhead or causes more than 1% false positives under honest deterministic replay.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-hashed-gradient-checksumming-for-volunteer-training-860bf023d663`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
