# Deduplication threshold sweep for tiny pretraining efficiency

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `deduplication-threshold-sweep-for-tiny-pretraining-efficiency-827383a1c4c2`
Run ID: `deduplication-threshold-sweep-for-tiny-pretraining-efficiency-827383a1c4c2-20260527T132900998705+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2bacaca076fc

## What looked useful

Exact dedup removed 20% of available training characters and lower near-dedup thresholds removed up to 51% while preserving all 760 source families, but validation-loss changes were tiny. The best threshold, 0.07, beat no dedup by only 0.000161 nats on average and paired seed deltas changed sign, so the result is useful negative/mixed evidence rather than a positive efficiency claim.

## Boundaries and scale limits

Single small corpus, synthetic duplicate contamination, character-level NumPy softmax LM, 360 SGD updates per run, five seeds, CPU-only local execution. Not evidence about BPE transformer pretraining, web-scale corpora, production MinHash/LSH deduplication, downstream tasks, or memorization reduction.

## Claim scope

In a controlled Tiny Shakespeare character-level pretraining proxy with injected exact and mutated duplicate documents, one-pass 9-character shingle Jaccard deduplication thresholds from 0.98 to 0.07 did not produce a robust fixed-token validation-loss efficiency gain over no dedup across five seeds.

## Why it stopped

Proxy early falsification: the local controlled sweep did not show a robust dedup-threshold efficiency optimum; observed gains were smaller than seed noise and not direct full-scale transformer evidence.

## Recommended next action

Stop this run as a bounded no-paper useful signal; only revisit with a medium direct tokenized-transformer experiment where the success threshold is a validation-loss gain larger than seed variance at equal processed tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium tokenized transformer dedup threshold confirmation
- Success threshold: Best dedup threshold improves clean validation loss over no dedup by at least 2x the across-seed standard error while preserving at least 95% of unique source families or an equivalent diversity metric.
- Stop condition: Stop if all thresholds are within seed noise of no dedup, or if any apparent gain requires removing more than 10% of unique source families/diversity without an offsetting validation-loss improvement.

## Evidence references

- Artifact root: `<local-path>/projects/deduplication-threshold-sweep-for-tiny-pretraining-efficiency-827383a1c4c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
