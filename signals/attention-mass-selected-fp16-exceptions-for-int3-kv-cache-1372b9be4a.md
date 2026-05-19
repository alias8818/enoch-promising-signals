# Attention-mass-selected FP16 exceptions for INT3 KV cache

Status: `useful_signal`
Project ID: `attention-mass-selected-fp16-exceptions-for-int3-kv-cache-1372b9be4a`
Run ID: `attention-mass-selected-fp16-exceptions-for-int3-kv-cache-1372b9be4a-20260516T144323512092+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3b8b513aeb52

## What looked useful

At 5% exceptions, INT3-attention-mass selection reduced relative L2 output error versus pure INT3 by 41.7% on diffuse random attention and by 92.9-99.4% on mixed/retrieval/adversarial 512-token cases; 2048-token confirmation showed similar 40.7% and 96.7-~100% reductions.

## Boundaries and scale limits

Tested synthetic single-query attention only: 8 heads, sequence lengths 512 and 2048, head dims 64 and 128, 16-32 seeds, GB10 PyTorch dequantized tensors. No real pretrained model perplexity, online policy, packed INT3 kernel, serving latency, or multi-token generation validation.

## Claim scope

Controlled single-step attention tests on synthetic FP16 K/V caches show that restoring 1-10% FP16 token-position exceptions selected by INT3 attention mass sharply reduces output error versus pure INT3 and random/recent/key-norm exception selectors.

## Why it stopped

Controlled mechanism evidence is positive, but this remains no-paper evidence because it lacks real-model quality, online policy, and packed-kernel performance validation.

## Recommended next action

Run a real pretrained transformer decode/perplexity test with an online attention-history exception policy and the same INT3 baseline before considering paper readiness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model INT3 KV cache with online attention-history FP16 exceptions
- Success threshold: At 1-5% FP16 exceptions, online attention-history selection closes at least 50% of the pure-INT3-to-FP16 quality gap and beats random and recent selectors at the same memory budget on real text.
- Stop condition: Stop if attention-history exceptions fail to beat random/recent by at least 20% relative gap closure at 5% budget, or if the online policy requires unavailable current-query oracle information.

## Evidence references

- Artifact root: `<local-path>/projects/attention-mass-selected-fp16-exceptions-for-int3-kv-cache-1372b9be4a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
