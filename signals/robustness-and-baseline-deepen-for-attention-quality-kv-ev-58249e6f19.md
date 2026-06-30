# Robustness and Baseline Deepen for Attention-Quality KV Eviction

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `robustness-and-baseline-deepen-for-attention-quality-kv-ev-58249e6f19`
Run ID: `robustness-and-baseline-deepen-for-attention-quality-kv-ev-58249e6f19-20260620T220147930451+0000`

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

- Parent run decision: Quality-Gated KV Eviction on a 125M Local Model: enoch://control-plane/projects/quality-gated-kv-eviction-on-a-125m-local-model-2a6fed1408a6/runs/quality-gated-kv-eviction-on-a-125m-local-model-2a6fed1408a6-20260620T214422260688+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/737af98364f9

## What looked useful

Recency was the best policy in both models and budgets. Attention-quality was weaker than recency throughout, near random in some settings, and only beat random for gpt2 at budget 64. The inverted anti-attention control was consistently much worse, indicating attention mass has signal but naive attention-quality eviction is not a robust standalone replacement for recency.

## Boundaries and scale limits

Small direct evaluation only: token-subset retained context rather than production past_key_values eviction; 3-4 text windows per model; GPT-2-family models only; no 7B+ long-context or downstream QA benchmark.

## Claim scope

Naive cumulative attention-quality eviction did not beat recency for retained-context next-token NLL on small WikiText-2 windows with cached distilgpt2 and gpt2 models at budgets 32 and 64.

## Why it stopped

Tier 1 controlled direct test failed the practical threshold of beating the recency baseline; this is not full-scale validation but is enough to reject the naive standalone policy for this scoped setting.

## Recommended next action

Stop this no-paper run; if continuing locally, test a recency-protected attention-quality hybrid against recency with the same NLL harness before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Recency-Protected Attention-Quality KV Eviction
- Success threshold: Hybrid mean NLL must beat pure recency by at least 0.05 on one budget without losing by more than 0.02 on any other tested budget, and must beat random in every tested setting.
- Stop condition: Stop if the hybrid fails to beat recency on both models at budgets 32 and 64 or if gains appear only against random/anti-attention controls.

## Evidence references

- Artifact root: `<local-path>/projects/robustness-and-baseline-deepen-for-attention-quality-kv-ev-58249e6f19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
