# GPU-native adversarial validation for bounded matrix-work certificates

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpu-native-adversarial-validation-for-bounded-matrix-work-90dd8b5a42`
Run ID: `gpu-native-adversarial-validation-for-bounded-matrix-work-90dd8b5a42-20260609T034247201559+0000`

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

- Parent run decision: Bounded Proof-of-Work Validation for Volunteer GPU Clusters: enoch://control-plane/projects/bounded-proof-of-work-validation-for-volunteer-gpu-clusters-3c43b2e5280f/runs/bounded-proof-of-work-validation-for-volunteer-gpu-clusters-3c43b2e5280f-20260609T014829298365+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/03443c9e91a1

## What looked useful

The mechanism is viable in a narrow bounded setting if projection count is high enough; near-threshold single-entry corruptions are the limiting case, and low projection counts are not reliable.

## Boundaries and scale limits

Only small dense matrices, synthetic bounded random inputs, fixed tolerance 1e-5, non-adaptive adversaries, one GPU, and no cryptographic transcript binding were tested. k<=4 failed the 99% detection threshold on near-threshold sparse corruptions, and k=8 narrowly failed on n=512 single-entry corruption.

## Claim scope

On NVIDIA GB10 with FP32 random dense matrix products at n=256 and n=512, GPU-native Freivalds validation with k=16 random projections detected all tested material corruptions across six attack families in a 200-trial-per-row focused confirmation, with zero clean false positives.

## Why it stopped

No-paper useful signal: the Tier 1 direct test supports the mechanism only for k=16 in small non-adaptive synthetic matrix products, while lower projection counts failed the stated threshold.

## Recommended next action

Run a bounded deepen test for adaptive/challenge-visible adversaries and near-threshold sparse corruptions at k=16 and k=32 before considering any larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive near-threshold sparse attacks against GPU Freivalds matrix-work validation
- Success threshold: For commit-before-challenge mode, achieve at least 99.5% detection with zero clean false positives across near-threshold sparse attacks; for challenge-visible mode, demonstrate either no practical nullspace evasion or a reproducible evasion that falsifies the broader certificate design.
- Stop condition: Stop if challenge-visible attacks reliably evade detection at material relative delta >=1e-5, or if commit-before-challenge k=32 fails to reach 99.5% detection on non-adaptive sparse attacks.

## Evidence references

- Artifact root: `<local-path>/projects/gpu-native-adversarial-validation-for-bounded-matrix-work-90dd8b5a42`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
