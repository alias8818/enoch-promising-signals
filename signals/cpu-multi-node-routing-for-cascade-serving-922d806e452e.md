# CPU Multi-Node Routing for Cascade Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-multi-node-routing-for-cascade-serving-922d806e452e`
Run ID: `cpu-multi-node-routing-for-cascade-serving-922d806e452e-20260614T051013470931+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a505c71cd74a

## What looked useful

Load-aware CPU multi-node routing is worth testing in a real cascade-serving prototype, but the local evidence points to queue awareness as the main mechanism rather than a distinct cascade-specific routing advantage.

## Boundaries and scale limits

Synthetic-only evidence; no real model inference, physical multi-node networking, batching, production traces, or calibrated model confidence distributions. Scenarios used 4 synthetic nodes, 5,000 requests per seed, and 5 seeds.

## Claim scope

In a deterministic synthetic two-stage CPU cascade-serving simulator with four nodes, five seeds per scenario, and 75 requests/second offered load, queue-aware multi-node routing substantially reduced p95 latency versus single-node, sticky-local, and round-robin baselines. The cascade-specific network-aware variant did not materially improve over a simpler shortest-queue policy.

## Why it stopped

Synthetic simulation supports the routing mechanism but is insufficient for publication-grade claims, and the cascade-specific router only slightly beat shortest-queue in the high-network scenario.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should replay the same policies against an actual CPU-hosted two-stage service with measured service times and network latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Replayed CPU Cascade Routing Prototype
- Success threshold: At least 25% p95 latency reduction versus sticky-local at matched accuracy and load, plus at least 5% p95 improvement of network-aware cascade routing over shortest-queue in a high-network-cost condition.
- Stop condition: Stop if real-service measurements show less than 10% p95 improvement versus sticky-local or no measurable advantage over shortest-queue in the high-network-cost condition after three seeds or replay windows.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-multi-node-routing-for-cascade-serving-922d806e452e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
