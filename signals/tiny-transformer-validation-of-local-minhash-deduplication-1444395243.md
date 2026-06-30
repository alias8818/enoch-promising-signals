# Tiny Transformer Validation of Local MinHash Deduplication

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-transformer-validation-of-local-minhash-deduplication-1444395243`
Run ID: `tiny-transformer-validation-of-local-minhash-deduplication-1444395243-20260520T080339421322+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Local MinHash Deduplication for Tiny Pretraining Gains: enoch://control-plane/projects/local-minhash-deduplication-for-tiny-pretraining-gains-bb1d1f6a8270/runs/local-minhash-deduplication-for-tiny-pretraining-gains-bb1d1f6a8270-20260520T075256466317+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0189f03a7099

## What looked useful

MinHash filtering directly matched the intended near-duplicate mechanism and removed the validation leakage signal that exact dedup could not address in this controlled setting.

## Boundaries and scale limits

Synthetic token corpus, 260 raw train documents, 40 contaminated-validation documents, 40 clean-validation documents, tiny 2-layer CPU Transformer, 500 optimizer steps, three seeds. Not a production corpus, not full-corpus dedup, not a large-model result, and not publication-grade evidence.

## Claim scope

In a controlled synthetic corpus with known near-duplicate train/validation contamination, local MinHash shingle filtering removed 95.0-96.25% of contaminants with no false positives across three seeds, while exact dedup removed none; identical tiny Transformer training showed the contaminated-validation leakage advantage disappear after MinHash filtering.

## Why it stopped

Tier 1 mechanism support achieved, but evidence remains synthetic and small-scale, so it is no-paper useful signal rather than publication readiness.

## Recommended next action

Run a bounded real-text deepen test with injected near-duplicates, threshold ablations, exact-dedup/no-contamination controls, and the same tiny Transformer leakage metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text threshold ablation for local MinHash deduplication leakage control
- Success threshold: MinHash achieves >=0.90 contaminant recall, >=0.95 precision, and >=80% reduction in leakage gap versus raw/exact controls without increasing clean-validation loss by more than 15% relative to no-contamination control.
- Stop condition: Stop if MinHash precision falls below 0.90 at thresholds that achieve 0.90 recall, or if leakage reduction is not consistently better than exact dedup across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-transformer-validation-of-local-minhash-deduplication-1444395243`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
