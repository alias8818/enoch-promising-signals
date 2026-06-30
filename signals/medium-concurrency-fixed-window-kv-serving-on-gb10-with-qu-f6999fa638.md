# Medium concurrency fixed-window KV serving on GB10 with quality guardrails

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `medium-concurrency-fixed-window-kv-serving-on-gb10-with-qu-f6999fa638`
Run ID: `medium-concurrency-fixed-window-kv-serving-on-gb10-with-qu-f6999fa638-20260610T192458380454+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-model fixed-window KV serving under GB10 memory pressure: enoch://control-plane/projects/real-model-fixed-window-kv-serving-under-gb10-memory-press-39d3736649/runs/real-model-fixed-window-kv-serving-under-gb10-memory-press-39d3736649-20260610T190441445218+0000
- Parent run decision: Bounded KV-Cache Pressure for Memory-Constrained GPU Workers: enoch://control-plane/projects/bounded-kv-cache-pressure-for-memory-constrained-gpu-workers-fb2cbe81ca54/runs/bounded-kv-cache-pressure-for-memory-constrained-gpu-workers-fb2cbe81ca54-20260610T184427769184+0000

## What looked useful

True eviction windows had severe quality divergence: top-1 match vs full-KV ranged from 0.0256 to 0.1250 and guardrail fail rate ranged from 0.8824 to 0.9748. The no-eviction 432-token control matched full-KV exactly, supporting that the negative result comes from context eviction rather than benchmark inability to reproduce the baseline.

## Boundaries and scale limits

Single in-process batched decode harness, one 0.5B model, synthetic-but-task-like prompts, no production arrival process, no streaming cancellation, and no deployable online quality oracle. Throughput timing showed order/cache effects, so speedup claims are not publication-grade.

## Claim scope

On GB10 with Qwen2.5-0.5B-Instruct, concurrency 16, 384-token prompts, 48-token greedy decode, and seeds 11/17/23, hard fixed-window KV truncation during decode did not satisfy quality guardrails against a full-KV baseline.

## Why it stopped

Tier 2 direct medium validation falsified the quality threshold for hard fixed-window KV truncation; this is not a full production-serving validation, but the guardrail failure is large enough to close this branch as no-paper evidence.

## Recommended next action

Stop this hard fixed-window KV serving branch; only revisit with a distinct information-preserving mechanism such as sink-token retention or summary/retrieval state evaluated against the same full-KV quality guardrails.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/medium-concurrency-fixed-window-kv-serving-on-gb10-with-qu-f6999fa638`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
