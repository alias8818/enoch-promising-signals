# INT2-FP16 Residual Q/K for GPT-2-small CPU Inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `int2-fp16-residual-q-k-for-gpt-2-small-cpu-inference-470cb95c9f88`
Run ID: `int2-fp16-residual-q-k-for-gpt-2-small-cpu-inference-470cb95c9f88-20260525T235652052486+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/23d032b8c77b

## What looked useful

In the proxy, small FP16 residuals did not rescue INT2 Q/K projection accuracy enough to preserve a useful compression tradeoff: group size 64 with 10% residual used 0.456x FP16 Q/K storage but still had about 37% projection relative error; group size 16 with 25% residual used 1.0x FP16 storage and still had about 18.5% projection relative error.

## Boundaries and scale limits

Direct Hugging Face GPT-2-small execution was attempted but blocked by local disk capacity during CPU PyTorch installation. Results use synthetic Gaussian weights with GPT-2-small Q/K matrix shapes and theoretical storage accounting, not packed INT2 kernels.

## Claim scope

Deterministic GPT-2-small-shape CPU proxy for grouped affine INT2 Q/K projection weights with sparse FP16 residual retention; not actual pretrained GPT-2 logits or perplexity.

## Why it stopped

Proxy evidence showed an unfavorable accuracy/storage tradeoff, and direct pretrained GPT-2-small validation was blocked by local disk capacity rather than by a scientific ambiguity.

## Recommended next action

Stop this run as proxy early falsification; the only worthwhile retry is a bounded direct GPT-2-small run on a worker with enough disk for CPU PyTorch and model weights.

## Follow-up

- Recommended: `true`
- Type: `retry`
- Title: Direct GPT-2-small INT2 plus FP16 residual Q/K validation
- Success threshold: At Q/K storage ratio below 0.6x FP16, logit relative L2 below 0.02 or perplexity degradation below 5%, with no end-to-end CPU decode slowdown versus FP16/baseline.
- Stop condition: Stop if residual fractions below 25% cannot meet the accuracy threshold or if packed-kernel CPU timing fails to beat the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/int2-fp16-residual-q-k-for-gpt-2-small-cpu-inference-470cb95c9f88`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
