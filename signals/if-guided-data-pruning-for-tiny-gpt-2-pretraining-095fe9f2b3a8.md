# IF-Guided Data Pruning for Tiny GPT-2 Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `if-guided-data-pruning-for-tiny-gpt-2-pretraining-095fe9f2b3a8`
Run ID: `if-guided-data-pruning-for-tiny-gpt-2-pretraining-095fe9f2b3a8-20260629T014821937886+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3f57fe012b74

## What looked useful

Across 10 seeds, IF-top 50% achieved mean target validation loss 3.5595 versus random 3.7667, loss-high 3.7205, loss-low 4.1317, and IF-bottom 6.6094. IF-top beat random in 10/10 paired seeds and selected almost no distractors on average.

## Boundaries and scale limits

Synthetic data only; tiny local transformer; short training budgets; no GPT-2 tokenizer, GPT-2-small-class model, real corpus, downstream transfer, or long-horizon pretraining validation.

## Claim scope

On a synthetic word-level mixture benchmark for a tiny GPT-like causal transformer, validation-gradient dot-product influence scoring selects a 50% pretraining subset that improves target validation loss versus random and loss-only pruning controls, but does not beat using all scored data.

## Why it stopped

This worker produced a useful synthetic mechanism signal, but it is proxy evidence and not a direct Tiny GPT-2 pretraining validation.

## Recommended next action

Run a bounded real-text follow-up with GPT-2 tokenization and a parameter-matched tiny causal transformer to test whether IF-top 50% still beats random and loss-only pruning on target validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text GPT-2-tokenized IF pruning confirmation
- Success threshold: IF-top must beat random and both loss-only controls in mean paired target validation loss at 50% pruning, with wins in at least 4/5 seeds and no catastrophic degradation versus full data beyond an agreed budget-quality tradeoff.
- Stop condition: Stop if IF-top fails to beat random in at least 3/5 seeds on the first real-text 50% pruning condition or if scoring cost dominates retraining cost enough to erase practical pruning value at this scale.

## Evidence references

- Artifact root: `<local-path>/projects/if-guided-data-pruning-for-tiny-gpt-2-pretraining-095fe9f2b3a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
