# Surprisal-Curriculum Data Ranking for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `surprisal-curriculum-data-ranking-for-tiny-pretraining-00d941e53ff0`
Run ID: `surprisal-curriculum-data-ranking-for-tiny-pretraining-00d941e53ff0-20260520T073933411510+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0189f03a7099

## What looked useful

Teacher surprisal correlated with latent difficulty (mean Spearman 0.702), but surprisal easy-to-hard worsened validation NLL by +0.3375 versus random and won 0/20 seeds; reverse surprisal was worse. Length/oracle easy-to-hard improved hard-document NLL but hurt overall NLL, suggesting pure sorting creates a distribution/recency tradeoff rather than a robust pretraining gain.

## Boundaries and scale limits

Synthetic token corpus, n-gram teacher, small non-transformer learner, CPU-only short run, document-order curriculum only; does not validate behavior on natural text, GPT-2-small-class transformers, data subset selection, or long multi-epoch shuffled curricula.

## Claim scope

In a reproducible synthetic tiny-LM proxy with a NumPy neural next-token model, document-level teacher trigram surprisal ranking used as a pure sorted curriculum did not improve fixed-budget pretraining validation NLL versus random ordering across 20 seeds.

## Why it stopped

Proxy early falsification of the simple pure-sort surprisal curriculum: it underperformed random on the primary validation metric in every seed, so there is no paper-positive result from this run.

## Recommended next action

Stop this run as a proxy negative; the next bounded test should use bucketed/interleaved surprisal replay on a small transformer to separate ranking quality from pure-sort recency bias.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Interleaved Surprisal Buckets for Tiny Transformer Pretraining
- Success threshold: Interleaved surprisal buckets beat random on mean overall validation NLL by at least 1 percent with non-negative hard/rare subset deltas across most seeds.
- Stop condition: Stop if interleaved surprisal fails to beat random overall or reproduces the same hard-subset-only tradeoff as pure sorting.

## Evidence references

- Artifact root: `<local-path>/projects/surprisal-curriculum-data-ranking-for-tiny-pretraining-00d941e53ff0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
