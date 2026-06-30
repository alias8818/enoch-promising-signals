# Residual-Channel 2bit GPT-2 Weight Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-2bit-gpt-2-weight-quantization-71eb1b7108d3`
Run ID: `residual-channel-2bit-gpt-2-weight-quantization-71eb1b7108d3-20260529T043557695654+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/013b87ae724f

## What looked useful

Top-error residual channels are much better than random residual channels at the same budget, but the simple method remains unusable: baseline loss was 3.8742, 5% top-error residual loss was 15.8364, and even 30% top-error residual loss was 11.6950.

## Boundaries and scale limits

Does not evaluate full WikiText-2, activation-aware quantization, quantization-aware fine-tuning, packed 2-bit kernels, embeddings/lm_head quantization, larger GPT models, or deployment throughput. Accuracy was measured with dequantized tensors.

## Claim scope

Bounded GPT-2-small post-training experiment: per-output affine 2-bit quantization of transformer 2D weights on 32,768 WikiText-2 tokens, with residual full-precision output channels selected by weight reconstruction error or randomly.

## Why it stopped

Direct bounded early falsification: the tested residual-channel mechanism improves over random selection but remains far from full-precision GPT-2 loss, so this is a no-paper useful signal rather than full validation.

## Recommended next action

Stop pursuing naive per-output min/max 2-bit GPT-2 residual-channel PTQ as a paper result; if continuing, run a bounded activation-aware GPTQ/AWQ-style residual-channel test with the same controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware residual-channel 2-bit GPT-2 quantization
- Success threshold: At 5-10% residual channels, activation-aware 2-bit quantization should reach loss within 0.5 of the full-precision GPT-2-small baseline and beat weight-error-only residual selection by at least 50% of the loss gap.
- Stop condition: Stop if activation-aware residual selection remains more than 2.0 loss above baseline at 10% residual channels on the bounded validation set.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-2bit-gpt-2-weight-quantization-71eb1b7108d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
