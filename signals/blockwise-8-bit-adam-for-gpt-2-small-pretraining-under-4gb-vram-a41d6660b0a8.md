# Blockwise 8-bit Adam for GPT-2-small pretraining under 4GB VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `blockwise-8-bit-adam-for-gpt-2-small-pretraining-under-4gb-vram-a41d6660b0a8`
Run ID: `blockwise-8-bit-adam-for-gpt-2-small-pretraining-under-4gb-vram-a41d6660b0a8-20260519T050532691613+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fe090176523b

## What looked useful

Blockwise 8-bit AdamW provided a measured 4x Adam-moment state reduction and practical microbatch headroom under a 4 GiB cap for GPT-2-small-shaped synthetic training, but the evidence is only a short memory/mechanics probe.

## Boundaries and scale limits

Synthetic random-token batches only; 10-step maximum at the distinguishing microbatch-4 boundary; no real corpus, validation loss, checkpoint/restart, data pipeline, or long-run convergence evidence. The prototype is unfused and slower than fp32 AdamW at microbatch 1. At lr=3e-4 it diverged in a 6-step synthetic run, while lr=1e-4 was bounded in the tested short runs.

## Claim scope

On a GB10 with PyTorch 2.11, a local blockwise int8 AdamW prototype ran GPT-2-small geometry, 1024-token synthetic causal-LM training with bf16 autocast and gradient checkpointing under an explicit 4 GiB CUDA allocator cap. It reduced persistent optimizer state from 949.4 MiB to 237.8 MiB and enabled a microbatch-4 short run that fp32 AdamW could not run under the same cap.

## Why it stopped

Synthetic short-run evidence supports a bounded mechanism and capacity signal, but it is not full pretraining validation or paper-ready evidence.

## Recommended next action

Stop this run as no-paper useful evidence; next run should test real-token GPT-2-small pretraining under the same 4 GiB cap with validation loss curves and restart/checkpoint behavior.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-token GPT-2-small 4 GiB blockwise AdamW validation
- Success threshold: Blockwise int8 AdamW completes at least a medium-length real-token run under 4 GiB with no divergence, validation loss within 5% of fp32 AdamW at matched effective batch, and either a larger feasible microbatch or at least 500 MiB lower peak allocated memory.
- Stop condition: Stop if blockwise int8 AdamW diverges across two reasonable learning-rate/warmup settings, cannot resume from checkpoint, or fails to provide memory headroom over fp32 AdamW under the documented 4 GiB cap.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-8-bit-adam-for-gpt-2-small-pretraining-under-4gb-vram-a41d6660b0a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
