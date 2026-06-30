# Extreme Quantization Agent Memory Architecture Test

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-quantization-agent-memory-architecture-test-f4744b0ea776`
Run ID: `extreme-quantization-agent-memory-architecture-test-f4744b0ea776-20260610T202335291873+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fb7c04855f43

## What looked useful

Int4 key storage achieved 7.76x compression versus fp32 with top-1 recall 0.7966 at the hardest noise setting versus 0.8088 for fp32. Ternary 2-bit fell to 0.6372 and binary 1-bit fell to 0.4296 at the same setting, showing that more extreme key quantization has a clear interference/noise failure mode.

## Boundaries and scale limits

Synthetic key lookup only; no real LLM-agent traces, learned embeddings, online memory updates, value compression, packed quantized retrieval kernels, long-running persistence tests, or end-to-end agent task metrics. Runtime numbers are not a packed-kernel throughput claim because quantized keys were dequantized for scoring.

## Claim scope

On a synthetic clustered episodic-memory retrieval benchmark with 20,000 normalized 256-dimensional keys and noisy lookup queries, 4-bit per-vector quantized memory keys preserved dense nearest-neighbor recall closely, while 2-bit ternary and 1-bit sign keys degraded sharply under high query noise/interference.

## Why it stopped

Bounded synthetic evidence is useful but proxy-only for agent memory architecture; it supports int4 key compression and early-falsifies 2-bit/1-bit robustness under hard synthetic interference, not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use real agent-memory embeddings or task traces and require int4 to stay within 2 percentage points of dense recall while measuring packed-kernel memory/latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace int4 agent memory retrieval validation
- Success threshold: Int4 top-1 recall no more than 0.02 absolute below dense on the hardest evaluated interference condition, with at least 7x stored-key compression and no latency regression in a packed or production-relevant retrieval path.
- Stop condition: Stop if int4 loses more than 0.05 absolute top-1 recall versus dense on real traces, or if packed retrieval cannot show a memory/latency advantage over dense/fp16 retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-quantization-agent-memory-architecture-test-f4744b0ea776`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
