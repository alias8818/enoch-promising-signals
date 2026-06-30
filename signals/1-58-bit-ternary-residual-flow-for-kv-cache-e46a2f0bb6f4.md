# 1.58-bit Ternary Residual Flow for KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-58-bit-ternary-residual-flow-for-kv-cache-e46a2f0bb6f4`
Run ID: `1-58-bit-ternary-residual-flow-for-kv-cache-e46a2f0bb6f4-20260605T032131095592+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6bd3f315dc2e

## What looked useful

1-step ternary averaged about 1.54 entropy bits/value and 0.613 attention-output relative L2 across the medium grid, better than tested int2 baselines overall. 2-step and 3-step residual ternary used about 3.11 and 4.65 bits/value but trailed int3/int4 affine baselines; outlier and correlated KV distributions were clear weak cases.

## Boundaries and scale limits

CPU-only NumPy proxy run; synthetic KV distributions only; no real transformer KV traces, no model perplexity or retrieval metrics, no cache packing kernel, and no serving latency measurement.

## Claim scope

Synthetic KV-cache attention experiments show that a single entropy-coded ternary stage can beat simple 2-bit baselines on Gaussian and Laplace proxy KV tensors, but greedy ternary residual-flow stages are not competitive with ordinary int3/int4 affine quantization at comparable effective bit neighborhoods.

## Why it stopped

Proxy evidence is mixed and specifically undermines the residual-flow claim; the result is useful but not a full validation or paper-ready positive.

## Recommended next action

Stop this run as no-paper evidence; run one bounded real-KV-trace follow-up before investing in kernels or larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV Trace Test for Entropy-Coded Ternary KV Compression
- Success threshold: Ternary KV achieves lower model-level degradation than int2 and no worse than 10 percent higher attention-output error than int3 while staying at or below 1.8 effective bits/value after metadata accounting.
- Stop condition: Stop if real KV traces reproduce the synthetic outlier/correlated failure pattern or if metadata pushes ternary storage above 2.0 effective bits/value without matching int3 quality.

## Evidence references

- Artifact root: `<local-path>/projects/1-58-bit-ternary-residual-flow-for-kv-cache-e46a2f0bb6f4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
