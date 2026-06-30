# KV-Cache Pressure Routing: Short-Context Priority at Depth >=20

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-pressure-routing-short-context-priority-at-depth-20-bb146887e883`
Run ID: `kv-cache-pressure-routing-short-context-priority-at-depth-20-bb146887e883-20260620T043457377163+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c1d9a11bb32e

## What looked useful

Across 12 seeds and three synthetic cache capacities, depth-gated short priority improved short mean latency by 9.30-9.84% and short p95 by 6.11-7.96% versus FIFO at identical throughput and 100% completion. Always-short priority improved short p95 by roughly 90-95% but worsened long p95 by 86-109%, showing a fairness risk that the depth-gated rule avoided in this proxy.

## Boundaries and scale limits

No real GPU serving stack, allocator, paged attention implementation, model outputs, production traces, multi-GPU routing, or live KV telemetry were tested. Capacity units and workload distribution are synthetic.

## Claim scope

In a deterministic synthetic 32-layer prefill simulator with reserved KV admission, bimodal prompt lengths, and high cache pressure, switching to short-context priority only for resident requests at depth >=20 improved short-request latency versus layer-wave FIFO without the long-tail blow-up caused by always-short priority.

## Why it stopped

Proxy-only simulator result supports the mechanism but is not direct serving-system evidence and is not publication-grade validation.

## Recommended next action

Stop this worker as no-paper useful-signal evidence; next, implement the policy family in a real inference scheduler on a 20+ layer model and measure request latency, KV allocation pressure, completion, and long-request fairness under mixed-context load.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Scheduler Test of Depth-Gated Short-Context KV Priority
- Success threshold: Short-request p95 latency improves by >=5% versus FIFO, throughput remains within 2% of FIFO, completion remains 100%, and long-request p95 is <=10% worse than FIFO.
- Stop condition: Stop if the live scheduler cannot reproduce at least a 5% short p95 improvement under pressure or if long-request p95 exceeds FIFO by more than 10% at matched throughput.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-pressure-routing-short-context-priority-at-depth-20-bb146887e883`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
