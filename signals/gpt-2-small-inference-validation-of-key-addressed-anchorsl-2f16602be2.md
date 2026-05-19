# GPT-2-Small Inference Validation of Key-Addressed AnchorSlot KV Cache

Status: `useful_signal`
Project ID: `gpt-2-small-inference-validation-of-key-addressed-anchorsl-2f16602be2`
Run ID: `gpt-2-small-inference-validation-of-key-addressed-anchorsl-2f16602be2-20260518T042104381028+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: GPT-2-Small Inference Validation of Key-Addressed AnchorSlot KV Cache: internal_generated:gpt-2-small-inference-validation-of-key-addressed-anchorsl-2f16602be2

## What looked useful

Bounded full run over 131,072 target tokens: full NLL 3.3401, truncation NLL 6.8482, position-anchor NLL 3.5610, key-anchor NLL 3.5239. Key-anchor was +0.1838 NLL versus full but -3.3242 versus truncation and beat position-anchor on 127/128 paired windows.

## Boundaries and scale limits

Validated only on GPT-2 small, WikiText-2 test, fp16 CUDA, batch-size-one chunked inference, and maximum 1,024-token GPT-2 contexts. No fused/incremental production cache, batched serving workload, larger model, longer context model, or downstream generation quality study was tested.

## Claim scope

On GPT-2-small WikiText-2 chunked autoregressive inference with a 256-token KV budget at 1,024-token context, key-addressed AnchorSlot compression preserves next-token NLL far better than same-budget recent-token truncation and modestly but consistently better than position-pooled anchor slots.

## Why it stopped

Direct GPT-2-small validation supports the compression mechanism but not a paper-ready or production-ready claim because key-anchor remains worse than full cache and the current implementation is slower than full-cache inference.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded follow-up should implement an incremental/fused key-anchor cache and test whether the quality-retention signal can become a real latency or memory win.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Incremental Key-Anchor KV Cache Serving Validation
- Success threshold: At 1,024-token context with a 256-token KV budget, incremental key-anchor must keep mean delta NLL versus full at or below +0.20, beat position-anchor by at least 0.02 paired NLL, beat truncation by at least 2.0 NLL, and show at least one concrete serving benefit: lower peak CUDA allocation under batched inference or higher tokens/s than full cache.
- Stop condition: Stop if incremental key-anchor exceeds +0.25 NLL versus full, fails to beat position-anchor on paired windows, or remains slower and not measurably lower-memory than full cache in batched inference.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-inference-validation-of-key-addressed-anchorsl-2f16602be2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
