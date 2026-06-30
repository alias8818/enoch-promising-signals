# 2-bit Weight Quantization with Learned Per-Layer Residual Scaling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-weight-quantization-with-learned-per-layer-residual-scaling-24f172be615d`
Run ID: `2-bit-weight-quantization-with-learned-per-layer-residual-scaling-24f172be615d-20260622T000601951821+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/78415dbfa451

## What looked useful

Plain 2-bit PTQ dropped mean accuracy from 0.7914 to 0.4999. Learned per-layer gains averaged 0.4951 accuracy, -0.0047 versus PTQ. Residual scaling averaged 0.7907 accuracy, but learned residual scalars were mostly near 1.0, meaning the diagnostic effectively restored dense residual information.

## Boundaries and scale limits

Synthetic 10-class teacher/student data, small NumPy MLP, post-training quantization only, no transformer/language-model validation, no quantization-aware training, no deployment kernels, and no compact residual storage.

## Claim scope

On a five-seed synthetic small-MLP post-training quantization probe, one learned deployable fp32 gain per 2-bit quantized layer did not improve test accuracy over plain 2-bit PTQ, while a residual-scaling diagnostic recovered dense accuracy only by using the full fp32 residual direction.

## Why it stopped

Bounded proxy evidence does not support the deployable learned per-layer scalar idea; the only strong recovery used full fp32 residual tensors, so this is an early negative rather than full validation.

## Recommended next action

Stop this run as no-paper useful signal; a future bounded deepen test should add a compact residual code and compare storage-normalized accuracy against plain 2-bit PTQ on a real small model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Storage-normalized compact residual code for 2-bit PTQ
- Success threshold: At equal or explicitly bounded extra storage, compact residual coding improves accuracy by at least 25% of the dense-to-PTQ gap over plain 2-bit PTQ across at least three seeds.
- Stop condition: Stop if the compact residual representation fails to beat plain 2-bit PTQ by at least 10% of the dense-to-PTQ gap or requires storing full/high-rank residual tensors.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-weight-quantization-with-learned-per-layer-residual-scaling-24f172be615d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
