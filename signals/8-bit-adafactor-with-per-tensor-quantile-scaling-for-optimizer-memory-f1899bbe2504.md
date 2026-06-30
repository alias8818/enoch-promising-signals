# 8-bit AdaFactor with Per-Tensor Quantile Scaling for Optimizer Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adafactor-with-per-tensor-quantile-scaling-for-optimizer-memory-f1899bbe2504`
Run ID: `8-bit-adafactor-with-per-tensor-quantile-scaling-for-optimizer-memory-f1899bbe2504-20260528T122221253090+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b36e65c0bc48

## What looked useful

The memory-saving mechanism works for AdaFactor row/column/bias states, but per-tensor quantile clipping is not a clear improvement over max scaling and can harm moment reconstruction or high-learning-rate stability.

## Boundaries and scale limits

No GPT-2-small, language-model corpus, distributed training, checkpoint integration, production kernel, or long training run was tested. The result measures optimizer-state bytes and short-run convergence only.

## Claim scope

On a CUDA synthetic teacher classification task with a 24 MiB MLP, uint8 factored AdaFactor state reduced AdaFactor optimizer-state bytes by 74.9%. With lr=0.001, max, q0.999, and q0.99 scaling stayed within about 1.1 percentage points of fp32 AdaFactor mean final accuracy over three seeds; with lr=0.003, quantized variants showed instability or degradation.

## Why it stopped

Closed as a no-paper useful signal: bounded local evidence supports memory reduction but shows mixed convergence and quantile-scaling stability risk.

## Recommended next action

Do not write a paper from this run; run a bounded GPT-2-small-class follow-up with lr sweep and checkpoint/restart tests before considering broader claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class 8-bit AdaFactor quantile scaling stability sweep
- Success threshold: At least one uint8 scaling variant reduces AdaFactor optimizer-state bytes by >=70%, has zero divergence across three seeds, and ends within 1% validation loss of fp32 AdaFactor on the same workload and tuned learning-rate budget.
- Stop condition: Stop if all uint8 variants either diverge or exceed 3% validation-loss degradation at every tested learning rate, or if checkpoint/resume changes the loss trajectory beyond normal seed variance.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adafactor-with-per-tensor-quantile-scaling-for-optimizer-memory-f1899bbe2504`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
