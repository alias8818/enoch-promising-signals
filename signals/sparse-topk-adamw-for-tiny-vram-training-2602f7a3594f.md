# Sparse-TopK-AdamW for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-topk-adamw-for-tiny-vram-training-2602f7a3594f`
Run ID: `sparse-topk-adamw-for-tiny-vram-training-2602f7a3594f-20260520T101922612223+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e443bd413bbe

## What looked useful

Cumulative sparse Adam moments are a poor tiny-VRAM strategy because the active state set quickly becomes nearly dense and sparse indices add overhead. A current-only TopK state policy produced a reproducible proxy signal at very small k, but should be treated as a different optimizer mechanism rather than drop-in AdamW.

## Boundaries and scale limits

The run did not test neural networks, transformers, GPT-2-small-class models, activation memory, gradient-buffer memory, GPU kernels, throughput, mixed precision, checkpointing, or real tiny-VRAM out-of-memory behavior. The proxy task has sparse ground truth and is favorable to TopK methods.

## Claim scope

On a five-seed NumPy sparse linear regression proxy, persistent cumulative Sparse-TopK-AdamW did not save optimizer memory, while a strict current-only TopK state variant at 0.5-1.0% k matched or beat dense AdamW validation MSE with about 0.34x modeled weights-plus-optimizer-state memory.

## Why it stopped

Closed as no-paper useful signal because evidence is a CPU/NumPy proxy, not direct tiny-VRAM model training; cumulative state is early-falsified for memory savings, while current-only state warrants a bounded deepen test.

## Recommended next action

Run one bounded direct neural benchmark comparing dense AdamW, cumulative Sparse-TopK-AdamW, and current-only Sparse-TopK-AdamW on validation loss plus peak memory; stop if the 0.5-1.0% current-only variant loses by more than 10% validation loss or does not reduce measured optimizer memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Neural Benchmark for Current-Only Sparse-TopK-AdamW
- Success threshold: Current-only Sparse-TopK-AdamW passes if 0.5-1.0% k is within 1.10x dense AdamW validation loss on at least 3/3 seeds and reduces measured optimizer-state memory by at least 40%; cumulative state passes only if active optimizer states remain below 60% of parameters without exceeding 1.10x validation loss.
- Stop condition: Stop as negative if current-only TopK exceeds 1.10x dense validation loss on two seeds, if measured memory is not at least 40% lower, or if cumulative state reaches near-dense active coverage before convergence.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-topk-adamw-for-tiny-vram-training-2602f7a3594f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
