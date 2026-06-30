# Bounded Gradient Checkpointing for Home Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-gradient-checkpointing-for-home-training-d3f169d4fb1a`
Run ID: `bounded-gradient-checkpointing-for-home-training-d3f169d4fb1a-20260607T224415227824+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fec5ab3734c4

## What looked useful

Bounded caps reduced peak allocated memory from 1189.9 MiB to 757.6 MiB at a 168 MiB estimated activation budget and to 973.7 MiB at a 336 MiB budget, while recovering speed relative to all-checkpointing. All policies had identical deterministic synthetic loss trajectories.

## Boundaries and scale limits

Evidence is limited to synthetic inputs, short 20-step runs, MLP-heavy blocks, one GB10 host, and CUDA peak memory metrics. It does not validate real language-model quality, GPT-2-small-class training, attention-heavy memory behavior, or long-run stability.

## Claim scope

On a synthetic 57.2M-parameter bf16 transformer-MLP stack on NVIDIA GB10, budgeted partial activation checkpointing produced a monotonic memory/speed tradeoff between no checkpointing and all-block checkpointing.

## Why it stopped

Proxy-only useful signal; not direct publication-grade evidence for home language-model training.

## Recommended next action

Run a bounded GPT-2-small-class language-model confirmation on a real token corpus with validation loss parity, OOM boundary checks, and the same no-checkpoint/all-checkpoint/bounded policy controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class bounded checkpointing confirmation
- Success threshold: Bounded policy achieves at least 25% lower peak allocated memory than no checkpointing, at least 90% of all-checkpoint tokens/second, and validation loss within 0.05 absolute loss or within one-seed run-to-run noise of the controls.
- Stop condition: Stop if bounded policies fail to beat all-checkpoint throughput by at least 5% at comparable memory, or if validation loss diverges beyond the predefined tolerance.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-gradient-checkpointing-for-home-training-d3f169d4fb1a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
