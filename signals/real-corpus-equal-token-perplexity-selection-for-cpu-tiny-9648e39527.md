# Real-corpus equal-token perplexity selection for CPU tiny neural LM pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-corpus-equal-token-perplexity-selection-for-cpu-tiny-9648e39527`
Run ID: `real-corpus-equal-token-perplexity-selection-for-cpu-tiny-9648e39527-20260524T034901259923+0000`

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

- Parent run decision: Perplexity-based Data Selection for CPU Tiny Pretraining: enoch://control-plane/projects/perplexity-based-data-selection-for-cpu-tiny-pretraining-6912adf7a600/runs/perplexity-based-data-selection-for-cpu-tiny-pretraining-6912adf7a600-20260524T033951193217+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c6d5d87a4c4e

## What looked useful

Perplexity scoring was informative, but the benefit in this controlled CPU-tiny setting came from selecting low-perplexity documents, not from equal-token coverage of perplexity strata. Equal-token selection was 0.12% worse than random at 60k tokens and 0.23% worse than random at 30k tokens; low-perplexity selection was 3.82% and 5.81% better than random respectively.

## Boundaries and scale limits

Single real corpus; tiny word-level neural bigram LM rather than transformer; smoothed bigram document scorer; same-corpus held-out perplexity only; no broad web-scale, multi-corpus, downstream, or long pretraining validation.

## Claim scope

On Tiny Shakespeare with a NumPy word-level neural bigram LM, matched 30k and 60k selected-token budgets, and three seeds per budget, equal-token document selection across perplexity buckets did not improve held-out perplexity over random selection and was consistently worse than lowest-perplexity selection.

## Why it stopped

Controlled small direct tests did not support the equal-token perplexity selection hypothesis; this is direct small-scale falsification, not full-scale validation.

## Recommended next action

Stop this run as a no-paper useful negative; if continuing, run a bounded transformer follow-up on a second real corpus to test whether low-perplexity filtering, not equal-token stratification, is the robust mechanism.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Second-corpus tiny transformer check for low-perplexity filtering versus equal-token stratification
- Success threshold: Low-perplexity selection beats random and equal-token selection by at least 2% lower mean validation perplexity across at least three seeds; equal-token selection must beat random by at least 2% to revive the original hypothesis.
- Stop condition: Stop if equal-token selection is within +/-1% of random or worse on mean validation perplexity, or if low-perplexity selection fails to beat random by at least 2%.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-equal-token-perplexity-selection-for-cpu-tiny-9648e39527`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
