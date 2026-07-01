# Reversible Transformer Blocks for Zero-Activation-Storage Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `reversible-transformer-blocks-for-zero-activation-storage-training-0290e9575c34`
Run ID: `reversible-transformer-blocks-for-zero-activation-storage-training-0290e9575c34-20260527T232331382365+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/03cd32ce872a

## What looked useful

At 12 blocks, custom reversible backward saved 13.6 MB of forward tensors versus 117.9 MB for the same reversible math under ordinary autograd, an 88.4% reduction, and reduced peak CUDA allocation from 263.9 MB to 115.0 MB. A 4-block training run reduced forward-saved bytes from 45.8 MB to 11.0 MB versus standard reversible autograd with matching losses and finite gradients.

## Boundaries and scale limits

Tested only on random next-token data at width 256, sequence length 128, up to 12 blocks for block-only memory scans and 16 optimizer steps for training. Dense baseline was not parameter matched to the reversible half-stream architecture. No real dataset, GPT-2-small-class scale, AMP/BF16, activation-checkpointing baseline, or distributed training was tested.

## Claim scope

Small CUDA experiments show that additive-coupling reversible Transformer-style blocks with a custom inverse-recompute backward can train with finite, autograd-matching gradients while storing no internal F/G block activations during the forward graph; remaining saved tensors are block boundary outputs and non-block/loss bookkeeping.

## Why it stopped

The local evidence supports the mechanism but is not publication-grade validation: it is a small synthetic/random-data CUDA benchmark and the stronger literal zero-total-activation-storage claim is not supported.

## Recommended next action

Run a bounded GPT-2-small-class real-data comparison against activation checkpointing before considering any paper claim; stop this run as useful no-paper evidence because the literal zero-activation claim is only supported for internal block activations at toy scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class reversible block memory and stability comparison
- Success threshold: Custom reversible training matches the standard reversible loss within 2% at the fixed sequence-item budget, reduces peak CUDA memory by at least 30% versus ordinary reversible autograd, and avoids NaN/Inf gradients under the chosen precision.
- Stop condition: Stop if loss diverges, gradients become non-finite, memory reduction is below 15% after instrumentation is verified, or the run would exceed the local bounded budget without producing partial metrics.

## Evidence references

- Artifact root: `<local-path>/projects/reversible-transformer-blocks-for-zero-activation-storage-training-0290e9575c34`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
