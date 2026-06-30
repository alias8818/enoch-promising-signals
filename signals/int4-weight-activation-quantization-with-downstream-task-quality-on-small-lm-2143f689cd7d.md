# INT4 Weight+Activation Quantization with Downstream Task Quality on Small LM

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `int4-weight-activation-quantization-with-downstream-task-quality-on-small-lm-2143f689cd7d`
Run ID: `int4-weight-activation-quantization-with-downstream-task-quality-on-small-lm-2143f689cd7d-20260612T222732372077+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e67206aaa6d

## What looked useful

Activation quantization is the observed bottleneck. Per-channel W4 raised WikiText perplexity from 77.813 to 118.964 and kept cloze accuracy near baseline, while per-channel W4 plus per-token A4 raised perplexity to 1113.425 and dropped cloze accuracy from 0.800 to 0.625.

## Boundaries and scale limits

Single small pretrained LM, 256 WikiText-2 test samples, 26,871 next-token targets, 40 handcrafted cloze items, simulated dequantized float math, no real INT4 kernels, no calibration search, no quantization-aware training, no broad downstream benchmark suite.

## Claim scope

On distilgpt2 with simulated post-training INT4 quantization of affine transformer modules only, simple W4A4 does not preserve small-LM quality: per-channel W4 alone is tolerable on this probe, but adding per-token A4 causes a large held-out perplexity increase and a cloze accuracy drop.

## Why it stopped

Proxy-scale early falsification, not full validation: the direct held-out language-modeling metric shows a 14.31x perplexity increase for the most practical tested W4A4 variant, so plain INT4 activations are not viable under the tested conditions.

## Recommended next action

Stop this run as a proxy-scale early falsification of simple post-training W4A4 preservation; a bounded follow-up should test activation calibration or smoothing against the same W4-only and A4-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated activation smoothing for W4A4 small-LM quantization
- Success threshold: Calibrated W4PC+A4TOK WikiText perplexity ratio <= 2.0x fp32 and cloze accuracy drop <= 5 percentage points on the same probe.
- Stop condition: Stop if calibrated W4PC+A4TOK remains above 4.0x fp32 perplexity or loses more than 10 percentage points cloze accuracy after one bounded calibration sweep.

## Evidence references

- Artifact root: `<local-path>/projects/int4-weight-activation-quantization-with-downstream-task-quality-on-small-lm-2143f689cd7d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
