# Dynamic Block-wise 8-bit AdamW for GPT-2 small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-block-wise-8-bit-adamw-for-gpt-2-small-77d7c4c00f1f`
Run ID: `dynamic-block-wise-8-bit-adamw-for-gpt-2-small-77d7c4c00f1f-20260601T011301899179+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c71372671f73

## What looked useful

Memory compression worked: dynamic8 used about 2.00 bytes/param for optimizer state versus 4.00 bytes/param for BF16 AdamW state and 8.00 bytes/param for FP32 AdamW state. However, static8 and dynamic8 diverged at the AdamW baseline lr=3e-4 while AdamW loss improved from 8.375 to 5.969. Dynamic8 became stable at lr=1e-4 with loss 8.375 to 7.063, comparable to AdamW lr=1e-4 loss 8.375 to 7.25, but throughput was much lower.

## Boundaries and scale limits

Synthetic task, 100 training steps, 12.3M parameters rather than GPT-2-small 124M, no real corpus validation, no fused optimizer kernels, and limited hyperparameter rescue checks.

## Claim scope

On a 12.3M-parameter GPT-style synthetic language task on GB10, the tested dynamic block-wise int8 AdamW state representation reduced optimizer-state memory but did not preserve AdamW-like stability at lr=3e-4; it was stable only after lowering lr to 1e-4 and was about 5.5x slower in this unfused implementation.

## Why it stopped

Bounded proxy early falsification: dynamic block sizing alone failed the baseline learning-rate stability test, although lower learning rate showed the memory-saving mechanism can train in a retuned regime.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should replace naive second-moment int8 quantization with a stabilized scheme and require stability at lr=3e-4 before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized second-moment quantization for block-wise 8-bit AdamW
- Success threshold: Stabilized dynamic8 remains finite for 100 steps at lr=3e-4, achieves final loss <= 6.3 on the same task, and keeps optimizer-state memory <= 2.5 bytes/param in BF16.
- Stop condition: Stop if the stabilized variant diverges before 100 steps at lr=3e-4 or requires lowering the learning rate below AdamW's tested baseline to remain finite.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-block-wise-8-bit-adamw-for-gpt-2-small-77d7c4c00f1f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
