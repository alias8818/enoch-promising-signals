# Attention-sink residual channels for sub-4-bit KV cache on long context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `attention-sink-residual-channels-for-sub-4-bit-kv-cache-on-long-context-30e9e62493fc`
Run ID: `attention-sink-residual-channels-for-sub-4-bit-kv-cache-on-long-context-30e9e62493fc-20260613T202928090302+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/63c9cb3c594b

## What looked useful

Across 108 CUDA synthetic attention records, targeted sink residual channels improved attention KL over naive quantized KV in 108/108 cases and relative output MSE in 103/108 cases, with mean relative-MSE improvement 1.62%, mean sink-mass error improvement 8.74%, and mean residual overhead 0.33% of quantized KV bits. The edge over a same-budget random residual control was modest: 71/108 relative-MSE wins and 84/108 KL wins.

## Boundaries and scale limits

No pretrained model, no language-model perplexity/task metric, no real activation traces, no serving latency measurement, and no full long-context model validation.

## Claim scope

Synthetic long-KV attention probe only: preserving 16 selected channels for 16 sink-token KV entries reduced quantized-attention error versus naive 2-4 bit per-token KV quantization across sequence lengths 2048-8192.

## Why it stopped

Synthetic/proxy evidence supports a plausible mechanism but is not direct/full validation and does not justify a paper.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should test the same sink-channel residual policy on real pretrained-model KV activations with logit drift or perplexity degradation metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-activation sink residual channels for 2-3 bit KV cache
- Success threshold: At equal memory budget, targeted sink residuals reduce logit KL or perplexity degradation by at least 5% versus both naive quantization and random residual controls on real activation traces, with no more than 1% additional KV memory over the quantized baseline.
- Stop condition: Stop if targeted sink residuals fail to beat random same-budget residuals on both logit drift and perplexity/task-loss metrics across the evaluated documents.

## Evidence references

- Artifact root: `<local-path>/projects/attention-sink-residual-channels-for-sub-4-bit-kv-cache-on-long-context-30e9e62493fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
