# Merkle Gradient Checkpointing for Untrusted CPU Workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-gradient-checkpointing-for-untrusted-cpu-workers-61f765e3fefc`
Run ID: `merkle-gradient-checkpointing-for-untrusted-cpu-workers-61f765e3fefc-20260607T072255565033+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c5f32c29a0f0

## What looked useful

Merkle-only gradient checkpointing is useful as an audit-log/challenge wrapper but is not viable as a standalone compute-saving verifier for untrusted CPU gradient workers. Final corrected benchmark showed Merkle hashing cost about 77-80% of a worker step on larger cases and correctness replay cost about one full worker step; sampling 256 of 8704 chunks detects 1% random chunk tamper with about 92.4% probability but only 0.1% tamper with about 22.6% probability.

## Boundaries and scale limits

Single-host CPU proxy with synthetic MLPs, no GPU/LLM/distributed training, no networked adversary, no privacy constraints, and no custom algebraic verifier. The tamper model is analytic uniform chunk corruption, not adaptive wrong-gradient generation.

## Claim scope

On deterministic NumPy MLP CPU-worker gradient steps up to depth 8 and width 1024, Merkle commitments over 4096-byte gradient/checkpoint chunks bind returned bytes and enable probabilistic post-commit tamper localization, but do not reduce correctness-verification compute without a full deterministic replay.

## Why it stopped

Bounded CPU proxy falsified the strong standalone claim: Merkle commitments alone bind bytes but do not prove gradient correctness or avoid replay; this is an early/proxy falsification rather than a full-scale distributed-training validation.

## Recommended next action

Stop this Merkle-only line as no-paper evidence; the concrete next bounded test is to combine Merkle commitments with Freivalds-style layer matrix-product checks and measure whether sampled gradient correctness can be checked without full replay.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Merkle plus Freivalds Layer Checks for CPU Gradient Worker Audits
- Success threshold: Verifier time below 25% of full replay on the depth 8 width 1024 case while detecting at least 99% of injected 1% gradient-chunk tamper and all tested structured single-layer matrix-product inconsistencies.
- Stop condition: Stop if Freivalds checks require recomputing most layer products or exceed 50% of full replay time while failing to improve detection beyond Merkle-only sampled chunks.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-gradient-checkpointing-for-untrusted-cpu-workers-61f765e3fefc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
