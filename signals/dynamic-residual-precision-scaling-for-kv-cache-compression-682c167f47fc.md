# Dynamic Residual Precision Scaling for KV Cache Compression

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `dynamic-residual-precision-scaling-for-kv-cache-compression-682c167f47fc`
Run ID: `dynamic-residual-precision-scaling-for-kv-cache-compression-682c167f47fc-20260524T231210805758+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2693334657a2

## What looked useful

Residual scores beat naive recency/random mixed precision in some cases, but fixed-bit quantization was consistently better at the same average bit budget; even oracle-attention mixed allocation lost to fixed-bit, suggesting unevenly lowering many tokens is harmful under this quantizer/metric.

## Boundaries and scale limits

Synthetic cache regimes used 1024-token sequences, 8 heads, 64 dimensions, 96 queries, and 5 seeds; the real-model probe used sshleifer/tiny-gpt2 only. No full autoregressive generation, perplexity, production LLM, or serving throughput validation was run.

## Claim scope

For the implemented per-token symmetric K/V quantization benchmark, residual-adaptive mixed precision at 3-bit and 4-bit average budgets did not improve attention-output reconstruction error over uniform fixed-bit quantization on synthetic smooth/mixed/bursty caches or a tiny-GPT2 cache probe.

## Why it stopped

Bounded proxy and tiny-model evidence falsified the simple dynamic residual precision scaling claim against the required fixed-bit baseline; this is not a full-scale validation, but it is enough to avoid scaling this implementation family as-is.

## Recommended next action

Stop this paper path unless a new mechanism is proposed; any next test should first beat fixed-bit KV quantization on tiny/small real-model perplexity before scaling.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Residual-coded KV delta quantization against fixed-bit baselines
- Success threshold: At equal memory, reduce attention-output relative MSE by at least 20% versus fixed-bit and avoid perplexity degradation relative to fixed-bit on the same tiny/small model probe.
- Stop condition: Stop if residual-coded deltas fail to beat fixed-bit on attention-output error across at least three real-text prompts or if memory accounting exceeds the fixed-bit budget.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-residual-precision-scaling-for-kv-cache-compression-682c167f47fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
