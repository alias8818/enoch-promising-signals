# Multi-seed longer GPT-2-small AdamW8bit validation curve check

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-seed-longer-gpt-2-small-adamw8bit-validation-curve-c-c81c806e82`
Run ID: `multi-seed-longer-gpt-2-small-adamw8bit-validation-curve-c-c81c806e82-20260610T170949427859+0000`

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

- Parent run decision: Real-text GPT-2-small AdamW8bit stability and validation-perplexity check on GB10: enoch://control-plane/projects/real-text-gpt-2-small-adamw8bit-stability-and-validation-p-75ddb1685c/runs/real-text-gpt-2-small-adamw8bit-stability-and-validation-p-75ddb1685c-20260610T163829376389+0000
- Parent run decision: 8-bit AdamW vs full AdamW on GPT-2-small, gb10: enoch://control-plane/projects/8-bit-adamw-vs-full-adamw-on-gpt-2-small-gb10-d7f5b2a6f68c/runs/8-bit-adamw-vs-full-adamw-on-gpt-2-small-gb10-d7f5b2a6f68c-20260610T125214723069+0000

## What looked useful

AdamW8bit mean final validation loss was 3.089354 versus 3.090447 for torch AdamW across three matched seeds; paired 8bit-minus-torch final loss mean was -0.001093 with values [-0.003091, 0.001369, -0.001557]. AdamW8bit also used lower active CUDA allocation in these runs.

## Boundaries and scale limits

Only 200 optimizer steps, WikiText-2, pretrained GPT-2 small, one learning-rate schedule, three main seeds, and one bnb AdamW32bit ablation seed were tested. This does not validate from-scratch pretraining, larger models, longer schedules, other corpora, or publication-grade robustness.

## Claim scope

In pretrained GPT-2 small fine-tuning on WikiText-2 for 200 optimizer steps with 8192 tokens per step, bitsandbytes AdamW8bit matched torch AdamW validation-loss curves across seeds 1001, 1002, and 1003 within a +0.02 final-validation-loss threshold.

## Why it stopped

Tier-2 direct evidence supports the bounded mechanism but is not broad or long enough for paper-positive validation.

## Recommended next action

Run a bounded deepen follow-up with 1000 optimizer steps, two learning rates, and a second corpus slice before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer GPT-2-small AdamW8bit robustness curve across learning rates and corpus slices
- Success threshold: AdamW8bit final validation loss no worse than +0.02 versus torch AdamW on matched seeds in both learning-rate settings, with no divergence or persistent validation-loss spikes.
- Stop condition: Stop early if AdamW8bit is worse than torch AdamW by more than +0.02 final validation loss on at least two of three matched seeds in any setting, or if optimizer instability appears in repeated checkpoints.

## Evidence references

- Artifact root: `<local-path>/projects/multi-seed-longer-gpt-2-small-adamw8bit-validation-curve-c-c81c806e82`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
