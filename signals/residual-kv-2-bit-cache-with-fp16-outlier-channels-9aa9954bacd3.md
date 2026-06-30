# Residual-KV: 2-bit cache with FP16 outlier channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-kv-2-bit-cache-with-fp16-outlier-channels-9aa9954bacd3`
Run ID: `residual-kv-2-bit-cache-with-fp16-outlier-channels-9aa9954bacd3-20260523T111544425674+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aaff3ccd450d

## What looked useful

Uniform 4-bit was far more accurate than residual 2-bit on no-outlier and moderate synthetic outlier cases. Residual 2-bit became competitive only at 8x to 16x injected outlier strength. On distilgpt2 at 512 tokens, 6.25% FP16 outlier channels improved rel MSE from 0.1331 to only 0.1267 while uniform 4-bit reached 0.0047.

## Boundaries and scale limits

No end-to-end perplexity, generation, packed-kernel latency, multi-layer cache replacement, larger LLM, or context beyond 512 tokens was tested. The real-model evidence is limited to distilgpt2 layer 0 on one repeated prompt.

## Claim scope

Synthetic attention-output tests and a first-layer distilgpt2 KV probe show that 2-bit KV plus FP16 outlier channels only helps substantially when a small set of channels has very strong injected outlier scale; the simple magnitude-selected residual scheme does not meaningfully recover real distilgpt2 first-layer attention-output fidelity relative to uniform 4-bit.

## Why it stopped

Proxy plus bounded real-model evidence is insufficient for a positive claim and early-falsifies the simple magnitude-selected FP16 outlier-channel variant, though it is not a full large-model validation.

## Recommended next action

Stop this simple residual-KV variant as no-paper evidence; only revisit with a bounded multi-layer real-model selector study that must show residual 2-bit closes at least half the error gap to 4-bit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-layer real-model test of calibrated residual KV outlier selectors
- Success threshold: Residual 2-bit plus 6.25% FP16 channels closes at least 50% of the rel-MSE gap from plain 2-bit to uniform 4-bit on a majority of layers while retaining at least 5x KV compression versus FP16.
- Stop condition: Stop if residual 2-bit fails to close at least 25% of the gap on the first two evaluated models or if gains appear only with oracle prompt-specific channel selection.

## Evidence references

- Artifact root: `<local-path>/projects/residual-kv-2-bit-cache-with-fp16-outlier-channels-9aa9954bacd3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
