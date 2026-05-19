# Merkle Shard Commitments for Data Poisoning Detection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-shard-commitments-for-data-poisoning-detection-486ee43d8a60`
Run ID: `merkle-shard-commitments-for-data-poisoning-detection-486ee43d8a60-20260519T062106369001+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f1d01a04c256

## What looked useful

Post-commit tampering changed the top root in every repeat and localized 100% of changed shards, with about 0.04% commitment storage overhead. Pre-commit poisoned records produced 0% detection because the commitments authenticated the poisoned baseline.

## Boundaries and scale limits

100,000 synthetic JSON records, shard size 512, five repeats, no real training pipeline, no semantic poisoning detector, no model-training backdoor evaluation, and no distributed object-store deployment.

## Claim scope

Synthetic local evidence shows Merkle shard commitments are effective for compact post-commit byte-tamper detection and shard localization against a trusted baseline, but they do not detect poisoned records that are committed as the baseline.

## Why it stopped

The result is a bounded synthetic mechanism test, not a full validation; it early-falsifies the broad claim that Merkle shard commitments alone detect data poisoning.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded test should add an independent semantic/provenance signal and evaluate pre-training poison detection on a real public dataset benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed shard commitments plus semantic scanner for pre-training poison detection
- Success threshold: The combined protocol detects at least 90% of injected poisoned records before training at no more than 5% false-positive rate and demonstrates a measurable operational benefit over scanner-only and signed-manifest baselines.
- Stop condition: Stop if commitments alone add no measurable localization, auditability, or operational benefit over simpler signed manifests after testing at least one real public benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-shard-commitments-for-data-poisoning-detection-486ee43d8a60`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
