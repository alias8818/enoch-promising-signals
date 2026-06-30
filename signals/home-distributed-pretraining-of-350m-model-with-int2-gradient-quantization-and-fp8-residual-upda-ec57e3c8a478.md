# Home distributed pretraining of 350M model with INT2 gradient quantization and FP8 residual updates

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `home-distributed-pretraining-of-350m-model-with-int2-gradient-quantization-and-fp8-residual-upda-ec57e3c8a478`
Run ID: `home-distributed-pretraining-of-350m-model-with-int2-gradient-quantization-and-fp8-residual-upda-ec57e3c8a478-20260621T161150207056+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/588e49d9c221

## What looked useful

FP32 validation loss improved by 2.7138, INT2 without residual improved by 1.6933, INT2 with FP32 residual improved by 1.5680, and INT2 with FP8 residual improved by 1.5321. FP8 residuals were slightly worse than no residual in this proxy while cutting the estimated 350M per-worker gradient payload from 667.57 MiB FP16 to 83.45 MiB INT2.

## Boundaries and scale limits

This did not run a 350M model, a real tokenizer/corpus, multi-host networking, or long pretraining. The result applies to the tested per-tensor affine INT2 quantizer and FP8 residual storage path, not to all possible INT2 schemes.

## Claim scope

A bounded GB10 proxy test of a 5.28M-parameter causal transformer with four simulated workers found that per-tensor affine INT2 gradient quantization with FP8 residual error-feedback is runnable and gives the expected 8x gradient-byte reduction versus FP16, but does not recover dense-gradient learning over 120 optimizer steps.

## Why it stopped

The tested proxy is not full validation, but it directly measured the optimizer communication mechanism and showed a large learning gap versus dense gradients, with FP8 residuals failing to improve over no residual.

## Recommended next action

Stop this run as a proxy early falsification of the naive per-tensor INT2 plus FP8 residual design; only spend more compute after replacing the quantizer with a bounded blockwise or stochastic INT2 scheme and rerunning the same control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise stochastic INT2 gradients with FP8 residual error-feedback
- Success threshold: FP8 residual blockwise INT2 reaches at least 80% of FP32 validation-loss improvement and beats blockwise INT2 without residual by at least 10% relative improvement over 120-500 steps.
- Stop condition: Stop if blockwise FP8 residual INT2 remains below 70% of FP32 validation-loss improvement or fails to beat no-residual INT2 under the matched proxy.

## Evidence references

- Artifact root: `<local-path>/projects/home-distributed-pretraining-of-350m-model-with-int2-gradient-quantization-and-fp8-residual-upda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
