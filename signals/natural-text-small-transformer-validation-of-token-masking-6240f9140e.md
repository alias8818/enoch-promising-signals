# Natural-text small-transformer validation of token masking versus sequence dropping

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `natural-text-small-transformer-validation-of-token-masking-6240f9140e`
Run ID: `natural-text-small-transformer-validation-of-token-masking-6240f9140e-20260605T131158511232+0000`

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

- Parent run decision: Token-Level Loss Masking versus Sequence Dropping: enoch://control-plane/projects/token-level-loss-masking-versus-sequence-dropping-3a012f35d8bc/runs/token-level-loss-masking-versus-sequence-dropping-3a012f35d8bc-20260605T041201088681+0000
- Parent run decision: Small Neural LM Validation of Token-Level Masking versus Sequence Dropping: enoch://control-plane/projects/small-neural-lm-validation-of-token-level-masking-versus-s-01fd3cc680/runs/small-neural-lm-validation-of-token-level-masking-versus-s-01fd3cc680-20260605T082723901311+0000

## What looked useful

Token masking was better than training on corrupted targets (dirty_unmasked - token_mask = +0.03145 NLL), but worse than sequence dropping on clean held-out NLL (token_mask - sequence_drop = +0.01704 NLL; PPL ratio 1.0172). Sequence dropping matched clean training because random corruption left enough clean windows to refill batches.

## Boundaries and scale limits

Small character-level model, short CPU-only training, synthetic content-independent corruption, and a resampling sequence-drop baseline; not a GPT-2-scale or web-corpus validation.

## Claim scope

On Tiny Shakespeare character-level natural text with synthetic localized token corruption, a 248k-parameter 2-layer causal Transformer, 3 fixed seeds, and 100 optimizer steps per seed, token-level loss masking did not beat a sequence-drop baseline that resamples clean windows to maintain batch size and step count.

## Why it stopped

Medium confirmation with fixed seeds, direct clean validation, a clean baseline, sequence-drop baseline, and dirty-target control did not support token masking over sequence dropping.

## Recommended next action

Stop this branch as no-paper evidence; if continuing, run the bounded finite-stream/no-replacement sequence-drop follow-up where dropped sequences reduce available training tokens rather than being replaced.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Finite-stream no-replacement validation of token masking versus sequence dropping
- Success threshold: Across 3 fixed seeds, token_mask mean clean-val NLL is at least 0.02 lower than sequence_drop_stream with no seed-level reversal, while dirty_unmasked remains worse than token_mask.
- Stop condition: Stop if token_mask fails to beat sequence_drop_stream at corruption settings p_seq=0.35 and p_seq=0.60, or if the result only improves by spending materially more optimizer updates/tokens than the drop baseline.

## Evidence references

- Artifact root: `<local-path>/projects/natural-text-small-transformer-validation-of-token-masking-6240f9140e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
