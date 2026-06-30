# 1.5-bit Weight Quantization with Learned Residual Channel Selection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `1-5-bit-weight-quantization-with-learned-residual-channel-selection-a821d3a65335`
Run ID: `1-5-bit-weight-quantization-with-learned-residual-channel-selection-a821d3a65335-20260629T191212885661+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d9402cc56d81

## What looked useful

Learned activation-aware 1.5-bit residual channel selection achieved 0.6191 mean test accuracy versus 0.5982 for weight-L2 1.5-bit, 0.5772 for random 1.5-bit, and 0.5436 for 1-bit binary; mean learned-minus-weight-L2 logit MSE was -2.24, though seed 2 lost 0.0103 accuracy to weight-L2.

## Boundaries and scale limits

Synthetic MLP-scale proxy only: no pretrained transformer, GPT-2-small-class baseline, language-model perplexity, quantization-aware training, hardware packing kernel, latency, or large-corpus validation was tested.

## Claim scope

In five seeded synthetic NumPy MLP teacher-task post-training quantization runs, learned activation-aware selection of residual-coded output channels at a 1.5-bit average weight budget improved mean test accuracy and logit reconstruction relative to same-budget random and weight-residual-L2 channel selection.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic post-training proxy, not direct transformer or language-model validation.

## Recommended next action

Run a bounded direct follow-up on a small pretrained transformer or GPT-2-small-class model measuring perplexity and task accuracy against same-budget 1-bit, random 1.5-bit, weight-L2 1.5-bit, and 2-bit references.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-transformer validation of learned 1.5-bit residual channel selection
- Success threshold: Learned activation-aware 1.5-bit selection improves perplexity degradation by at least 10% relative to weight-L2 1.5-bit on paired runs while staying at the same average bit budget.
- Stop condition: Stop if learned selection does not beat weight-L2 1.5-bit on at least two of three paired calibration slices or if the direct transformer run cannot be completed within local resource limits.

## Evidence references

- Artifact root: `<local-path>/projects/1-5-bit-weight-quantization-with-learned-residual-channel-selection-a821d3a65335`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
