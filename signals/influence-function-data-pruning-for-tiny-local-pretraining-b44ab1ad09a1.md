# Influence-Function Data Pruning for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `influence-function-data-pruning-for-tiny-local-pretraining-b44ab1ad09a1`
Run ID: `influence-function-data-pruning-for-tiny-local-pretraining-b44ab1ad09a1-20260619T083111473886+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8977943e21b7

## What looked useful

Influence pruning improved mean clean test CE from 1.5403 to 1.3473 and won against baseline and random pruning in 5/5 seeds while pruning 97.8% noisy examples on average. However, validation gradient-dot pruning was effectively tied, so exact influence functions are not yet justified over a cheaper score.

## Boundaries and scale limits

Evidence is limited to a convex one-token softmax proxy with synthetic noise. It does not validate transformer pretraining, real text corpora, tokenization effects, long-context examples, or the cost-benefit of influence estimation in nonconvex tiny local pretraining.

## Claim scope

On a synthetic 12-token Markov next-token task with injected adversarial transition noise, exact-Hessian influence pruning removed harmful examples and improved clean test cross-entropy versus no-prune, random-prune, and train-loss-prune controls across five seeds.

## Why it stopped

No paper: current evidence is a bounded synthetic convex proxy that supports the pruning mechanism but does not directly validate tiny neural pretraining, and exact influence did not outperform a cheaper gradient-dot baseline.

## Recommended next action

Run a bounded direct tiny-transformer or GPT-2-small-class pretraining follow-up on a real text corpus with matched token budget, comparing influence, gradient-dot, loss, random, and no-prune controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Influence pruning on a real-corpus tiny transformer pretraining budget
- Success threshold: Influence pruning improves held-out cross-entropy versus no-prune and random-prune in at least 3/3 seeds and beats gradient-dot by at least 0.02 CE or 1% relative perplexity at comparable pruning budget.
- Stop condition: Stop if influence fails to beat gradient-dot or random pruning in two seeds, or if the influence computation overhead dominates the fixed local pretraining budget without a measurable held-out loss gain.

## Evidence references

- Artifact root: `<local-path>/projects/influence-function-data-pruning-for-tiny-local-pretraining-b44ab1ad09a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
