# Perplexity-bucketed data curriculum for GPT-2-small pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-bucketed-data-curriculum-for-gpt-2-small-pretraining-32b52743113d`
Run ID: `perplexity-bucketed-data-curriculum-for-gpt-2-small-pretraining-32b52743113d-20260620T085242029985+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bd9b07e16388

## What looked useful

Across three seeds, easy-to-hard perplexity bucketing was worse than random sampling on overall validation loss by a mean relative +0.355%. Bucket diagnostics showed a small easy-bucket gain but harder-bucket degradation, suggesting naive curriculum shifts capacity toward easy examples under a fixed sequence-item budget.

## Boundaries and scale limits

This was not GPT-2-small scale, did not use a GPT-2 tokenizer, used a byte-bigram teacher rather than a neural perplexity scorer, and ran only 350 optimizer steps per schedule across three seeds.

## Claim scope

In a bounded local byte-level GPT-style pretraining proxy on Wikitext-2 text blocks, a naive easy-to-hard curriculum based on frozen byte-bigram perplexity buckets did not improve equal-budget validation loss over random sampling.

## Why it stopped

Proxy early falsification: the simple easy-to-hard perplexity-bucket curriculum consistently lost to random sampling under equal token and step budgets, so it is not paper-ready and should not be scaled unchanged.

## Recommended next action

Stop this naive curriculum variant; a bounded follow-up should test paced curriculum with hard-bucket replay to see whether the observed hard-bucket degradation can be removed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paced perplexity curriculum with hard-bucket replay
- Success threshold: Paced curriculum beats random validation loss by at least 1% mean relative improvement across three seeds and has no positive mean delta on the hardest validation bucket.
- Stop condition: Stop if paced replay is not better than random overall or still worsens the hardest bucket after the equal-token endpoint.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-bucketed-data-curriculum-for-gpt-2-small-pretraining-32b52743113d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
