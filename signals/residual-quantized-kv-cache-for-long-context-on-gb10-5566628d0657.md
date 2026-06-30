# Residual-Quantized KV Cache for Long Context on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-quantized-kv-cache-for-long-context-on-gb10-5566628d0657`
Run ID: `residual-quantized-kv-cache-for-long-context-on-gb10-5566628d0657-20260527T165213362332+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fe6b5049c075

## What looked useful

Residual correction produced consistent numerical gains over plain int4, including 17.2% lower relative attention-output L2 error and 25.0% lower KL at 16k tokens under the outlier proxy, while retaining an estimated 2.61x KV-cache compression versus fp16. The same residual path added 32.3% latency over plain int4 and was 13.3x slower than fp16 at 16k in the unfused PyTorch reconstruction path.

## Boundaries and scale limits

No trained model, perplexity, generation quality, multi-layer accumulation, paged-cache implementation, fused CUDA kernel, or end-to-end serving benchmark was tested. Memory savings are estimated from packed-cache accounting, while tensors in the PyTorch proxy are not actually nibble-packed.

## Claim scope

On a GB10 synthetic single-query attention proxy with sequence lengths up to 16384, int4 KV cache plus a 6.25% sparse fp16 residual lowers attention-output error and KL versus plain int4, but a naive PyTorch dense reconstruction path is substantially slower than fp16 and plain int4.

## Why it stopped

Proxy evidence supports the numerical mechanism but early-falsifies practical usefulness for an unfused GB10 decode path; this is not a full validation or a paper-ready result.

## Recommended next action

Stop this no-paper proxy run; the concrete next action is a bounded fused-kernel or serving-path follow-up that tests residual dequantization inside attention rather than reconstructing dense K/V tensors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused Residual-Int4 KV Dequantization Inside GB10 Attention
- Success threshold: At 8k and 16k context, residual-int4 must keep at least a 10% relative attention-error or perplexity/logit-error improvement over plain int4 while running no more than 15% slower than fp16 and preserving at least 2.5x estimated KV-cache compression.
- Stop condition: Stop if fused residual-int4 remains more than 25% slower than fp16 or fails to improve attention/logit/perplexity error by at least 5% versus plain int4 on matched shapes.

## Evidence references

- Artifact root: `<local-path>/projects/residual-quantized-kv-cache-for-long-context-on-gb10-5566628d0657`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
