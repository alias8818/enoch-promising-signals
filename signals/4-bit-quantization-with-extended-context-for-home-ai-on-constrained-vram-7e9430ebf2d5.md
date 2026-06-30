# 4-bit quantization with extended context for home AI on constrained VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-quantization-with-extended-context-for-home-ai-on-constrained-vram-7e9430ebf2d5`
Run ID: `4-bit-quantization-with-extended-context-for-home-ai-on-constrained-vram-7e9430ebf2d5-20260611T100833888027+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/29ac784301c8

## What looked useful

KV-cache memory becomes the dominant footprint after weight-only 4-bit quantization. For a 7B MHA profile, bf16 KV cache is 4 GiB at 8k, 16 GiB at 32k, 32 GiB at 64k, and 64 GiB at 128k, making common constrained-VRAM targets sharply context-limited. For an 8B GQA profile, KV cache is one quarter as large: 1 GiB at 8k, 4 GiB at 32k, 8 GiB at 64k, and 16 GiB at 128k. Decode attention latency in the probe roughly doubled with each context doubling.

## Boundaries and scale limits

No real 4-bit model was served end-to-end; no tokenizer/model download, perplexity, retrieval, prefill, batching, offload, or consumer discrete-GPU run was performed. CUDA allocation probes validate KV-cache tensor sizes on GB10 UMA, not exact usable VRAM on 8/12/16/24 GiB cards. Attention timing is a decode-style microbenchmark, not full model latency.

## Claim scope

On a GB10 CUDA host, analytic budgets and direct KV-cache tensor allocations for 7B/8B-class model profiles show that 4-bit weight quantization helps base-model fit but does not by itself enable extended context under constrained memory; KV-cache size and attention cost dominate as context grows. The strongest bounded positive signal is for GQA 8B-class profiles, where 4-bit weights plus reduced KV heads can make 32k-64k memory-feasible under 16-24 GiB assumptions, subject to untested serving overhead and quality.

## Why it stopped

Bounded direct-mechanism and proxy evidence falsifies the broad weight-only claim but does not replace full end-to-end serving validation.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded direct test is end-to-end serving of a real 4-bit GQA 7B/8B model at 8k, 32k, and 64k contexts with measured peak memory, tokens/s, and quality on a 24 GiB-class target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end 4-bit GQA long-context serving on a 24 GiB memory budget
- Success threshold: 32k context completes without OOM under the 24 GiB budget, decode remains at or above 8 tokens/s for single-user generation, and quality/task success is within 5% absolute of the 8k baseline on the selected suite.
- Stop condition: Stop if 32k cannot run under the 24 GiB budget, if decode falls below 4 tokens/s, or if task quality drops more than 10% absolute versus the 8k baseline.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-quantization-with-extended-context-for-home-ai-on-constrained-vram-7e9430ebf2d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
