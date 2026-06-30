# KV-cache 1.5-bit with per-head FP16 residual for attention sink tokens

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-1-5-bit-with-per-head-fp16-residual-for-attention-sink-tokens-235f75e57cd2`
Run ID: `kv-cache-1-5-bit-with-per-head-fp16-residual-for-attention-sink-tokens-235f75e57cd2-20260610T040902115371+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b44fd0375346

## What looked useful

Synthetic main probe: ternary KV output relative L2 0.7869 dropped to 0.3256 with sink FP16 residuals at 1.616 bits/scalar, and attention KL dropped from 0.4733 to 0.0859. DistilGPT2 probe: first-4-token sink mass averaged 0.3686; ternary output relative L2 dropped from 0.5946 to 0.5508 and attention KL from 0.5974 to 0.4493 with sink residuals.

## Boundaries and scale limits

Synthetic probe used generated Q/K/V tensors; real-model probe used DistilGPT2 only, 4 prompts, 256-token contexts, all 6 layers, and recomputed attention projections offline. No end-to-end perplexity, generation-quality, long-context, 7B+ model, packed-kernel, memory-bandwidth, or decode-throughput evidence was produced.

## Claim scope

Bounded attention-math probes show that preserving the first 4 sink-token K/V entries as FP16 residuals can reduce distortion from per-head ternary approximately-1.5-bit KV quantization. The effect is large in controlled synthetic high-sink regimes and consistent but modest on pretrained DistilGPT2 attention projections.

## Why it stopped

No-paper closure: bounded synthetic and DistilGPT2 attention probes support the mechanism but do not provide end-to-end model-quality or hardware evidence needed for a paper-positive decision.

## Recommended next action

Run a bounded real-model perplexity/generation-quality evaluation on GPT-2-small-class or comparable models using true incremental KV-cache decoding, comparing ternary 1.5-bit, ternary plus sink FP16 residual, and standard 2-bit/4-bit baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small incremental KV-cache quality test for ternary sink-token residuals
- Success threshold: At matched prompts and sequence lengths, sink residuals must reduce ternary-only perplexity degradation by at least 25% relative to FP16 cache and improve next-token distribution KL by at least 15%, while keeping effective KV storage below 1.75 bits per scalar excluding shared metadata.
- Stop condition: Stop if sink residuals reduce attention-math error but fail to improve perplexity or next-token distribution metrics versus ternary-only KV, or if effective storage exceeds the stated memory budget after honest residual and metadata accounting.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-1-5-bit-with-per-head-fp16-residual-for-attention-sink-tokens-235f75e57cd2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
