# Adaptive Queue Depth Throttling for Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-queue-depth-throttling-for-local-serving-e76375461066`
Run ID: `adaptive-queue-depth-throttling-for-local-serving-e76375461066-20260530T032051069097+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8eee2585211c

## What looked useful

Across 630 policy/scenario/seed runs, unbounded queues caused high tail latency and badput under overload, while cap-16 throttling minimized badput in mild and bursty scenarios and tied the best adaptive variant in sustained overload. Adaptive variants helped versus unbounded admission but either lagged bursts or converged to the fixed cap.

## Boundaries and scale limits

Synthetic/proxy only; no real model server, GPU scheduler, tokenizer, network IO, production traces, or multi-model workloads were tested. Full validation requires direct serving benchmarks with real prompt/output length distributions and tuned fixed-cap controls.

## Claim scope

In a dependency-free discrete-event proxy for local batched serving with bursty arrivals and a 180 ms latency SLO, queue-depth throttling is useful versus unbounded admission, but latency-driven adaptive AIMD throttling does not improve on a conservative tuned fixed queue cap.

## Why it stopped

Proxy evidence is useful but not paper-ready, and the scoped adaptive-improvement hypothesis is not supported against the tuned fixed-cap control.

## Recommended next action

Stop this proxy run; a future bounded direct benchmark should compare adaptive throttling against a tuned fixed queue cap in a real local serving stack before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Local Serving Queue-Cap Benchmark
- Success threshold: Adaptive policy reduces badput by at least 10% relative to the best tuned fixed cap in at least two traffic regimes while keeping accepted completion throughput within 3%.
- Stop condition: Stop if the best adaptive policy fails to beat the tuned fixed cap by at least 5% badput in a smoke plus medium direct-serving benchmark, or if real-server overhead makes queue-depth control non-dominant compared with another bottleneck.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-queue-depth-throttling-for-local-serving-e76375461066`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
