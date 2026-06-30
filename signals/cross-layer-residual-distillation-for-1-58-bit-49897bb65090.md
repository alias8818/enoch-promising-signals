# Cross-Layer Residual Distillation for 1.58-bit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-layer-residual-distillation-for-1-58-bit-49897bb65090`
Run ID: `cross-layer-residual-distillation-for-1-58-bit-49897bb65090-20260604T185613595010+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/56ed13c59bd9

## What looked useful

CLRD produced a consistent bounded gain over hard labels (-0.1430 validation loss) and logit KD (-0.0460), but consistently trailed boundary hidden KD (+0.0489), making the headline objective unsupported against the strongest local control.

## Boundaries and scale limits

Synthetic task only; 3 corrected seeds; small transformer dimensions; not validated on real language modeling corpora, GPT-2-small-class scale, downstream tasks, 7B+ models, or production quantized kernels.

## Claim scope

On a corrected fixed nonlinear synthetic causal sequence task with a 6-layer dense teacher and 3-layer ternary/1.58-bit student, cross-layer residual distillation improved validation loss over hard-label training and logit-only KD but did not beat boundary hidden-state KD.

## Why it stopped

Bounded local evidence is mixed: CLRD helps versus weaker controls but fails to beat boundary hidden KD, so the result is not publication-grade support for the proposed method.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate a CLRD-plus-hidden hybrid and residual-loss weight sweep on a small real language corpus before any larger-scale work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CLRD hybrid and loss-weight sweep on small real language modeling
- Success threshold: Hybrid CLRD must beat hidden-only KD by at least 0.03 validation loss or equivalent perplexity improvement on mean across 3 seeds without more than 5% training-time overhead.
- Stop condition: Stop if hidden-only KD remains best across the loss-weight grid or if CLRD/hybrid gains appear only in one seed.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-residual-distillation-for-1-58-bit-49897bb65090`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
