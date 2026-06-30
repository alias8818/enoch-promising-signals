# Quality-Filtered Small Corpus vs Matched Random Subset

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-filtered-small-corpus-vs-matched-random-subset-8990bbbeb6ac`
Run ID: `quality-filtered-small-corpus-vs-matched-random-subset-8990bbbeb6ac-20260628T220002415631+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4581481eb0d4

## What looked useful

Quality-top subsets beat matched random controls at every tested budget: +14.78, +12.50, +6.12, and +4.21 accuracy points for 5, 10, 20, and 40 docs/class, with 10/10 seed wins at each budget.

## Boundaries and scale limits

One public corpus, four classes, one hand-built quality score, one simple classifier, and no language-model pretraining or generation evaluation. The result is a bounded mechanism signal, not a broad corpus-curation validation.

## Claim scope

On a four-class 20 Newsgroups classification probe with 5-40 documents per class, an intrinsic quality-filtered subset improved multinomial Naive Bayes accuracy over matched class-stratified random subsets across 10 random seeds.

## Why it stopped

Closed as no-paper useful signal because the local evidence supports the mechanism but is too narrow for publication-grade general claims.

## Recommended next action

Run a bounded deepen follow-up on at least three public corpora with multiple quality scorers and at least two classifier families before considering a paper gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-corpus validation of intrinsic quality filtering for small text subsets
- Success threshold: Quality filtering beats matched random in at least two of three corpora and has a positive mean paired accuracy difference with confidence intervals excluding zero for the smallest two budgets.
- Stop condition: Stop if quality filtering fails to beat random on two corpora or gains disappear after removing length-dominated scoring.

## Evidence references

- Artifact root: `<local-path>/projects/quality-filtered-small-corpus-vs-matched-random-subset-8990bbbeb6ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
