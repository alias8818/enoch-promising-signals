# Residual-Channel 4-bit KV Cache Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-4-bit-kv-cache-compression-1d32b2744594`
Run ID: `residual-channel-4-bit-kv-cache-compression-1d32b2744594-20260527T212843334697+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4b794cb3bc8e

## What looked useful

Residual-channel 4-bit shows a real monotonic mechanism versus plain 4-bit: attention proxy NMSE improves by 6.66% to 27.48% as 1/64 to 8/64 channels are stored in fp16. However, the 4/64 residual setting uses 4.75 effective bits/channel and still has 0.02037 attention proxy NMSE versus 0.00484 for plain 5-bit; even the 8/64 setting at 5.5 effective bits/channel remains 3.63x worse than plain 5-bit. This early proxy result argues against the naive design as a practical KV cache compression scheme.

## Boundaries and scale limits

Single small decoder-only model, 16 natural-language prompts repeated to 256 tokens, all 6 layers, numerical reconstruction and attention-output proxy only. No perplexity, generation quality, fused kernel, decode throughput, long-context, or larger-model validation.

## Claim scope

On distilgpt2 KV cache tensors, naive high-energy fp16 residual channels on top of per-token/head 4-bit quantization reduce reconstruction and proxy attention-output error versus plain 4-bit, but are not bit-efficient against a plain 5-bit quantization control.

## Why it stopped

Proxy/early falsification rather than full validation: the mechanism helps over plain 4-bit, but the bit/error tradeoff is poor against a simple 5-bit control on real distilgpt2 KV activations.

## Recommended next action

Stop this naive residual-channel 4-bit line as no-paper evidence; the only worthwhile continuation is a bounded deepen test that adds bit-matched perplexity/generation metrics and a better residual allocation control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bit-matched perplexity test for residual-channel KV quantization
- Success threshold: At equal or lower effective bits/channel than plain 5-bit, residual-channel KV compression must reduce perplexity or attention-output error by at least 10% versus plain 5-bit on two models without increasing decode-time memory traffic in the estimated layout.
- Stop condition: Stop if any residual-channel allocation remains worse than plain 5-bit at matched effective bits on the primary quality metric, or if the only improvement requires more storage than plain 5-bit.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-4-bit-kv-cache-compression-1d32b2744594`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
