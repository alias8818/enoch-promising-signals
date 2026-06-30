# Perplexity-based data selection for tiny local pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-based-data-selection-for-tiny-local-pretraining-7c35a9e6d021`
Run ID: `perplexity-based-data-selection-for-tiny-local-pretraining-7c35a9e6d021-20260620T004122247704+0000`

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

- Provider-backed Research Facility batch: z-ai/glm-5.2: enoch://research-facility/provider/z-ai/glm-5.2/3a37e5a28273

## What looked useful

Scorer perplexity can act as an easiness/familiarity filter rather than a utility signal. In this run, low-PPL selection chose 180/260 easy_repetitive documents, improved common-target PPL to 144.80 vs 220.65 random, but worsened rare PPL to 27092.20 vs 619.69 and broad PPL to 37986.33 vs 465.74; balanced PPL was 12.98x worse than random.

## Boundaries and scale limits

Synthetic token domains, tiny 2-layer Transformer models, short local CUDA runs, 3 seeds per policy; not validated on natural-language corpora, larger models, longer training, or production data-selection pipelines.

## Claim scope

Controlled synthetic tiny causal-LM experiment: with a biased tiny scorer, naive lowest-perplexity selection improved common-target perplexity but severely harmed rare-target and broad held-out perplexity versus random equal-token selection.

## Why it stopped

No-paper closure: the synthetic local evidence is a useful mechanism signal and early warning, but it is not direct natural-language or publication-grade validation.

## Recommended next action

Run a bounded real-text confirmation using a tiny tokenizer/model, equal-token budgets, random and low/middle/high-PPL controls, plus diversity-capped low-PPL selection on target and off-target held-out sets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text confirmation of perplexity selection failure modes for tiny pretraining
- Success threshold: Naive low-PPL must be at least 10% worse than random or diversity-capped low-PPL on balanced held-out loss while improving or matching narrow target loss, demonstrating the same tradeoff on real text.
- Stop condition: Stop if low-PPL does not improve narrow target loss or if all policies are within 3% balanced loss across 3 seeds, because the synthetic failure would not transfer clearly.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-based-data-selection-for-tiny-local-pretraining-7c35a9e6d021`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
