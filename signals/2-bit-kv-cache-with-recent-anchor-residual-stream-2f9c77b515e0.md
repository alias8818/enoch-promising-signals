# 2-bit KV-cache with Recent/Anchor Residual Stream

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `2-bit-kv-cache-with-recent-anchor-residual-stream-2f9c77b515e0`
Run ID: `2-bit-kv-cache-with-recent-anchor-residual-stream-2f9c77b515e0-20260620T074752170669+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a258cba71a72

## What looked useful

A direct modified-past-key-values probe found anchor+recent residuals reduced mean KL from 0.3714 for all-2-bit cache to 0.00787 and restored top-1 agreement from 93.75% to 100% on a 192-token-prefix distilgpt2 test while retaining an estimated 26.5% fp16 KV memory ratio.

## Boundaries and scale limits

No packed 2-bit kernel, no actual KV memory allocation reduction, no throughput benchmark, no standard long-context corpus, no GPT-2-small/7B+ model validation, and optimistic memory accounting excludes quantization metadata.

## Claim scope

On distilgpt2 with 6 synthetic prompt templates, 96 or 192 token prefills, and 16 teacher-forced continuation tokens, preserving 16 full-precision anchor and 16 recent KV positions reduced logit drift from an otherwise 2-bit min/max KV cache compared with all-2-bit quantization, especially at 192-token prefix length.

## Why it stopped

Bounded local evidence supports the mechanism but is insufficient for a paper because it is a small proxy/logit-drift probe without packed 2-bit serving, broad benchmarks, or larger-model validation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should implement faithful packed-cache accounting and evaluate recent-only versus anchor+recent on a standard long-context or perplexity benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed-accounting long-context KV residual validation
- Success threshold: At matched KV memory ratio within 5 percentage points, anchor+recent must reduce mean KL or perplexity degradation by at least 20% versus recent-only on tasks with early-anchor dependencies while preserving decode top-1 agreement within 1 percentage point of fp16.
- Stop condition: Stop if anchor+recent fails to beat recent-only at matched memory on two standard tasks or if metadata overhead removes most of the claimed memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-recent-anchor-residual-stream-2f9c77b515e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
