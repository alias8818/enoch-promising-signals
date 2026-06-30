# Diversity-Filtered Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `diversity-filtered-tiny-pretraining-15098aa00c4e`
Run ID: `diversity-filtered-tiny-pretraining-15098aa00c4e-20260523T040434484985+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2783101e236a

## What looked useful

Diversity filtering can recover wasted pretraining budget in redundant tiny-data pools, but naive lexical diversity is not generally beneficial and can hurt when redundancy is absent.

## Boundaries and scale limits

No neural transformer was trained; no tokenizer, downstream task, natural web-scale deduplication, or large-corpus pretraining claim is supported. The redundant condition used injected duplicates, and the model was a tiny count-based character 5-gram LM.

## Claim scope

In a small CPU-only character n-gram language-model proxy using Gutenberg text chunks, greedy character-5-gram diversity selection improved held-out bits per character versus a 30-seed random baseline when the candidate pool contained injected duplicates and near-duplicates, but underperformed random selection on a balanced non-duplicated pool.

## Why it stopped

No-paper closure: this is a useful but mixed proxy result, not a direct neural pretraining validation.

## Recommended next action

Run a bounded neural follow-up with a tiny transformer on the same redundant and balanced pools, comparing random, dedup-only, and diversity-greedy selection at matched token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Check for Redundancy-Conditional Diversity Filtering
- Success threshold: Diversity or dedup-aware selection beats the random mean validation loss by at least 1% on the redundant pool with no worse than 0.5% degradation on the balanced pool.
- Stop condition: Stop after the matched-budget tiny-transformer comparison completes or after a calibrated CPU/GPU budget cap is reached with checkpointed partial metrics.

## Evidence references

- Artifact root: `<local-path>/projects/diversity-filtered-tiny-pretraining-15098aa00c4e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
