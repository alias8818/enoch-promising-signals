# Learned-memory downstream benchmark for residual-update quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `learned-memory-downstream-benchmark-for-residual-update-qu-78acb06d5a`
Run ID: `learned-memory-downstream-benchmark-for-residual-update-qu-78acb06d5a-20260614T010310672216+0000`

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

- Parent run decision: Quantized Residual Connections for Agent Memory Architecture: enoch://control-plane/projects/quantized-residual-connections-for-agent-memory-architecture-f99f05b6b1be/runs/quantized-residual-connections-for-agent-memory-architecture-f99f05b6b1be-20260613T212311999210+0000
- Parent run decision: Learned Agent Memory Residual-Update Quantization: enoch://control-plane/projects/learned-agent-memory-residual-update-quantization-f621f3932a/runs/learned-agent-memory-residual-update-quantization-f621f3932a-20260614T004229125275+0000

## What looked useful

Learned residual memory consistently beat the no-memory int4 residual-update ablation across all three seeds, but it only matched a budget-matched dense downstream fine-tune control, so the result supports a bounded task-directed residual adaptation mechanism rather than a paper-ready quantization method.

## Boundaries and scale limits

Single dataset, compact non-transformer classifier, 6000 source examples, 6000 downstream train examples, 7600 held-out test examples, three fixed seeds. Does not validate GPT-2-small-class transformers, multi-task robustness, large language models, serving compression, optimizer-state compression, or publication-scale claims.

## Claim scope

On a three-seed AG News downstream fine-tuning benchmark with a compact mean-pooled PyTorch text classifier, int4 residual-update quantization plus learned low-rank residual memory improved held-out accuracy over plain int4 residual deltas by 1.145 percentage points on average while using about 5.03 effective bits per float parameter.

## Why it stopped

Tier 2 local evidence produced a useful mechanism signal but not paper-positive support; learned memory matched rather than beat the budget-matched dense control.

## Recommended next action

Run a bounded transformer-class deepen test, preferably GPT-2-small-class or DistilBERT on one or two text benchmarks, with fixed seeds, rank and bit ablations, and equalized dense/parameter-efficient training budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-class learned residual-memory update compression benchmark
- Success threshold: Across at least three fixed seeds, learned residual memory should beat plain quantized residual deltas by at least 1 accuracy point and match or beat equal-budget dense or LoRA controls within 0.5 accuracy points at a materially smaller stored update size.
- Stop condition: Stop if learned memory fails to beat plain quantized deltas on at least two of three seeds, or if any gain disappears after equalizing downstream training budget and effective stored parameter cost.

## Evidence references

- Artifact root: `<local-path>/projects/learned-memory-downstream-benchmark-for-residual-update-qu-78acb06d5a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
