# Coverage-constrained sampled AdamW recomputation on the same small transformer

Status: `useful_signal`
Project ID: `coverage-constrained-sampled-adamw-recomputation-on-the-sa-04a71608ba`
Run ID: `coverage-constrained-sampled-adamw-recomputation-on-the-sa-04a71608ba-20260517T164403339632+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Coverage-constrained sampled AdamW recomputation on the same small transformer: internal_generated:coverage-constrained-sampled-adamw-recomputation-on-the-sa-04a71608ba

## What looked useful

Coverage-constrained sampling at 50% update coverage ended at mean validation loss 2.0112 versus dense AdamW 1.6060 and iid 50% sampling 1.7689; 25% coverage ended at 2.2444. Sampled variants were about 1.65-1.67x slower wall-clock because unfused mask/index optimizer work dominated.

## Boundaries and scale limits

Small local language-model task only; no custom fused CUDA/Triton optimizer, no GPT-2-small-class tokenized corpus, no large model, and no sampled-update-specific learning-rate retuning.

## Claim scope

On a 4-layer, 4-head, 192-dim char-level transformer trained for 2,000 steps on Tiny Shakespeare across three fixed seeds, the tested coverage-constrained sampled AdamW lazy-recomputation optimizer does not preserve dense AdamW validation loss and is slower wall-clock in this unfused implementation.

## Why it stopped

Direct bounded validation on the target small transformer showed consistent quality regression versus dense AdamW and versus the iid sampling control, plus no practical speed benefit in the runnable implementation.

## Recommended next action

Stop this follow-up branch as no-paper evidence; only revisit if implementing a fused sampled optimizer and retuning it against dense AdamW on a larger direct LM target.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/coverage-constrained-sampled-adamw-recomputation-on-the-sa-04a71608ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
