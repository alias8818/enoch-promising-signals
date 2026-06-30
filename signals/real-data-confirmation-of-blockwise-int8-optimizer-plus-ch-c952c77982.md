# Real-data confirmation of blockwise int8 optimizer plus checkpointed FP8 saved tensors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-data-confirmation-of-blockwise-int8-optimizer-plus-ch-c952c77982`
Run ID: `real-data-confirmation-of-blockwise-int8-optimizer-plus-ch-c952c77982-20260610T090711845310+0000`

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

- Parent run decision: implementation_gap: Unified Tiny-VRAM Training Framework Combining Checkpointing, FP8, and Int8 Optimizer: enoch://control-plane/projects/implementation-gap-unified-tiny-vram-training-framework-combining-checkpointing-fp8-and-int8-opt-9cf530452b37/runs/implementation-gap-unified-tiny-vram-training-framework-combining-checkpointing-fp8-and-int8-opt-9cf530452b37-20260610T051005835068+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6d2ab989b5e9

## What looked useful

Optimizer state bytes fell from 6,611,680 to 1,687,400 (25.5% of baseline), peak CUDA allocation fell from 215,341,568 to 115,795,968 bytes (53.8% of baseline), validation loss was 2.5763 versus 2.5912 baseline, and throughput was 50.9% of baseline.

## Boundaries and scale limits

Single tiny char-level model, one real-text dataset, 120 training steps, one seed, Python-level optimizer implementation, and combined intervention only; not GPT-2-small scale, not long-horizon convergence, and not publication-grade.

## Claim scope

In a one-seed Tier 1 CUDA run on Tiny Shakespeare with an 826k-parameter GPT-like char language model, blockwise-int8 AdamW moments plus activation checkpointing with FP8 saved-tensor hooks reduced optimizer-state bytes and peak CUDA allocation without observed short-run loss degradation.

## Why it stopped

Tier 1 direct test produced useful mechanism support, but the run is too small and insufficiently ablated for publication readiness.

## Recommended next action

Run a bounded deepen follow-up with checkpoint-only, FP8-only, int8-optimizer-only, and combined controls across at least 3 seeds on a standard real corpus before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ablated multi-seed real-corpus confirmation of int8 optimizer and FP8 saved-tensor memory savings
- Success threshold: Combined method reaches validation loss within 2% of AdamW while reducing optimizer-state bytes by at least 60% and peak CUDA allocation by at least 25% beyond the relevant control.
- Stop condition: Stop if two seeds show validation loss more than 2% worse than AdamW or if checkpoint-only explains essentially all measured peak-memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/real-data-confirmation-of-blockwise-int8-optimizer-plus-ch-c952c77982`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
