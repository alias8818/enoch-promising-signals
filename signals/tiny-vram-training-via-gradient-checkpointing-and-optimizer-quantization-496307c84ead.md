# tiny-VRAM training via gradient checkpointing and optimizer quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-vram-training-via-gradient-checkpointing-and-optimizer-quantization-496307c84ead`
Run ID: `tiny-vram-training-via-gradient-checkpointing-and-optimizer-quantization-496307c84ead-20260610T225400800013+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6e35676d305a

## What looked useful

Checkpointing and optimizer quantization produced additive memory savings: seq256 peak CUDA allocation fell from 1596.4 MiB to 843.5 MiB, and seq512 fell from 2656.7 MiB to 1384.5 MiB. AdamW optimizer state fell from about 319 MiB to about 80 MiB. The cost was roughly 26-33% lower throughput in the combined configuration.

## Boundaries and scale limits

Evidence is limited to synthetic random-token data, one local GB10 worker, short 6-10 step measured runs, one model scale, and a local custom 8-bit AdamW implementation. It does not establish real-data convergence, final model quality, GPT-2-small-class behavior, production optimizer parity, or a strict tiny-VRAM OOM boundary.

## Claim scope

On short synthetic GPT-style language-model training runs around 42M parameters on a GB10, per-block activation checkpointing plus blockwise uint8 AdamW optimizer states reduced peak CUDA allocation by about 47-48% versus full AdamW without checkpointing, while completing training steps with comparable short-run synthetic loss.

## Why it stopped

No-paper useful signal: the local synthetic runs support the memory-saving mechanism, but the result is not a full validation because it lacks real-data convergence and production optimizer comparisons.

## Recommended next action

Run a bounded real-data GPT-2-small-class fine-tuning comparison with baseline AdamW, checkpointing, 8-bit optimizer state, and the combined configuration under a fixed memory cap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data GPT-2-small memory-cap validation for checkpointing plus 8-bit optimizer state
- Success threshold: Combined configuration achieves at least 40% peak CUDA allocation reduction or at least 1.5x larger feasible batch/sequence under the same cap, with final validation loss within 5% of baseline AdamW over the bounded run.
- Stop condition: Stop as unsupported if the combined configuration saves less than 25% peak memory, cannot train stably for the bounded run, or validation loss degrades by more than 10% versus baseline at matched tokens.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-vram-training-via-gradient-checkpointing-and-optimizer-quantization-496307c84ead`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
