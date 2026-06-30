# FLOP-Weighted Selective Gradient Checkpointing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `flop-weighted-selective-gradient-checkpointing-367dc6f67fc0`
Run ID: `flop-weighted-selective-gradient-checkpointing-367dc6f67fc0-20260601T094021520536+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e1263501b224

## What looked useful

At target fraction 0.50, FLOP-weighted selection reduced peak CUDA memory by 29.86% versus no checkpointing with 10.86% mean time overhead across three seeds, compared with activation-greedy at 26.86% memory reduction and 12.35% overhead. At target fractions 0.35 and 0.65, activation-greedy was equal or better on the measured reduction/overhead ratio, so the hypothesis is budget-sensitive rather than broadly supported.

## Boundaries and scale limits

Tested one synthetic residual stack on one NVIDIA GB10 with batch 8, sequence length 512, dimension 512, 8-10 measured steps per run, and three target fractions. This is not GPT-2-small-class, multi-GPU, long-horizon, or production-training evidence.

## Claim scope

On a synthetic heterogeneous PyTorch CUDA benchmark, FLOP-weighted selective checkpointing improved the memory/runtime tradeoff over activation-greedy selection at a mid-range analytic activation-saving target, but did not dominate across all tested checkpoint budgets.

## Why it stopped

No-paper closure: bounded synthetic evidence is useful and reproducible but mixed across budgets and not direct transformer-scale validation.

## Recommended next action

Run a bounded GPT-2-small-class follow-up with real per-region profiling and compare policies at matched measured peak-memory reductions before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small measured-memory FLOP-weighted checkpointing
- Success threshold: At two or more matched measured-memory targets on a GPT-2-small-class model, FLOP-weighted selection achieves at least 10% lower step-time overhead than activation-greedy while matching loss behavior and peak-memory reduction.
- Stop condition: Stop if FLOP-weighted selection fails to beat activation-greedy overhead by 5% at matched measured-memory targets, or if measured profiling overhead dominates the training step enough to make the policy impractical.

## Evidence references

- Artifact root: `<local-path>/projects/flop-weighted-selective-gradient-checkpointing-367dc6f67fc0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
