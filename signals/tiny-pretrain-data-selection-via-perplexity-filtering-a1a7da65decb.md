# Tiny Pretrain Data Selection via Perplexity Filtering

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-pretrain-data-selection-via-perplexity-filtering-a1a7da65decb`
Run ID: `tiny-pretrain-data-selection-via-perplexity-filtering-a1a7da65decb-20260529T200411085165+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5373dc933828

## What looked useful

Perplexity filtering was useful for removing noisy candidate chunks and improving target-domain bpc at fixed budget, but naive lowest-PPL-only selection was not optimal in this setup; moderate-PPL band-pass selection was best.

## Boundaries and scale limits

This run did not train a neural LM, did not use a tokenizer, did not test web-scale or multi-domain corpora, and included deterministic synthetic noise. Results support only a small count-based language-model proxy mechanism.

## Claim scope

In a CPU-bounded character 5-gram proxy using Tiny Shakespeare as the target domain and a mixed Shakespeare/Alice/noise candidate pool, reference-perplexity filtering improved held-out in-domain bits/character versus random equal-budget selection. Mid-percentile and 20-60% band-pass filters slightly outperformed pure lowest-perplexity selection.

## Why it stopped

No-paper closure: the result is a bounded count-based proxy signal, not direct neural pretraining evidence or publication-grade validation.

## Recommended next action

Run a bounded neural follow-up on the same frozen selected subsets with a tiny character or byte-level LM before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Neural LM Validation of Perplexity Band-Pass Data Selection
- Success threshold: Band-pass or mid-PPL selection improves mean held-out bpc over random by at least 0.03 with no overlap in standard-error intervals across three neural seeds, while high-PPL remains worse than random.
- Stop condition: Stop as unsupported if neural runs show random equal or better than all PPL filters, or if differences are below 0.01 bpc across three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-pretrain-data-selection-via-perplexity-filtering-a1a7da65decb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
