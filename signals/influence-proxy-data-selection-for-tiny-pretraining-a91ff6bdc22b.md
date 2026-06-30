# Influence-Proxy Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `influence-proxy-data-selection-for-tiny-pretraining-a91ff6bdc22b`
Run ID: `influence-proxy-data-selection-for-tiny-pretraining-a91ff6bdc22b-20260628T043821946634+0000`

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

Across 12 seeds, proxy_bigram reduced target test NLL versus random by 0.590, 0.495, and 0.234 at 45, 90, and 180 document budgets, and beat unigram_overlap by 0.249, 0.249, and 0.098 NLL.

## Boundaries and scale limits

Synthetic corpus only; count-based bigram LM only; no neural optimizer dynamics, real text, tokenizer effects, downstream tasks, or large-scale pretraining tested.

## Claim scope

In a synthetic tiny smoothed-bigram language-model setting with lexical-trap distractors, transition-level influence-proxy data selection improves held-out target NLL versus random selection and unigram-overlap selection at fixed document budgets.

## Why it stopped

Bounded synthetic evidence supports the mechanism, but this is proxy/count-based evidence rather than direct neural tiny-pretraining validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same proxy against random and unigram controls on a public real-text corpus with a tiny neural LM.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny neural LM validation of influence-proxy data selection on public text
- Success threshold: Influence-proxy selector beats both random and unigram-overlap controls by at least 3% relative held-out target perplexity at two or more budgets with non-overlapping or clearly separated seed distributions.
- Stop condition: Stop if the proxy fails to beat unigram overlap at two budgets or if runtime exceeds the local CPU/GPU budget without producing at least one complete multi-seed budget comparison.

## Evidence references

- Artifact root: `<local-path>/projects/influence-proxy-data-selection-for-tiny-pretraining-a91ff6bdc22b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
