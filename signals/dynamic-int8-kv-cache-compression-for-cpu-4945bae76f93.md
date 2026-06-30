# Dynamic INT8 KV-Cache Compression for CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-int8-kv-cache-compression-for-cpu-4945bae76f93`
Run ID: `dynamic-int8-kv-cache-compression-for-cpu-4945bae76f93-20260526T044111373921+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ff40aea468c3

## What looked useful

Dynamic INT8 KV-cache compression is useful for CPU memory capacity and has a plausible long-context single-thread latency benefit, with about 0.8-1.0% synthetic output relative L2 error and about 2 us/token-pair quantization overhead at d=128. It should not be claimed as an end-to-end CPU serving speedup without a tuned multithreaded kernel and model-level validation.

## Boundaries and scale limits

No real LLM integration, no perplexity/task-quality measurement, no multi-layer/multi-head runtime scheduling, no tuned VNNI/AMX production kernel, and context scale limited to 16,384 synthetic tokens on one CPU worker.

## Claim scope

Synthetic CPU decode microbenchmark at d=128 shows per-token dynamic INT8 K/V cache storage reduces memory footprint by 3.88x and can speed up naive single-thread long-context attention after about 4096 cached tokens, but the tested OpenMP multithread path is mostly neutral and not a broad CPU serving win.

## Why it stopped

Synthetic microbenchmark evidence supports memory savings and a limited long-context single-thread mechanism, but the multithreaded and model-level evidence needed for a paper or broad serving claim is absent.

## Recommended next action

Stop this run as a no-paper useful signal; next, test a bounded model-integrated CPU decode path on a small transformer with real tokens/sec and perplexity controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-integrated CPU INT8 KV-cache decode validation
- Success threshold: At 8k or longer context, demonstrate at least 1.2x end-to-end decode tokens/sec improvement or at least 3.5x measured KV memory reduction with no more than 1% perplexity regression on the bounded evaluation set.
- Stop condition: Stop if real-model quality regression exceeds 1% perplexity at 8k context or if end-to-end decode speed is not improved and the only benefit is already-known memory compression.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-int8-kv-cache-compression-for-cpu-4945bae76f93`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
