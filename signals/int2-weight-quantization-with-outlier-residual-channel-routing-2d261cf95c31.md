# INT2 Weight Quantization with Outlier Residual Channel Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-weight-quantization-with-outlier-residual-channel-routing-2d261cf95c31`
Run ID: `int2-weight-quantization-with-outlier-residual-channel-routing-2d261cf95c31-20260523T152054756151+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/34cc41ba48dc

## What looked useful

ORCR selected synthetic outlier channels with high recall and reduced output MSE by 8.38% at 2% residual channels versus plain INT2, compared with 2.23% for random residual routing at the same 2.625 effective bits/parameter. Plain 3-bit quantization reached 0.2306 mean relative output MSE versus 1.1789 for 2% ORCR, so the current INT2+ORCR formulation is not paper-ready.

## Boundaries and scale limits

Synthetic dense linear layers only; no real transformer weights, real calibration activations, end-to-end perplexity/accuracy, or production residual-kernel bandwidth measurement. CPU-only bounded sweep, not full-scale LLM validation.

## Claim scope

On synthetic heavy-tailed linear layers, INT2 quantization with outlier residual channel routing reduces relative output MSE versus plain INT2 and random residual channel routing at the same residual budget, but it does not approach plain 3-bit per-row quantization in this proxy.

## Why it stopped

Closed as a no-paper useful signal: synthetic proxy supports the routing mechanism but also early-falsifies a broad INT2+ORCR advantage because a simple 3-bit control is much stronger.

## Recommended next action

Run a bounded real-model layer study on pretrained transformer weights and calibration activations, with plain INT3 and storage-matched low-bit baselines, before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real transformer layer validation for INT2 outlier residual channel routing
- Success threshold: At less than or equal to 3.0 effective weight bits/parameter, ORCR should reduce at least 50% of the plain INT2-to-INT3 layerwise output-MSE gap on a majority of tested real transformer layers without worse end-to-end perplexity than plain INT3.
- Stop condition: Stop if ORCR recovers less than 25% of the INT2-to-INT3 output-MSE gap on most real layers, or if residual bandwidth/storage accounting makes it no better than plain INT3.

## Evidence references

- Artifact root: `<local-path>/projects/int2-weight-quantization-with-outlier-residual-channel-routing-2d261cf95c31`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
