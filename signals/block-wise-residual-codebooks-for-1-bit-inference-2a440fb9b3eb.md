# Block-wise residual codebooks for 1-bit inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `block-wise-residual-codebooks-for-1-bit-inference-2a440fb9b3eb`
Run ID: `block-wise-residual-codebooks-for-1-bit-inference-2a440fb9b3eb-20260525T222531346967+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/85f01aa3b2bb

## What looked useful

Across 20 medium runs, block size 16 and K=16 improved output NMSE by 2.611x over the 1-bit baseline and beat the same-index scalar residual control in 20/20 cases. Across 36 ablation rows, every tested block/codebook setting beat the scalar control.

## Boundaries and scale limits

Synthetic matrices only; no trained transformer weights, perplexity/task accuracy, quantization-aware fine-tuning, deployment storage accounting, or hardware kernel throughput was tested.

## Claim scope

On bounded synthetic matrix-output probes, block-wise vector residual codebooks after 1-bit sign+scale reduce output NMSE versus plain 1-bit blocks and versus a same-index-budget block-scalar residual control.

## Why it stopped

This run produced a reproducible useful mechanism signal, but it is proxy synthetic evidence rather than direct model-inference validation.

## Recommended next action

Run a bounded trained-weight follow-up on real small transformer or MLP layers, measuring layer output NMSE and task loss against equal-storage residual baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained-weight residual codebook validation
- Success threshold: Vector residual codebooks improve held-out layer output NMSE by at least 15% over the strongest equal-storage residual baseline and do not degrade task loss/accuracy beyond the plain 1-bit baseline tradeoff.
- Stop condition: Stop if trained-layer output NMSE fails to beat the equal-storage residual baseline on a majority of tested layers/seeds or if complete metadata accounting removes the effective storage advantage.

## Evidence references

- Artifact root: `<local-path>/projects/block-wise-residual-codebooks-for-1-bit-inference-2a440fb9b3eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
