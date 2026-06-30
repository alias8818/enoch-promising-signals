# Layer-Type Residual: Preserve Attention Output Projections at 2-bit MLP

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-type-residual-preserve-attention-output-projections-at-2-bit-mlp-837041ac1b94`
Run ID: `layer-type-residual-preserve-attention-output-projections-at-2-bit-mlp-837041ac1b94-20260528T104749771917+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b81ac000324e

## What looked useful

Attention output projection preservation helped within extreme 2-bit MLP quantization (PPL 5671 vs 6809 when attention output projections were also quantized), but the preserved scheme was still 172x worse than FP16 perplexity on the tested slice.

## Boundaries and scale limits

Single pretrained GPT-2-small model; 65,536 validation tokens; fake dequantized 2-bit weights; no packed kernels, quantization-aware training, GPTQ/AWQ reconstruction, downstream tasks, larger models, or full validation sweep.

## Claim scope

On GPT-2 small with WikiText-2 validation fake post-training quantization, preserving attention output projections reduces degradation relative to also quantizing attention output projections, but 2-bit MLP projection quantization remains far worse than FP16.

## Why it stopped

Direct GPT-2-small proxy falsified practical viability of naive 2-bit MLP post-training quantization despite supporting the narrower attention-output-preservation mechanism.

## Recommended next action

Stop this naive post-training 2-bit MLP variant as no-paper; a bounded follow-up should test whether reconstruction-aware 2-bit MLP quantization preserves the same attention-output sensitivity while recovering acceptable perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Reconstruction-Aware 2-bit MLP Quantization with Attention Output Preservation
- Success threshold: Reconstruction-aware preserve-attn-out must cut at least 80% of the naive NLL gap to FP16 and remain measurably better than quantizing attention output projections at matched or explicitly accounted bit budget.
- Stop condition: Stop if reconstruction-aware 2-bit MLP remains above 2x FP16 perplexity on GPT-2-small or if the attention-output preservation advantage disappears under matched bit budget.

## Evidence references

- Artifact root: `<local-path>/projects/layer-type-residual-preserve-attention-output-projections-at-2-bit-mlp-837041ac1b94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
