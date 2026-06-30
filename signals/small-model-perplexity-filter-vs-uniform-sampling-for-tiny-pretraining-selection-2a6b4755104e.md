# Small-model perplexity filter vs uniform sampling for tiny pretraining selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-model-perplexity-filter-vs-uniform-sampling-for-tiny-pretraining-selection-2a6b4755104e`
Run ID: `small-model-perplexity-filter-vs-uniform-sampling-for-tiny-pretraining-selection-2a6b4755104e-20260620T142742471365+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b2ebbeadc454

## What looked useful

Naive low-perplexity selection was unstable across selection budgets and usually worse than uniform; it overselected easy off-target Plato shards rather than target-like Shakespeare shards.

## Boundaries and scale limits

Not a neural transformer result; not web-scale pretraining; one target distribution; one public-domain corpus family; no tokenizer-matched neural scorer or downstream model; no broad benchmark suite.

## Claim scope

Bounded CPU proxy using Project Gutenberg text, a Shakespeare-sonnets seed/eval split, lowest-perplexity shard selection by a character 5-gram scorer, and downstream character 5-gram held-out bits per character.

## Why it stopped

Bounded proxy/early falsification: the naive lowest-perplexity filter did not robustly beat uniform and showed an off-target easy-text selection failure mode; this is not full-scale validation.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, run a bounded neural follow-up with a tokenizer-matched tiny transformer scorer/downstream model and explicit source-diversity diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-matched tiny transformer check for low-perplexity selection collapse
- Success threshold: Naive low-perplexity filtering is considered confirmed as risky if it loses to uniform on mean held-out loss in at least two of three budgets or selects less target-domain/diversity than uniform while losing downstream loss.
- Stop condition: Stop after three seeds across three budgets or earlier if all first-budget/seed combinations show the same direction with source-collapse diagnostics.

## Evidence references

- Artifact root: `<local-path>/projects/small-model-perplexity-filter-vs-uniform-sampling-for-tiny-pretraining-selection-2a6b4755104e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
