# Perplexity-curriculum ordering for tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-curriculum-ordering-for-tiny-pretraining-c439aba1f17a`
Run ID: `perplexity-curriculum-ordering-for-tiny-pretraining-c439aba1f17a-20260528T152232689364+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/45f7ea8c7955

## What looked useful

Random ordering beat both strict easy-to-hard and hard-to-easy perplexity sorting on all 5 seeds. Easy-to-hard had +0.0758 mean validation loss and 1.079x byte perplexity versus random; hard-to-easy had +0.0530 mean validation loss and 1.054x byte perplexity versus random.

## Boundaries and scale limits

This run used a tiny byte-level Transformer, WikiText-2, fixed strict sorted orders, and a short local training budget. It does not test GPT-2-small-class models, larger corpora, subword tokenization, dynamic curricula, or perplexity bucketing with within-bucket shuffling.

## Claim scope

In a bounded WikiText-2 byte-level tiny causal-LM pretraining setup with 4096 training chunks, 512 validation chunks, 400 main training steps, and 5 seeds, strict ordering by probe-model per-chunk perplexity did not improve validation byte perplexity over random ordering.

## Why it stopped

Bounded direct tiny-pretraining evidence falsified the strict sorted-order variant: both perplexity sort directions were consistently worse than random ordering, so this is a no-paper useful negative signal rather than a publication-grade positive result.

## Recommended next action

Stop scaling strict sorted perplexity curricula as-is; if continuing, run a bounded follow-up that preserves local diversity with coarse perplexity buckets and within-bucket shuffling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-preserving perplexity bucket curriculum
- Success threshold: A bucket-shuffled or annealed perplexity curriculum beats random ordering by at least 0.02 validation loss on mean paired delta across 5 seeds without losing on more than one seed.
- Stop condition: Stop if bucket-shuffled and annealed variants fail to beat random on mean paired validation loss or if improvements are smaller than 0.02 loss with mixed seed outcomes.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-curriculum-ordering-for-tiny-pretraining-c439aba1f17a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
