# Semantic Memory Compression vs Flat Retrieval on Repeated Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `semantic-memory-compression-vs-flat-retrieval-on-repeated-tasks-14ce74431ace`
Run ID: `semantic-memory-compression-vs-flat-retrieval-on-repeated-tasks-14ce74431ace-20260611T191507748011+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2dbc57aa11d0

## What looked useful

Compression reached 1.000 accuracy across noisy repeated-task seeds while naive flat retrieval ranged from 0.399 to 0.699 depending on budget; parsed flat retrieval also reached 1.000, showing the useful mechanism is semantic filtering/sufficient-statistic storage rather than compression alone.

## Boundaries and scale limits

CPU-only synthetic benchmark; no real LLM agent, no natural-language extraction errors, no embedding retriever, no production traces, no long-horizon drift.

## Claim scope

Synthetic repeated structured tasks with bounded retrieval budgets: compressed task/value summaries outperform naive whole-text flat retrieval, but do not outperform a parsed flat control using the same semantic extraction.

## Why it stopped

Proxy synthetic evidence supports a narrow mechanism but the stronger parsed flat control matches compressed memory, so this is not a publication-grade positive result.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a natural-language repeated-task agent benchmark with equal parser/embedding access for compressed and flat memories.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language repeated-task memory benchmark with equal semantic extraction
- Success threshold: Compressed memory improves task success by at least 5 percentage points or reduces context tokens by at least 30% at matched success against the strongest flat baseline across at least 3 seeds and 2 distractor/drift settings.
- Stop condition: Stop if a parsed or embedding-indexed flat baseline matches compressed memory within 2 percentage points while using no more than 10% additional context tokens, or if extraction errors dominate both systems.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-memory-compression-vs-flat-retrieval-on-repeated-tasks-14ce74431ace`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
