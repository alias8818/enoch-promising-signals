# GPT-2-small-class BF16 AdamW8bit checkpoint/resume equivalence near 6GB

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpt-2-small-class-bf16-adamw8bit-checkpoint-resume-equival-29ec4a120f`
Run ID: `gpt-2-small-class-bf16-adamw8bit-checkpoint-resume-equival-29ec4a120f-20260607T120818589332+0000`

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

- Parent run decision: Real-dataset BF16 persistence test for 8-bit AdamW plus checkpointing under a 6GB cap: enoch://control-plane/projects/real-dataset-bf16-persistence-test-for-8-bit-adamw-plus-ch-03dc5d074c/runs/real-dataset-bf16-persistence-test-for-8-bit-adamw-plus-ch-03dc5d074c-20260607T065226496003+0000
- Parent run decision: 8-bit AdamW with gradient checkpointing for 6GB VRAM: enoch://control-plane/projects/8-bit-adamw-with-gradient-checkpointing-for-6gb-vram-3aa1aaf98536/runs/8-bit-adamw-with-gradient-checkpointing-for-6gb-vram-3aa1aaf98536-20260607T050249523559+0000

## What looked useful

AdamW8bit checkpoint/resume appears practically near-equivalent under the tested GPT-2-small-class BF16 setting, and optimizer state restoration is necessary. Strict bitwise equivalence is not supported across all seeds; the residual drift is comparable to a standard AdamW BF16 baseline and likely reflects CUDA/BF16 nondeterminism in this stack rather than a bitsandbytes-only checkpoint failure.

## Boundaries and scale limits

Synthetic fixed token batches only; 16 total training steps; single GB10 process; no real dataset, dataloader-worker checkpointing, distributed training, longer horizon, or publication-scale loss curve. Single-run calibration was near 6 GB allocated, but equivalence comparison peaks are higher because multiple model instances are retained for comparison.

## Claim scope

On NVIDIA GB10 with Torch 2.12.0+cu130, Transformers 4.57.6, and bitsandbytes 0.49.2, a GPT-2-small-class BF16 CUDA training run using AdamW8bit at batch 8 and sequence length 512 resumed near-equivalently from checkpoint over 16 synthetic-token steps across three fixed seeds; proper-resume drift was zero for two seeds and at most 4.96e-05 loss / 6.10e-04 parameter max absolute diff for one seed, while model-only bad-resume controls diverged much more.

## Why it stopped

Tier 2 evidence supports practical near-equivalence but falsifies strict bitwise equivalence across all fixed seeds; the result is useful engineering evidence but not publication-grade.

## Recommended next action

Stop as no-paper useful signal; for a bounded deepen follow-up, rerun with deterministic PyTorch settings where supported and a 100-200 step real-token stream, requiring proper-resume drift to remain at least 10x smaller than model-only bad-resume drift across five seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deterministic and real-token checkpoint/resume drift bounds for GPT-2-small BF16 AdamW8bit
- Success threshold: For every seed, proper-resume max tail-loss drift and final parameter max absolute drift are at least 10x smaller than model-only bad-resume drift, with no unexplained checkpoint load failures and calibrated single-run peak allocation within the declared memory envelope.
- Stop condition: Stop if deterministic settings do not reduce residual drift below the baseline or if proper-resume drift approaches model-only bad-resume drift for any seed.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-bf16-adamw8bit-checkpoint-resume-equival-29ec4a120f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
