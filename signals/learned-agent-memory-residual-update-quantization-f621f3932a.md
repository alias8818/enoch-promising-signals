# Learned Agent Memory Residual-Update Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `learned-agent-memory-residual-update-quantization-f621f3932a`
Run ID: `learned-agent-memory-residual-update-quantization-f621f3932a-20260614T004229125275+0000`

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

- Parent run decision: Quantized Residual Connections for Agent Memory Architecture: enoch://control-plane/projects/quantized-residual-connections-for-agent-memory-architecture-f99f05b6b1be/runs/quantized-residual-connections-for-agent-memory-architecture-f99f05b6b1be-20260613T212311999210+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fdc72ec0d6bc

## What looked useful

At 4 bits over 12 seeds and 12000 steps, residual-update quantization reduced MSE by 86.6% versus absolute-state quantization and residual-update quantization with error feedback reduced MSE by 97.0%, while improving sign accuracy by 4.8 and 7.2 percentage points respectively. A 3/4/6-bit sweep also passed the preregistered threshold.

## Boundaries and scale limits

Synthetic slot-memory workload only; no trained neural agent, language model, real trajectory memory, downstream benchmark, or large-scale serving/training validation.

## Claim scope

In a controlled slot-memory recurrent-update test with smooth residual writes, quantizing residual updates, especially with error feedback, preserves memory state substantially better than quantizing the full memory state after each update at equal bitwidth.

## Why it stopped

No-paper useful signal: the Tier 1 controlled direct mechanism test passed, but publication readiness requires learned-agent downstream evidence rather than synthetic slot-memory dynamics alone.

## Recommended next action

Run a bounded learned-memory benchmark that inserts absolute-state, residual-update, and residual-update-with-error-feedback quantizers into the same trained memory module and measures downstream task accuracy plus memory error.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned-memory downstream benchmark for residual-update quantization
- Success threshold: Residual-update with error feedback must improve downstream task accuracy by at least 2 percentage points or cut memory reconstruction error by at least 25% versus absolute-state quantization at equal bitwidth without increasing memory footprint.
- Stop condition: Stop if residual-update with error feedback fails to beat absolute-state quantization on both downstream accuracy and memory reconstruction error across the selected learned-memory task and at least two bitwidths.

## Evidence references

- Artifact root: `<local-path>/projects/learned-agent-memory-residual-update-quantization-f621f3932a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
