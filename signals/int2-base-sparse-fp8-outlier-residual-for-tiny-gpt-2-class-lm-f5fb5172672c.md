# INT2 base + sparse FP8 outlier residual for tiny GPT-2-class LM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-base-sparse-fp8-outlier-residual-for-tiny-gpt-2-class-lm-f5fb5172672c`
Run ID: `int2-base-sparse-fp8-outlier-residual-for-tiny-gpt-2-class-lm-f5fb5172672c-20260630T061657807293+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1ff1ce5b8c3a

## What looked useful

Best tested signed-zero INT2 plus 2% FP8 residual density reduced mean output relative MSE from 0.2227 to 0.1498 at 2.59 effective bits/weight, about 6.17x FP16 compression. Midrise INT2 remained much worse, with 0.6717 mean residual output relative MSE at 2% density.

## Boundaries and scale limits

Proxy-only NumPy test on synthetic heavy-tailed weights and activations; no pretrained LM perplexity, downstream accuracy, training, kernel latency, or real calibration traces were measured.

## Claim scope

Sparse FP8 residuals reduce reconstruction and synthetic projection output error for GPT-2-small-shaped linear matrices, but the tested 0.25%-2% residual densities do not make INT2 base quantization viable enough to claim tiny GPT-2-class LM success.

## Why it stopped

This is an early proxy falsification, not a full validation: the residual mechanism helps but leaves high synthetic projection error at the tested sparse densities, so the current evidence is insufficient for a paper or viability claim.

## Recommended next action

Run a bounded direct tiny-GPT-2 perplexity experiment with real calibration text, learned or activation-aware INT2 scales, and comparisons against FP16, INT4, and a stronger INT2 baseline; stop unless 1%-2% FP8 residual density keeps perplexity within 5% of the best low-bit baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct tiny-GPT-2 perplexity test for INT2 plus sparse FP8 residuals
- Success threshold: At 1%-2% residual density, perplexity degradation is no more than 5% versus the best tested low-bit baseline while retaining at least 5x FP16 weight compression.
- Stop condition: Stop if INT2 plus sparse FP8 residual remains more than 10% worse in perplexity than INT4 or requires more than 4% residual density to approach the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/int2-base-sparse-fp8-outlier-residual-for-tiny-gpt-2-class-lm-f5fb5172672c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
