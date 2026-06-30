# Binary Weights with FP4 Attention-Only Residual Path

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `binary-weights-with-fp4-attention-only-residual-path-b92628471e8c`
Run ID: `binary-weights-with-fp4-attention-only-residual-path-b92628471e8c-20260629T000655249060+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/640fda8882d3

## What looked useful

Low-bit residual precision can recover part of the binary-weight training loss gap, but the evidence does not support attention-only placement as uniquely effective or paper-ready.

## Boundaries and scale limits

2-layer, 4-head, 128-hidden character LM for 300 steps; not parameter-matched across residual variants; uniform 4-bit STE simulation rather than hardware FP4; no GPT-2-small-class, large-corpus, or inference-throughput validation.

## Claim scope

On a three-seed TinyShakespeare tiny decoder-only transformer probe, a uniform 4-bit simulated residual path on attention projections improved binary-weight validation loss, but non-attention and all-linear residual controls improved more.

## Why it stopped

No-paper mixed result: attention-only FP4 residual improved over binary in a small direct probe, but a non-attention residual control improved more and the experiment is not parameter-matched or hardware-FP4 validated.

## Recommended next action

Stop this run; if continuing, run a parameter-matched residual-budget allocation study comparing attention-only, MLP/head-only, and all-linear FP4 residual placement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched FP4 residual budget allocation for binary-weight transformers
- Success threshold: Attention-only residual placement must beat binary-only by at least 0.04 validation-loss points and beat equal-budget MLP/head-only and distributed residual controls by at least 0.02 validation-loss points on mean final validation loss.
- Stop condition: Stop if attention-only does not beat the equal-budget non-attention residual control after three seeds, or if the effect reverses before the larger confirmation run.

## Evidence references

- Artifact root: `<local-path>/projects/binary-weights-with-fp4-attention-only-residual-path-b92628471e8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
