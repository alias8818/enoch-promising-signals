# Linear Recurrence Injection for Tiny Model Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `linear-recurrence-injection-for-tiny-model-long-context-63138fd48d87`
Run ID: `linear-recurrence-injection-for-tiny-model-long-context-63138fd48d87-20260607T202505168370+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b929845421d7

## What looked useful

Across 3 seeds, recurrence injection improved mean accuracy over the same-width tiny Transformer by +4.16 points at 512 tokens and +4.39 points at 1024 tokens, but the larger dense Transformer reached higher long-context accuracy and the recurrence implementation trained slower.

## Boundaries and scale limits

Synthetic classification only; no natural-language LM training, no GPT-2-small-class baseline, no parameter-matched dense control within 1%, and no optimized parallel-scan recurrence kernel.

## Claim scope

On a synthetic marker-value recall probe trained at 128 tokens and evaluated at 512/1024 tokens, linear recurrence injection into a tiny causal Transformer produced a small same-width long-context lift but did not outperform a larger dense Transformer control; no parameter-matched architecture advantage is supported.

## Why it stopped

No-paper closure: bounded direct synthetic evidence is mixed and dominated by a larger dense control, so this is not a publication-grade positive result or full validation of recurrence-augmented language models.

## Recommended next action

Run a bounded parameter-matched deepen test with a dense control adjusted to within 1% of recurrence parameters and an optimized scan/vectorized recurrence; stop if recurrence fails to beat the matched dense control by at least 10 absolute accuracy points at 1024 tokens across 5 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched recurrence injection on synthetic long-context recall
- Success threshold: Recurrence model beats the parameter-matched dense control by at least 10 absolute accuracy points at 1024 tokens with no training-length regression larger than 2 points and no more than 2x wall-clock overhead.
- Stop condition: Stop as negative if recurrence does not exceed the parameter-matched dense control by 10 points at 1024 tokens across 5 seeds or if the optimized recurrence remains more than 2x slower.

## Evidence references

- Artifact root: `<local-path>/projects/linear-recurrence-injection-for-tiny-model-long-context-63138fd48d87`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
