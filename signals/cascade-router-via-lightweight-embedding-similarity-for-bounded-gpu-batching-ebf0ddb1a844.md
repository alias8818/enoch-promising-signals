# Cascade Router via Lightweight Embedding Similarity for Bounded GPU Batching

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cascade-router-via-lightweight-embedding-similarity-for-bounded-gpu-batching-ebf0ddb1a844`
Run ID: `cascade-router-via-lightweight-embedding-similarity-for-bounded-gpu-batching-ebf0ddb1a844-20260607T102505230715+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2fe9114ac6a6

## What looked useful

Similarity routing was nearly oracle in clustered embeddings (route accuracy 0.997, purity 0.995) and became throughput-positive versus FIFO once clustered arrival rate reached 3600 req/s (+28.6%), 7200 req/s (+58.7%), and 14400 req/s (+80.1%). At 1800 req/s it lost 3.2% throughput despite high purity because per-route queues formed small batches. Moderate and diffuse embeddings lost about 31.8% and 30.3% throughput versus FIFO.

## Boundaries and scale limits

No real LLM cascade, production trace, model-quality metric, or measured GPU serving kernel was tested. GPU evidence is limited to a small Torch similarity-routing microbenchmark on NVIDIA GB10. The GPU service-time result is modeled, not measured end-to-end serving throughput.

## Claim scope

Synthetic bounded-wait batching with 16 route classes, 128-dimensional embeddings, prototype cosine-similarity routing, FIFO/hash/oracle controls, and modeled GPU service time. Similarity routing is useful only when embeddings strongly identify route and per-route arrival density is high enough to fill batches inside the wait bound.

## Why it stopped

This is a proxy/synthetic useful signal, not direct production validation; the hypothesis is conditionally supported under clustered high-arrival traffic but unsupported for moderate/diffuse route separability and sparse per-route traffic.

## Recommended next action

Run a bounded adaptive-router follow-up that estimates per-route fill rate and falls back to FIFO/coarser grouping when similarity queues cannot reach a target batch size before max_wait.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Similarity Router with Fill-Rate Fallback for Bounded Batching
- Success threshold: Adaptive routing must match or exceed FIFO modeled throughput within 2% in moderate/diffuse and low-arrival clustered settings, while retaining at least 80% of static similarity's throughput gain in clustered high-arrival settings.
- Stop condition: Stop if adaptive routing cannot avoid more than a 5% throughput loss versus FIFO in any sparse or weakly separable scenario, or if it erases more than half of the high-arrival clustered gain.

## Evidence references

- Artifact root: `<local-path>/projects/cascade-router-via-lightweight-embedding-similarity-for-bounded-gpu-batching-ebf0ddb1a844`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
