# Int2-Resid GPT2: Skip-Channel Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-resid-gpt2-skip-channel-quantization-d6c6fbd51199`
Run ID: `int2-resid-gpt2-skip-channel-quantization-d6c6fbd51199-20260530T060331027182+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/dc7e51af54d2

## What looked useful

High-variance residual channels matter: with 256/768 skipped channels, relative PPL improved from 356x fp32 for all-channel int2 to 46.7x fp32, and high-variance skipping beat random and low-variance skipping. However, the best condition still had +3.84 NLL versus fp32, so the simple skip-channel int2 residual scheme is not viable as tested.

## Boundaries and scale limits

Small local CPU-only inference study; no training or quantization-aware adaptation; no packed int2 kernels; no larger models; no full validation-corpus perplexity; one main calibration/evaluation slice plus one skip-selection control.

## Claim scope

On pretrained GPT-2 small forward passes over a 4,096-token WikiText-2 validation slice, naive per-token signed int2 quantization of residual outputs after every transformer block is highly destructive; skipping calibrated high-variance hidden channels reduces but does not solve the loss degradation.

## Why it stopped

Proxy-sized but direct GPT-2 inference evidence early-falsifies the naive skip-channel int2 residual method: the mechanism helps, but not nearly enough to approach baseline perplexity.

## Recommended next action

Stop this run as a no-paper useful negative signal; next bounded action is to test a less biased/learned residual int2 quantizer or different sublayer placement using the same high-variance, random, and low-variance skip controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layerwise residual int2 quantizer placement with high-variance skip controls
- Success threshold: At 256 or fewer skipped channels, best method achieves NLL delta <= +0.5 versus fp32 and beats random skip by at least 0.5 NLL on the same tokens.
- Stop condition: Stop if all tested quantizer/placement variants remain above +1.0 NLL delta or fail to beat random skip on the 16k-token evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/int2-resid-gpt2-skip-channel-quantization-d6c6fbd51199`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
