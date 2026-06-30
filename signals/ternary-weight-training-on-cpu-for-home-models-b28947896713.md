# Ternary Weight Training on CPU for Home Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weight-training-on-cpu-for-home-models-b28947896713`
Run ID: `ternary-weight-training-on-cpu-for-home-models-b28947896713-20260529T223953456885+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9cb0c1dbbdea

## What looked useful

The tested naive ternary training path is not a practical home-CPU training win: ternary validation loss was 0.0207 higher than dense, training throughput was 0.998x dense, naive training memory was 1.33x dense, and ternary quantize-plus-float-GEMM microbenchmarks were 2.1-2.4x slower than dense GEMM. The only clear win was theoretical inference weight storage at 0.069x dense.

## Boundaries and scale limits

Not a transformer or GPT-2-small-class run; not a full home-LLM training validation; no custom bitpacked ternary kernels or compressed optimizer states were tested.

## Claim scope

For a small CPU-only character language-model proxy, naive STE ternary-weight training with fp32 latent weights, Adam states, and quantize-to-fp32 matrix multiplies did not improve training speed or validation loss and increased estimated training memory, though it greatly reduced theoretical inference weight storage.

## Why it stopped

Bounded proxy evidence falsified the practical CPU-training benefit of the naive ternary STE formulation; this is not a full-scale validation of all ternary training approaches.

## Recommended next action

Stop this naive STE path as no-paper evidence; a bounded follow-up should test whether bitpacked ternary CPU kernels plus compressed optimizer/training state can beat dense BLAS and reduce total training memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bitpacked ternary CPU kernels and compressed optimizer-state probe
- Success threshold: At matched or no more than 1% worse validation loss, show at least 1.25x dense training throughput and at least 25% lower total measured training memory on CPU.
- Stop condition: Stop if ternary-native kernels fail to beat dense BLAS at representative matrix shapes or if optimizer/training state remains within 10% of dense memory.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weight-training-on-cpu-for-home-models-b28947896713`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
