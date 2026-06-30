# Online perplexity-driven data curriculum for tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `online-perplexity-driven-data-curriculum-for-tiny-pretraining-c9f56f08eb09`
Run ID: `online-perplexity-driven-data-curriculum-for-tiny-pretraining-c9f56f08eb09-20260611T215936430010+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c05ce8741705

## What looked useful

Across 3 seeds at 1500 steps, random sampling reached mean validation loss 2.00019 while online easy-to-hard reached 2.00678, a +0.00658 loss regression and 1.0066x relative perplexity. The online sampler ran at 0.662x random throughput because rescoring added overhead.

## Boundaries and scale limits

Tested only a tiny character-level LM on Tiny Shakespeare with 500-step and 1500-step local GPU probes. It did not test tokenized web-scale corpora, downstream transfer, GPT-2-small-class baselines, offline difficulty curricula, perplexity-difference curricula, or equal-FLOPs accounting beyond measured throughput.

## Claim scope

A simple online current-perplexity curriculum, implemented as periodic per-block rescoring and easy-to-hard percentile sampling, did not improve held-out validation loss over uniform random sampling for a tiny character-level Transformer pretrained on Tiny Shakespeare under equal optimizer-step budgets.

## Why it stopped

Proxy/local early falsification: the directly tested simple online current-perplexity sampler failed to beat random sampling and imposed a clear throughput penalty, but this is not a full validation or broad falsification of curriculum learning.

## Recommended next action

Do not write a paper from this run; if continuing, run a bounded deepen test on a tokenized corpus comparing online current-perplexity sampling against random and known offline/perplexity-difference curriculum baselines under equal-FLOPs accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Equal-FLOPs tokenized comparison of online current-perplexity and offline curriculum samplers
- Success threshold: Online current-perplexity sampling beats random and at least one offline curriculum baseline by at least 1% validation perplexity at equal FLOPs, with no more than 10% wall-clock overhead.
- Stop condition: Stop if online current-perplexity sampling is not better than random under equal FLOPs or if rescoring overhead exceeds the validation-loss gain.

## Evidence references

- Artifact root: `<local-path>/projects/online-perplexity-driven-data-curriculum-for-tiny-pretraining-c9f56f08eb09`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
