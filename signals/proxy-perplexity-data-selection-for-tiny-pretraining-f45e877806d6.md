# Proxy Perplexity Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `proxy-perplexity-data-selection-for-tiny-pretraining-f45e877806d6`
Run ID: `proxy-perplexity-data-selection-for-tiny-pretraining-f45e877806d6-20260608T175936734760+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7039c70da27b

## What looked useful

Across five synthetic seeds, proxy_low selected 100% target-domain documents and improved target eval NLL over random by mean -0.0895, while proxy_high selected 0% target-domain documents and was worse than random by mean +1.3939 NLL.

## Boundaries and scale limits

Synthetic corpus only; no natural web corpus, tokenizer-scale pretraining, GPT-2-small-class baseline, downstream task evaluation, deduplication, contamination, or long-run scaling was tested.

## Claim scope

On a controlled synthetic four-domain corpus, byte-level 4-gram proxy perplexity trained from a small target-domain seed selected target-domain documents and improved tiny byte-GRU held-out target perplexity versus random selection under a fixed document and training-step budget.

## Why it stopped

No-paper useful signal: the mechanism was supported only in a synthetic favorable setting, which is insufficient for publication-grade validation.

## Recommended next action

Run a bounded natural-corpus deepen test with the same low/random/middle/high proxy-perplexity controls and at least three seeds before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-corpus proxy perplexity selection for tiny LM pretraining
- Success threshold: proxy_low mean held-out target NLL at least 0.03 lower than random across seeds, with no material duplicate-rate or diversity collapse relative to random.
- Stop condition: Stop if proxy_low does not beat random by 0.03 mean held-out target NLL, if the effect is seed-unstable, or if gains are explained by near-duplicate selection.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-perplexity-data-selection-for-tiny-pretraining-f45e877806d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
