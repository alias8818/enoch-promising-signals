# Residual-Aware 2-bit GPT-2-small with Channel-Wise Outlier Residuals

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-aware-2-bit-gpt-2-small-with-channel-wise-outlier-residuals-3b90a09e0c5e`
Run ID: `residual-aware-2-bit-gpt-2-small-with-channel-wise-outlier-residuals-3b90a09e0c5e-20260609T055625228555+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ca8959169993

## What looked useful

Top-error channel residuals are much better than random residuals, confirming that residual placement matters, but the recovery is far too weak for practical 2-bit compression: 32% restored channels still had PPL 33194 versus FP PPL 44.996, and 75% restored channels still had 33.7x FP perplexity while implying about 14 bits per quantized parameter.

## Boundaries and scale limits

No packed compressed kernels, no activation-aware reconstruction, no quantization-aware training, no full benchmark suite, and only a 4096-token WikiText-2 slice. Results falsify the naive local scheme, not all possible 2-bit GPT-style quantizers.

## Claim scope

Bounded GPT-2-small post-training experiment: per-output-channel affine 2-bit quantization of projection weights plus full-precision channel residuals selected by weight-error outliers, evaluated on 4096 WikiText-2 test next-token targets.

## Why it stopped

Early bounded falsification of the naive post-training scheme: residual-aware channel selection shows a mechanism signal but does not recover usable perplexity at a practical residual budget.

## Recommended next action

Stop pursuit of this exact min/max 2-bit plus weight-error channel residual scheme; only continue via a bounded activation-aware reconstruction variant with a standard 4-bit control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware 2-bit GPT-2-small residual reconstruction against a 4-bit baseline
- Success threshold: Activation-aware residual variant reaches no worse than 2x FP perplexity and beats the 4-bit baseline at no more than 4 effective bits per quantized projection parameter.
- Stop condition: Stop if the activation-aware variant remains worse than 4x FP perplexity or fails to beat the 4-bit baseline under the 4 effective bits-per-parameter budget.

## Evidence references

- Artifact root: `<local-path>/projects/residual-aware-2-bit-gpt-2-small-with-channel-wise-outlier-residuals-3b90a09e0c5e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
