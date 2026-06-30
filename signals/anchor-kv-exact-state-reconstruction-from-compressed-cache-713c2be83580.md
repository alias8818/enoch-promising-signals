# Anchor-KV: Exact State Reconstruction from Compressed Cache

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `anchor-kv-exact-state-reconstruction-from-compressed-cache-713c2be83580`
Run ID: `anchor-kv-exact-state-reconstruction-from-compressed-cache-713c2be83580-20260610T224829339825+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d9d36ccd668d

## What looked useful

The probe constructed explicit nullspace collisions: two different full KV caches with identical compressed caches up to <1e-10 numerical tolerance. Across all 360 m<T cases, attention output changed despite identical compressed cache; mean L2 change was 0.0206 and max was 0.1455. m=T controls reconstructed to numerical precision and had zero attention collision.

## Boundaries and scale limits

Synthetic NumPy linear-algebra probe only: T<=64, d<=16, 20 seeds, prefix-anchor/random-projection/orthogonal-projection compression matrices. No learned decoder, real transformer checkpoint, production trace, nonlinear compression format, or long-context workload was tested.

## Claim scope

For arbitrary synthetic KV cache states, an undercomplete sequence-axis anchor/projection compression C=P@X with m<T is not sufficient for exact full-state reconstruction or guaranteed exact downstream single-query attention-output reconstruction.

## Why it stopped

Proxy/structural early falsification of broad arbitrary exact reconstruction from undercomplete anchor/projection-compressed caches; not a full model-scale validation.

## Recommended next action

Stop this run as a bounded early falsification; any future exact Anchor-KV proposal should first specify extra side information or a restricted state class that removes the nullspace collision, then test exact logit equivalence on a real transformer checkpoint.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exactness Test for Restricted Anchor-KV State Classes on a Real Transformer
- Success threshold: For the restricted claimed state class, max absolute logit difference <=1e-5 versus full KV on at least 100 sampled contexts, while out-of-class perturbation controls fail exactness.
- Stop condition: Stop if the specified compression remains non-injective over the restricted class or if real-checkpoint max logit differences exceed 1e-5 under exact arithmetic/float64 reconstruction controls.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-kv-exact-state-reconstruction-from-compressed-cache-713c2be83580`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
