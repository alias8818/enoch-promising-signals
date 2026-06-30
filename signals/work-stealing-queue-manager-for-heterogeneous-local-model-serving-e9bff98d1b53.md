# Work-Stealing Queue Manager for Heterogeneous Local Model Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `work-stealing-queue-manager-for-heterogeneous-local-model-serving-e9bff98d1b53`
Run ID: `work-stealing-queue-manager-for-heterogeneous-local-model-serving-e9bff98d1b53-20260620T123552919520+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f2b1df03f253

## What looked useful

Work stealing improved static-affinity throughput by 1.77x to 2.79x and reduced static p95 latency by 77.8% to 99.2% across burst settings, including robustness to 2 ms and 5 ms per-stolen-request overhead. Centralized JSQ still had 1.7x to 2.5x lower p95 latency than work stealing in the same synthetic setup.

## Boundaries and scale limits

Synthetic 4-worker simulator only; no real LLM inference, GPU residency, batching, KV-cache behavior, or measured production trace replay. Medium runs used 5000 requests x 20 seeds per condition and completed as short CPU-only local simulations.

## Claim scope

In a deterministic synthetic discrete-event benchmark for heterogeneous local model-serving queues, work stealing from static-affinity local queues recovered most lost throughput and sharply reduced tail latency versus static affinity, but did not beat a centralized speed-aware shortest-queue baseline on tail latency.

## Why it stopped

Proxy-only simulator evidence supports work stealing as an imbalance rescue mechanism but is insufficient for publication-grade claims and does not outperform centralized JSQ on tail latency.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement a direct trace-replay harness on a real local-serving stack and keep JSQ as the primary latency baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace Replay Work-Stealing Scheduler for Real Local Model Serving
- Success threshold: Work stealing must reduce static-affinity p95 latency by at least 50%, keep throughput within 5% of JSQ, and avoid more than 10% extra model reload/cold-start events versus static affinity.
- Stop condition: Stop if real-serving work stealing fails to reduce static-affinity p95 latency by 25% in two representative traces, or if model reload/cold-start churn dominates the latency gains.

## Evidence references

- Artifact root: `<local-path>/projects/work-stealing-queue-manager-for-heterogeneous-local-model-serving-e9bff98d1b53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
