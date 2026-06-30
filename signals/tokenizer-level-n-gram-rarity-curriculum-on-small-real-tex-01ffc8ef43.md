# Tokenizer-level n-gram rarity curriculum on small real-text pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tokenizer-level-n-gram-rarity-curriculum-on-small-real-tex-01ffc8ef43`
Run ID: `tokenizer-level-n-gram-rarity-curriculum-on-small-real-tex-01ffc8ef43-20260528T103154278006+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: N-gram Rarity Curriculum for Local Pretraining: enoch://control-plane/projects/n-gram-rarity-curriculum-for-local-pretraining-593b4bb8ce7d/runs/n-gram-rarity-curriculum-for-local-pretraining-593b4bb8ce7d-20260528T063953343266+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/06d174cb09bf

## What looked useful

Hard tokenizer n-gram rarity front-loading did not improve rare-token/block modeling. At 600 steps rare_first was worse than baseline on all target metrics in both seeds; at 3000 steps rare_first degraded rare-test loss by about 9.9% and 11.0% relative to seed-matched baselines. A common_first control also degraded at 3000 steps, suggesting the failure mechanism is hard subset front-loading/distribution narrowing rather than rarity-specific benefit.

## Boundaries and scale limits

Limited to WikiText-2 raw, 2M train characters, non-overlapping 128-token blocks, two seeds, and hard restricted-pool curricula. Does not test larger corpora, GPT-2-small-class models, more seeds, smooth rarity weighting, or long full-scale pretraining.

## Claim scope

Small direct real-text pretraining test on WikiText-2 raw with a 2.2M-parameter causal Transformer, 2048-token byte-level BPE, tokenizer bigram/trigram rarity scoring, two seeds, and hard first-half rare-only curriculum versus uniform sampling.

## Why it stopped

Controlled small direct evidence failed the success threshold and showed persistent degradation, not a rare-block improvement, versus uniform random sampling.

## Recommended next action

Stop this hard rare-first curriculum line as no-paper evidence; the only bounded next test worth running is a smooth rarity-weighted sampler that never restricts training to the rare pool.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Smooth rarity-weighted sampling without hard rare-only front-loading
- Success threshold: Smooth rarity-weighted sampler improves rare validation and rare test loss by at least 1% relative to seed-matched uniform baseline while changing ordinary validation/test loss by no worse than +0.2%.
- Stop condition: Stop if smooth rarity weighting fails to improve rare validation loss in at least 2 of 3 seeds, or if ordinary validation/test loss worsens by more than 0.2% relative to baseline.

## Evidence references

- Artifact root: `<local-path>/projects/tokenizer-level-n-gram-rarity-curriculum-on-small-real-tex-01ffc8ef43`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
