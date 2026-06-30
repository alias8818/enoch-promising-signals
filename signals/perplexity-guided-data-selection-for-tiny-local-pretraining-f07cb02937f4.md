# Perplexity-Guided Data Selection for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-guided-data-selection-for-tiny-local-pretraining-f07cb02937f4`
Run ID: `perplexity-guided-data-selection-for-tiny-local-pretraining-f07cb02937f4-20260527T175831100155+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7a7e6dcc5445

## What looked useful

Perplexity scoring worked as a reject signal for extreme out-of-domain data, but lowest-perplexity positive selection was effectively tied with random at equal byte budget: 8-seed low-PPL mean held-out loss 1.4098 versus random 1.4036, paired low-minus-random delta +0.0062 with low-PPL winning 4/8 seeds.

## Boundaries and scale limits

Synthetic generated corpus, n-gram scorer, byte-level 4-layer Transformer, 45k-byte selected subsets, 450 optimizer steps per run, 8 seeds for low-vs-random. No real web corpus, pretrained scorer, GPT-2-small-class model, downstream evaluation, or long-token-budget validation.

## Claim scope

In a controlled synthetic mixed-corpus proxy using a character n-gram perplexity scorer and tiny byte-level Transformer pretraining at equal byte budget, naive lowest-perplexity subset selection did not improve held-out target LM loss over random selection; high-perplexity selection was clearly harmful.

## Why it stopped

Equal-byte local proxy did not support naive low-perplexity selection as an improvement over random; evidence is useful but not paper-positive or full validation.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should add diversity or deduplication constraints to low-perplexity selection and compare against random and low-PPL-only on a small real corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-Constrained Perplexity Selection for Tiny Pretraining
- Success threshold: Diversity-constrained low-PPL selection reduces mean held-out loss by at least 3% versus random and naive low-PPL with paired improvement in at least 4 of 5 seeds.
- Stop condition: Stop if diversity-constrained low-PPL is within 1% of random/naive low-PPL or loses on at least 3 of 5 paired seeds.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-guided-data-selection-for-tiny-local-pretraining-f07cb02937f4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
