# Real-model 4 GiB cap test for checkpoint-persistent 8-bit AdamW

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-model-4-gib-cap-test-for-checkpoint-persistent-8-bit-ecb0a14d8c`
Run ID: `real-model-4-gib-cap-test-for-checkpoint-persistent-8-bit-ecb0a14d8c-20260612T065054101955+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Medium persistence test for 8-bit AdamW under a 4 GiB cap: enoch://control-plane/projects/medium-persistence-test-for-8-bit-adamw-under-a-4-gib-cap-e69597a302/runs/medium-persistence-test-for-8-bit-adamw-under-a-4-gib-cap-e69597a302-20260612T064023826335+0000
- Parent run decision: Hard-memory validation of 8-bit AdamW on a small transformer under a 4GB cap: enoch://control-plane/projects/hard-memory-validation-of-8-bit-adamw-on-a-small-transform-8385a50887/runs/hard-memory-validation-of-8-bit-adamw-on-a-small-transform-8385a50887-20260612T062953985729+0000

## What looked useful

Direct checkpoint-size evidence supports the storage mechanism: persistent 8-bit AdamW state can cross the 4 GiB checkpoint boundary for a GPT-2-large-class model where fp32 AdamW state cannot. Smoke tests showed exact checkpoint/resume persistence for both fp32 and q8 paths.

## Boundaries and scale limits

Large cap test used deterministic synthetic gradients to initialize optimizer state for all real model tensors, not a full GPT-2-large training run. Training-quality, convergence, blockwise quantization, and long-horizon resume stability are not established.

## Claim scope

On this GB10 worker, a GPT-2-large-class 772,943,360-parameter bf16 model with checkpoint-persistent uint8 AdamW first/second moments produced a 2.880 GiB model+optimizer checkpoint, below a 4 GiB cap, while the same model with persistent fp32 AdamW moments produced a 7.199 GiB checkpoint.

## Why it stopped

No-paper useful signal: the direct checkpoint cap threshold passed, but the simple tensorwise q8 optimizer showed unstable short-run losses and the large test did not validate real training convergence.

## Recommended next action

Run a bounded deepen test using blockwise q8 AdamW on GPT-2-small or GPT-2-medium with real data, fixed seeds, fp32/bf16 AdamW baseline, validation loss curves, and repeated checkpoint/resume cycles.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise q8 AdamW training stability with checkpoint persistence
- Success threshold: q8 checkpoint remains below 4 GiB at the target model scale and validation loss stays within 5% of the fp32/bf16 AdamW baseline after the bounded run, with exact or numerically explained checkpoint/resume continuity.
- Stop condition: Stop if q8 validation loss diverges by more than 20% from baseline, resume continuity fails, or checkpoint size no longer stays below the 4 GiB cap.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-4-gib-cap-test-for-checkpoint-persistent-8-bit-ecb0a14d8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
