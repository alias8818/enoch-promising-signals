# Speculative Decoding via Local Model Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-via-local-model-cascade-fdfc6eea042d`
Run ID: `speculative-decoding-via-local-model-cascade-fdfc6eea042d-20260527T122801364025+0000`

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

Cascade won in 75.8% of simulated cases and improved mean speedup from 2.412x to 2.620x over target-only cost, but performance was regime-dependent: at small draft cost 0.05 of target, cascade won only 41.7% of cases and had negative mean delta; at small/intermediate mismatch 0.50, mean delta was approximately zero.

## Boundaries and scale limits

No real LLM inference was run. Results are CPU-only, stationary-distribution simulations with modeled verifier batch costs, 864 grid cases, and 1,500 Monte Carlo outer iterations per case. Transformer latency, KV-cache behavior, prompt-conditioned distributions, and trained local draft quality remain untested.

## Claim scope

In a controlled categorical speculative decoding simulator, a two-level local cascade improves mean cost-normalized throughput over a single intermediate draft only when the small draft is cheap and close enough to the intermediate draft to keep inner acceptance high; it is not generally dominant across the tested grid.

## Why it stopped

Closed as no-paper useful signal because the evidence is a proxy simulator result: it supports a conditional mechanism but does not provide direct real-model serving evidence.

## Recommended next action

Run a bounded real-model follow-up with tiny or small transformer target/intermediate/small models, measured wall-clock latency, distribution-correct speculative verification, and matched single-draft controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model latency test for local cascade speculative decoding
- Success threshold: Cascade improves median tokens per second by at least 10% over the best single-intermediate speculative baseline on at least 100 prompts while preserving target-sampling correctness.
- Stop condition: Stop if inner acceptance is below 70% or cascade median tokens per second is not at least 5% above the single-intermediate baseline after the first 30 prompts.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-via-local-model-cascade-fdfc6eea042d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
