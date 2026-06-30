# Real Scheduler Test of Depth-Gated Short-Context KV Priority

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-scheduler-test-of-depth-gated-short-context-kv-priori-9ef24acd3b`
Run ID: `real-scheduler-test-of-depth-gated-short-context-kv-priori-9ef24acd3b-20260620T050633321397+0000`

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

- Parent run decision: KV-Cache Pressure Routing: Short-Context Priority at Depth >=20: enoch://control-plane/projects/kv-cache-pressure-routing-short-context-priority-at-depth-20-bb146887e883/runs/kv-cache-pressure-routing-short-context-priority-at-depth-20-bb146887e883-20260620T043457377163+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c1d9a11bb32e

## What looked useful

Across 3 load points, 12 seeds, and 194400 simulated requests, depth-gated short-context KV priority passed the predeclared threshold: short p95 TTFT fell by about 99.97-99.98% versus FCFS, throughput did not regress, long p95 latency rose by less than 1% versus FCFS, and long p95 latency improved by 4.6-13.5% versus ungated short-context priority. Gate-depth diagnostics showed gate depth 0 loses the benefit, while depths 1-12 preserve near-immediate short TTFT.

## Boundaries and scale limits

Simulator-only Tier 1 evidence; no real GPU serving stack, no vLLM/SGLang/TGI integration, no real model kernel timing, no production trace, and no model-quality validation.

## Claim scope

In a controlled discrete-event decode scheduler simulation with mixed short/long contexts, finite batch slots, and prompt-length-dependent KV decode cost, depth-gated short-context priority reduced short-request p95 TTFT versus FCFS while keeping throughput and long-request p95 latency within the predeclared bounds.

## Why it stopped

Tier 1 controlled simulator produced a useful mechanism signal but is not paper-ready direct serving evidence.

## Recommended next action

Run a bounded deepen follow-up in a real inference serving harness, using the same mixed short/long workload and the same TTFT, throughput, long-latency, and fairness thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Serving Harness Test of Depth-Gated Short-Context KV Priority
- Success threshold: At two or more load points, reduce short-request p95 TTFT by at least 25% versus FCFS, keep throughput loss under 5%, keep long-request p95 latency increase under 15%, and improve long p95 latency or fairness relative to ungated short-context priority.
- Stop condition: Stop as unsupported if the real serving harness fails the short TTFT threshold at all load points or meets short TTFT only by exceeding the throughput or long-latency harm bounds.

## Evidence references

- Artifact root: `<local-path>/projects/real-scheduler-test-of-depth-gated-short-context-kv-priori-9ef24acd3b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
