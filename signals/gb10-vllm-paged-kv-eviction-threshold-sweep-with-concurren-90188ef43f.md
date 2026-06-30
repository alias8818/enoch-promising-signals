# GB10 vLLM paged-KV eviction threshold sweep with concurrent prompt pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gb10-vllm-paged-kv-eviction-threshold-sweep-with-concurren-90188ef43f`
Run ID: `gb10-vllm-paged-kv-eviction-threshold-sweep-with-concurren-90188ef43f-20260605T201419251284+0000`

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

- Parent run decision: KV-cache eviction under GB10 queue pressure: enoch://control-plane/projects/kv-cache-eviction-under-gb10-queue-pressure-5c40b653ada2/runs/kv-cache-eviction-under-gb10-queue-pressure-5c40b653ada2-20260605T145139376639+0000
- Parent run decision: Direct GB10 paged-KV eviction test in a real serving stack: enoch://control-plane/projects/direct-gb10-paged-kv-eviction-test-in-a-real-serving-stack-1135178c4d/runs/direct-gb10-paged-kv-eviction-test-in-a-real-serving-stack-1135178c4d-20260605T173519525655+0000

## What looked useful

The practical threshold for this workload was between 16384 and 32768 KV tokens: preemptions fell from 5 at 16384 to 0 at 32768, and p95 latency improved from 1.113s to 0.788s, matching the 65536-token baseline at 0.780s. vLLM did not expose a named eviction-threshold knob, so this is useful capacity-pressure evidence, not paper-ready threshold-algorithm evidence.

## Boundaries and scale limits

Single GB10, one small OPT-125M-class model, one fixed seed, one prompt-pressure shape, and vLLM capacity controls rather than a source-level configurable eviction-threshold algorithm. Auto-capacity default was only smoke-tested because it consumed nearly all UMA memory.

## Claim scope

On a swapless GB10 host with vLLM 0.22.1, facebook/opt-125m, 48 fixed-seed completion requests at concurrency 12 and roughly 1536 prompt tokens/request, bounded paged-KV block capacity shows a clear pressure knee: 8192 and 16384 KV-token caps cause preemptions and worse latency, while 32768 KV tokens matches a 65536-token high-capacity baseline with zero preemptions.

## Why it stopped

Medium direct vLLM pressure sweep completed, but current vLLM exposes block-capacity controls rather than a named paged-KV eviction threshold, so the original mechanism is only partially tested and not paper-positive.

## Recommended next action

Stop this run as no-paper useful signal; a next bounded deepen should add or expose a real vLLM eviction-threshold control and repeat the sweep across at least three fixed seeds and a larger model/workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Instrument explicit vLLM paged-KV eviction thresholds under GB10 prompt pressure
- Success threshold: Across all seeds, an explicit threshold setting reduces preemptions to zero or near-zero and keeps p95 latency within 5% of the high-capacity baseline while using materially less KV capacity than the baseline.
- Stop condition: Stop if the explicit threshold cannot be exposed without invasive scheduler changes, if the effect disappears across seeds, or if the threshold setting does not beat the high-capacity baseline/resource tradeoff.

## Evidence references

- Artifact root: `<local-path>/projects/gb10-vllm-paged-kv-eviction-threshold-sweep-with-concurren-90188ef43f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
