# Context-Adaptive Precision: Exact Anchors FP16, Spans INT3

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `context-adaptive-precision-exact-anchors-fp16-spans-int3-0bb9b6665c91`
Run ID: `context-adaptive-precision-exact-anchors-fp16-spans-int3-0bb9b6665c91-20260604T033753643712+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/79f886d5213e

## What looked useful

Anchor-residual stride 16 reduced attention relative L2 by 38.9% on synthetic KV and 28.3% on real distilgpt2 KV versus plain INT3, while retaining about 4.1x compression versus FP16. Stride 8 improved drift further at about 3.4x compression.

## Boundaries and scale limits

No end-to-end perplexity, generation-quality, latency-kernel, packing-overhead, large-model, or serving-system validation was run. Results are short GB10 PyTorch proxy tests, not publication-grade full validation.

## Claim scope

Bounded proxy evidence on synthetic AR(1) KV tensors and real distilgpt2 KV tensors shows FP16 exact anchors plus INT3 residual spans reduce attention-output drift versus plain per-vector INT3 at 3.4x to 4.6x estimated KV compression.

## Why it stopped

No-paper closure: bounded proxy evidence supports the mechanism, but this run did not produce end-to-end decoding, quality, or serving evidence required for a paper-positive result.

## Recommended next action

Run a direct autoregressive decoding-cache follow-up on GPT-2-small-class models with real packed 3-bit kernels, measuring perplexity, generation drift, decode latency, and memory bandwidth.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct decoding-cache validation for FP16 anchors plus INT3 residual spans
- Success threshold: At least 3.3x KV-cache compression, lower perplexity degradation than plain INT3 by at least 25%, lower attention-output relative L2 than plain INT3 by at least 25%, and decode throughput no worse than 10% below FP16 cache baseline after packing overhead is included.
- Stop condition: Stop if compressed-cache perplexity degradation is not materially better than plain INT3 or if packing/unpacking overhead erases the memory-bandwidth benefit.

## Evidence references

- Artifact root: `<local-path>/projects/context-adaptive-precision-exact-anchors-fp16-spans-int3-0bb9b6665c91`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
