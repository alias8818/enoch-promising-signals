# Train a calibrated GPT-2 intermediate head for self-speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `train-a-calibrated-gpt-2-intermediate-head-for-self-specul-ab7b7bb3b5`
Run ID: `train-a-calibrated-gpt-2-intermediate-head-for-self-specul-ab7b7bb3b5-20260516T170303180488+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/651118c6a43c

## What looked useful

Target-aligned distillation gave a small held-out acceptance gain over a calibrated intermediate tied-head control, while ordinary CE training was not compelling. Calibration dominates much of the benefit, and the trained head's distribution quality is mixed.

## Boundaries and scale limits

Single GPT-2-small model, one dataset, one layer, one seed, 16,384 collected training tokens, 2,048 calibration tokens, 2,048 held-out evaluation tokens, one-token distribution metric only; no multi-token autoregressive speculative decoding or throughput benchmark.

## Claim scope

On GPT-2-small layer 6 with WikiText-2 and one seed, a distribution-distilled intermediate vocabulary head improved held-out one-token speculative acceptance mass over a temperature-calibrated tied-head baseline by 0.0203 absolute, but did not improve held-out top-1 agreement and worsened KL(final || draft).

## Why it stopped

Tier 1 direct held-out test produced a small mixed mechanism signal, not publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded direct test is a multi-seed layer/objective sweep with generated-prefix speculative decoding acceptance and overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layer and objective sweep for GPT-2 self-speculative intermediate heads
- Success threshold: Median held-out acceptance gain of at least 0.03 absolute over calibrated tied-head control, no median KL(final || draft) regression, and generated-prefix accept rate improvement sufficient to plausibly offset draft-head overhead.
- Stop condition: Stop if no layer/objective reaches +0.03 held-out acceptance gain over the calibrated control or if generated-prefix simulation loses the one-token acceptance improvement.

## Evidence references

- Artifact root: `<local-path>/projects/train-a-calibrated-gpt-2-intermediate-head-for-self-specul-ab7b7bb3b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
