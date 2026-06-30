# Sparse Optimizer Updates for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `sparse-optimizer-updates-for-tiny-vram-training-41f7ef820ff3`
Run ID: `sparse-optimizer-updates-for-tiny-vram-training-41f7ef820ff3-20260528T203921071711+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/24065d3f03ce

## What looked useful

Dense AdamW reached 0.9196 final-window loss and 69.1% accuracy with 0.0396 GiB estimated optimizer state. Top-k sparse AdamW at 0.001 and 0.005 update fractions kept lower state estimates (0.0122 and 0.0305 GiB) but stayed near chance accuracy (4.1% and 6.5%). At 0.01, state estimate already exceeded dense AdamW (0.0443 GiB) with only 9.5% accuracy. At 0.05 and 0.10, state estimates rose to 0.0765 and 0.0824 GiB while accuracy remained well below AdamW.

## Boundaries and scale limits

Synthetic teacher-labeled classification proxy only; no tokenizer, real corpus, transformer/GPT-2-scale run, multi-seed robustness, or production-quality fused sparse optimizer kernel. Metrics are bounded to 120 training steps on one GB10 host.

## Claim scope

On a 5.3M-parameter CUDA MLP dense-gradient proxy, naive coordinate top-k AdamW-style sparse optimizer updates did not deliver a useful tiny-VRAM tradeoff: fractions low enough to preserve optimizer-state memory barely learned, while trainable fractions rapidly accumulated state coverage and metadata overhead.

## Why it stopped

Proxy early falsification rather than full validation: in the tested dense-gradient setup, memory-preserving sparsity failed to learn and learning-oriented sparsity erased the tiny-VRAM memory benefit.

## Recommended next action

Stop this naive coordinate top-k sparse-update line as no-paper evidence; if continuing, test a structured block/row sparse optimizer that avoids per-coordinate index overhead and has an explicit persistence criterion.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Structured Block Sparse Optimizer State for Tiny-VRAM Training
- Success threshold: Structured sparse optimizer uses <=50% of AdamW optimizer-state bytes after 500 steps and reaches >=80% of AdamW final-window accuracy without lower throughput than 50% of AdamW.
- Stop condition: Stop if state bytes exceed 75% of AdamW before 500 steps or final-window accuracy remains below 50% of AdamW after 500 steps.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-optimizer-updates-for-tiny-vram-training-41f7ef820ff3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
