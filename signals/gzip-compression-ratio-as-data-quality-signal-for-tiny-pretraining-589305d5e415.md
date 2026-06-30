# Gzip compression ratio as data quality signal for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gzip-compression-ratio-as-data-quality-signal-for-tiny-pretraining-589305d5e415`
Run ID: `gzip-compression-ratio-as-data-quality-signal-for-tiny-pretraining-589305d5e415-20260621T180332000017+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.2: enoch://research-facility/provider/hf:zai-org/GLM-5.2/108df8742e54

## What looked useful

Raw gzip ratio should not be treated as a monotonic data-quality score. In this probe, the lowest ratios selected repetitive junk and the highest ratios selected random-like junk; the useful behavior was filtering or selecting a middle gzip-ratio band.

## Boundaries and scale limits

No neural Transformer/tokenizer pretraining, no natural web-scale noisy corpus, no downstream task evaluation, and no full-scale validation. The result is a CPU-only proxy with 2 KiB shards and about 184 KiB of training bytes per strategy per seed.

## Claim scope

In a controlled five-seed byte-trigram tiny-pretraining proxy over public-domain prose plus synthetic corruptions, gzip ratio is useful as a band-pass/outlier feature: middle-ratio shards nearly match clean-only selection, while lowest-ratio repetition and highest-ratio random text are harmful.

## Why it stopped

Proxy evidence supports a practical mechanism but is not a full validation of gzip ratio for neural tiny pretraining.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded test should apply gzip band-pass filtering to naturally noisy web/document shards and train a small neural LM under equal token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gzip band-pass filtering on naturally noisy shards for neural tiny LM pretraining
- Success threshold: Middle-band or extreme-filtered gzip selection improves held-out clean validation loss by at least 3 percent versus random selection without collapsing source/language diversity.
- Stop condition: Stop if gzip-band selection is within 1 percent of random or worse across three seeds, or if improvements disappear after length/source/dedup controls.

## Evidence references

- Artifact root: `<local-path>/projects/gzip-compression-ratio-as-data-quality-signal-for-tiny-pretraining-589305d5e415`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
