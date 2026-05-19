# Small-transformer perplexity test for gradient-informed residual channel preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-transformer-perplexity-test-for-gradient-informed-re-53132be3e8`
Run ID: `small-transformer-perplexity-test-for-gradient-informed-re-53132be3e8-20260516T201923539536+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/9f35e150e0c8

## What looked useful

Gradient-informed residual-channel preservation beat the aggregate random-mask mean at 25%, 50%, and 75% channel keep fractions, with perplexity-ratio deltas of -1.242, -0.058, and -0.314 respectively; however, the 50% condition beat the per-seed random mean in only 1 of 3 seeds and activation-only remained a strong control.

## Boundaries and scale limits

Small character-level corpus, 128-wide 4-layer Transformer, 1400 training steps, no GPT-2-small-class model, no large-token corpus, no fine-tuning recovery, and only 3 training seeds.

## Claim scope

In a 3-seed Tiny Shakespeare character-level 4-layer Transformer test, residual channels ranked by abs(activation * gradient) produced lower aggregate validation perplexity degradation than random, activation-only, and weight-magnitude masks, but the effect was not robust at every keep fraction or against activation-only per seed.

## Why it stopped

This Tier 1 direct small-transformer test produced a useful but mixed mechanism signal, not paper-ready evidence: aggregate grad-act masks beat random, but robustness at 50% keep and superiority over activation-only were insufficient.

## Recommended next action

Run one deepen follow-up with at least 5 seeds, a stronger small/GPT-2-small-class tokenizer-based LM if feasible, and a short post-pruning fine-tuning recovery phase; stop if grad-act does not beat activation-only and random in at least 4 of 5 seeds at 50% and 75% keep.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust residual-channel preservation with tokenizer LM and recovery fine-tuning
- Success threshold: Grad-act must beat both activation-only and the random-mask mean in at least 4 of 5 seeds at both 50% and 75% keep, and must retain a lower aggregate recovered validation perplexity after fine-tuning.
- Stop condition: Stop as negative if grad-act fails to beat activation-only or random in at least 4 of 5 seeds at either 50% or 75% keep, or if recovered perplexity is statistically indistinguishable from activation-only.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-perplexity-test-for-gradient-informed-re-53132be3e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
