# Bounded Mixed-Precision Search for Residual-Heavy Architectures on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-mixed-precision-search-for-residual-heavy-architectures-on-cpu-455c16c62d27`
Run ID: `bounded-mixed-precision-search-for-residual-heavy-architectures-on-cpu-455c16c62d27-20260611T043431794002+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ef360c99b240

## What looked useful

Bounded search reduced relative RMSE from 0.00760 all-int8 to 0.00455 with a 7-fp32/5-int8 policy under a 0.005 bound, but that policy ran at 9.138 ms median versus 1.224 ms fp32. A stricter 0.002 bound required all 12 blocks to return to fp32. Naive CPU mixed precision is therefore error-controllable but not latency-competitive in this implementation.

## Boundaries and scale limits

Depth 4 smoke and depth 12 width 128 batch 32 proxy only; untrained synthetic residual MLP; no task accuracy; NumPy int8/fp16 kernels rather than optimized CPU inference backends; not GPT-2-small or production residual models.

## Claim scope

On a synthetic residual MLP CPU proxy using NumPy dynamic symmetric int8 and fp16 kernels, greedy bounded mixed-precision search can enforce relative output-RMSE bounds, but the resulting int8/fp16 policies are slower than fp32 BLAS and are not practically useful as implemented.

## Why it stopped

Early proxy falsification of the practical CPU efficiency claim for a naive NumPy implementation; this is not a full validation or full rejection of optimized backend implementations.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next bounded test is to repeat the same search on a trained residual-heavy model with an optimized CPU quantized inference backend such as oneDNN/OpenVINO/ONNX Runtime.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded residual mixed-precision search with optimized CPU quantized kernels
- Success threshold: At least one bounded mixed policy meets a predeclared accuracy/output error bound while improving median latency by >=15% over fp32 on the optimized CPU backend.
- Stop condition: Stop if optimized all-int8 is not faster than fp32, or if every policy meeting the error bound is slower than fp32 across two seeds/configurations.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-mixed-precision-search-for-residual-heavy-architectures-on-cpu-455c16c62d27`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
