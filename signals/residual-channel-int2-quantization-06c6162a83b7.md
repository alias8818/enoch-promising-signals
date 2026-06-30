# Residual-Channel INT2 Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-int2-quantization-06c6162a83b7`
Run ID: `residual-channel-int2-quantization-06c6162a83b7-20260529T194401122776+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/03f6686f4884

## What looked useful

Residual-channel selection by INT2 residual energy was consistently but only slightly better than random channels. At 5% residual channels it reduced Frobenius MSE to 0.9436x INT2 versus 0.9505x for random; at 10% it reached 0.8891x versus 0.8998x random. Even with about 2.79-3.60 effective bits assuming FP16 residual values, corrected INT2 remained about 5.4x-5.1x worse than INT3 error.

## Boundaries and scale limits

No end-to-end language-model perplexity, real calibration activations, packed INT2 kernels, latency, or generation-quality measurements were run. Evidence is a CPU-only weight-matrix and randomized-activation proxy on one 33M-parameter checkpoint.

## Claim scope

On 24 two-dimensional tensors from TinyStories-Instruct-33M, row-wise affine INT2 plus exact FP16 residual corrections for 1-10% of input channels reduces weight/output error only modestly and remains far worse than row-wise INT3 under randomized activation probes.

## Why it stopped

Early proxy falsification: on real pretrained weights, small exact residual input-channel tables did not substantially close the INT2-to-INT3 error gap, so the strong claim is unsupported without activation-aware or reconstruction-based changes.

## Recommended next action

Stop this simple residual-channel INT2 variant as no-paper evidence; the only bounded next test worth running is an activation-aware end-to-end fake-quantized TinyStories pass with perplexity and random-channel controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-Aware Residual-Channel INT2 Perplexity Probe
- Success threshold: Activation-aware residual-channel INT2 at no more than 3.0 effective bits must recover at least 50% of the validation-loss gap between plain INT2 and INT3 and beat random residual channels by at least 20% of the INT2-to-INT3 gap.
- Stop condition: Stop if activation-aware residual channels fail to beat random channels by the specified margin on validation loss or if implementation requires nonlocal training/serving infrastructure beyond this CPU worker.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-int2-quantization-06c6162a83b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
