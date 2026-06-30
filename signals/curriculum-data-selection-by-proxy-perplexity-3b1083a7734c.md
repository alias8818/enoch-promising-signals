# Curriculum Data Selection by Proxy Perplexity

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `curriculum-data-selection-by-proxy-perplexity-3b1083a7734c`
Run ID: `curriculum-data-selection-by-proxy-perplexity-3b1083a7734c-20260608T151615204421+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ddd8ca4fc941

## What looked useful

Low proxy perplexity selection consistently underperformed random by about 0.004 to 0.006 validation-loss nats; high proxy perplexity was worse by about 0.008 to 0.011 nats; middle-ranked proxy perplexity was closest to random. The naive easiest-example curriculum appears to overfit or reduce useful diversity under this setup.

## Boundaries and scale limits

Small local corpus, cheap character n-gram proxy, small target model, three training seeds, short fixed-step training; not evidence about neural proxy scorers, larger target models, long training, downstream transfer, or diversity-aware curricula.

## Claim scope

On Wikitext-2 with a character 5-gram proxy selector and a small byte-level Transformer target trained for 300 steps, naive low-proxy-perplexity selection did not improve held-out byte cross entropy over random selection at equal example count or equal byte budget.

## Why it stopped

Proxy/early falsification: the simple low-proxy-perplexity curriculum failed the predefined 0.03-nat improvement threshold and was consistently worse than random in the equal-byte direct target-model test.

## Recommended next action

Stop this run as a bounded proxy/early falsification of naive low-proxy-perplexity selection; a separate deepen follow-up should test neural-proxy quantile mixtures with fixed token budgets and diversity controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural proxy quantile mixtures for curriculum data selection
- Success threshold: A quantile-mixture policy improves final validation loss over random by at least 0.03 nats at equal token budget and beats low-only and high-only selectors in at least three paired seeds.
- Stop condition: Stop if no proxy-perplexity quantile or mixture beats random by at least 0.01 nats after the first calibrated medium run at equal token budget.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-data-selection-by-proxy-perplexity-3b1083a7734c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
