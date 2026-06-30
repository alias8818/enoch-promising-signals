# Queue-Pressure Adaptive Spec Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `queue-pressure-adaptive-spec-decoding-2a2894c921a0`
Run ID: `queue-pressure-adaptive-spec-decoding-2a2894c921a0-20260602T113220818360+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/250464260a3e

## What looked useful

A tuned fixed speculative depth, k=4, dominated the main simulation sweep; hand-written pressure-adaptive policies were 14.8-35.1% worse on p95 than the best fixed depth, and an exhaustive paired-randomness queue-map grid found only exact ties or sub-0.5% p95 changes.

## Boundaries and scale limits

No real LLM server, GPU decode kernels, batching implementation, KV-cache telemetry, production traffic trace, or measured draft/target acceptance distribution was tested.

## Claim scope

Bounded CPU-only discrete-event simulation of online speculative decoding with fixed-depth, hand-written queue-pressure, acceptance-aware, and exhaustive simple queue-map policies.

## Why it stopped

Proxy simulation does not support the queue-pressure-only mechanism as a meaningful improvement over a tuned fixed speculative depth; this is an early falsification, not full validation.

## Recommended next action

Stop this run as a no-paper simulation negative; only reopen with direct small-model serving evidence that queue-pressure adaptation beats a tuned fixed depth by at least 5% p95 at matched throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-Model Serving Test for Queue-Pressure Speculative Depth
- Success threshold: Queue-pressure adaptive policy improves p95 latency by >=5% versus the best tuned fixed depth at matched throughput, without worsening p99 latency by more than 2%.
- Stop condition: Stop if the adaptive policy fails to beat the best fixed depth by 5% p95 on two replayed arrival traces or if GPU/KV telemetry shows the policy is only changing load without improving service efficiency.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-adaptive-spec-decoding-2a2894c921a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
