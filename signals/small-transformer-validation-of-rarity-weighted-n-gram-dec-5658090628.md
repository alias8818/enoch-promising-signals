# Small-transformer validation of rarity-weighted n-gram decontamination

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-transformer-validation-of-rarity-weighted-n-gram-dec-5658090628`
Run ID: `small-transformer-validation-of-rarity-weighted-n-gram-dec-5658090628-20260528T153013401823+0000`

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

- Parent run decision: Contamination-aware n-gram filtering for pretraining: enoch://control-plane/projects/contamination-aware-n-gram-filtering-for-pretraining-b12df577d4e7/runs/contamination-aware-n-gram-filtering-for-pretraining-b12df577d4e7-20260528T114612824177+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/45f7ea8c7955

## What looked useful

Rarity weighting separated rare answer-bearing leaks from common boilerplate overlap at the data level and preserved the benign-overlap behavior in the trained small Transformer. Compared with unweighted filtering, it kept 120 additional benign examples per seed and reduced held-out benign-overlap loss from 4.7526 to 1.3521 while still removing all injected leaks.

## Boundaries and scale limits

Synthetic corpus only; exact/near-exact contamination only; manually calibrated thresholds; 2-layer tiny Transformer trained for 450 steps across 3 seeds; no natural web corpus, paraphrase contamination, threshold sweep, or GPT-2-small-scale validation.

## Claim scope

In a controlled synthetic QA-like corpus with repeated exact rare canary contamination and common-template benign overlap, rarity-weighted 5-gram decontamination removed all contaminated training examples while retaining benign overlap examples; a tiny causal Transformer trained after filtering showed reduced canary answer likelihood versus no filtering and much better benign-overlap validation loss than an unweighted overlap filter.

## Why it stopped

Tier-1 direct small-transformer validation completed; evidence supports the mechanism locally but is not publication-grade because it is synthetic, threshold-calibrated, and small-scale.

## Recommended next action

Run a bounded deepen follow-up with threshold sweeps and partial/paraphrased contamination on a natural text benchmark before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Threshold and paraphrase robustness for rarity-weighted n-gram decontamination
- Success threshold: Across at least 3 seeds and a nontrivial threshold band, rarity-weighted filtering removes at least 95% of exact/partial injected leaks, keeps benign false-positive rate at least 50% lower than unweighted filtering at matched leak removal, and does not reduce canary answer NLL by more than 0.25 relative to the stricter unweighted filter.
- Stop condition: Stop if rarity weighting cannot maintain at least 95% leak removal with a materially lower benign false-positive rate than unweighted filtering, or if trained-model canary suppression collapses relative to unweighted filtering under matched thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-validation-of-rarity-weighted-n-gram-dec-5658090628`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
