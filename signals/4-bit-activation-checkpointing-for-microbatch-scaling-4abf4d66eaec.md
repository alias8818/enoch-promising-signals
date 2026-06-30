# 4-bit Activation Checkpointing for Microbatch Scaling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-activation-checkpointing-for-microbatch-scaling-4abf4d66eaec`
Run ID: `4-bit-activation-checkpointing-for-microbatch-scaling-4abf4d66eaec-20260525T133721470789+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7cb06f40219f

## What looked useful

At batch 64, q4 saved activations used 4320.9 MiB versus 5952.3 MiB for fp16 saves, a 27.4% reduction, but recompute checkpointing used only 2016.3 MiB. Q4 was 3.68x slower than fp16 and 3.19x slower than recompute. Corrected gradient probe showed relative L2 gradient error 0.589 and gradient cosine 0.814.

## Boundaries and scale limits

No full transformer attention stack, optimizer state, dataset training curve, GPT-2-small class baseline, fused CUDA/Triton q4 kernel, or multi-GPU/datacenter-scale validation was run. Batches were proxy microbatches up to 64 with sequence length 256 and hidden size 2048.

## Claim scope

On a single NVIDIA GB10, an 8-layer fp16 transformer-style MLP proxy showed that naive packed 4-bit saved activations can reduce peak memory versus fp16 saved activations at activation-heavy batches, but it does not beat standard recompute checkpointing and has large gradient distortion.

## Why it stopped

Bounded proxy early falsification: q4 saved activations reduced memory versus fp16 saves but lost decisively to recompute checkpointing on memory and speed, and the corrected gradient probe showed substantial distortion.

## Recommended next action

Stop this naive implementation as no-paper evidence; only continue with a fused q4 checkpoint kernel if it is required to test whether implementation overhead, not the idea, caused the negative Pareto result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused q4 activation checkpoint kernel versus recompute checkpointing
- Success threshold: Fused q4 must meet the gradient thresholds and either beat recompute on median step time at comparable memory or allow at least 1.5x larger batch than recompute under an explicitly stated memory cap.
- Stop condition: Stop if fused q4 still has gradient cosine < 0.99, relative L2 gradient error > 0.05, or remains slower and higher-memory than recompute at batch 64.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-activation-checkpointing-for-microbatch-scaling-4abf4d66eaec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
