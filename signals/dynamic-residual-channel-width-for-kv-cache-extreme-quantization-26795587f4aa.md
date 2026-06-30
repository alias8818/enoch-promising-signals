# Dynamic Residual Channel Width for KV-Cache Extreme Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-residual-channel-width-for-kv-cache-extreme-quantization-26795587f4aa`
Run ID: `dynamic-residual-channel-width-for-kv-cache-extreme-quantization-26795587f4aa-20260609T004646007324+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ca8959169993

## What looked useful

Residual exact channels gave a 46.1% mean relative MSE reduction versus no residual, but dynamic width averaged only +0.039% versus a local fixed-width static comparator and +0.085% versus a global fixed-width comparator, with only 2 of 6 model/coverage points positive.

## Boundaries and scale limits

Tested distilgpt2 and gpt2 Q/K/V tensors only, with 120 total layer/sample blocks at sequence length 96. No end-to-end perplexity, decode latency, fused kernel, long-context, or 7B+ serving validation was performed.

## Claim scope

Bounded GPT-2-family attention-output reconstruction probe for 2-bit KV-cache quantization: exact residual channels reduce reconstruction error versus no residual, but the tested salience-coverage dynamic residual-width policy does not reliably outperform fixed residual width at the same average residual-channel budget.

## Why it stopped

The core dynamic-width mechanism was mixed and effectively neutral versus fixed-width residual channels in direct reconstruction metrics; this is a bounded proxy result, not a full serving-quality validation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up only if testing a stronger dynamic gating policy on end-to-end perplexity at the same KV memory budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end perplexity test for learned or variance-aware dynamic KV residual gating
- Success threshold: Dynamic residual gating must improve end-to-end perplexity or NLL by at least 1% and attention-output relative MSE by at least 3% versus fixed residual width at the same measured average KV memory budget on two coverage/budget settings.
- Stop condition: Stop if dynamic gating fails to beat fixed residual width on both end-to-end metric and reconstruction metric, or if the measured advantage remains below 1% on perplexity/NLL.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-residual-channel-width-for-kv-cache-extreme-quantization-26795587f4aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
