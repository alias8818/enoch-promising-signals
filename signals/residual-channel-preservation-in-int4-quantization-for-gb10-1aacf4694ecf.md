# Residual Channel Preservation in INT4 Quantization for GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-channel-preservation-in-int4-quantization-for-gb10-1aacf4694ecf`
Run ID: `residual-channel-preservation-in-int4-quantization-for-gb10-1aacf4694ecf-20260608T230015704132+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1df1b8106c17

## What looked useful

Residual-channel preservation appears mechanistically useful when INT4 error is dominated by a small set of high-energy residual channels. The gaussian control showed no special benefit over random preservation, bounding the effect to outlier-channel regimes.

## Boundaries and scale limits

Synthetic residual activations only; no real transformer residual traces, no perplexity/task-quality measurement, no packed INT4 kernel throughput measurement, and scale metadata overhead was not included in the storage estimate.

## Claim scope

On synthetic GB10 CUDA residual-stream probes with identifiable high-energy outlier channels, preserving the calibrated top-energy 3.125% channels in fp16 while INT4-quantizing the rest reduced downstream projection output NMSE by about 97-98% versus plain INT4, while an overhead-matched random preservation control reduced only about 3-4%.

## Why it stopped

Closed as a no-paper useful signal because the evidence is synthetic/proxy mechanism evidence rather than real-model quality or packed-kernel GB10 performance validation.

## Recommended next action

Run a bounded direct model-level follow-up on a small transformer or GPT-2-small-class model using real residual activations and matched INT4, INT8, random-preserve, and SmoothQuant/AWQ-style controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Activation Residual Channel Preservation for INT4 Small Transformers
- Success threshold: At matched storage overhead, top-energy residual-channel preservation reduces held-out projection/output error by at least 50% versus plain INT4 and beats random preservation by at least 25 percentage points, with no worse than a small measured task-quality regression relative to the selected baseline.
- Stop condition: Stop if real residual activations do not show stable high-energy channels or if top-energy preservation fails to materially beat random preservation at matched overhead.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-preservation-in-int4-quantization-for-gb10-1aacf4694ecf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
