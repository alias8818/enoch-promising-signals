# Ultra-Low Bit Quantization for Home Training on Budget Hardware

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ultra-low-bit-quantization-for-home-training-on-budget-hardware-7762217dd7e4`
Run ID: `ultra-low-bit-quantization-for-home-training-on-budget-hardware-7762217dd7e4-20260607T163601427887+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/240bf78d3f82

## What looked useful

Low-bit forward/backward quantization alone is not the bottleneck on this proxy; q4 and q1 with Adam remained trainable. The practical home-training claim is not supported unless optimizer/master-state memory is also compressed without the loss hit seen from plain SGD.

## Boundaries and scale limits

No real transformer, tokenizer, corpus, GPU, GB10, GPT-2-small-class, activation-memory, checkpointing, or full home-hardware validation was run. Memory conclusions are parameter-state accounting and exclude activations, gradients, framework overhead, and checkpoints.

## Claim scope

On a controlled NumPy next-token proxy, q4 and q1 quantized forward/backward training with fp32 master weights and Adam matched dense Adam within about 0.012 validation-loss points across 3 seeds, but this retained dense training state. Plain low-state SGD reduced state memory and underperformed.

## Why it stopped

Proxy evidence is mixed: low-bit Adam trains, but the home-training memory mechanism remains unsupported because fp32 master weights and Adam moments dominate training state; this is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replace dense Adam state with a true low-state or quantized optimizer on a small transformer and require near-dense validation loss plus measured memory savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Low-state optimizer test for low-bit small-transformer home training
- Success threshold: q4 low-state optimizer reaches validation perplexity within 5% of dense Adam while reducing measured peak training memory by at least 2x on the same model, batch, and sequence length.
- Stop condition: Stop if q4 low-state optimizer is more than 10% worse in validation perplexity after matched tokens, or if measured memory reduction is below 1.5x after including optimizer, gradients, activations, and checkpoint overhead.

## Evidence references

- Artifact root: `<local-path>/projects/ultra-low-bit-quantization-for-home-training-on-budget-hardware-7762217dd7e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
