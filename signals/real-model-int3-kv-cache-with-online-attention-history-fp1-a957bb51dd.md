# Real-model INT3 KV cache with online attention-history FP16 exceptions

Status: `useful_signal`
Project ID: `real-model-int3-kv-cache-with-online-attention-history-fp1-a957bb51dd`
Run ID: `real-model-int3-kv-cache-with-online-attention-history-fp1-a957bb51dd-20260516T144823476192+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Real-model INT3 KV cache with online attention-history FP16 exceptions: internal_generated:real-model-int3-kv-cache-with-online-attention-history-fp1-a957bb51dd

## What looked useful

INT3 KV-cache error is measurable on a real model, and FP16 exceptions can help, but the proposed attention-history selector is close to random/all-INT3 and is consistently dominated by keeping recent positions FP16.

## Boundaries and scale limits

Tested one pretrained small real model, sequence length 256, 3 fixed seeds, 9,216 scored tokens per policy, fake quantization only; no packed INT3 kernel, long-context serving, or 7B+ model validation.

## Claim scope

On distilgpt2 WikiText-2 next-token evaluation with fake INT3 KV-cache quantization and a 5% FP16 exception budget, online decayed attention-history exceptions do not provide a competitive recovery policy versus a simple recent-token FP16 exception control.

## Why it stopped

Direct Tier-2 real-model evaluation with fixed seeds, ablations, and a real FP16 baseline found that attention-history exceptions reduce INT3 NLL loss only marginally and fail against the recent-token control.

## Recommended next action

Stop this attention-history branch as no-paper evidence; branch only to a bounded recency-first or hybrid exception-policy test before considering packed-kernel work.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Recency-first INT3 KV-cache FP16 exceptions
- Success threshold: Hybrid or recent-first policy achieves mean delta NLL versus FP16 no worse than 0.05 at a 5% FP16 exception budget and beats attention-history-only by at least 0.05 NLL on every tested model/length.
- Stop condition: Stop if recent-first or hybrid policies fail to beat attention-history-only by at least 0.03 NLL on a second model or if the improvement disappears at longer context.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-int3-kv-cache-with-online-attention-history-fp1-a957bb51dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
