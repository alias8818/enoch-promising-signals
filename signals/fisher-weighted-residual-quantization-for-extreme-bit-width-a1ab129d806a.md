# Fisher-Weighted Residual Quantization for Extreme Bit-Width

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fisher-weighted-residual-quantization-for-extreme-bit-width-a1ab129d806a`
Run ID: `fisher-weighted-residual-quantization-for-extreme-bit-width-a1ab129d806a-20260523T185312824879+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e93004b3c107

## What looked useful

Fisher-weighted residual quantization is a real optimization mechanism for the Fisher objective, with 10/10 wins in most 1-bit and 1.585-bit synthetic regimes and 3.24% Fisher-loss reduction in the sparse spiky-Fisher 2-bit case. Raw weighting is unsafe as a standalone method because correlated high-Fisher outliers produced 99% Fisher-loss reductions while increasing ordinary MSE by hundreds of times, and the anti-correlated 2-bit case lost by 5.89%.

## Boundaries and scale limits

No real model weights, activation-derived Fisher estimates, downstream perplexity/task metrics, or GPT-2-small-class baseline were tested. The run used CPU-only synthetic arrays of 65,536 weights, 10 seeds, and four Fisher/weight correlation regimes.

## Claim scope

Synthetic diagonal-Fisher layer probes at 1.0, 1.585, and 2.0 bits/weight show that unregularized Fisher-weighted residual scalar quantization often reduces Fisher-weighted reconstruction loss, but can badly worsen ordinary reconstruction error and is not robust across regimes.

## Why it stopped

Synthetic proxy evidence is mixed: the mechanism improves the target Fisher objective but raw unregularized weighting is practically unsafe and lacks direct model-level validation.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should evaluate clipped or mixed-objective Fisher weighting on a small public model with real activation/gradient-derived Fisher estimates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Clipped Fisher residual quantization on a small public language model
- Success threshold: At 1-2 bits/weight, clipped or mixed Fisher RQ reduces Fisher-weighted layer reconstruction loss by at least 5% versus unweighted RQ while keeping ordinary MSE degradation under 10% and downstream loss no worse than the unweighted baseline.
- Stop condition: Stop if raw and clipped/mixed Fisher variants do not beat unweighted RQ on Fisher-weighted reconstruction in at least two representative layer types, or if downstream loss is consistently worse than unweighted RQ.

## Evidence references

- Artifact root: `<local-path>/projects/fisher-weighted-residual-quantization-for-extreme-bit-width-a1ab129d806a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
