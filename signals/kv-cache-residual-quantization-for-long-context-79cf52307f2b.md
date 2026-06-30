# KV Cache Residual Quantization for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-residual-quantization-for-long-context-79cf52307f2b`
Run ID: `kv-cache-residual-quantization-for-long-context-79cf52307f2b-20260528T141754886093+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9eafc81d5e7c

## What looked useful

Ultra-compact RVQ failed early, but matched-rate RVQ showed a strong fidelity mechanism: on real distilgpt2 KV rows, rvq8x256 at 1 payload bit/dim reached attention relative MSE 0.0061 versus scalar4 at 4 bits/dim with 0.0107, while rvq16x256 at 2 payload bits/dim reached 0.0007. This is useful as a bounded mechanism signal, not a paper-ready validation.

## Boundaries and scale limits

No native long-context model, no end-to-end perplexity or generation benchmark, no serving latency measurement, and RVQ codebooks were fit to the same cache rows being evaluated. Codebook overhead is large at 768 GPT-2 tokens and only becomes attractive if amortized over much longer contexts or shared codebooks.

## Claim scope

On synthetic long-context-like KV rows and real distilgpt2 middle-layer KV rows, residual vector quantization with enough stages preserves sampled attention outputs better than row-wise scalar quantization at matched payload bits per dimension, but ultra-low-rate RVQ is not viable.

## Why it stopped

Closed as no-paper useful signal: local KV and attention metrics support the mechanism at matched payload, but deployment-critical codebook overhead, fitting policy, held-out generalization, and end-to-end long-context quality remain unvalidated.

## Recommended next action

Run a bounded deepen test with held-out or shared RVQ codebooks plus end-to-end perplexity on a small long-context-capable model; stop this run because the current evidence is not publication-grade.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out RVQ Codebooks for Long-Context KV Cache
- Success threshold: At equal effective bits per dimension including codebooks, held-out RVQ improves attention-output relative MSE or next-token KL by at least 25% over the best scalar baseline and does not add more than 10% decode-time overhead in the measured setting.
- Stop condition: Stop if held-out RVQ loses its advantage after codebook overhead is included, or if decode overhead exceeds the memory savings at the tested context lengths.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-residual-quantization-for-long-context-79cf52307f2b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
