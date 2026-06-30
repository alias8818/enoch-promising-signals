# Semantic Affinity Router for KV-Cache Reuse

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `semantic-affinity-router-for-kv-cache-reuse-1fbb4b14ed89`
Run ID: `semantic-affinity-router-for-kv-cache-reuse-1fbb4b14ed89-20260621T115752187728+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6677ab870bb4

## What looked useful

Semantic affinity is useful as a secondary cold-placement hint, not as an independent KV-cache reuse mechanism. Exact prefix/cache-event awareness remains the dominant routing signal; semantic-only concentration can create load imbalance without valid cache hits.

## Boundaries and scale limits

No live LLM server, GPU KV allocator, tokenizer, batching scheduler, production traffic trace, or model-quality validation was run. Latency is a proxy simulation metric, not measured TTFT/TPOT.

## Claim scope

Synthetic discrete-event routing evidence shows semantic affinity can improve exact-prefix KV-cache locality over cache-oblivious routing only when semantic clusters predict repeated exact prefixes, but it does not beat exact-prefix-aware routing and can severely worsen latency under semantic-only or overcapacity workloads.

## Why it stopped

Closed as no-paper useful signal: proxy evidence supports a limited mechanism but falsifies semantic affinity as a standalone KV-cache reuse router and does not provide direct live-serving evidence.

## Recommended next action

Run a bounded live-serving follow-up on a tiny model with real prefix caching and two or more replicas, comparing exact-prefix, exact-plus-semantic, and load-aware semantic fallback on measured TTFT/TPOT and cache-hit telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Tiny-Model Validation of Exact-Plus-Semantic KV Routing
- Success threshold: Exact-plus-semantic improves token/cache hit rate by at least 15 percentage points over round-robin on clustered-template traffic, stays within 5% of exact-prefix-aware P95 TTFT, and causes less than 10% P95 TTFT regression versus round-robin on semantic-only-unique traffic.
- Stop condition: Stop if semantic fallback fails to improve hit rate over round-robin by 10 percentage points on clustered-template traffic or causes more than 20% P95 TTFT regression on semantic-only-unique traffic.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-affinity-router-for-kv-cache-reuse-1fbb4b14ed89`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
