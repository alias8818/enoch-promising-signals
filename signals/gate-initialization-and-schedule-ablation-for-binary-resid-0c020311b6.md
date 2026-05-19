# Gate initialization and schedule ablation for binary residual bottleneck adapters

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `gate-initialization-and-schedule-ablation-for-binary-resid-0c020311b6`
Run ID: `gate-initialization-and-schedule-ablation-for-binary-resid-0c020311b6-20260518T111304663378+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Gate initialization and schedule ablation for binary residual bottleneck adapters: internal_generated:gate-initialization-and-schedule-ablation-for-binary-resid-0c020311b6

## What looked useful

Binary residual bottleneck adapters were trainable and beat frozen target evaluation by about 0.21 validation loss with 38404 trainable parameters, but gate init/schedule effects were within seed-scale variation and the best binary mean loss 1.5622 trailed dense adapters at 1.5376 and full finetuning at 1.5212.

## Boundaries and scale limits

Single small character-level corpus, 1.8M-parameter transformer, 1500 adaptation steps, PyTorch STE binary weights without packed binary inference kernels; no GPT-2-small-class tokenizer/model, no broad corpus/task suite, and no hardware efficiency validation.

## Claim scope

On a three-seed Tiny Shakespeare chronological domain-adaptation benchmark with a 1.8M-parameter causal transformer, rank-24 binary residual bottleneck adapters improve over a frozen pretrained model but do not benefit meaningfully from tested gate initialization or 400-step gate warmup choices, and they underperform matched dense bottleneck adapters and full finetuning on best target validation loss.

## Why it stopped

Bounded direct validation with fixed seeds, dense/control baselines, and target validation metrics found useful trainability but no robust gate-init/schedule advantage and no quality win over matched dense adapters.

## Recommended next action

Stop this follow-up as no-paper evidence; pursue a materially different binary-adapter mechanism or a packed-kernel hardware-efficiency study rather than another gate-init/schedule sweep.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/gate-initialization-and-schedule-ablation-for-binary-resid-0c020311b6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
