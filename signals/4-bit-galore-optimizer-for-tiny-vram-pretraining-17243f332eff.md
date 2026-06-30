# 4-bit GaLore Optimizer for Tiny-VRAM Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-galore-optimizer-for-tiny-vram-pretraining-17243f332eff`
Run ID: `4-bit-galore-optimizer-for-tiny-vram-pretraining-17243f332eff-20260522T170904355557+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/93f4f84942ac

## What looked useful

The core memory-compression mechanism is plausible but rank-sensitive. Rank-32 int4 produced final loss 2.677 versus AdamW 2.027 while using 94,568 optimizer-state bytes versus AdamW's 3,371,120 bytes, but the naive SVD implementation ran at about 12% of AdamW throughput.

## Boundaries and scale limits

Synthetic data only; one seed; 120 training steps; tiny 2-layer 128-hidden Transformer; simplified per-step SVD rank-state mechanism rather than a faithful production GaLore schedule; no real tiny-VRAM memory-cap run and no GPT-2-small-class validation.

## Claim scope

On a synthetic 120-step tiny-Transformer next-token proxy, a simplified GaLore-style optimizer with packed int4 rank-space Adam moments reduced estimated optimizer-state memory to about 2.8% of AdamW; rank 32 approached but did not equal AdamW final loss, while ranks 8 and 16 lagged badly.

## Why it stopped

No-paper closure: the run produced a useful proxy signal but not direct publication-grade evidence for tiny-VRAM pretraining.

## Recommended next action

Do not write a paper from this run; next implement a faithful GaLore projector schedule and test AdamW, fp32/8-bit GaLore, and 4-bit GaLore on a small real corpus with an explicit memory cap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Faithful 4-bit GaLore under a real tiny-VRAM cap
- Success threshold: 4-bit GaLore fits within the memory cap, reaches validation loss within 10% of fp32 or 8-bit GaLore and within 20% of unconstrained AdamW for the bounded run, and retains at least 50% of AdamW token throughput after projector amortization.
- Stop condition: Stop if faithful 4-bit GaLore diverges in two seeds, cannot beat the rank-8/16 proxy gap with higher rank, or throughput remains below 25% of AdamW after projector reuse.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-galore-optimizer-for-tiny-vram-pretraining-17243f332eff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
