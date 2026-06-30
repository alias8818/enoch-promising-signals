# Residual-Channel KV-Cache Compression for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-kv-cache-compression-for-long-context-266cc595b8c4`
Run ID: `residual-channel-kv-cache-compression-for-long-context-266cc595b8c4-20260601T030451090558+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4ec8f6b79033

## What looked useful

Residual-channel selection consistently beat random-channel preservation at matched keep fractions; 3-bit plus 25% fp16 channels improved mean NLL from 4.015 random to 3.949 residual, while full fp16 cache was 3.682. The mechanism is real enough to justify a bounded long-context follow-up but not enough for a paper.

## Boundaries and scale limits

Single GPT-2-class model, 1024-position architecture, 24 validation spans, simulated dequantized cache rather than packed serving kernels, one random-channel draw, no 2k-8k long-context model, no latency or memory-bandwidth benchmark.

## Claim scope

In a distilgpt2 WikiText-2 KV-cache perturbation probe with 768-token prefixes, preserving high-energy residual channels at fp16 while quantizing remaining KV channels to 2 or 3 bits produced lower continuation NLL than preserving random channels at the same channel fraction.

## Why it stopped

Current result is a small-model proxy useful signal, not full long-context validation or a packed serving result.

## Recommended next action

Run a bounded deepen follow-up on a small RoPE long-context model with 2k-8k contexts, multiple random-channel draws, packed-cache memory accounting, and retrieval plus NLL metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-Channel KV Compression on a Small RoPE Long-Context Model
- Success threshold: Residual-channel compression must improve mean NLL by at least 0.03 over random-channel preservation at matched budget, match or exceed retrieval accuracy of uniform quantization, and show an actual cache-memory reduction of at least 2x versus fp16 without severe latency regression.
- Stop condition: Stop if residual-channel selection fails to beat random-channel preservation at matched memory on two prefix lengths or if packed-cache overhead erases the intended memory savings.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-kv-cache-compression-for-long-context-266cc595b8c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
