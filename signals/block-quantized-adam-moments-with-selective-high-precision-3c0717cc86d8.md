# Block-Quantized Adam Moments with Selective High-Precision

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `block-quantized-adam-moments-with-selective-high-precision-3c0717cc86d8`
Run ID: `block-quantized-adam-moments-with-selective-high-precision-3c0717cc86d8-20260527T142544389216+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/14b3509bc498

## What looked useful

Blockwise int8 Adam moment storage achieved about 3.3x-4.0x estimated moment-state compression and matched AdamW on a small dense classifier, but exact-gradient traces showed mean update relative errors of about 19x-40x and final parameter relative errors of about 20x-28x. Selective fp32 storage of the top 1%-5% high-v blocks barely improved the trace error.

## Boundaries and scale limits

No LLM-scale training, no fused compact kernel, no real compact high-precision storage allocation, no sparse/embedding-heavy workloads, and only 3 seeds with 180-step toy training. Trace evidence is direct for optimizer dynamics but synthetic.

## Claim scope

Bounded local evidence on synthetic exact-gradient traces and a small dense GPU classifier: naive per-block linear int8 Adam moments with optional top-v high-precision blocks reduce estimated state memory and can train the toy dense task, but do not faithfully preserve exact Adam update trajectories on spiky traces.

## Why it stopped

Early/proxy falsification of faithful Adam replacement: memory savings and toy convergence were observed, but the direct optimizer-trajectory test failed badly, so this does not justify paper writing or scale-up as formulated.

## Recommended next action

Stop this naive formulation as no-paper useful signal; branch only to a denominator-safe v representation such as log-domain or lower-bounded quantization and require exact-trace update error below 5% before larger training.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Denominator-Safe Quantized Adam Second Moments
- Success threshold: At least 3x estimated Adam moment-state compression, mean update relative error below 5%, final parameter relative error below 2%, and validation loss within 1% of AdamW on the same small classifier.
- Stop condition: Stop if exact-gradient trace mean update relative error remains above 10% or if denominator-safety fixes reduce compression below 2x before training-scale evidence.

## Evidence references

- Artifact root: `<local-path>/projects/block-quantized-adam-moments-with-selective-high-precision-3c0717cc86d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
