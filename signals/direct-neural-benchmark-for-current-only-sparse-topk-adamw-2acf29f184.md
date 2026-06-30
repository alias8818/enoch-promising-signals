# Direct Neural Benchmark for Current-Only Sparse-TopK-AdamW

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-neural-benchmark-for-current-only-sparse-topk-adamw-2acf29f184`
Run ID: `direct-neural-benchmark-for-current-only-sparse-topk-adamw-2acf29f184-20260520T102857777219+0000`

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

- Parent run decision: Sparse-TopK-AdamW for Tiny-VRAM Training: enoch://control-plane/projects/sparse-topk-adamw-for-tiny-vram-training-2602f7a3594f/runs/sparse-topk-adamw-for-tiny-vram-training-2602f7a3594f-20260520T101922612223+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e443bd413bbe

## What looked useful

TopK selection has a real mechanism signal versus random sparse updates: at 10% density it reached 0.9971 mean test accuracy versus dense 0.9967 and random-k 0.9946, with lower loss than random-k. It failed dense loss matching: 1.397x dense loss at 1200 steps and 1.254x after a 2400-step 10% convergence check.

## Boundaries and scale limits

Five seeds, synthetic 2D spiral classification, small MLP, CPU NumPy implementation, no transformer/LM/image task, no distributed sparse communication or kernel-speed measurement.

## Claim scope

On a controlled NumPy 2-hidden-layer MLP spiral-classification benchmark, current-gradient-only TopK AdamW at 10% update density preserves dense AdamW test accuracy and beats random-k sparse AdamW, but does not meet the predeclared <=1.10x dense test-loss threshold.

## Why it stopped

Tier 1 direct neural test completed; the current-only 10% TopK optimizer failed the predeclared dense-loss threshold despite preserving accuracy, so this run is useful no-paper evidence rather than paper-positive support.

## Recommended next action

Run one bounded deepen follow-up on a harder non-saturated neural task with dense AdamW and random-k controls, using validation loss as the primary metric and an LR/step budget fixed before running.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder Direct Neural Loss-Gap Test for Current-Only TopK AdamW
- Success threshold: At 10% update density, TopK AdamW must achieve >=95% of dense AdamW mean validation accuracy, <=1.10x dense AdamW mean validation loss, and lower mean validation loss than random-k at the same density.
- Stop condition: Stop as negative if TopK AdamW remains >1.25x dense validation loss or fails the 95% dense accuracy bar after the predeclared budget across five seeds.

## Evidence references

- Artifact root: `<local-path>/projects/direct-neural-benchmark-for-current-only-sparse-topk-adamw-2acf29f184`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
