# Ternary Weights with Group-Wise Scaling and Bias Residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weights-with-group-wise-scaling-and-bias-residual-3353624633a4`
Run ID: `ternary-weights-with-group-wise-scaling-and-bias-residual-3353624633a4-20260630T143253088422+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5ae17bc3184a

## What looked useful

Group-wise scaling was useful: group_g64 averaged 94.88% accuracy versus 91.12% for global_twn and 96.14% for dense, cutting the dense accuracy drop from 5.02 to 1.26 percentage points at about 57% nonzero ternary weights. Bias residual variants were negative: group_g64_layerwise_bias_residual fell to 90.60% and group_g64_logit_bias_residual fell to 93.81%.

## Boundaries and scale limits

Small MLP and MNIST only; no transformer language modeling, GPT-2-small-class baseline, ternary-aware training, large-corpus validation, bit-packed kernel implementation, or hardware speed/energy measurement.

## Claim scope

On a 5-seed MNIST MLP post-training quantization probe, per-output-row group-wise ternary scaling preserved accuracy substantially better than one global ternary row scale, but naive layerwise and final-logit bias residual calibration reduced accuracy relative to the same group-wise ternary model without residual.

## Why it stopped

No-paper mixed result: the bounded probe supports the group-wise scaling component but early-falsifies the naive bias residual component in this setting; larger claims require direct transformer and kernel evidence.

## Recommended next action

Run a bounded small-transformer language-modeling follow-up that keeps group-wise ternary scaling but drops naive mean bias residuals, comparing dense, global ternary, and group-wise ternary models on validation perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Group-wise ternary scaling without naive bias residuals on a small transformer LM
- Success threshold: Group-wise ternary validation perplexity degradation is at least 25% smaller than global ternary degradation versus dense, without more than 2 percentage points worse token-level accuracy or equivalent task metric.
- Stop condition: Stop if group-wise ternary does not beat global ternary on mean validation perplexity degradation across replicates or if dense-to-ternary degradation exceeds a practical small-model threshold for both ternary methods.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weights-with-group-wise-scaling-and-bias-residual-3353624633a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
