# Extreme gradient checkpointing with FP16/INT8 mixed precision for <4GB VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-gradient-checkpointing-with-fp16-int8-mixed-precision-for-4gb-vram-3bdf58e86715`
Run ID: `extreme-gradient-checkpointing-with-fp16-int8-mixed-precision-for-4gb-vram-3bdf58e86715-20260608T045945239923+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b03e7ab43830

## What looked useful

Checkpointing plus INT8 Adam moments reduced the stress model peak from 4.883 GiB with FP32 moments to 3.236 GiB with INT8 moments at lr=5e-5 over 3 synthetic steps, with similar short-run loss movement but slower updates. This supports the memory mechanism but not paper-ready training viability.

## Boundaries and scale limits

Not tested on an actual 4 GB VRAM GPU or hard CUDA memory cap; not trained on a real dataset; only 1-3 synthetic steps per case; local INT8 optimizer is a transparent proxy and not a production 8-bit optimizer; no quality, convergence, or robustness claims beyond short-step viability.

## Claim scope

On GB10 using PyTorch allocation telemetry as a proxy for a 4 GiB VRAM budget, a GPT-like synthetic training step with per-block activation checkpointing and FP16 weights plus INT8-compressed Adam moment buffers fit a stress configuration under 4 GiB allocated CUDA memory while the same checkpointed model with FP32 Adam moments exceeded 4 GiB.

## Why it stopped

Bounded proxy evidence supports the memory mechanism but is insufficient for a paper because it lacks actual 4 GB hardware enforcement, real-data convergence, and production optimizer validation.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next bounded test is a real-dataset 4 GB or hard-capped CUDA run comparing production 8-bit optimizer behavior against FP32-state AMP and checkpointing controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-capped 4GB real-data checkpointed FP16 plus 8-bit optimizer validation
- Success threshold: At least one model configuration where the 8-bit optimizer variant completes 100 or more real-data training steps under 4 GiB with validation loss within 5% of the FP32-state checkpointed baseline, while the FP32-state variant exceeds the memory cap at the same configuration.
- Stop condition: Stop if the 8-bit optimizer variant cannot complete stable real-data training under 4 GiB at any configuration where the FP32-state baseline fails, or if validation loss diverges by more than 5% after tuning only learning rate and standard optimizer hyperparameters.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-gradient-checkpointing-with-fp16-int8-mixed-precision-for-4gb-vram-3bdf58e86715`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
