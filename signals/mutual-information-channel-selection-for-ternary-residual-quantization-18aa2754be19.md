# Mutual-Information Channel Selection for Ternary+Residual Quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `mutual-information-channel-selection-for-ternary-residual-quantization-18aa2754be19`
Run ID: `mutual-information-channel-selection-for-ternary-residual-quantization-18aa2754be19-20260601T063750879900+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/03d2b34b4c60

## What looked useful

Across 5 seeds, 4 datasets, and residual budgets 4/8/12/16, MI-label selection had 0 wins, 12 losses, and 4 ties versus the best non-oracle baseline. The strongest simple control was usually activation_residual_energy, indicating residual-channel allocation should account for quantization error and activation scale rather than task MI alone.

## Boundaries and scale limits

NumPy-only CPU experiment; synthetic datasets; small softmax classifiers; no pretrained transformer, no LLM perplexity, no hardware quantized kernel, and no transformer activation-channel MI measurement.

## Claim scope

On four synthetic trained softmax-classifier regimes with ternary weight quantization plus exact residual restoration for selected input channels, empirical label-MI channel selection improves over ternary-only but does not outperform quantization-aware residual-energy or residual-magnitude selectors at matched residual budgets.

## Why it stopped

Proxy/local mechanism evidence was sufficient to early-falsify the claim that label MI alone is a superior residual-channel selector, but it is not a full transformer-scale validation.

## Recommended next action

Stop this standalone MI-label selector as no-paper evidence; run a bounded transformer-layer follow-up only if comparing residual-energy-weighted MI or conditional MI against activation_residual_energy on direct perplexity metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-Energy-Weighted MI for Transformer Ternary Residual Channels
- Success threshold: At least 1 percent relative perplexity or next-token-loss improvement over activation_residual_energy at two or more residual budgets, consistent across at least three calibration seeds or splits.
- Stop condition: Stop if weighted/conditional MI fails to beat activation_residual_energy by the success threshold on a small pretrained-transformer calibration benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/mutual-information-channel-selection-for-ternary-residual-quantization-18aa2754be19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
