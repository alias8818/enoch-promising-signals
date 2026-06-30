# Queue-Pressure Adaptive Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-pressure-adaptive-speculative-decoding-c3ba1490928c`
Run ID: `queue-pressure-adaptive-speculative-decoding-c3ba1490928c-20260629T053144944353+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/95600b59db12

## What looked useful

Do not disable speculative decoding solely because queue pressure is high; in the simulator this collapses service capacity toward non-speculative decoding and worsens p95 latency. A practical controller should first measure the throughput-optimal speculative floor, then adapt only around that floor.

## Boundaries and scale limits

Proxy-only CPU simulation. No real target/draft model pair, no GPU serving kernels, no KV-cache memory pressure, no vLLM/SGLang/TensorRT-LLM integration, and no production arrival traces.

## Claim scope

In a synthetic continuous-batching queue simulator, queue-pressure adaptive speculative-depth control did not robustly dominate the best fixed speculative depth. Controllers that disabled speculation under backlog were harmful under overload; controllers preserving a k=2 speculative floor were competitive in some regimes but not consistently better than fixed k=2 or fixed k=4.

## Why it stopped

No-paper useful signal: synthetic evidence falsifies the naive pressure-to-zero controller but is not direct systems evidence for a paper.

## Recommended next action

Stop this proxy run and run a bounded real-serving follow-up in vLLM with a target/draft pair, dynamic arrivals, measured GPU/KV-cache telemetry, and controller variants that never drop below the measured throughput-optimal speculative depth.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: vLLM Queue-Pressure Speculative-Floor Controller Benchmark
- Success threshold: Adaptive speculative-floor policy improves p95 latency by at least 5% versus the best fixed-depth baseline in at least two dynamic-arrival regimes without reducing throughput by more than 2%.
- Stop condition: Stop if the adaptive speculative-floor policy fails to beat the best fixed-depth baseline on p95 latency in two independent arrival regimes or if GPU/KV telemetry shows adaptation overhead dominates.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-adaptive-speculative-decoding-c3ba1490928c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
