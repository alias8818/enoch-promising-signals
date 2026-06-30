# Dynamic Quantization Routing for Lane Feed Pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-quantization-routing-for-lane-feed-pressure-3bba0dac5fe2`
Run ID: `dynamic-quantization-routing-for-lane-feed-pressure-3bba0dac5fe2-20260527T122344548392+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/526badc83053

## What looked useful

Measured fp16 median service was 0.179 ms, while int8/int4 PyTorch quantization proxies were about 4.7x slower. Using those measured service times, pressure_dynamic p99 latency rose from 0.945 ms to 5540 ms. In an idealized fused-low-bit model using the same error costs, pressure_dynamic reduced p99 latency by 21.8% with mean quality cost 0.00019, showing the routing mechanism is conditional on truly faster low-bit kernels.

## Boundaries and scale limits

No end-to-end transformer serving, no fused production int8/int4 backend, no language-task quality metric, no KV-cache or dynamic batching integration, and no multi-GPU/datacenter validation.

## Claim scope

On a GB10 PyTorch matmul proxy plus bursty four-lane queue simulation, pressure-aware quantization routing only helps when the lower-bit route is modeled as a genuinely faster fused service path; the directly measured unfused PyTorch quantization proxies are slower than fp16 and make pressure routing much worse.

## Why it stopped

Mixed proxy result: direct measured low-bit routes violate the speed premise, while idealized fused service suggests only conditional promise; this is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should integrate a real fused quantized inference backend and compare pressure-aware routing against fp16 on task-level quality and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused-kernel dynamic quantization routing in a real inference backend
- Success threshold: p99 latency improves by at least 15% over fp16_only under bursty load and task-level quality degrades by less than 1% relative to fp16.
- Stop condition: Stop negative if fused low-bit service is not faster than fp16 for the target model shapes or if latency gains require more than 1% task-quality loss.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-quantization-routing-for-lane-feed-pressure-3bba0dac5fe2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
