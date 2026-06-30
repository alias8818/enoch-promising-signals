# Small Neural LM Validation of Token-Level Masking versus Sequence Dropping

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-neural-lm-validation-of-token-level-masking-versus-s-01fd3cc680`
Run ID: `small-neural-lm-validation-of-token-level-masking-versus-s-01fd3cc680-20260605T082723901311+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Token-Level Loss Masking versus Sequence Dropping: enoch://control-plane/projects/token-level-loss-masking-versus-sequence-dropping-3a012f35d8bc/runs/token-level-loss-masking-versus-sequence-dropping-3a012f35d8bc-20260605T041201088681+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/05124460a93a

## What looked useful

Token masking beat sequence dropping by 0.1737 nats/token mean held-out clean cross-entropy across 8 seeds and won on 8/8 seeds, exceeding the pre-registered 0.05 nats/token Tier 1 threshold.

## Boundaries and scale limits

Synthetic Markov data, compact NumPy neural LM, independent token corruption, short sequences, and about 37k train positions per seed; no natural-language corpus, transformer, GPT-2-small-class baseline, long-context task, or large-scale training was tested.

## Claim scope

In an 8-seed controlled synthetic Markov next-token LM with independent token corruptions and known clean-token labels, token-level loss masking outperformed dropping whole corrupted sequences on held-out clean cross entropy.

## Why it stopped

Tier 1 controlled direct validation completed and supported the mechanism, but the result is no-paper evidence because it is synthetic and small-scale.

## Recommended next action

Run a bounded natural-text small-transformer follow-up with equal parameter budget, real token-quality labels or simulated span corruptions, and a control matching the number of clean training positions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-text small-transformer validation of token masking versus sequence dropping
- Success threshold: Token masking beats sequence dropping by at least 0.03 nats/token mean held-out clean validation loss and wins on at least two thirds of seeds or shards, while retaining the advantage under a clean-position-count matched control.
- Stop condition: Stop if token masking fails to beat sequence dropping by 0.01 nats/token on the first two seeds/shards or if the clean-position-count matched control removes the advantage.

## Evidence references

- Artifact root: `<local-path>/projects/small-neural-lm-validation-of-token-level-masking-versus-s-01fd3cc680`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
