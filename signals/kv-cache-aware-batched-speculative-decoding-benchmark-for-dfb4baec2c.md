# KV-cache-aware batched speculative decoding benchmark for Qwen 0.5B draft and 1.5B target

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-aware-batched-speculative-decoding-benchmark-for-dfb4baec2c`
Run ID: `kv-cache-aware-batched-speculative-decoding-benchmark-for-dfb4baec2c-20260607T051758621168+0000`

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

- Parent run decision: Speculative Decoding with Local Small Model Drafts: enoch://control-plane/projects/speculative-decoding-with-local-small-model-drafts-70e2ad0bce03/runs/speculative-decoding-with-local-small-model-drafts-70e2ad0bce03-20260605T212258756566+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1fd369b1bf6e

## What looked useful

Single-prompt assisted decoding produced identical greedy output and a 4.20x tiny-smoke speedup, but true batch-4 assisted generation failed with ValueError: assisted generate is only supported for batch_size = 1. The practical sequential batch-1 assisted fallback matched outputs but averaged only 0.296x the throughput of target-only batch-4, about 3.38x slower.

## Boundaries and scale limits

Only 4 short prompts and up to 16 generated tokens per prompt were tested. No custom per-row KV-cache batched speculative decoder was implemented, and no long serving workload, batch-size sweep, or request-scheduler benchmark was run.

## Claim scope

Tier 1 controlled small direct test of the current Transformers 4.57.6 assisted-generation path for Qwen/Qwen2.5-0.5B-Instruct draft and Qwen/Qwen2.5-1.5B-Instruct target on one GB10 worker, with batch size 1 smoke and batch size 4 direct/fallback checks.

## Why it stopped

Proxy/full distinction: the run directly tested the supported Transformers cache-aware assisted path and directly falsified its batch-4 viability; it did not implement a custom full batched KV-cache speculative decoder.

## Recommended next action

Stop this off-the-shelf benchmark path; if continuing, implement or use a backend with true batched assisted decoding and per-row KV-cache accept/reject handling, then require exact greedy-output equivalence and at least 1.2x throughput over target-only batch-4 or batch-8.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Custom per-row KV-cache batched speculative decoder for Qwen 0.5B/1.5B
- Success threshold: On GB10, true batched assisted decoding for Qwen2.5 0.5B draft and 1.5B target must match target-only greedy outputs and reach at least 1.2x target-only throughput for batch size 4 or 8 with at least 32 generated tokens per prompt.
- Stop condition: Stop if exact per-row KV-cache correctness cannot be maintained, if batch-4 throughput remains below target-only after one bounded implementation pass, or if memory pressure prevents both models plus batch KV caches from fitting.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-aware-batched-speculative-decoding-benchmark-for-dfb4baec2c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
