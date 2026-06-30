# Residual adapter training on 1-bit base for home CPU fine-tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-adapter-training-on-1-bit-base-for-home-cpu-fine-tuning-b9827178eb2b`
Run ID: `residual-adapter-training-on-1-bit-base-for-home-cpu-fine-tuning-b9827178eb2b-20260525T071131050545+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/278e45695bb5

## What looked useful

Residual adapters on a frozen 1-bit MLP base are trainable and useful in a toy shifted-domain setting, but random-sign controls recover much of the same performance. The clearest 1-bit-base edge appeared in the 5 examples/class regime, with paired onebit-minus-random gains of +2.6 to +5.1 percentage points at ranks 2-8.

## Boundaries and scale limits

This run did not test transformers, language modeling, GPT-2-small-class baselines, 7B-class models, native 1-bit pretraining, real instruction fine-tuning, or actual home CPU wall-clock usability. Random-sign adapter controls were close, so the base-preservation mechanism is only weakly separated from adapter capacity.

## Claim scope

In a sklearn-digits MLP proxy, frozen sign-plus-scale 1-bit base weights with trainable low-rank residual adapters can recover target-domain accuracy from near chance to 82-92% with 20 examples per class and 65-78% with 5 examples per class.

## Why it stopped

The result is a proxy-only mixed signal: the residual adapter works, but random-sign controls are too competitive to support the broad home CPU 1-bit fine-tuning claim.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded small-transformer language-modeling follow-up only if the next campaign can compare frozen 1-bit, dense, and random-sign bases at matched adapter ranks on validation perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer residual adapters on frozen 1-bit language-model bases
- Success threshold: The 1-bit residual-adapter condition improves validation perplexity by at least 5% relative to the random-sign residual-adapter control at matched trainable parameter count in at least two adapter ranks, without worse CPU memory or wall-clock behavior than dense-base adapters.
- Stop condition: Stop as negative if random-sign residual adapters are within 5% relative perplexity of the 1-bit condition across ranks or if CPU wall-clock exceeds the bounded local budget before producing paired validation metrics.

## Evidence references

- Artifact root: `<local-path>/projects/residual-adapter-training-on-1-bit-base-for-home-cpu-fine-tuning-b9827178eb2b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
