# 1-bit weights with int8 residual channel for CPU inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `1-bit-weights-with-int8-residual-channel-for-cpu-inference-d985d2aaeee8`
Run ID: `1-bit-weights-with-int8-residual-channel-for-cpu-inference-d985d2aaeee8-20260525T064101079036+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/278e45695bb5

## What looked useful

The residual channel reduced binary-only RMSE, but bit+residual reached only 0.062x-0.526x of dense int8 throughput and retained 0.41-0.55 relative RMSE at tested residual densities; dense int8 stayed near 0.017-0.020 relative RMSE.

## Boundaries and scale limits

This run did not test trained transformer layers, perplexity, batched GEMM, or hand-written AVX-512 production kernels. It is a bounded kernel-level early falsification, not a full model validation.

## Claim scope

For synthetic CPU single-token matvec with int8 activations on this Xeon CPU, packed 1-bit sign weights plus a 1.56%-6.25% sparse int8 residual channel is slower and much less accurate than a simple per-row dense int8 weight baseline.

## Why it stopped

Proxy early falsification: the bounded CPU matvec benchmark directly tested the target inference kernel shape and found the proposed 1-bit plus int8 residual tradeoff slower and less accurate than dense int8.

## Recommended next action

Stop this paper path unless a new implementation supplies a production 1-bit x int8 CPU kernel and real transformer-layer quality evidence that directly overturns this proxy early falsification.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-weights-with-int8-residual-channel-for-cpu-inference-d985d2aaeee8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
