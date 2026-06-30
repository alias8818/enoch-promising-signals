# Queue-Pressure-Adaptive Speculative Draft Batcher

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-pressure-adaptive-speculative-draft-batcher-62de988722e8`
Run ID: `queue-pressure-adaptive-speculative-draft-batcher-62de988722e8-20260613T085325283477+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/22a04b86cca6

## What looked useful

Naive queue-pressure-only adaptive draft length did not beat best fixed-k baselines. Best adaptive p95 latency matched fixed_k8 under steady load, was effectively tied under near saturation, was 0.92% worse under overloaded load, and was 4.66% worse than fixed_k4 under bursty pressure. Throughput deltas versus best fixed policy were effectively zero. Aggressive pressure thresholds shortened drafts too much and substantially worsened p95 latency.

## Boundaries and scale limits

Proxy simulation only; no real GPU inference, model-pair acceptance traces, KV-cache pressure, kernel scheduling, production admission control, or hardware utilization measurements. Medium run used 4 workloads x 6 policies x 10 seeds x 2500 requests.

## Claim scope

Dependency-free discrete-event simulation of speculative decoding request scheduling with fixed draft-token budget, synthetic arrivals, fixed acceptance probability, and fixed/adaptive draft-length policies across steady, near-saturation, overloaded, and bursty workloads.

## Why it stopped

The local proxy produced useful negative/mixed evidence: pressure-only adaptive policies failed to materially improve p95 latency or throughput over tuned fixed-k baselines, so the idea is not paper-ready from this evidence.

## Recommended next action

Stop this run as a proxy early falsification of naive queue-pressure-only adaptation; a bounded follow-up should test acceptance-aware adaptive control on real or trace-derived speculative decoding data.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Acceptance-aware adaptive speculative draft control on trace replay
- Success threshold: Across at least three trace-derived workloads, acceptance-aware adaptive control must improve p95 latency by >=5% versus the best fixed-k baseline while keeping throughput within 1% and not increasing wasted draft tokens by more than 10%.
- Stop condition: Stop if adaptive control fails to beat best fixed-k p95 latency by 5% on two workloads or requires oracle future knowledge unavailable to an online scheduler.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-adaptive-speculative-draft-batcher-62de988722e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
