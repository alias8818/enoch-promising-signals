# Hard-memory validation of 8-bit AdamW on a small transformer under a 4GB cap

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hard-memory-validation-of-8-bit-adamw-on-a-small-transform-8385a50887`
Run ID: `hard-memory-validation-of-8-bit-adamw-on-a-small-transform-8385a50887-20260612T062953985729+0000`

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

- Parent run decision: 8-bit Block Quantized Adam for sub-4GB VRAM Training: enoch://control-plane/projects/8-bit-block-quantized-adam-for-sub-4gb-vram-training-1f6f97c637a0/runs/8-bit-block-quantized-adam-for-sub-4gb-vram-training-1f6f97c637a0-20260612T040800070896+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b976a0e4c66e

## What looked useful

8-bit AdamW provided a direct memory-feasibility win under the 4 GiB cap in a controlled small transformer test: peak CUDA reserved was 3.127 GiB for AdamW8bit, while standard AdamW reached 3.998 GiB reserved and failed with CUDA OOM under the same cap.

## Boundaries and scale limits

Synthetic data only; one model shape; one seed; three 8-bit optimizer steps; no real-corpus convergence, quality parity, longer-sequence, larger-batch, or multi-configuration robustness validation.

## Claim scope

On this GB10 host, a 251.9M-parameter GPT-style transformer with batch size 1 and sequence length 64 completed three CUDA optimizer steps under a 4 GiB allocator cap using bitsandbytes AdamW8bit, while the same configuration with torch.optim.AdamW hit the 4 GiB CUDA allocator limit before completing the first step.

## Why it stopped

Tier 1 direct memory threshold was met for the scoped setup, but this remains no-paper useful signal because training stability and quality were not validated beyond three synthetic steps.

## Recommended next action

Run a bounded medium follow-up on a real tokenized corpus for at least 500 optimizer steps under the same 4 GiB cap, comparing AdamW8bit memory persistence, loss trajectory, and any instability against the largest standard AdamW configuration that fits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium persistence test for 8-bit AdamW under a 4 GiB cap
- Success threshold: AdamW8bit completes at least 500 capped steps with peak CUDA reserved below 4 GiB, no NaN/Inf events, and a non-divergent loss trend, while preserving a clear parameter-count or memory-headroom advantage over standard AdamW.
- Stop condition: Stop if AdamW8bit exceeds the 4 GiB cap, produces NaN/Inf loss, shows repeated loss divergence over the short run, or if standard AdamW fits the same shape with comparable memory headroom under corrected measurement.

## Evidence references

- Artifact root: `<local-path>/projects/hard-memory-validation-of-8-bit-adamw-on-a-small-transform-8385a50887`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
