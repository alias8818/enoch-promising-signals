# Real-data GPT-2-small memory-cap validation for checkpointing plus 8-bit optimizer state

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-data-gpt-2-small-memory-cap-validation-for-checkpoint-6852c9b0f9`
Run ID: `real-data-gpt-2-small-memory-cap-validation-for-checkpoint-6852c9b0f9-20260610T231457087515+0000`

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

- Parent run decision: tiny-VRAM training via gradient checkpointing and optimizer quantization: enoch://control-plane/projects/tiny-vram-training-via-gradient-checkpointing-and-optimizer-quantization-496307c84ead/runs/tiny-vram-training-via-gradient-checkpointing-and-optimizer-quantization-496307c84ead-20260610T225400800013+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6e35676d305a

## What looked useful

The combined memory-saving configuration produced a real pass/fail threshold improvement on GPT-2-small/Wikitext under a CUDA cap. Optimizer-state compression was necessary to pass below 2 GiB; activation checkpointing supplied a smaller additional margin that crossed the 1.75 GiB viability boundary.

## Boundaries and scale limits

Short single-host, single-seed cap-threshold test only; no long training, no convergence/quality claim, no multi-batch or multi-sequence sweep, no broad dataset robustness, and no publication-grade ablation depth.

## Claim scope

Tier 1 direct GB10 test: GPT-2-small trained on real Wikitext-2 text for 6 steps at batch size 1 and sequence length 512 under explicit PyTorch CUDA memory caps. Checkpointing plus bitsandbytes Adam8bit completed at 1.75 GiB where Adam8bit alone failed after one step, and full AdamW failed at 2.00 GiB even with checkpointing.

## Why it stopped

No-paper closure: this Tier 1 direct test supports the mechanism but is too short and narrow for a paper-ready training-memory claim.

## Recommended next action

Run a medium direct follow-up with binary-searched cap thresholds across multiple seeds, sequence lengths, and batch sizes, plus longer Wikitext training windows with validation loss and throughput tracking.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium GPT-2-small cap-threshold sweep for checkpointing plus 8-bit optimizer state
- Success threshold: Combined checkpointing plus Adam8bit must reduce the median minimum viable cap by at least 5 percent versus Adam8bit alone and by at least 20 percent versus full AdamW controls while completing the longer run without loss divergence.
- Stop condition: Stop if the combined configuration loses its cap advantage in two or more tested settings, if throughput overhead exceeds 25 percent without a cap-bound benefit, or if repeated runs show unstable OOM boundaries.

## Evidence references

- Artifact root: `<local-path>/projects/real-data-gpt-2-small-memory-cap-validation-for-checkpoint-6852c9b0f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
