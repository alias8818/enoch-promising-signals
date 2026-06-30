# Self-Speculative Decoding via Intermediate Layer Unembedding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-intermediate-layer-unembedding-b6bc42d8dffa`
Run ID: `self-speculative-decoding-via-intermediate-layer-unembedding-b6bc42d8dffa-20260525T190221485070+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f0343368d0fd

## What looked useful

Intermediate-layer agreement rises with depth, reaching 55.9% teacher-forced top-1 agreement and 66.2% greedy acceptance at layer 11, but cheaper early layers accept only about 10-21% of greedy drafts. All tested layer/gamma cost estimates were below break-even, with best estimated speedup 0.945x versus full greedy.

## Boundaries and scale limits

Single pretrained GPT-2-small model, 26,306 teacher-forced positions, 1,024 greedy draft checks per layer, no optimized serving kernel, no trained exit head, no larger-model validation, no sampling-distribution speculative decoding.

## Claim scope

On GPT-2-small with Wikitext-2 validation and greedy generation contexts, direct final-layer-norm plus tied-LM-head unembedding of intermediate hidden states produces a measurable alignment signal but does not reach cost-adjusted speculative decoding break-even under a layer-fraction cost model.

## Why it stopped

Bounded direct evidence shows the raw mechanism aligns only in late, expensive layers and fails the practical speedup threshold; this is not a full large-model validation, but it is an early negative for the untrained direct-unembedding method.

## Recommended next action

Stop this direct-unembedding variant as no-paper evidence; a next bounded test should train or calibrate a cheap early-exit head and require cost-adjusted speedup above 1.1x on GPT-2-small before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated early-exit head for cost-adjusted self-speculative decoding
- Success threshold: Layer 4 or earlier achieves at least 45% greedy acceptance and at least 1.1x cost-adjusted estimated speedup for gamma 1 or 2 on GPT-2-small generated contexts.
- Stop condition: Stop if calibrated layer 4 or earlier remains below 30% greedy acceptance or below 1.0x estimated speedup after a bounded training/calibration run.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-intermediate-layer-unembedding-b6bc42d8dffa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
