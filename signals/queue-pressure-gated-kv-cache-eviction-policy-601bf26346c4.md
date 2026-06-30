# Queue-Pressure-Gated KV Cache Eviction Policy

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `queue-pressure-gated-kv-cache-eviction-policy-601bf26346c4`
Run ID: `queue-pressure-gated-kv-cache-eviction-policy-601bf26346c4-20260528T111915613590+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b486f625560c

## What looked useful

Queue pressure alone is not a sufficient eviction gate: once sustained backlog keeps pressure high, QPG repeatedly evicts partially served requests, generating about 5.56M recompute tokens and completing only 44.5 requests on average versus 2019.75 for never-evict in the medium run.

## Boundaries and scale limits

Synthetic CPU-only simulator; no real model kernels, no production trace replay, no vLLM/TGI/SGLang integration, and no hardware latency measurements.

## Claim scope

In a bounded synthetic discrete-event serving simulator, naive queue-pressure-gated active KV eviction under sustained bursty memory pressure caused recomputation thrash and much lower completed-request throughput than never-evict.

## Why it stopped

Proxy/early falsification in a direct mechanism simulator: QPG completed only 2.2% of never-evict throughput and produced millions of recompute tokens, so this is not a full validation and not paper-ready.

## Recommended next action

Stop paper path for the naive policy; only test a progress-protected, cooldown-limited QPG variant if a follow-up is opened.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anti-thrash queue-pressure KV eviction with progress protection
- Success threshold: At least 90% of never-evict completed throughput, at least 25% lower p95 TTFT than never-evict, and recompute tokens below 10% of total generated work on the bounded simulator.
- Stop condition: Stop if the protected variant completes below 80% of never-evict throughput or still accumulates million-scale recompute tokens in the 8-seed medium simulator.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-gated-kv-cache-eviction-policy-601bf26346c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
