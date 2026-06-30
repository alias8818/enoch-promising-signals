# Quality-Filtered Data Quantity Crossover for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-filtered-data-quantity-crossover-for-tiny-pretraining-4249c16c87d6`
Run ID: `quality-filtered-data-quantity-crossover-for-tiny-pretraining-4249c16c87d6-20260628T040304566243+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/253d88d48df7

## What looked useful

A quality-filtered versus mixed-data crossover appeared at 2x total characters in both the primary and lower-learning-rate runs, but larger mixed budgets were nonmonotonic, indicating optimizer/data interaction rather than a universal more-data rule.

## Boundaries and scale limits

Only 25k-400k training characters, three seeds, character-level model, synthetic corruption, one clean validation distribution, no tokenizer/Transformer/GPT-2-small-class run, no real web quality filter, and no large-scale pretraining.

## Claim scope

In a self-contained NumPy character-level tiny language model trained on Tiny Shakespeare with deterministic 50% synthetic low-quality contamination, mixed/noisy corpora at roughly 2x the best filtered character budget achieved lower clean held-out NLL in two learning-rate settings.

## Why it stopped

Closed as no-paper useful signal: local proxy evidence supports the mechanism narrowly but is insufficient for publication-grade tiny pretraining claims.

## Recommended next action

Run a bounded deepen test with a tokenizer-based small Transformer on real filtered web/text samples, sweeping noise fractions and compute-matched token budgets before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer Transformer Quality-Quantity Crossover Sweep
- Success threshold: At least two contamination fractions show mixed-data clean validation NLL below the best filtered baseline by >=0.01 mean NLL with overlapping compute documented and no degradation on a second clean validation slice.
- Stop condition: Stop if no mixed condition beats the best filtered baseline by >=0.01 mean NLL across three seeds, or if the effect vanishes under compute-matched scheduling.

## Evidence references

- Artifact root: `<local-path>/projects/quality-filtered-data-quantity-crossover-for-tiny-pretraining-4249c16c87d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
