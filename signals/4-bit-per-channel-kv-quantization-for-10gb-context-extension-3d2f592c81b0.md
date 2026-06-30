# 4-Bit Per-Channel KV Quantization for 10GB Context Extension

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-per-channel-kv-quantization-for-10gb-context-extension-3d2f592c81b0`
Run ID: `4-bit-per-channel-kv-quantization-for-10gb-context-extension-3d2f592c81b0-20260603T191030927581+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/810c7576d010

## What looked useful

The memory-accounting mechanism is supported, but naive block-128 per-channel int4 KV produces relative L2 attention-output errors around 0.16-0.28 on synthetic caches and 0.183 mean layer error on distilgpt2, below the required fidelity for a standalone context-extension claim.

## Boundaries and scale limits

Tested batch 1, 8 synthetic heads, dim 64, sequence lengths up to 32768, plus distilgpt2 at sequence 512. Did not test packed int4 kernels, real long-context perplexity, full decode loops, larger models, or production serving.

## Claim scope

On GB10/PyTorch, symmetric signed int4 per-channel block-128 quantization of KV tensors gives 3.8788x KV storage reduction, but fails the predeclared attention-output fidelity threshold on synthetic KV caches and a small distilgpt2 real-KV probe.

## Why it stopped

Proxy/early falsification: the tested quantizer achieves the expected memory reduction but misses the predeclared attention fidelity threshold; this is not a full long-context validation.

## Recommended next action

Stop this exact design as no-paper evidence; the next bounded test should compare calibrated variants against this baseline using end-to-end GPT-2-small perplexity/decode with quantized KV reads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated int4 KV variants with end-to-end GPT-2-small decode metrics
- Success threshold: An int4 variant keeps KV compression at least 3.5x versus fp16, preserves perplexity or next-token NLL within 5% of fp16 on the bounded prompt set, and does not regress decode latency by more than 25% versus fp16 for the tested shape.
- Stop condition: Stop if all calibrated int4 variants exceed 5% NLL/perplexity degradation or require metadata/residual storage that drops effective compression below 3.5x.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-per-channel-kv-quantization-for-10gb-context-extension-3d2f592c81b0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
