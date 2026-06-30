# GPT-2-small-class GB10 checkpointing memory-throughput validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-small-class-gb10-checkpointing-memory-throughput-val-d4ddcfd314`
Run ID: `gpt-2-small-class-gb10-checkpointing-memory-throughput-val-d4ddcfd314-20260613T143900467360+0000`

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

- Parent run decision: Tiny-VRAM Gradient Checkpointing for GB10: enoch://control-plane/projects/tiny-vram-gradient-checkpointing-for-gb10-8a995d8cb53c/runs/tiny-vram-gradient-checkpointing-for-gb10-8a995d8cb53c-20260613T141302730439+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2cedb9658183

## What looked useful

Activation checkpointing reduced peak PyTorch CUDA allocation by 15.4% to 26.4% across valid GPT-2-small-class GB10 comparisons. Throughput ranged from 0.922x to 1.187x of the no-checkpoint baseline, with seq1024 fresh sequential reruns reproducing lower memory and no throughput penalty.

## Boundaries and scale limits

Synthetic random tokens only; short step counts; one model implementation; one precision; no real corpus, convergence, optimizer-state scaling study, multi-seed statistics, dataloader pressure, distributed training, or independent hardware memory counter beyond PyTorch CUDA allocator plus host UMA telemetry.

## Claim scope

Single-GB10 Tier 1 direct benchmark of GPT-2-small-class bf16 synthetic causal-LM training steps in PyTorch 2.12/CUDA 13.0, comparing per-block activation checkpointing against the same model without checkpointing.

## Why it stopped

Tier 1 direct validation target was met and produced a useful mechanism signal, but the evidence remains short-run synthetic benchmarking and is not publication-grade.

## Recommended next action

Run a bounded deepen test with repeated randomized order, 3+ repetitions per config, a real tokenized dataset or cached batches, and success threshold of at least 20% peak allocated-memory reduction with no more than 10% throughput loss on seq1024 GPT-2-small-class training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Repeated GB10 GPT-2-small checkpointing benchmark with real cached token batches
- Success threshold: Checkpointing achieves >=20% lower peak PyTorch CUDA allocated memory and >=0.90x no-checkpoint throughput in every tested batch-size condition, with no OOM or loss/step execution failures.
- Stop condition: Stop if any repeated condition shows <10% memory saving, >20% throughput loss, unexplained instability, or telemetry cannot distinguish allocated-memory effects from allocator artifacts.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-gb10-checkpointing-memory-throughput-val-d4ddcfd314`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
