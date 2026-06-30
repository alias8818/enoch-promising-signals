# Adaptive-draft speculative decoding under queue pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-draft-speculative-decoding-under-queue-pressure-91ad3a107ee9`
Run ID: `adaptive-draft-speculative-decoding-under-queue-pressure-91ad3a107ee9-20260611T050144787972+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2cab43e8fd26

## What looked useful

Adaptive pressure policies prevented collapse of fixed_k4/fixed_k8 under high offered load, reducing p95 latency by 81-99% versus fixed_k8 at 20-50 req/s and by 94% versus fixed_k4 at 50 req/s. However, adaptive_conservative was worse than fixed_k2 at every tested load and worse than the minimal k1 control at 50 req/s, so the broad adaptive-draft claim is not supported against tuned controls.

## Boundaries and scale limits

No real model execution, no GPU kernels, no continuous batching runtime, no KV-cache telemetry, hand-parameterized acceptance and cost model, 24 paired seeds per load point, four offered loads only.

## Claim scope

CPU-only synthetic discrete-event queueing simulation of adaptive speculative draft lengths under Poisson arrivals, heavy-tailed output lengths, stochastic acceptance, and batched verification cost. The result supports adaptive draft cutovers as overload protection against overly large fixed draft spans, but not as superior to tuned fixed/minimal draft controls.

## Why it stopped

Proxy early falsification rather than full validation: synthetic queueing evidence shows overload guardrail value but not superiority over tuned fixed/minimal policies.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should benchmark the same policies in a real continuous-batching speculative decoder and require adaptive control to beat per-load tuned fixed/minimal baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real continuous-batching benchmark for pressure-adaptive speculative draft length
- Success threshold: Adaptive policy achieves at least 10% lower p95 latency than the best fixed/minimal baseline at near-saturation or overload while keeping tokens/s within 2% of that baseline.
- Stop condition: Stop if adaptive fails to beat the best tuned fixed/minimal baseline on p95 latency in two consecutive load regimes or if throughput drops by more than 2% without a compensating p95 latency win.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-draft-speculative-decoding-under-queue-pressure-91ad3a107ee9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
