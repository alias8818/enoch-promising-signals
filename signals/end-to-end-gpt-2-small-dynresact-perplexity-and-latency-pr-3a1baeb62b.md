# End-to-end GPT-2-small DynResAct perplexity and latency probe

Status: `useful_signal`
Project ID: `end-to-end-gpt-2-small-dynresact-perplexity-and-latency-pr-3a1baeb62b`
Run ID: `end-to-end-gpt-2-small-dynresact-perplexity-and-latency-pr-3a1baeb62b-20260517T154604411677+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a6cce9232f27

## What looked useful

DynResAct 1% residual budget achieved PPL 71.93 vs baseline 63.90 while plain int4 was 2473.81 and static 1% was 814.24; DynResAct 2% reached PPL 68.08. Decode latency was 8.49-8.63 ms versus 2.42 ms baseline, about 3.5x slower.

## Boundaries and scale limits

Single model, one dataset split, 64 short chunks, unbatched prompt/decode latency, no fused kernels, no packed int4 storage, no residual metadata bandwidth implementation, no larger models or long-context serving.

## Claim scope

On pretrained GPT-2-small evaluated on 8,128 WikiText-2 next-token predictions, dynamic top-k residual activation entries at 1-2% residual budget recover most baseline perplexity under int4 activation quantization and strongly outperform static residual channels, but the naive PyTorch implementation is much slower than baseline for cached single-token decode.

## Why it stopped

Tier-1 direct GPT-2-small evidence supports the perplexity-recovery mechanism but directly falsifies a practical latency benefit for the naive end-to-end implementation; this is not full validation of fused DynResAct.

## Recommended next action

Stop paper escalation for the naive implementation; run one bounded fused-kernel or realistic metadata-accounting follow-up only if testing whether the quality signal can survive practical latency overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused GPT-2-small DynResAct latency and metadata accounting
- Success threshold: PPL <= 1.10x fp16 baseline at 1-2% residual budget and cached single-token decode mean latency <= 1.20x fp16 baseline, or a measured throughput/memory-bandwidth win versus a credible int4 activation baseline at comparable quality.
- Stop condition: Stop if fused/realistic DynResAct remains >1.20x baseline decode latency without a compensating bandwidth/throughput win, or if PPL exceeds 1.10x baseline at 2% residual budget.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-gpt-2-small-dynresact-perplexity-and-latency-pr-3a1baeb62b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
