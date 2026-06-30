# Static-scale int4 QAT validation beyond Optdigits MLP

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `static-scale-int4-qat-validation-beyond-optdigits-mlp-ce07427039`
Run ID: `static-scale-int4-qat-validation-beyond-optdigits-mlp-ce07427039-20260605T135715270989+0000`

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

- Parent run decision: Quantization-Aware Training for 4-bit Inference: enoch://control-plane/projects/quantization-aware-training-for-4-bit-inference-7e69c96c0295/runs/quantization-aware-training-for-4-bit-inference-7e69c96c0295-20260605T084344134083+0000
- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/d8e1b158b562

## What looked useful

Static-scale int4 QAT is not universally reliable under the tested threshold, but it can remain competitive with fp32/dynamic int4 on some non-Optdigits tabular MLPs; WDBC showed a 5.15 point static-vs-fp32 accuracy gap.

## Boundaries and scale limits

Three small tabular datasets, five stratified seeds each, one hidden-layer MLP, fake quantization only, no packed int4 inference kernels, no CNN/transformer/language-model validation, no broad hyperparameter or calibration sweep.

## Claim scope

Small direct NumPy MLP test on three non-Optdigits UCI tabular classification datasets: static signed int4 fake-quantized QAT with fixed post-warmup scales met the predeclared fp32/dynamic accuracy threshold on Wine and Ionosphere, but failed it on WDBC.

## Why it stopped

Tier 1 direct test completed; result is mixed useful signal rather than paper-ready validation.

## Recommended next action

Run a bounded deepen follow-up over 8-12 additional tabular datasets and two hidden widths, with calibration/clipping diagnostics, to determine whether the WDBC failure mode is isolated or common.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Static int4 QAT tabular robustness and calibration failure map
- Success threshold: Static int4 QAT mean accuracy within 0.03 of fp32 and within 0.02 of dynamic int4 on at least 75% of dataset-width conditions, with no unexplained catastrophic failures over 0.08 absolute accuracy.
- Stop condition: Stop as negative if more than 25% of dataset-width conditions miss the fp32 gap by over 0.03 or any recurring calibration diagnostic predicts failures without an available bounded fix.

## Evidence references

- Artifact root: `<local-path>/projects/static-scale-int4-qat-validation-beyond-optdigits-mlp-ce07427039`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
