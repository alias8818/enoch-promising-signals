# Dynamic loss scaling with mixed precision for tiny-VRAM stable training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dynamic-loss-scaling-with-mixed-precision-for-tiny-vram-stable-training-17c266387675`
Run ID: `dynamic-loss-scaling-with-mixed-precision-for-tiny-vram-stable-training-17c266387675-20260614T073801270226+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5687ed737c89

## What looked useful

Dynamic loss scaling is a practical overflow recovery mechanism for mixed-precision microbatch training under induced FP16 overflow pressure, but no-spike controls show no stability advantage when overflow pressure is absent and the mechanism is not novel.

## Boundaries and scale limits

Toy synthetic data, 60 optimizer steps, ~77-79 MiB CUDA allocation, tiny-VRAM only proxied by micro-batches and accumulation; no real memory-capped GPU, real dataset, multi-seed robustness, or convergence-scale training.

## Claim scope

On a GB10 CUDA FP16 toy transformer with micro-batch gradient accumulation and injected overflow pressure, PyTorch dynamic loss scaling completed 60/60 optimizer steps by skipping 5 overflowed updates, while unguarded high static scaling failed at step 11.

## Why it stopped

No-paper closure: the local evidence supports the expected mechanism but is toy/proxy evidence and dynamic loss scaling is already standard practice, so this is not publication-grade novelty.

## Recommended next action

Run a bounded deepen test on a real small model/dataset under an explicit memory cap, comparing dynamic FP16 scaling with BF16, FP32, AMP no-scale, and static-scale controls across multiple seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Memory-capped real-task validation of dynamic FP16 loss scaling
- Success threshold: Dynamic FP16 completes all seeds with zero nonfinite parameter failures and validation loss within 2% of BF16/FP32 while at least one static/no-scale FP16 control fails or needs manual restart under the same memory cap.
- Stop condition: Stop if all FP16 controls complete without nonfinite events under the memory cap, or if dynamic FP16 shows worse validation loss by more than 2% despite no stability failures.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-loss-scaling-with-mixed-precision-for-tiny-vram-stable-training-17c266387675`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
