# CPU-capped LoRA versus dense controls on GPT-2 Wikitext-2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-capped-lora-versus-dense-controls-on-gpt-2-wikitext-2-1de811d5ff`
Run ID: `cpu-capped-lora-versus-dense-controls-on-gpt-2-wikitext-2-1de811d5ff-20260610T215501815210+0000`

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

- Parent run decision: LoRA Adapter Fine-tuning for CPU Memory-constrained Domain Adaptation: enoch://control-plane/projects/lora-adapter-fine-tuning-for-cpu-memory-constrained-domain-adaptation-559390b33bb9/runs/lora-adapter-fine-tuning-for-cpu-memory-constrained-domain-adaptation-559390b33bb9-20260610T204248272481+0000
- Parent run decision: CPU-capped LoRA adaptation on a small real transformer corpus: enoch://control-plane/projects/cpu-capped-lora-adaptation-on-a-small-real-transformer-cor-d154f7fae0/runs/cpu-capped-lora-adaptation-on-a-small-real-transformer-cor-d154f7fae0-20260610T210347545311+0000

## What looked useful

LoRA rank 8 improved mean validation loss from 3.9813 frozen to 3.7609, and LoRA rank 2 reached 3.8432, indicating rank-sensitive LoRA benefit. Dense last-block control reached 3.7320 mean validation loss and beat LoRA rank 8 by 0.0236, 0.0293, and 0.0338 loss on seeds 17, 29, and 43.

## Boundaries and scale limits

Short local CPU schedule; dense control is not parameter-matched and has about 8.7x more trainable parameters than LoRA rank 8. No longer schedules, learning-rate sweeps, full fine-tuning, larger models, or broader datasets were tested.

## Claim scope

GPT-2-small on WikiText-2 with 40 CPU-capped fine-tuning steps, block size 128, batch size 2, 8 Torch CPU threads, seeds 17/29/43, and 24,576 validation tokens per seed. LoRA attention adapters improve over frozen GPT-2 and rank 8 beats rank 2, but dense last-block fine-tuning achieves lower validation loss than LoRA rank 8 in all tested seeds.

## Why it stopped

Direct medium CPU evidence does not support a positive paper claim: LoRA improves over frozen and rank 8 beats rank 2, but the real dense last-block control beats LoRA rank 8 on all fixed seeds in the tested regime.

## Recommended next action

Stop this run as no-paper useful signal; if continuing the line, run a parameter-matched dense-control follow-up before making any LoRA efficiency claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched dense controls for CPU-capped GPT-2 LoRA on WikiText-2
- Success threshold: LoRA rank 8 has lower mean validation loss than the parameter-matched dense control across 3 fixed seeds, wins at least 2 of 3 seeds, and preserves the rank-8 over rank-2 ordering.
- Stop condition: Stop if the parameter-matched dense control beats or ties LoRA rank 8 in mean validation loss after the predeclared schedule, or if runtime exceeds the local CPU budget without producing all fixed-seed direct metrics.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-capped-lora-versus-dense-controls-on-gpt-2-wikitext-2-1de811d5ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
