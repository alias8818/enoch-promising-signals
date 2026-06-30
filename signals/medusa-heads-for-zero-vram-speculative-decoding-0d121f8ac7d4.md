# Medusa Heads for Zero-VRAM Speculative Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `medusa-heads-for-zero-vram-speculative-decoding-0d121f8ac7d4`
Run ID: `medusa-heads-for-zero-vram-speculative-decoding-0d121f8ac7d4-20260524T041309431334+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e3b3d8e8ad10

## What looked useful

The CPU head path is the binding bottleneck: 4 CPU full-vocabulary heads plus hidden transfer took 23.2403 ms, while cached target decoding took 1.8874 ms/token. Even oracle-perfect 4-head acceptance could emit at most 5 tokens per iteration, but the measured iteration cost requires 13.53 emitted tokens to break even.

## Boundaries and scale limits

This is a small proxy, not production Medusa training or large-model serving. It does not rule out larger target models, tree attention, quantized or candidate-restricted CPU heads, or better-trained auxiliary heads. It directly rules out the tested naive full-vocabulary CPU-head path for GPT-2-class latency.

## Claim scope

Early local falsification of naive zero-VRAM speculative decoding using CPU-resident full-vocabulary linear Medusa-style heads with a distilgpt2 target on GB10. The calibrated 4-head probe measured mean greedy acceptance of 0.28125 draft tokens and estimated throughput of 0.0947x cached greedy baseline.

## Why it stopped

Proxy early falsification: the tested zero-VRAM CPU full-vocabulary heads are both too inaccurate and too slow to improve a GPT-2-class GPU-served target, and the perfect-acceptance speed ceiling remains below baseline.

## Recommended next action

Stop this project as no-paper useful negative evidence; a separate bounded follow-up should test candidate-restricted or low-rank CPU heads with an explicit overhead target below 3 ms.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Candidate-restricted CPU Medusa heads for zero-VRAM speculative decoding
- Success threshold: CPU hidden-transfer plus head inference below 3 ms, mean accepted draft tokens above 1.5 for 4 heads, and estimated speedup_vs_baseline greater than 1.05 on at least 64 held-out contexts.
- Stop condition: Stop if CPU head latency remains above 6 ms or mean accepted draft tokens remains below 1.0 after a calibrated local run, because the path cannot plausibly beat the measured baseline.

## Evidence references

- Artifact root: `<local-path>/projects/medusa-heads-for-zero-vram-speculative-decoding-0d121f8ac7d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
