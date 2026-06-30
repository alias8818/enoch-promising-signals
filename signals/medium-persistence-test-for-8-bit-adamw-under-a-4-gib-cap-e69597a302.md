# Medium persistence test for 8-bit AdamW under a 4 GiB cap

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-persistence-test-for-8-bit-adamw-under-a-4-gib-cap-e69597a302`
Run ID: `medium-persistence-test-for-8-bit-adamw-under-a-4-gib-cap-e69597a302-20260612T064023826335+0000`

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

- Parent run decision: Hard-memory validation of 8-bit AdamW on a small transformer under a 4GB cap: enoch://control-plane/projects/hard-memory-validation-of-8-bit-adamw-on-a-small-transform-8385a50887/runs/hard-memory-validation-of-8-bit-adamw-on-a-small-transform-8385a50887-20260612T062953985729+0000
- Parent run decision: 8-bit Block Quantized Adam for sub-4GB VRAM Training: enoch://control-plane/projects/8-bit-block-quantized-adam-for-sub-4gb-vram-training-1f6f97c637a0/runs/8-bit-block-quantized-adam-for-sub-4gb-vram-training-1f6f97c637a0-20260612T040800070896+0000

## What looked useful

8-bit optimizer state reduced optimizer-state memory to 0.6706 GiB and kept peak reserved memory at 2.6973 GiB with checkpoint/resume, whereas FP32 moments OOMed under the 4 GiB cap. Restoring 8-bit moments gave mean final/step-1 loss ratio 0.3271 versus 0.4910 when moments were reset at the midpoint.

## Boundaries and scale limits

Synthetic vector objective only; not a real transformer or language-model workload; local custom optimizer rather than production bitsandbytes kernels; 48 optimizer steps; checkpoint files were measured and reloaded during the run but deleted afterward to avoid large artifacts.

## Claim scope

Under an enforced 4 GiB CUDA allocator cap on GB10, a custom chunked 8-bit-moment AdamW implementation successfully trained and checkpoint/resumed a 360M-parameter fp16 synthetic optimizer-stress vector for 48 steps across seeds 101, 202, and 303, while the same-equation FP32-moment AdamW baseline OOMed for all three seeds.

## Why it stopped

No-paper useful signal: the direct cap and persistence mechanism is supported, but the workload is synthetic and not sufficient for publication readiness.

## Recommended next action

Run a bounded real-model deepen test: GPT-2-small-class or parameter-matched transformer training under the same 4 GiB cap, comparing production 8-bit AdamW against FP32 AdamW and a reset-state checkpoint ablation on validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model 4 GiB cap test for checkpoint-persistent 8-bit AdamW
- Success threshold: Across at least three fixed seeds, production 8-bit AdamW completes checkpoint/resume under 4 GiB with validation loss no worse than 5% relative to the strongest fitting baseline, and the FP32 AdamW baseline either OOMs at the same setting or requires a materially smaller batch/context with documented loss or throughput cost.
- Stop condition: Stop if production 8-bit AdamW cannot complete checkpoint/resume under the cap, if validation loss is more than 5% worse than the strongest fitting baseline across seeds, or if FP32 AdamW fits the same setting with no material memory/quality/throughput disadvantage.

## Evidence references

- Artifact root: `<local-path>/projects/medium-persistence-test-for-8-bit-adamw-under-a-4-gib-cap-e69597a302`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
