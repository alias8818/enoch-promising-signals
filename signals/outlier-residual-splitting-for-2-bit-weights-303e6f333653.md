# Outlier-Residual Splitting for 2-bit Weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `outlier-residual-splitting-for-2-bit-weights-303e6f333653`
Run ID: `outlier-residual-splitting-for-2-bit-weights-303e6f333653-20260526T065311065553+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c5410934474a

## What looked useful

Residual-after-quantization failed: at about 3.08 estimated bpw it retained 91.2% of dense 2-bit output NMSE and beat dense 3-bit on 0/50 GPT-2 tensors. Outlier-first splitting was useful: 1% exact outliers at about 2.27 bpw reduced output NMSE to 31.3% of dense 2-bit, and 4% exact outliers at about 3.08 bpw reached 15.7% of dense 2-bit versus dense 3-bit at 16.6%, beating dense 3-bit on 17/50 tensors.

## Boundaries and scale limits

Evidence is limited to synthetic matrices and GPT-2 layer weight tensors with random-activation output NMSE. It does not include end-to-end perplexity, activation-aware calibration, packed sparse-residual kernels, latency, bandwidth, or larger model families.

## Claim scope

On GPT-2 weight tensors, naive 2-bit plus largest post-quantization residuals is not competitive with dense 3-bit, while outlier-first splitting before 2-bit quantization provides a reproducible layer-output-error tradeoff and can reach dense-3-bit average output NMSE only near the same estimated storage budget.

## Why it stopped

Proxy evidence is sufficient to reject the naive residual-after-quantization version and identify a better variant, but not sufficient for a paper or full validation.

## Recommended next action

Run a bounded direct follow-up on GPT-2-small perplexity with calibration data, comparing outlier-first 2-bit splitting against dense 3-bit and a standard PTQ baseline at matched storage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2 perplexity test for outlier-first 2-bit splitting
- Success threshold: Outlier-first 2-bit splitting must match or beat dense 3-bit perplexity at no more than dense 3-bit estimated storage, while preserving the layer-output NMSE advantage on at least 60% of major transformer matrices.
- Stop condition: Stop if perplexity is worse than dense 3-bit at matched storage or if sparse metadata/runtime overhead removes the storage advantage.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-residual-splitting-for-2-bit-weights-303e6f333653`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
