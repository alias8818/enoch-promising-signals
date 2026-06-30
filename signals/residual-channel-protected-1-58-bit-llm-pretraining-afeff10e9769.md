# Residual-Channel-Protected 1.58-bit LLM Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-protected-1-58-bit-llm-pretraining-afeff10e9769`
Run ID: `residual-channel-protected-1-58-bit-llm-pretraining-afeff10e9769-20260524T225231455004+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2693334657a2

## What looked useful

All-ternary training lagged fp32 by 0.1877 validation loss. Static 6.25% protected channels did not improve over all-ternary despite 3.48 effective layer weight bits. Larger reserves helped monotonically but incompletely: 12.5% recovered 13.7% of the ternary gap and 25% recovered 29.8% while using about 9.17 effective bits.

## Boundaries and scale limits

2-layer 428,800-parameter character Transformer, 1200 steps, three seeds per variant; not GPT-2-small-class, not subword-tokenized, not long-token LLM pretraining, and not an inference efficiency test.

## Claim scope

Tiny character-level GPT pretraining on TinyShakespeare with static full-precision output-channel protection in otherwise ternary 1.58-bit linear layers.

## Why it stopped

Bounded local evidence is mixed and not paper-positive: the cheap 6.25% static protection variant failed, while larger protected fractions show only partial recovery at substantially higher effective bit cost.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replace static protected rows with activation- or gradient-selected protected residual channels at 12.5% and 25% on a tokenized small corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Importance-selected protected residual channels for ternary pretraining
- Success threshold: At 12.5% protected channels, importance-selected protection recovers at least 30% of the ternary-vs-fp32 validation-loss gap and beats static 12.5% protection by at least 0.03 validation loss mean across seeds.
- Stop condition: Stop if importance-selected 12.5% protection fails to beat static 12.5% protection by 0.03 validation loss or if gains require 25% protected channels with less than 50% gap recovery.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-protected-1-58-bit-llm-pretraining-afeff10e9769`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
