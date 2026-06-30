# Deadline-aware admission under real CUDA inference workload sweeps

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deadline-aware-admission-under-real-cuda-inference-workloa-86eb81ea1a`
Run ID: `deadline-aware-admission-under-real-cuda-inference-workloa-86eb81ea1a-20260613T114511130861+0000`

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

- Parent run decision: Queue admission policy under near-capacity gb10 lane: enoch://control-plane/projects/queue-admission-policy-under-near-capacity-gb10-lane-527f13858bd1/runs/queue-admission-policy-under-near-capacity-gb10-lane-527f13858bd1-20260613T105911856467+0000
- Parent run decision: Live GB10 deadline-aware admission under concurrent CUDA request dispatch: enoch://control-plane/projects/live-gb10-deadline-aware-admission-under-concurrent-cuda-r-88413a02f3/runs/live-gb10-deadline-aware-admission-under-concurrent-cuda-r-88413a02f3-20260613T112945130777+0000

## What looked useful

Across 90 policy-condition-seed runs using actual CUDA forward passes, deadline-aware admission reduced all-request miss rate by 0.7956 to 0.9060 absolute versus FIFO and EDF admit-all baselines, increased all-request deadline-success rate by 0.2880 to 0.5628 absolute, and kept admitted-success rates between 0.792 and 0.957 by rejecting infeasible requests.

## Boundaries and scale limits

Not production LLM serving evidence: no 7B+ model, no prefill/decode split, no KV-cache pressure, no live traffic traces, no network/HTTP serving path, no multi-GPU or multi-tenant deployment.

## Claim scope

In a single-GB10, single-process CUDA inference harness with seeded mixed-deadline Poisson arrivals, compact encoder-like PyTorch batches, 5 fixed seeds, 3 overload arrival rates, 2 deadline slack regimes, and FIFO/EDF admit-all baselines, EDF feasibility-based deadline admission reduced deadline misses and improved deadline-successful throughput under overload.

## Why it stopped

Tier-2 bounded validation supports the mechanism, but the result is not paper-positive because the direct CUDA workload is a compact synthetic inference harness rather than a production LLM serving stack.

## Recommended next action

Run a bounded deepen test on a local decoder-style inference stack with prefill/decode phases and KV-cache memory pressure, then compare against the same FIFO and EDF admit-all baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deadline-aware admission on local decoder-style CUDA inference with prefill/decode pressure
- Success threshold: Deadline-aware admission improves all-request deadline-success rate by at least 0.20 absolute versus both admit-all baselines in at least 4 of 6 overload conditions while keeping admitted-success rate at or above 0.80.
- Stop condition: Stop as unsupported if the decoder-style workload shows less than 0.10 absolute all-request deadline-success improvement versus either baseline in at least 4 of 6 conditions, or if the implementation cannot produce real CUDA prefill/decode timings locally.

## Evidence references

- Artifact root: `<local-path>/projects/deadline-aware-admission-under-real-cuda-inference-workloa-86eb81ea1a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
