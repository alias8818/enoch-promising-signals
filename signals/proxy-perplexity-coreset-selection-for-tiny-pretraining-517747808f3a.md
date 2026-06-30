# Proxy-perplexity coreset selection for tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `proxy-perplexity-coreset-selection-for-tiny-pretraining-517747808f3a`
Run ID: `proxy-perplexity-coreset-selection-for-tiny-pretraining-517747808f3a-20260607T194140309352+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d4d11440c3cb

## What looked useful

Naive lowest-proxy-perplexity selection failed the predeclared threshold and was much worse than random: mean eval NLL 2.7502 for low_ppl versus 0.7796 for random. The failure was explained by coverage collapse: low_ppl selected 100% alpha-domain documents while target validation was balanced across alpha, bravo, and charlie. Perplexity-stratified selection preserved coverage and slightly beat random.

## Boundaries and scale limits

No neural transformer training, no real corpus, no tokenizer or optimizer effects, and no large-scale pretraining validation. CPU-only run completed 20 synthetic trials in 14.1 seconds.

## Claim scope

Synthetic character-language-model coreset test: a biased 3-gram proxy scored mixed-domain documents, fixed-budget subsets trained a 5-gram target LM, and evaluation used balanced held-out synthetic domains.

## Why it stopped

The predeclared success threshold was missed in a direct small proxy test: low_ppl did not improve over random by 1% and instead increased balanced target validation NLL by 252.8% relative to random. This is an early falsification, not a full-scale validation.

## Recommended next action

Stop this run as a proxy/synthetic early falsification of naive low-proxy-perplexity coreset selection; run the bounded follow-up comparing low-ppl, random, and ppl-stratified selection in a tiny transformer on a real mixed corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer test of perplexity-stratified coreset selection on a real mixed corpus
- Success threshold: ppl_stratified beats random by at least 1% held-out perplexity and beats low_ppl in at least 3 of 3 seeds without reducing source/domain coverage below random by more than 10%.
- Stop condition: Stop if low_ppl and ppl_stratified are statistically indistinguishable from random, or if domain/source coverage diagnostics do not explain any observed difference.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-perplexity-coreset-selection-for-tiny-pretraining-517747808f3a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
