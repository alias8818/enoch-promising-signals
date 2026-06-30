# Cross-layer KV cache sharing for GPT-2-small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cross-layer-kv-cache-sharing-for-gpt-2-small-26bca2ba0afd`
Run ID: `cross-layer-kv-cache-sharing-for-gpt-2-small-26bca2ba0afd-20260603T155213355094+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae55cc497071

## What looked useful

Manual GPT-2 forward matched the official model exactly for the baseline. On the medium probe, baseline PPL was 64.72; pairwise previous-layer K/V sharing raised PPL to 902.15, group-of-4 anchor sharing to 1177.29, and all-layer0 sharing to 1315.75. Single-layer substitutions also degraded quality, with the best case only_l1_prev raising PPL to 68.43 for just 8.3% theoretical cache savings.

## Boundaries and scale limits

Evaluated 32,512 next-token targets from WikiText-2 test at sequence length 128 on GPT-2-small. Cache memory savings are theoretical layer-cache counts, not measured in an optimized autoregressive decoding kernel. No retraining, adapter learning, long-context serving, larger models, or multi-corpus robustness were tested.

## Claim scope

Pretrained GPT-2-small with no retraining does not tolerate direct cross-layer K/V cache substitution on a bounded WikiText-2 test probe; adjacent-pair sharing gives theoretical 50% KV-cache savings but collapses perplexity.

## Why it stopped

Bounded direct evaluation falsified naive post-hoc cross-layer K/V sharing: the 50% cache-saving variant increased PPL from 64.72 to 902.15, so this is not a full validation but is a sufficient early negative for the tested no-retraining mechanism.

## Recommended next action

Stop this no-retraining line as an early negative; if pursuing the idea further, run a separately scoped train-aware shared-KV GPT-2-small experiment with direct decode-memory and perplexity metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train-aware adjacent-pair KV sharing for GPT-2-small
- Success threshold: At least 50% measured KV-cache memory reduction with validation PPL no more than 10% worse than the matched standard GPT-2-small-class baseline and no decode-throughput regression larger than the memory benefit justifies.
- Stop condition: Stop if, after the fixed fine-tuning budget, PPL remains more than 25% worse than baseline or decode throughput/memory measurements fail to show real cache savings.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-cache-sharing-for-gpt-2-small-26bca2ba0afd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
