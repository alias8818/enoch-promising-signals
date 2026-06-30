# Ternary weight transformer with per-block FP8 residual for top-k outlier magnitudes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weight-transformer-with-per-block-fp8-residual-for-top-k-outlier-magnitudes-0fdc2ed4e9c1`
Run ID: `ternary-weight-transformer-with-per-block-fp8-residual-for-top-k-outlier-magnitudes-0fdc2ed4e9c1-20260609T235521909993+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b44fd0375346

## What looked useful

At k=2 on explicit outlier-mixture matrices, output relative RMSE fell from 0.7755 to 0.3675 at 2.25 bits/weight, 7.11x smaller than FP16. At k=4, Student-t output relative RMSE fell from 0.6521 to 0.3951 and outlier-mixture fell to 0.2820 at 2.38 bits/weight. Gaussian weights improved only modestly, showing the mechanism depends on concentrated residual outliers.

## Boundaries and scale limits

No pretrained transformer weights, no language-model perplexity, no quantization-aware training, no GPT-2-small-class baseline, and no hardware kernel/decode throughput were tested.

## Claim scope

Synthetic NumPy proxy over 512x512 transformer-like linear weights: blockwise ternary plus top-k per-block FP8 residuals reduces reconstruction and random-activation output error versus pure ternary when residual errors are heavy-tailed or outlier-concentrated.

## Why it stopped

Synthetic/proxy evidence supports the outlier-residual mechanism but is not direct transformer or perplexity validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should evaluate the same quantizer on real pretrained transformer layer weights and held-out activations/loss before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate ternary plus sparse FP8 residuals on real pretrained transformer weights
- Success threshold: At <=2.5 bits/weight, k<=4 residuals improve mean projection output relative RMSE by at least 25% and reduce LM loss/perplexity degradation versus pure ternary on a real pretrained model without losing to a same-bit-budget baseline.
- Stop condition: Stop if real transformer residuals are not top-k concentrated, if k<=4 gives less than 10% output-error reduction, or if same-bit-budget baselines match or beat the scheme.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weight-transformer-with-per-block-fp8-residual-for-top-k-outlier-magnitudes-0fdc2ed4e9c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
