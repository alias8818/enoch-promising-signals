# Cumulative-Attention KV Eviction

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cumulative-attention-kv-eviction-ffbcbdaace71`
Run ID: `cumulative-attention-kv-eviction-ffbcbdaace71-20260522T140735907549+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/579f753113a8

## What looked useful

Raw cumulative-attention eviction helped at the tightest 16-token budget but failed to robustly beat recency or random at 32 and 64 tokens. This is a useful early falsification of the broad raw-cumulative scoring claim and motivates only a bounded variant test, not a paper.

## Boundaries and scale limits

No training, no production serving traces, no 7B+ or long-context models, no real benchmark dataset, and no exact-match task accuracy. Results are bounded to short-context distilgpt2 inference with per-layer KV cropping.

## Claim scope

Small-model inference probe of raw cumulative-attention KV eviction on distilgpt2 with token budgets 16, 32, and 64, using next-token NLL on natural snippets and synthetic retrieval-style prompts.

## Why it stopped

Bounded direct inference probe, not full validation, showed mixed results: cumulative won only at budget 16 and lost at moderate budgets 32 and 64 on at least one baseline.

## Recommended next action

Stop this raw cumulative-attention claim as no-paper evidence; if continuing, run a bounded age-normalized or sink-aware cumulative-score variant on the same harness before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Age-normalized cumulative-attention KV eviction
- Success threshold: The normalized or sink-aware variant must beat raw cumulative and both simple baselines at budgets 32 and 64 on both prompt types, with no loss of the budget-16 advantage.
- Stop condition: Stop if the variant fails to beat recency or random on either prompt type at budgets 32 and 64, or if diagnostics show it still primarily retains low-information sink tokens.

## Evidence references

- Artifact root: `<local-path>/projects/cumulative-attention-kv-eviction-ffbcbdaace71`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
