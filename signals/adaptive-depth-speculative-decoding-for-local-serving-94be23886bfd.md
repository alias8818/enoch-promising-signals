# Adaptive-Depth Speculative Decoding for Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-depth-speculative-decoding-for-local-serving-94be23886bfd`
Run ID: `adaptive-depth-speculative-decoding-for-local-serving-94be23886bfd-20260524T202518492455+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b5ed284b6fb1

## What looked useful

Adaptive depth produced 1.802x mean speedup versus target-only and improved mean cost by 1.316% versus the best single global fixed depth, but still had 2.323% mean regret versus a per-request oracle fixed-depth choice and lost materially on stationary high/mid acceptance regimes.

## Boundaries and scale limits

No real model inference, no GPU kernels, no production serving engine, no batching or queueing, no KV-cache memory pressure, and no measured target/draft acceptance from real prompts.

## Claim scope

Synthetic local-serving cost simulator with 8 acceptance-regime scenarios, 128 seeds per scenario, 8192 emitted tokens per seed, fixed depths 1-16, and an EWMA adaptive-depth controller.

## Why it stopped

Proxy simulator produced a useful mixed signal but not direct serving evidence; this closes as no-paper evidence rather than full validation.

## Recommended next action

Run a bounded real-model follow-up using a small target/draft pair and live prompt traces to measure acceptance, latency, and throughput for fixed depth versus the same adaptive controller.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model adaptive-depth speculative decoding smoke and medium validation
- Success threshold: Adaptive throughput is at least 3% higher than the best single global fixed depth overall, has no more than 3% regret on stable high-acceptance prompts, and does not increase p90 latency by more than 5%.
- Stop condition: Stop if adaptive depth fails to beat the best single global fixed depth overall or shows more than 10% regret on stable high-acceptance prompts after a smoke plus medium run.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-depth-speculative-decoding-for-local-serving-94be23886bfd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
