# Gradient Checkpointing + Mixed Precision for 60% VRAM Reduction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-checkpointing-mixed-precision-for-60-vram-reduction-a3afc381745a`
Run ID: `gradient-checkpointing-mixed-precision-for-60-vram-reduction-a3afc381745a-20260607T170532278631+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d23b46f8b45c

## What looked useful

The mechanism is activation-fraction dependent: bf16+checkpointing did not reach 60% peak allocated-memory reduction at seq_len=1024, but did reach 62.4% at seq_len=2048. This supports using the technique when activation memory dominates peak training memory, while warning against a universal 60% claim.

## Boundaries and scale limits

Evidence is limited to synthetic token data, short runs of 2-3 measured steps after warmup, single-GPU GB10 execution, and PyTorch allocator telemetry. It does not validate real-corpus convergence, long-run stability, multi-GPU behavior, 7B+ models, or all model shapes; a seq_len=1024 setting reached only 54.3% allocated-memory reduction.

## Claim scope

On a synthetic GPT-style 12-layer, 768-dim transformer training step on NVIDIA GB10, combining bfloat16 autocast with per-block activation checkpointing reduced PyTorch peak allocated memory by 62.4% versus an fp32 non-checkpointed baseline for the activation-heavy batch_size=4, seq_len=2048 setting.

## Why it stopped

No-paper useful signal: local synthetic evidence supports the memory-reduction mechanism in activation-heavy settings, but this is not direct publication-grade evidence for real training workloads.

## Recommended next action

Run a bounded real-data GPT-2-small-class training confirmation with the same four cases, reporting peak memory, throughput, and matched loss trajectory over enough steps to rule out synthetic/short-run artifacts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data GPT-2-small confirmation of bf16 checkpointing memory reduction
- Success threshold: bf16_checkpointed achieves at least 60% lower peak allocated memory than fp32 without checkpointing and final/mean loss remains within 5% of the comparable precision baseline over the bounded run.
- Stop condition: Stop if bf16_checkpointed fails to reach 55% peak allocated-memory reduction on the real-data run or if loss diverges relative to the baseline under the same optimizer and batch/token budget.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-checkpointing-mixed-precision-for-60-vram-reduction-a3afc381745a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
