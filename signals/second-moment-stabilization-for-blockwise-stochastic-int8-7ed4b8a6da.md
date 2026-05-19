# Second-moment stabilization for blockwise stochastic int8 Adam states

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `second-moment-stabilization-for-blockwise-stochastic-int8-7ed4b8a6da`
Run ID: `second-moment-stabilization-for-blockwise-stochastic-int8-7ed4b8a6da-20260516T045242981212+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6eeb1383b126

## What looked useful

The run directly supports the mechanism that Adam v-state quantization needs denominator-aware stabilization: naive raw-v int8 can round small positive second moments to zero and immediately destabilize Adam, while sqrt-domain quantization with zero reserved for exact zeros prevents that failure in this controlled setting.

## Boundaries and scale limits

Evidence is limited to a Python reference optimizer, synthetic teacher-student regression, small MLP parameters, 600-step runs, and block sizes 64-1024. It does not validate real language-model training, production kernels, mixed precision, distributed runs, checkpoint behavior, memory bandwidth, or comparisons to mature 8-bit Adam implementations.

## Claim scope

On a deterministic small synthetic MLP regression task, raw blockwise stochastic int8 Adam second-moment states diverged within 5-8 steps, while sqrt-domain blockwise stochastic int8 second-moment states with a minimum active code completed 600 steps across 5 seeds with fp32-matched final eval loss and update cosine above 0.9995.

## Why it stopped

No-paper useful signal: Tier 1 direct mechanism evidence is positive, but it is synthetic small-model evidence and not sufficient for a paper or broad optimizer claim.

## Recommended next action

Run a bounded medium direct validation on a small transformer language-model task comparing fp32 Adam, raw int8 v, sqrt-stabilized int8 v, and a practical existing 8-bit Adam baseline with validation loss, update diagnostics, memory, and throughput metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer validation of sqrt-stabilized blockwise int8 Adam v states
- Success threshold: Sqrt-stabilized int8 v completes all planned runs, has mean validation loss or perplexity within 1% of fp32 Adam, maintains update cosine above 0.995 after warmup, and shows a measured v-state memory reduction; raw int8 either fails or is clearly worse on stability or update distortion.
- Stop condition: Stop as negative if sqrt-stabilized int8 v diverges in any repeated run, exceeds 1% validation loss or perplexity degradation versus fp32 Adam, or loses its advantage over an existing practical 8-bit Adam baseline.

## Evidence references

- Artifact root: `<local-path>/projects/second-moment-stabilization-for-blockwise-stochastic-int8-7ed4b8a6da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
