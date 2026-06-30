# Bounded Long-Context Training on 6GB VRAM with Compressed State

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-long-context-training-on-6gb-vram-with-compressed-state-aa49984e05df`
Run ID: `bounded-long-context-training-on-6gb-vram-with-compressed-state-aa49984e05df-20260611T185932980583+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2dbc57aa11d0

## What looked useful

Compressed-state chunking reduced peak memory enough to complete a 16k one-step probe under a 6GB cap, but sustained 16k training OOMed after one step and 8k learnability remained at chance after 200 steps.

## Boundaries and scale limits

Synthetic delayed-key task only; no natural language corpus, no GPT-2-small parameter-matched full baseline with controlled positional embedding size, no physical 6GB GPU, no activation checkpointing or reduced optimizer state, and only short bounded runs.

## Claim scope

Allocator-capped GB10 experiments with PyTorch BF16 show a narrow memory-feasibility edge for a chunked detached single-vector compressed-state transformer: an 86.9M-parameter compressed model completed one 16,384-token training step under a 6GB CUDA cap where a full causal transformer stress baseline OOMed. The tested prototype did not demonstrate sustained 16k training or learning on the synthetic delayed-key task.

## Why it stopped

No-paper useful signal: proxy experiments show a memory-feasibility mechanism but not sustained training or task learning; this is not full validation.

## Recommended next action

Run a bounded deepen test with activation checkpointing and reduced optimizer state, using controlled positional embeddings, and require sustained 16k training plus above-chance delayed-key accuracy before considering scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sustain 16k Compressed-State Training Under 6GB With Optimizer-State Controls
- Success threshold: Complete 100 consecutive 16,384-token compressed-state training steps under 6GB with validation accuracy at least 2x random chance and no OOM.
- Stop condition: Stop if the compressed model OOMs before 100 steps after checkpointing and optimizer-state reduction, or if validation accuracy remains at chance after the full bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-long-context-training-on-6gb-vram-with-compressed-state-aa49984e05df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
