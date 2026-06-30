# Progressive Residual Channel Precision Collapse Mapping

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `progressive-residual-channel-precision-collapse-mapping-aa5d4878bee8`
Run ID: `progressive-residual-channel-precision-collapse-mapping-aa5d4878bee8-20260601T065942118903+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/01a2d3206567

## What looked useful

2-bit channel collapse produced a small ordering signal, with least-sensitive-first AUC 0.6743 versus random 0.6683 and most-sensitive-first 0.6608. Zero-collapse strengthened the map, with least-sensitive-first AUC 0.6498 versus random 0.6337 and most-sensitive-first 0.5981. Sensitivity correlated with absolute readout weight (Spearman about 0.36 to 0.39) but not activation energy, and the top 10% of channels explained about 41% to 43% of positive single-channel sensitivity.

## Boundaries and scale limits

Proxy-only evidence: no trained Transformer residual streams, no language modeling loss or perplexity, no real calibration corpus, no learned full-model adaptation, no hardware kernel measurement, and only 5 seeds at width 64 with 4 residual blocks.

## Claim scope

In a small NumPy residual feature network with frozen residual blocks and a trained ridge readout on a synthetic nonlinear binary task, per-channel residual activation precision-collapse sensitivity is non-random: least-sensitive-first collapse preserves accuracy better than random order and most-sensitive-first collapse degrades accuracy faster.

## Why it stopped

Proxy evidence supports a mechanism but does not directly validate progressive residual-channel precision collapse in trained Transformer residual streams.

## Recommended next action

Stop this run as a proxy useful signal; the concrete next test is a bounded trained small-Transformer residual-stream quantization study with perplexity/accuracy controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained Small-Transformer Residual Channel Precision Collapse Map
- Success threshold: Least-sensitive-first collapse must preserve validation loss or accuracy significantly better than all control orders for at least two precision levels, with stable rank correlation across batches/checkpoints and no reliance on a single seed.
- Stop condition: Stop if baseline model quality is too weak for meaningful loss deltas, or if measured sensitivity order fails to beat random and simple norm-based controls across seeds/checkpoints.

## Evidence references

- Artifact root: `<local-path>/projects/progressive-residual-channel-precision-collapse-mapping-aa5d4878bee8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
