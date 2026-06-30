# Stabilized sparse 8-bit Adam state with real small-model convergence check

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `stabilized-sparse-8-bit-adam-state-with-real-small-model-c-410cdc6d22`
Run ID: `stabilized-sparse-8-bit-adam-state-with-real-small-model-c-410cdc6d22-20260522T102304594496+0000`

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

- Parent run decision: CPU-Offloaded Dynamic Sparse 8-bit Optimizer: enoch://control-plane/projects/cpu-offloaded-dynamic-sparse-8-bit-optimizer-f3035350a459/runs/cpu-offloaded-dynamic-sparse-8-bit-optimizer-f3035350a459-20260522T093044403740+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/97c0e59c9136

## What looked useful

A second-moment dequantization floor was necessary for numerical stability. With that stabilization, sparse 8-bit Adam state at 25% density matched Adam32 mean test accuracy within 0.044 percentage points using 18.8% of modeled optimizer-state bytes; 10% density stayed within 0.311 percentage points using 7.5% of state bytes but had higher train loss.

## Boundaries and scale limits

Single small handwritten-digit dataset, single MLP architecture, CPU NumPy prototype, analytical state-byte model, no production sparse checkpoint/restart test, no transformer/CNN/language-model validation, and no runtime-speed claim.

## Claim scope

On a NumPy 64-128-10 MLP trained on sklearn.load_digits for 60 epochs across 5 seeds, stabilized sparse 8-bit Adam state preserved mean test accuracy within 0.31 percentage points of Adam32 while using 7.5% to 18.8% of modeled Adam32 optimizer-state bytes.

## Why it stopped

Tier 1 direct small-model validation completed and produced a useful mechanism signal, but evidence remains too narrow and prototype-level for publication readiness.

## Recommended next action

Run one bounded deepen test on a real small transformer language-model or CNN workload with serialized sparse optimizer-state measurement and checkpoint resume fidelity before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Serialized sparse 8-bit Adam state on a small transformer or CNN convergence task
- Success threshold: Sparse 8-bit state reaches final validation accuracy or perplexity within 1 percentage point or equivalent relative metric tolerance of Adam32, uses at least 4x less serialized optimizer-state storage, and checkpoint resume changes the next validation metric by less than 0.2 percentage points or equivalent.
- Stop condition: Stop if sparse 8-bit state misses the convergence threshold on 2 of 3 seeds, fails checkpoint resume fidelity, or measured serialized storage is less than 4x smaller than Adam32.

## Evidence references

- Artifact root: `<local-path>/projects/stabilized-sparse-8-bit-adam-state-with-real-small-model-c-410cdc6d22`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
