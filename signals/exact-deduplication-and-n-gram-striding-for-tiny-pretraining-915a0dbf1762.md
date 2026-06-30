# Exact Deduplication and N-gram Striding for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-deduplication-and-n-gram-striding-for-tiny-pretraining-915a0dbf1762`
Run ID: `exact-deduplication-and-n-gram-striding-for-tiny-pretraining-915a0dbf1762-20260529T172913385290+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c54bb4f578ef

## What looked useful

Exact deduplication removed 1,980 duplicate documents and reduced training events to 56.3% of raw stride-1 with only +0.021 BPC. Fixed striding degraded validation much more: stride 2 was +0.267 to +0.294 BPC and stride 16 was about +1.12 to +1.15 BPC.

## Boundaries and scale limits

This run used a count language model, character tokens, one public small text corpus, deterministic injected exact duplicates, and no neural transformer training. It does not validate GPT-2-small-class or larger pretraining behavior.

## Claim scope

On a Tiny Shakespeare character 5-gram count-LM proxy with injected exact duplicate training documents, exact document deduplication preserved dense validation cross-entropy much better than fixed n-gram striding while reducing redundant training events.

## Why it stopped

No-paper closure: this is a useful proxy signal, not direct publication-grade evidence for neural tiny pretraining.

## Recommended next action

Run a bounded tiny-transformer follow-up with matched update budgets for raw, exact-dedup, and stride policies, measuring validation loss and memorization/leakage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny transformer validation of exact deduplication versus n-gram striding
- Success threshold: Dedup policy matches or improves raw duplicated validation loss within 1% at equal update budget, and any stride policy must beat dedup by at least 1% validation loss or show a clear throughput-quality Pareto gain.
- Stop condition: Stop if stride policies are worse than dedup by more than 2% validation loss after the planned matched-budget runs, or if the transformer result reverses the count-LM proxy for dedup across fewer than two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/exact-deduplication-and-n-gram-striding-for-tiny-pretraining-915a0dbf1762`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
