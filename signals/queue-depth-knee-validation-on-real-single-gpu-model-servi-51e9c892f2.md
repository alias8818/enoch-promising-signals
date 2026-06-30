# Queue-depth knee validation on real single-GPU model serving traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-depth-knee-validation-on-real-single-gpu-model-servi-51e9c892f2`
Run ID: `queue-depth-knee-validation-on-real-single-gpu-model-servi-51e9c892f2-20260608T020253276813+0000`

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

- Parent run decision: Queue Depth Scheduling for Bounded GPU Worker Throughput: enoch://control-plane/projects/queue-depth-scheduling-for-bounded-gpu-worker-throughput-7c39fed74232/runs/queue-depth-scheduling-for-bounded-gpu-worker-throughput-7c39fed74232-20260607T214611877457+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7a12bd32f122

## What looked useful

Queue depth 8 reached >=95% of best observed throughput in both 80 rps and 120 rps sweeps. At 80 rps, depth 16 improved throughput only 1.6% over depth 8 while increasing p95 latency 48.6%. At 120 rps, depth 32 was slower than depth 16 and had substantially higher p95 latency.

## Boundaries and scale limits

Single host, one GPT-2-class model, in-process server, seeded Poisson arrivals, 192 requests per depth per load condition, no production trace, no standard vLLM/TGI/Triton server, no long-duration robustness or larger-model validation.

## Claim scope

A short local GPT-2 CUDA dynamic-batching service on one NVIDIA GB10 showed a stable queue-depth knee at depth 8 under two offered-load traces; deeper queues provided at most marginal throughput gain and sometimes increased p95 latency.

## Why it stopped

Tier 1 direct validation produced a useful mechanism signal but is not publication-grade because it used local synthetic arrivals and an in-process GPT-2 serving harness rather than production-like traces or a standard serving stack.

## Recommended next action

Run a bounded deepen validation with vLLM or TGI on the same GB10, three seeded arrival traces, and the same queue-depth knee rule before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standard-server queue-depth knee validation with repeated arrival traces
- Success threshold: The selected knee is stable within one queue-depth step across runs and a queue limit at the knee yields at least 25% lower p95 latency than deeper queue settings while retaining at least 95% of peak throughput.
- Stop condition: Stop if the standard-server runs show no stable knee across repeated traces or if deeper queue settings consistently improve throughput by more than 5% without a p95 latency penalty.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-knee-validation-on-real-single-gpu-model-servi-51e9c892f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
