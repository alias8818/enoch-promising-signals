# INT8 Optimizer State Quantization for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-optimizer-state-quantization-for-tiny-vram-training-527cc2c2895b`
Run ID: `int8-optimizer-state-quantization-for-tiny-vram-training-527cc2c2895b-20260612T002202016738+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f85850fdce43

## What looked useful

The memory mechanism works, but naive all-INT8 AdamW at standard eps=1e-8 produced a NaN on one of three calibrated seeds. A stabilized variant preserved the memory reduction but ran at about 66.6% of AdamW throughput.

## Boundaries and scale limits

Evidence is limited to a synthetic short-run classifier workload and a Python/PyTorch reference optimizer. It is not evidence for long-horizon LLM training, real datasets, hard VRAM caps, fused-kernel performance, or GPT-2-small-class convergence.

## Claim scope

On a 17.4M-parameter deterministic CUDA teacher/student workload, reference blockwise INT8 storage for both AdamW moment states reduced persistent optimizer-state bytes by 74.6% and peak CUDA allocation by 25.0%; with eps=1e-6, three 240-step seeds stayed finite and matched AdamW short-run loss/accuracy closely.

## Why it stopped

Proxy GPU evidence supports the memory-saving mechanism but also exposes stability and throughput risks; this is insufficient for a paper claim or full tiny-VRAM training validation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded transformer follow-up with fused or vectorized INT8 state updates, eps/second-moment ablations, and a hard memory-cap success threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded transformer validation of stabilized INT8 AdamW state quantization
- Success threshold: Across at least three seeds, INT8-state training remains finite, achieves at least 60% persistent optimizer-state reduction and at least 15% peak CUDA memory reduction, and finishes within 5% validation loss of AdamW while running at least 80% of AdamW throughput.
- Stop condition: Stop if the stabilized INT8 optimizer produces NaNs in two seeds, loses the peak-memory advantage below 15%, or remains below 60% of AdamW throughput after vectorization/fusion.

## Evidence references

- Artifact root: `<local-path>/projects/int8-optimizer-state-quantization-for-tiny-vram-training-527cc2c2895b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
