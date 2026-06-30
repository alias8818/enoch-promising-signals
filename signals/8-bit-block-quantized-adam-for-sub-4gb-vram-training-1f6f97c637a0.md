# 8-bit Block Quantized Adam for sub-4GB VRAM Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `8-bit-block-quantized-adam-for-sub-4gb-vram-training-1f6f97c637a0`
Run ID: `8-bit-block-quantized-adam-for-sub-4gb-vram-training-1f6f97c637a0-20260612T040800070896+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b976a0e4c66e

## What looked useful

The mechanism behaves as expected locally: approximately 75% optimizer-state byte reduction and unchanged short-run loss. Measured bytes per parameter project to about 1.6x more resident fp32 parameters under a 4GiB params+grads+optimizer-state-only budget, but this is not an end-to-end training-capacity result.

## Boundaries and scale limits

Synthetic 80-step MLP benchmark only; no real language-model or vision-model convergence; no fused CUDA optimizer kernel; no direct 4GB discrete-VRAM device test; GB10 UMA memory telemetry is not equivalent to consumer VRAM occupancy; projection excludes activations, allocator overhead, fragmentation, and temporary dequantization tensors.

## Claim scope

On a GB10 CUDA worker, a transparent PyTorch block-wise 8-bit AdamW state implementation reduced resident optimizer-state storage from 8.0000 to 2.0042 bytes per parameter on a 13.9M-parameter synthetic MLP benchmark while matching short-run synthetic regression loss within 0.00019 final MSE of AdamW.

## Why it stopped

The result is a bounded proxy/mechanism validation with strong prior art, not a full validation of novel sub-4GB training.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a hard-memory-cap or actual 4GB-GPU run using bitsandbytes or a fused optimizer on a small transformer workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-memory validation of 8-bit AdamW on a small transformer under a 4GB cap
- Success threshold: 8-bit AdamW completes at least 500 optimizer steps under a 4GiB cap with final validation loss within 2% of the uncapped AdamW control, while the same capped workload with standard AdamW fails or requires at least 25% fewer parameters/tokens per batch.
- Stop condition: Stop if bitsandbytes/fused optimizer cannot run on the target hardware, if 8-bit AdamW diverges before 500 steps, or if the capped AdamW baseline fits with no meaningful capacity disadvantage.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-block-quantized-adam-for-sub-4gb-vram-training-1f6f97c637a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
