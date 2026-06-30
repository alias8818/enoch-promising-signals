# Merkle-ized Activation Provenance for Volunteer Distributed Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-ized-activation-provenance-for-volunteer-distributed-training-f31210db69b7`
Run ID: `merkle-ized-activation-provenance-for-volunteer-distributed-training-f31210db69b7-20260531T174740650373+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/dc0f2874ac2c

## What looked useful

Full activation Merkleization is feasible but adds meaningful CPU-side overhead; sampled commitment is cheaper but only covers a small evidence surface. Merkle roots prove consistency with committed bytes, not correctness of the original activation computation.

## Boundaries and scale limits

Single-process synthetic workload only; no multi-node volunteer setting, network transport, persistent public log, adversarial pre-commit correctness proof, redundant recomputation, or GPT-2-small-class training validation.

## Claim scope

On a local synthetic GPU MLP training loop, SHA-256 Merkle commitments over captured activations provide post-commit tamper evidence when an altered chunk is audited, with measured overhead of about 38% for full activation commitment and about 9% for sampled commitment in the tested configuration.

## Why it stopped

Bounded local proxy supports post-commit provenance but does not provide full volunteer distributed training validation or pre-commit correctness evidence.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement a two-worker pipeline/offload prototype with root publication before backward exchange and injected Byzantine activation faults.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-worker Merkle activation audit with injected Byzantine faults
- Success threshold: At least 1000 training steps on a nontrivial model shard with under 20% overhead at the chosen audit rate, observed post-commit fault detection matching analytic probability within 5 percentage points, and clear separation between detected post-commit mutation and undetected pre-commit wrong computation without recomputation.
- Stop condition: Stop early if end-to-end overhead exceeds 50% at audit rates below 5%, or if the protocol cannot distinguish post-commit mutation from ordinary serialization/nondeterminism errors.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-ized-activation-provenance-for-volunteer-distributed-training-f31210db69b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
