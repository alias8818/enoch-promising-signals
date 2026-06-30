# Small-transformer RCQ LoRA validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-transformer-rcq-lora-validation-fb672ae5ba`
Run ID: `small-transformer-rcq-lora-validation-fb672ae5ba-20260528T035742187866+0000`

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

- Parent run decision: Residual Channel Quantization for Home Fine-Tuning: VRAM-Efficient LoRA on Quantized Base: enoch://control-plane/projects/residual-channel-quantization-for-home-fine-tuning-vram-efficient-lora-on-quantized-base-6521d0dcaf1a/runs/residual-channel-quantization-for-home-fine-tuning-vram-efficient-lora-on-quantized-base-6521d0dcaf1a-20260528T020513233565+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/93bf42d03423

## What looked useful

RCQ carries the single-linear mechanism into transformer layers at the weight-reconstruction level, but this Tier 1 direct transformer run did not show a practically meaningful validation-loss benefit. Best RCQ loss was 0.299959 vs q4 LoRA 0.300365, a 0.000406 loss improvement below across-seed standard deviation, with 23.5% estimated memory overhead over q4 LoRA.

## Boundaries and scale limits

Tested only a tiny synthetic causal transformer: d_model 96, 2 layers, 4 heads, seq_len 48, vocab 64, 220 base steps, 180 adapter steps, 3 seeds. It did not test real text, GPT-2-small-class checkpoints, production q4 kernels, optimizer/activation memory, long runs, or downstream task quality.

## Claim scope

In a 3-seed synthetic small-transformer language-model adaptation test, RCQ residual rows monotonically reduced q4 linear-weight reconstruction error and produced a tiny best held-out loss improvement at 10% residual rows, but the improvement was smaller than seed noise and q4 LoRA already matched fp LoRA.

## Why it stopped

Tier 1 direct transformer validation was mixed: RCQ corrected quantization error and gave a tiny best loss gain, but the effect was below seed noise and not a practical or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; only deepen if running a bounded real-text GPT-2-small-class validation where q4 LoRA has a measurable gap for RCQ to close.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text GPT-2-small-class RCQ LoRA validation
- Success threshold: RCQ must improve validation perplexity or loss over q4 LoRA by at least 10% of the q4-vs-fp LoRA gap across seeds, with no more than 60% of fp/bf16 base+adapter memory.
- Stop condition: Stop if q4 LoRA has no measurable degradation versus fp/bf16 LoRA, or if RCQ improvement over q4 LoRA is under 0.5% relative validation loss/perplexity or inconsistent across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-rcq-lora-validation-fb672ae5ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
