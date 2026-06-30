# 8-bit optimizer state quantization with dynamic scaling for tiny model training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `8-bit-optimizer-state-quantization-with-dynamic-scaling-for-tiny-model-training-83b33a417cb4`
Run ID: `8-bit-optimizer-state-quantization-with-dynamic-scaling-for-tiny-model-training-83b33a417cb4-20260611T135329835104+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/329924fa12c8

## What looked useful

Dynamic per-block 8-bit optimizer state is viable as a mechanism at toy scale: validation-loss deltas were -0.0096, -0.0247, and -0.0127 versus fp32 AdamW, persistent state ratio was 0.2539, throughput ratio averaged 0.9489, and peak CUDA allocation ratio remained 0.9887 due to fp32 dequantization temporaries.

## Boundaries and scale limits

Synthetic sequence data, tiny GRU model, short training horizon, unfused Python optimizer, no natural-language dataset, no transformer or GPT-2-small-class baseline, and no proof that persistent-state savings translate to peak-memory savings.

## Claim scope

In a three-seed, 240-step CUDA tiny GRU language-model proxy, AdamW with persistent 8-bit dynamically scaled first/second moment state matched fp32 AdamW validation loss while reducing persistent optimizer-state bytes by about 74.6%.

## Why it stopped

Bounded proxy evidence supports the mechanism but is not direct or broad enough for publication-grade claims; the run intentionally closes before overstating toy synthetic results.

## Recommended next action

Stop this run as no-paper useful signal; next concrete step is a bounded transformer/natural-data follow-up with a fused or memory-aware 8-bit AdamW implementation and direct perplexity plus peak-memory metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer validation of dynamically scaled 8-bit AdamW state on real token data
- Success threshold: Validation perplexity within 1% of fp32 AdamW, persistent optimizer-state reduction at least 70%, peak memory reduction measurable in a memory-aware implementation, and throughput at least 85% of fp32 AdamW.
- Stop condition: Stop if validation perplexity is more than 3% worse than fp32 AdamW in two independent runs, if quantized state becomes numerically unstable, or if memory-aware implementation cannot reduce peak allocation.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-optimizer-state-quantization-with-dynamic-scaling-for-tiny-model-training-83b33a417cb4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
