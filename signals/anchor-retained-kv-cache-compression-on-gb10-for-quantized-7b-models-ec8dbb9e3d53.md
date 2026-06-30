# Anchor-Retained KV Cache Compression on gb10 for Quantized 7B Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-retained-kv-cache-compression-on-gb10-for-quantized-7b-models-ec8dbb9e3d53`
Run ID: `anchor-retained-kv-cache-compression-on-gb10-for-quantized-7b-models-ec8dbb9e3d53-20260630T152133738720+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e261507cbe2

## What looked useful

Anchor retention is conditionally useful: moderate-anchor traces reduced relative L2 output error from about 1.0008 for recent-only to about 0.0380 for anchor+recent at the same 1024-token budget, close to the oracle top-mass control at about 0.0226. In the no-anchor control, anchor+recent was worse than recent-only, increasing relative L2 from about 0.0016 to about 0.2625.

## Boundaries and scale limits

No real quantized 7B checkpoint, tokenizer, generation loop, downstream task, or serving stack was tested. Evidence is limited to synthetic KV traces, one-step attention, 4096-token contexts, 1024-token retained budgets, and memory arithmetic for a 32-layer 32-head head_dim-128 model shape.

## Claim scope

On GB10, a synthetic single-step GPU attention proxy with Llama-7B-shaped KV tensors shows that static anchor+recent retention preserves full-cache attention outputs far better than recent-only when early anchor tokens carry attention mass, but is worse than recent-only when anchor tokens carry no useful mass.

## Why it stopped

The result is a bounded synthetic proxy, not direct quantized-7B model evidence; it supports a mechanism and a control condition but cannot validate end-to-end generation quality or serving performance.

## Recommended next action

Stop this worker run as a no-paper useful signal; next, implement the same anchor+recent policy inside a locally runnable quantized 7B inference path and test long-context retrieval/perplexity against recent-only and an attention-mass baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Quantized 7B Anchor-Retained KV Cache Evaluation on GB10
- Success threshold: Anchor+recent must improve retrieval accuracy or perplexity over recent-only by a practically meaningful margin at the same KV budget while keeping decode throughput within 10% of recent-only.
- Stop condition: Stop if anchor+recent does not beat recent-only on direct model quality metrics, or if throughput/memory overhead exceeds the 10% budget without a compensating quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-retained-kv-cache-compression-on-gb10-for-quantized-7b-models-ec8dbb9e3d53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
