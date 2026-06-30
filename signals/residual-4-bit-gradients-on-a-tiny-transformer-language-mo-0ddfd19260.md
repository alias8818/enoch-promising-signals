# Residual 4-bit gradients on a tiny transformer language-modeling proxy

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `residual-4-bit-gradients-on-a-tiny-transformer-language-mo-0ddfd19260`
Run ID: `residual-4-bit-gradients-on-a-tiny-transformer-language-mo-0ddfd19260-20260523T133304584826+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: 4-bit Gradients with Residual Error Compensation: enoch://control-plane/projects/4-bit-gradients-with-residual-error-compensation-74ff73c2871b/runs/4-bit-gradients-with-residual-error-compensation-74ff73c2871b-20260523T110534573378+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aaff3ccd450d

## What looked useful

A 20-step smoke run showed a small residual advantage, but controlled 800-step and 2000-step runs did not support it. In the 2000-step/5-seed confirmation, FP32 final validation loss was 2.2626, naive 4-bit was 2.2907, and residual 4-bit was 2.2962; residual widened the naive-vs-FP32 gap by 19.8% rather than closing it.

## Boundaries and scale limits

This was a small direct Tier 1 proxy: character-level Tiny Shakespeare, d_model=64, 2 layers, 5 seeds, single-GPU local training. It does not cover GPT-2-small-class or larger models, longer horizons, tokenized corpora, distributed training, or optimizer-aware residual variants.

## Claim scope

On a tiny 2-layer character-level transformer language-modeling proxy trained with AdamW on Tiny Shakespeare for up to 2000 steps, residual/error-feedback symmetric per-tensor 4-bit gradient quantization did not improve validation loss versus naive 4-bit gradient quantization.

## Why it stopped

Controlled small direct evidence falsified a meaningful residual 4-bit benefit on the stated tiny transformer LM proxy; this is an early proxy falsification, not a full-scale validation.

## Recommended next action

Stop this follow-up as a no-paper useful negative signal; only revisit if testing an explicitly different optimizer-aware residual scheme or a larger direct model scale with a predeclared threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/residual-4-bit-gradients-on-a-tiny-transformer-language-mo-0ddfd19260`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
