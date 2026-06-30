# LoRA-Style Low-Rank Adaptation for Tiny VRAM Fine-tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lora-style-low-rank-adaptation-for-tiny-vram-fine-tuning-333711f0555a`
Run ID: `lora-style-low-rank-adaptation-for-tiny-vram-fine-tuning-333711f0555a-20260613T142118770109+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2cedb9658183

## What looked useful

Parameter-efficient updates were useful under a tiny trainable-state budget: LoRA reached 0.5280 mean target accuracy versus 0.4596 for head-only and 1.0000 for full fine-tuning. A parameter-matched adapter reached 0.5232, so the evidence supports parameter-efficient adaptation generally rather than a distinctive LoRA advantage.

## Boundaries and scale limits

Small synthetic classification task only; no GPT-2-small-class pretrained baseline, no natural-language corpus, no quantized base weights, no long-run robustness, and no validation under real near-limit VRAM pressure.

## Claim scope

On a 535k-parameter CUDA-backed synthetic arithmetic adaptation probe, rank-4 LoRA recovered more target accuracy than head-only tuning while using 4.59% of full fine-tune trainable parameters and optimizer-state memory, but it tied a parameter-matched bottleneck adapter and did not approach full fine-tuning.

## Why it stopped

The local evidence is a synthetic bounded signal, not a full validation: LoRA improved over head-only but tied a parameter-matched adapter and remained far below full fine-tuning.

## Recommended next action

Stop this run as no-paper useful-signal evidence; run one bounded deepen follow-up on a GPT-2-small-class or real text benchmark with matched LoRA, adapter, and full fine-tune controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class matched LoRA versus adapter tiny-VRAM adaptation
- Success threshold: LoRA must match or exceed the parameter-matched adapter within statistical noise and recover at least 80% of the full fine-tune improvement over the frozen/head-only control while using no more than 10% of full fine-tune optimizer-state memory.
- Stop condition: Stop as negative if LoRA remains tied with or below the adapter and recovers less than 80% of the full fine-tune improvement after a documented rank/lr/step ablation.

## Evidence references

- Artifact root: `<local-path>/projects/lora-style-low-rank-adaptation-for-tiny-vram-fine-tuning-333711f0555a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
