# INT4 Residual-Aware Quantization for Small LM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-residual-aware-quantization-for-small-lm-4a82248ab0d3`
Run ID: `int4-residual-aware-quantization-for-small-lm-4a82248ab0d3-20260613T070652101384+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5c3872ec47f2

## What looked useful

Top-error residual selection is meaningfully better than random residual selection, but simple uniform residual-aware INT4 restored only 14.8% of the plain-INT4-to-FP16 perplexity gap at a 2% residual budget while increasing estimated storage to 5.02 bits/weight.

## Boundaries and scale limits

Mechanism-only post-training probe using dense dequantized weights; no packed INT4 kernels, latency, energy, activation-aware calibration, layerwise residual allocation, multiple models, multiple corpora, or larger-scale validation were tested.

## Claim scope

On one cached 135M causal LM evaluated over 16,352 held-out IMDB tokens, uniform sparse FP16 residual correction of the highest INT4 weight-quantization errors improves perplexity more than random residual correction at the same storage budget, but does not recover enough quality to support a paper-positive or deployment-positive claim.

## Why it stopped

No-paper useful signal: bounded mechanism evidence supports residual-aware selection over random residuals, but quality recovery is too small under the tested naive uniform scheme.

## Recommended next action

Run a bounded deepen test comparing top-error residuals against activation-aware or layerwise residual allocation on the same model plus one additional cached small causal LM; stop if the best method does not recover at least 50% of the plain-INT4 perplexity gap at no more than 5.5 estimated bits/weight.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware and layerwise residual allocation for small-LM INT4 quantization
- Success threshold: Recover at least 50% of the plain-INT4-to-FP16 perplexity gap at no more than 5.5 estimated bits per weight on both small-LM models.
- Stop condition: Stop as negative if activation-aware or layerwise allocation fails to beat uniform top-error residuals by at least 20 percentage points of gap recovery at matched storage on either model.

## Evidence references

- Artifact root: `<local-path>/projects/int4-residual-aware-quantization-for-small-lm-4a82248ab0d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
