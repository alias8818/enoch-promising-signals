# Does cleaner pretraining data make INT4-quantized small models more robust?

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `does-cleaner-pretraining-data-make-int4-quantized-small-models-more-robust-c4d306512d6d`
Run ID: `does-cleaner-pretraining-data-make-int4-quantized-small-models-more-robust-c4d306512d6d-20260610T033328568928+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7ed16ef07a68

## What looked useful

Across seeds 13, 31, and 47, deduped minus non-deduped clean INT4 quantization NLL damage averaged +13.1169, and deduped minus non-deduped mean INT4 perturbation NLL delta averaged +0.4151; positive values are worse for the deduped checkpoint. The tested proxy therefore falsifies the simple hypothesis that cleaner/deduplicated pretraining data automatically improves naive INT4 robustness in this small model pair.

## Boundaries and scale limits

Small probe only: 3 seeds, 48 WikiText-2 snippets per seed, synthetic typo/word-drop/word-swap perturbations, simulated dequantized INT4 weights rather than production INT4 kernels, and a v0 non-deduped checkpoint because the current pythia-70m cache was incomplete and network fetch stalled.

## Claim scope

In a local paired Pythia-70M-family probe using pythia-70m-v0 as the non-deduped control and pythia-70m-deduped as the deduped control, deduplication-as-cleaner-data did not improve robustness after deterministic simulated weight-only INT4 quantization on WikiText-2 perturbation NLL.

## Why it stopped

Proxy early falsification: the directly tested deduplication-as-cleanliness Pythia-70M pair showed worse, not better, simulated INT4 robustness for the deduped checkpoint; this is not a full validation across data-cleaning methods or quantizers.

## Recommended next action

Stop this run as a no-paper useful negative signal; only reopen with a bounded follow-up that uses complete current-revision paired checkpoints and a standard INT4 quantizer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Retest Pythia deduplication with current checkpoints and standard INT4 quantizers
- Success threshold: Deduped checkpoint must show lower INT4 clean quantization damage and at least 10% lower mean robustness degradation than non-deduped across two quantization methods without worse full-precision baseline quality explaining the result.
- Stop condition: Stop if current paired checkpoints cannot be loaded reproducibly, or if two standard quantizers reproduce deduped-minus-non-deduped robustness deltas greater than or equal to zero on the larger evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/does-cleaner-pretraining-data-make-int4-quantized-small-models-more-robust-c4d306512d6d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
