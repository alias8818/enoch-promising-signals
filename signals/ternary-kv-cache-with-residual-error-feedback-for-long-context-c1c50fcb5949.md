# Ternary KV Cache with Residual Error Feedback for Long Context

Status: `useful_signal`
Project ID: `ternary-kv-cache-with-residual-error-feedback-for-long-context-c1c50fcb5949`
Run ID: `ternary-kv-cache-with-residual-error-feedback-for-long-context-c1c50fcb5949-20260518T113528751006+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b7309050a869

## What looked useful

Plain ternary sometimes preserved retrieval better than int2 at similar nominal data bits, but streaming residual feedback consistently inflated token-local KV error and degraded attention fidelity. GPT-2-small trace: ternary_ef output rel MSE 4.548 versus 0.486 for plain ternary and 0.028 for int4.

## Boundaries and scale limits

Synthetic probes used 4 heads, dim 64, 16 queries, 1,024-8,192 token caches; real-model evidence used GPT-2-small at 512 tokens and did not include integrated perplexity, generation quality, or serving throughput.

## Claim scope

Inference-only attention/KV-cache probes show that the tested streaming cross-token residual-error-feedback ternary KV cache is worse than plain ternary on synthetic 1k-8k attention probes and on a GPT-2-small 512-token KV trace.

## Why it stopped

Proxy plus real-trace evidence directly falsified the tested mechanism: residual feedback worsened attention-output error, retrieval stability, and KV reconstruction versus plain ternary, so the result is not paper-ready or deployment-viable.

## Recommended next action

Stop this run as an early negative for streaming residual-feedback ternary KV; only pursue a bounded follow-up if testing a modified residual design against plain ternary with direct LM perplexity evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Chunk-reset or value-only residual feedback for ternary KV cache
- Success threshold: Modified residual feedback must improve output relative MSE or perplexity delta by at least 10% versus plain ternary without lowering retrieval/top-1 stability, at the same effective cache storage budget.
- Stop condition: Stop if modified residual feedback fails to beat plain ternary on either attention probes or integrated small-LM perplexity, or if residual metadata erases the ternary cache memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-kv-cache-with-residual-error-feedback-for-long-context-c1c50fcb5949`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
