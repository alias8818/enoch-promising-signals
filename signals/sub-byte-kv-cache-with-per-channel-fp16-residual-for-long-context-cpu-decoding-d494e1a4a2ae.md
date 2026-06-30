# Sub-byte KV cache with per-channel FP16 residual for long-context CPU decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-byte-kv-cache-with-per-channel-fp16-residual-for-long-context-cpu-decoding-d494e1a4a2ae`
Run ID: `sub-byte-kv-cache-with-per-channel-fp16-residual-for-long-context-cpu-decoding-d494e1a4a2ae-20260619T150139632390+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/aca463b9eee0

## What looked useful

FP16 residual channels substantially reduced synthetic attention error, but no tested sub-byte KV setting met the predefined fidelity threshold of output_rel_l2 <= 0.05 and attention argmax agreement >= 0.75. Best 8192-token outlier setting was 4-bit with 25% FP16 residual channels, about 50.0% of FP16 KV memory, with output_rel_l2 0.0752.

## Boundaries and scale limits

No full transformer integration, no real model KV activations, no perplexity/task accuracy, and no packed sub-byte CPU kernel throughput measurement. Runtime was a bounded NumPy proxy, not a production decode path.

## Claim scope

Synthetic single-token CPU attention proxy with 8 heads, head dimension 64, sequence lengths 1024/4096/8192, symmetric per-channel 2/3/4-bit K/V quantization, and FP16 residual-channel fractions up to 25%.

## Why it stopped

Proxy benchmark showed the mechanism is directionally useful but insufficient for the bounded fidelity target; this is not a full validation or full invalidation of all model-integrated variants.

## Recommended next action

Stop this run as a proxy early falsification; next, test the same residual-channel cache inside a small transformer decode/perplexity harness with real KV activations before considering larger CPU-kernel work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer KV residual-channel cache validation
- Success threshold: At sequence length >= 2048, 4-bit residual-channel KV cache achieves >= 2x KV memory reduction with <= 1% perplexity regression or >= 98% next-token top-1 agreement versus FP16 KV, and does not slow CPU decode by more than 25% in the measured harness.
- Stop condition: Stop if 4-bit with up to 25% FP16 residual channels causes > 3% perplexity regression or < 95% next-token top-1 agreement on the small-model harness, because that would confirm the synthetic negative at model level.

## Evidence references

- Artifact root: `<local-path>/projects/sub-byte-kv-cache-with-per-channel-fp16-residual-for-long-context-cpu-decoding-d494e1a4a2ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
