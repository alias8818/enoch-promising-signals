# Extreme INT4 Quantization with Principled Residual Channel Preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-int4-quantization-with-principled-residual-channel-preservation-dcce2a55cd22`
Run ID: `extreme-int4-quantization-with-principled-residual-channel-preservation-dcce2a55cd22-20260609T061940331074+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/25069159f620

## What looked useful

AW-saliency residual preservation reduced relative output MSE by 67.8% at 1% residual channels and 93.0% at 4% residual channels in the mixed-outlier proxy, outperforming random and single-norm policies. In uniform channels it only gave budget-proportional gains, and in single-source outlier regimes it tied the corresponding simple norm rule.

## Boundaries and scale limits

No pretrained transformer, perplexity, downstream task, packed INT4 kernel, latency, or real calibration-dataset validation was run. CPU-only NumPy proxy with 10 seeds, 512 input channels, 1024 output channels, and synthetic channel distributions.

## Claim scope

Synthetic linear-layer reconstruction only: preserving a small set of activation-weight salient input channels in full precision materially reduces output MSE for INT4 weight-only quantization when salient channel outliers are concentrated, especially under mixed activation and weight outliers.

## Why it stopped

Closed as no-paper useful signal: the run directly supports the residual-channel mechanism in a synthetic layer proxy, but does not provide end-to-end model evidence required for publication-grade validation.

## Recommended next action

Run a bounded real-model follow-up on a small pretrained transformer, comparing perplexity at equal bit budgets for no residual, random, weight-norm, activation-norm, and AW-saliency residual policies.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model INT4 residual-channel preservation perplexity probe
- Success threshold: AW-saliency residual policy improves validation loss/perplexity degradation by at least 25% relative to the best non-AW residual baseline at the same effective bit budget, without increasing effective storage above the declared residual budget.
- Stop condition: Stop if AW-saliency is not better than the best simple residual policy on two model layers or calibration subsets, or if equal-budget overhead eliminates the apparent quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int4-quantization-with-principled-residual-channel-preservation-dcce2a55cd22`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
