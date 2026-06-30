# Proxy-scored data filtering for tiny pretraining on gb10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `proxy-scored-data-filtering-for-tiny-pretraining-on-gb10-bcb7e110f2a5`
Run ID: `proxy-scored-data-filtering-for-tiny-pretraining-on-gb10-bcb7e110f2a5-20260614T085618380031+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/665fad9cd7d2

## What looked useful

Proxy scoring ranked block difficulty, but naive easiest-block filtering lowered target training loss while worsening validation loss versus random in every seed. Mean validation perplexity was 631.67 for low proxy loss, 623.33 for random, and 647.17 for high proxy loss.

## Boundaries and scale limits

Toy-to-small local evidence only: 6,500 train lines, 1,500 validation lines, 11,750 train blocks, 3 seeds, short training horizon, one corpus, one tokenizer, one model size, one proxy-loss scoring rule, no GPT-2-small-class or internet-scale validation.

## Claim scope

On WikiText-2 subsets with a 2.53M-parameter causal transformer, a brief proxy LM, 35% candidate-block filtering, and 260 equal-budget target updates across three seeds, selecting lowest proxy-loss blocks did not improve validation perplexity over random filtering; selecting highest proxy-loss blocks was worse.

## Why it stopped

Proxy/early falsification rather than full validation: the tested naive low-proxy-loss policy was consistently worse than random on validation perplexity across three GB10 toy-scale runs.

## Recommended next action

Stop this run as a proxy/early falsification of naive low-loss proxy filtering; a bounded next test should evaluate diversity-constrained or stratified proxy-score mixtures against random at the same token budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-constrained proxy-score mixtures for tiny pretraining
- Success threshold: Stratified or diversity-constrained proxy filtering improves mean validation loss by at least 0.01 versus random across at least five seeds, with no single seed worse than random by more than 0.005.
- Stop condition: Stop if the mixture fails to beat random mean validation loss by 0.01 or if improvements are explained only by seed variance or unequal token/update budgets.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-scored-data-filtering-for-tiny-pretraining-on-gb10-bcb7e110f2a5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
