# 8-bit AdamW vs full AdamW on GPT-2-small, gb10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `8-bit-adamw-vs-full-adamw-on-gpt-2-small-gb10-d7f5b2a6f68c`
Run ID: `8-bit-adamw-vs-full-adamw-on-gpt-2-small-gb10-d7f5b2a6f68c-20260610T125214723069+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/021ea2559543

## What looked useful

bitsandbytes AdamW8bit is operational on this CUDA 13/aarch64 GB10 stack and gives a clear short-run memory/throughput advantage over full AdamW on the GPT-2-small architecture without short-run loss divergence. A naive local blockwise 8-bit moment optimizer diverged in calibration, showing implementation details matter.

## Boundaries and scale limits

Not real-corpus pretraining; only 40 completed optimizer steps, one seed, deterministic synthetic batches, no validation perplexity, no checkpoint/restart test, no mixed-precision ablation, and no multi-run robustness.

## Claim scope

On a bounded 40-step deterministic synthetic GPT-2-small CUDA training workload on NVIDIA GB10, bitsandbytes AdamW8bit reduced optimizer-state bytes by 74.5%, reduced final CUDA allocated memory to 71.7% of full AdamW, ran at 1.21x the measured token throughput, and closely tracked full AdamW losses.

## Why it stopped

Closed as no-paper useful signal: the completed evidence directly measures GB10 optimizer-state memory and short-run loss behavior, but synthetic data and 40 steps are insufficient for publication-grade optimizer claims.

## Recommended next action

Run a bounded real-text follow-up using the same GPT-2-small shape for at least 2,000 optimizer steps, three seeds, fixed-token validation perplexity checkpoints, and checkpoint/restart verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text GPT-2-small AdamW8bit stability and validation-perplexity check on GB10
- Success threshold: AdamW8bit validation perplexity is within 1% of full AdamW at the final checkpoint, no loss instability occurs, and optimizer-state bytes remain at least 60% lower than full AdamW.
- Stop condition: Stop early if AdamW8bit validation perplexity exceeds full AdamW by more than 5% at two consecutive checkpoints, produces NaN/Inf loss, or checkpoint resume fails.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-vs-full-adamw-on-gpt-2-small-gb10-d7f5b2a6f68c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
