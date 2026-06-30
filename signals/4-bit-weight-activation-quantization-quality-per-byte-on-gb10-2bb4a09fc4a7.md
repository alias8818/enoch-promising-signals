# 4-bit weight+activation quantization quality-per-byte on gb10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `4-bit-weight-activation-quantization-quality-per-byte-on-gb10-2bb4a09fc4a7`
Run ID: `4-bit-weight-activation-quantization-quality-per-byte-on-gb10-2bb4a09fc4a7-20260629T192229117239+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cdcc5f8089e1

## What looked useful

W4A16 raised loss by +3.9005 and W4A4 raised loss by +13.8027 versus fp16 on the same batches, while W8A8 was a less severe control at +1.0804 loss. The failure appears tied to the simple 4-bit path rather than all quantized evaluation.

## Boundaries and scale limits

Small model, small token sample, fake quantization only, no calibration set beyond max-abs statistics, no packed int4 kernels, no throughput or energy claim.

## Claim scope

On a bounded GB10 probe using distilgpt2 and 2,048 WikiText-2 tokens, naive deterministic fake post-training W4A4 quantization does not improve quality-per-stored-model-byte; it collapses perplexity despite a 74.0% model byte reduction.

## Why it stopped

Proxy/early falsification: the directly tested naive W4A4 fake-PTQ setup fails the quality-per-byte goal on a real small-LM/text probe, but this is not a full validation of all 4-bit quantization methods.

## Recommended next action

Stop this run as a no-paper early falsification of naive W4A4; if continuing locally, test a calibrated activation-aware 4-bit method against the same fp16 baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated W4A8/W4A4 quantization quality-per-byte on distilgpt2
- Success threshold: Calibrated W4A8 or W4A4 keeps loss delta versus fp16 at <= +0.5 on the bounded probe while retaining >=65% estimated stored model byte reduction.
- Stop condition: Stop if calibrated W4 remains worse than +1.0 loss delta versus fp16 on the bounded probe or if the method requires unavailable private/full-scale evidence.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-weight-activation-quantization-quality-per-byte-on-gb10-2bb4a09fc4a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
