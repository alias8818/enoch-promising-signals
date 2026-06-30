# Speculative Decoding with Quantized Draft Residuals

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `speculative-decoding-with-quantized-draft-residuals-dddcaffd8959`
Run ID: `speculative-decoding-with-quantized-draft-residuals-dddcaffd8959-20260604T230803891957+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/56ed13c59bd9

## What looked useful

Exact acceptance rose from 0.7296 to 0.9590 with full-vocabulary 8-bit residuals, but that costs about 50 KB/token. Sparse residuals under 1 KB/token improved acceptance by only about +0.0024, and the best tested sparse setting at about 2.6 KB/token improved by only about +0.0041.

## Boundaries and scale limits

Direct metric only, 256 prompt contexts, GPT-2/distilGPT-2 pair, no end-to-end serving benchmark, no learned residual predictor, no larger model pairs or benchmark corpus.

## Claim scope

Naive per-context quantized residual logits for GPT-2 target and DistilGPT-2 draft do not provide a practical speculative-acceptance gain when residual payload is constrained to sparse low-k storage; full-vocabulary 8-bit residuals improve acceptance but require about 50 KB per token.

## Why it stopped

Bounded direct acceptance probe falsified the practical form of the hypothesis: useful acceptance gain appeared only for impractically large full-vocabulary residual payloads, while sparse low-payload residuals barely improved or harmed acceptance.

## Recommended next action

Stop naive sparse residual storage; only revisit with a distinct residual predictor or structured compressor that can be tested against the same acceptance and payload threshold.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Structured residual predictor for speculative decoding
- Success threshold: Held-out mean acceptance improves by at least +0.10 absolute over draft while online residual payload remains under 1 KB/token and end-to-end latency is not worse than baseline speculative decoding.
- Stop condition: Stop if held-out acceptance gain is below +0.03 absolute at under 1 KB/token or if predictor compute eliminates the speculative decoding speed advantage.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-quantized-draft-residuals-dddcaffd8959`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
