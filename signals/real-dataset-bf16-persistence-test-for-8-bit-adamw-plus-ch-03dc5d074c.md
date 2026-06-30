# Real-dataset BF16 persistence test for 8-bit AdamW plus checkpointing under a 6GB cap

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-dataset-bf16-persistence-test-for-8-bit-adamw-plus-ch-03dc5d074c`
Run ID: `real-dataset-bf16-persistence-test-for-8-bit-adamw-plus-ch-03dc5d074c-20260607T065226496003+0000`

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

- Parent run decision: 8-bit AdamW with gradient checkpointing for 6GB VRAM: enoch://control-plane/projects/8-bit-adamw-with-gradient-checkpointing-for-6gb-vram-3aa1aaf98536/runs/8-bit-adamw-with-gradient-checkpointing-for-6gb-vram-3aa1aaf98536-20260607T050249523559+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/61f3ac8109ea

## What looked useful

Checkpointing-enabled Tier 1 run preserved 25744384 BF16 parameters after reload, restored non-empty bitsandbytes optimizer state with 51380224 uint8 elements, reduced loss from 3.2939 to 2.6107, and peaked at 433085952 CUDA allocated bytes under the 6442450944-byte cap. Matched no-checkpoint control also reloaded correctly and peaked at 856863744 bytes.

## Boundaries and scale limits

Only 25.7M parameters, 24 measured steps, Wikitext-2 cached train data, local custom Transformer rather than a pretrained GPT-2/HF Trainer stack, and peak allocation stayed far below 6GB rather than stress-testing the cap boundary.

## Claim scope

A small byte-level Transformer trained on real Wikitext-2 data on GB10 can use CUDA BF16 parameters, bitsandbytes AdamW8bit optimizer state, activation checkpointing, and checkpoint save/reload while staying below a 6GB CUDA allocation cap for a 24-step Tier 1 run.

## Why it stopped

Tier 1 direct real-dataset mechanism check succeeded, but evidence is too small and too custom-model-specific for publication readiness.

## Recommended next action

Run a bounded GPT-2-small-class Hugging Face checkpoint/resume equivalence test near 5.5GB peak allocation before considering any paper path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class BF16 AdamW8bit checkpoint/resume equivalence near 6GB
- Success threshold: Resumed run has BF16-only parameters, non-empty uint8 bitsandbytes optimizer state, no OOM, peak CUDA allocation <= 6GB, and next-step loss within 1e-4 relative or 1e-3 absolute of uninterrupted control on the same batch.
- Stop condition: Stop negative if reload drops BF16 parameters, loses optimizer state, OOMs below the 6GB cap after calibration, or resumed next-step loss exceeds the equivalence threshold in two reproducible attempts.

## Evidence references

- Artifact root: `<local-path>/projects/real-dataset-bf16-persistence-test-for-8-bit-adamw-plus-ch-03dc5d074c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
