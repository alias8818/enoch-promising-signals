# 8-bit AdamW with gradient checkpointing for 6GB VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `8-bit-adamw-with-gradient-checkpointing-for-6gb-vram-3aa1aaf98536`
Run ID: `8-bit-adamw-with-gradient-checkpointing-for-6gb-vram-3aa1aaf98536-20260607T050249523559+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/61f3ac8109ea

## What looked useful

8-bit AdamW plus checkpointing cut peak allocated memory by 1778.66 MiB (43.33%) versus full AdamW without checkpointing on a 354.8M-parameter BF16 seq1024 case, and 8-bit AdamW completed a 774.0M-parameter fp16 seq1024 step under the 6GB cap where full AdamW failed.

## Boundaries and scale limits

Synthetic random-token batches only; 1-3 optimizer steps; allocator-cap proxy for 6GB VRAM on GB10 UMA rather than a physical 6GB discrete GPU; no convergence, validation-loss, dataset, checkpoint-restart, or long-run stability evidence.

## Claim scope

On a GB10 host using a 6GB PyTorch CUDA allocator cap, bitsandbytes AdamW8bit plus gradient checkpointing reduces peak allocated memory for GPT-2-style synthetic causal-language-model steps and permits a 774M-parameter fp16 step where full AdamW OOMs.

## Why it stopped

Closed as no-paper useful signal because evidence is direct for short synthetic step feasibility and memory savings, but not for real training quality or physical 6GB GPU behavior.

## Recommended next action

Run a bounded real-dataset BF16 persistence test under the same 6GB cap with GPT-2-small/medium configs, validation loss, restart checks, and full AdamW controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-dataset BF16 persistence test for 8-bit AdamW plus checkpointing under a 6GB cap
- Success threshold: AdamW8bit plus checkpointing completes the planned run under the 6GB cap with finite losses, validation loss not diverging, and at least 25% lower peak allocated memory than the strongest full-AdamW control at the same model/sequence/batch setting.
- Stop condition: Stop if AdamW8bit plus checkpointing OOMs or develops non-finite loss on both GPT-2-small and GPT-2-medium-class configs under BF16 while a smaller control configuration remains healthy.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-with-gradient-checkpointing-for-6gb-vram-3aa1aaf98536`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
