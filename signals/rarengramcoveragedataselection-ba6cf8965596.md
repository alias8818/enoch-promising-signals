# RareNGramCoverageDataSelection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rarengramcoveragedataselection-ba6cf8965596`
Run ID: `rarengramcoveragedataselection-ba6cf8965596-20260523T161654705410+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d1f0bf117fed

## What looked useful

Rare-greedy achieved 1.92x to 5.00x random weighted pool rare n-gram coverage across 1-10% token budgets and 1.09x to 1.27x random held-out rare n-gram coverage. At 10% tokens it beat random on classifier accuracy and macro-F1, but shortest-document selection won the classifier proxy.

## Boundaries and scale limits

Single corpus; word n-grams only; no language model training; downstream classifier proxy is confounded by selected document count and class coverage; not evidence for pretraining-scale model quality.

## Claim scope

On a 4000-document 20 Newsgroups pool, token-budgeted greedy selection for rare word bigram/trigram coverage covers substantially more rare n-gram mass than random, length, shortest-document, and one-pass rarity-density baselines, and modestly improves held-out rare n-gram coverage.

## Why it stopped

Bounded local evidence supports the coverage mechanism but gives mixed downstream proxy results, so it is not publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should train matched small language models or a document-count/class-balanced classifier to separate rare n-gram coverage from document-count effects.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Document-balanced downstream test for rare n-gram coverage selection
- Success threshold: Rare-greedy must improve held-out rare-span model metric by at least 5% relative to random while matching or exceeding shortest-document/class-balanced baselines on rare coverage without losing more than 1% absolute overall metric.
- Stop condition: Stop if rare-greedy loses its rare-coverage advantage under matched document/class controls or if downstream rare-span metrics do not improve over random.

## Evidence references

- Artifact root: `<local-path>/projects/rarengramcoveragedataselection-ba6cf8965596`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
