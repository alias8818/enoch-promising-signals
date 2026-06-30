# Sparse Top-K AdamW for Sub-4GB VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-top-k-adamw-for-sub-4gb-vram-training-1c55498fbee8`
Run ID: `sparse-top-k-adamw-for-sub-4gb-vram-training-1c55498fbee8-20260524T204427949719+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e69fa536fd13

## What looked useful

Sparse top-k AdamW needs strict capacity-bounded moment state to plausibly help sub-4GB training. In the tested bounded form, memory savings were large but optimization quality degraded substantially relative to dense AdamW, so the idea is not paper-ready and should not be claimed as validated.

## Boundaries and scale limits

Toy synthetic data, 80 training steps, prototype Python/CPU sparse-state bookkeeping, no real-corpus GPT-2-small-class run, no hard <=4GB VRAM enforcement, and memory projections exclude activations, allocator fragmentation, dataloader buffers, and production-kernel metadata.

## Claim scope

On an 87k-parameter CUDA toy causal language-model benchmark for 80 steps, capacity-bounded sparse top-k AdamW reduced optimizer-state byte accounting by 85% to 98.5% versus dense AdamW, but achieved only 19.0% to 33.7% of dense AdamW's loss reduction. Unbounded sparse state can lose the memory advantage as selected indices accumulate.

## Why it stopped

Proxy/direct-small early falsification: the local benchmark directly tested sparse top-k AdamW behavior on a toy CUDA language model and only proxied large sub-4GB feasibility by byte accounting; results showed a substantial memory-quality tradeoff rather than paper-ready viability.

## Recommended next action

Do not write a paper from this run; the only worthwhile next step is a bounded production-GPU sparse-state optimizer evaluated on real-text GPT-2-small-class or parameter-matched training under an actual <=4GB VRAM cap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded GPU Sparse-State AdamW Under a Real 4GB Cap
- Success threshold: At <=4GB measured peak VRAM, bounded sparse-state AdamW reaches at least 70% of dense AdamW's loss reduction over the same training budget while using at least 50% less optimizer-state memory than dense AdamW and not falling more than 25% behind the best memory-saving baseline.
- Stop condition: Stop if the bounded sparse optimizer remains below 50% of dense AdamW's loss reduction after the calibrated early-training window, exceeds the 4GB cap, or is slower than dense AdamW by more than 3x after implementation-level bottlenecks are removed.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-top-k-adamw-for-sub-4gb-vram-training-1c55498fbee8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
