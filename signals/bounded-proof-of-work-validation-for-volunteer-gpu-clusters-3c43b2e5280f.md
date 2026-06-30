# Bounded Proof-of-Work Validation for Volunteer GPU Clusters

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-proof-of-work-validation-for-volunteer-gpu-clusters-3c43b2e5280f`
Run ID: `bounded-proof-of-work-validation-for-volunteer-gpu-clusters-3c43b2e5280f-20260609T014829298365+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/03443c9e91a1

## What looked useful

Bounded validation showed the expected n^2 verifier versus n^3 recomputation scaling on local exact matrix tasks. PoW verification cost was microsecond-class while nonce generation imposed measurable prover work. The result is useful for designing bounded validation certificates but not sufficient for a paper or full volunteer-cluster claim.

## Boundaries and scale limits

No multi-node volunteer cluster, network churn, heterogeneous workers, collusion, adaptive adversary, remote attestation, or GPU-native exact modular matmul was tested. GPU use was limited to float32 matmul throughput calibration as a worker analogue.

## Claim scope

On one GB10 host, for exact modular matrix-output certificates up to n=2048, a verifier using one SHA-256 PoW target check plus 16 Freivalds rounds accepted honest outputs, detected 100/100 random single-cell corruptions at each tested main size, and validated 7.18x to 159.41x faster than exact CPU recomputation.

## Why it stopped

No-paper closure: local bounded mechanism evidence is useful, but cluster-scale and adversarial evidence required for publication-grade validation was not produced in this run.

## Recommended next action

Run a bounded deepen follow-up with a GPU-native exact modular kernel and adaptive forged-output tests before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPU-native adversarial validation for bounded matrix-work certificates
- Success threshold: At n>=2048, honest certificates validate at least 50x faster than exact recomputation and adaptive corruptions escape no more often than the Freivalds theoretical bound for the selected round count.
- Stop condition: Stop if GPU-native exact prover cannot be made deterministic locally, if verifier speedup falls below 10x at n>=2048, or if any adaptive corruption family exceeds the expected Freivalds false-accept probability by more than 2x.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-proof-of-work-validation-for-volunteer-gpu-clusters-3c43b2e5280f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
