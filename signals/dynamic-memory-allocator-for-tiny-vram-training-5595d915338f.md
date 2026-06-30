# Dynamic Memory Allocator for tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dynamic-memory-allocator-for-tiny-vram-training-5595d915338f`
Run ID: `dynamic-memory-allocator-for-tiny-vram-training-5595d915338f-20260614T105139548116+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/49180dbfc469

## What looked useful

Training graph future-use/deadline information plus tensor size is a practical allocator signal for tiny-VRAM/offload training; generic LRU eviction left consistent transfer savings on the table in all tested traces.

## Boundaries and scale limits

Synthetic replay only; no real CUDA allocation cap, no PyTorch autograd integration, no measured training step time, no loss/convergence validation, no allocator-fragmentation measurement, and no GPT-2-small-class end-to-end run.

## Claim scope

In synthetic transformer-like training-step memory traces with CPU offload allowed and VRAM budgets from 8% to 32% of static keep-everything memory, a byte-aware deadline eviction heuristic reduced replayed transfer volume by about 13-16% on average versus LRU and was near a farthest-next-use baseline.

## Why it stopped

Synthetic/proxy allocator replay supports the mechanism but is not direct full validation of tiny-VRAM training.

## Recommended next action

Stop this run as no-paper useful signal; next concrete step is a bounded PyTorch prototype that enforces a device-memory cap and measures real step time, max memory, and loss parity against LRU/offload and checkpointing controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch capped-memory allocator prototype for tiny-VRAM training
- Success threshold: At least 10% lower measured step time or transfer bytes than LRU/offload at the same memory cap, no higher max device memory, and loss within 2% of the baseline over the fixed short run.
- Stop condition: Stop if the prototype cannot enforce the memory cap correctly, if allocator overhead erases transfer savings, or if loss diverges beyond the parity threshold in two repeated short runs.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-memory-allocator-for-tiny-vram-training-5595d915338f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
