# Trace-Derived Semantic Compression for Memory Efficiency

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-derived-semantic-compression-for-memory-efficiency-91ededb4dc90`
Run ID: `trace-derived-semantic-compression-for-memory-efficiency-91ededb4dc90-20260613T071901721115+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6db3840ff63f

## What looked useful

The mechanism appears useful when traces are repetitive and the target memory is low-entropy latest semantic state: semantic records achieved 100% mean exact-answer accuracy at 0.001 raw-byte budget fraction with about 1887.6x compression, while raw_recent reached 8.125% and trace_template reached 12.5%.

## Boundaries and scale limits

Synthetic traces only; fixed small fact schema; hand-coded extraction; byte-level rather than tokenizer-level accounting; no LLM-integrated retrieval or downstream natural-language answer evaluation; no real agent trace corpus.

## Claim scope

In a deterministic synthetic trace benchmark with redundant noisy fact updates, trace-derived canonical semantic records preserved exact latest-state answers at 0.1% of raw trace bytes and outperformed raw-prefix, raw-recent, lexical-summary, and template-count controls at equal byte budgets.

## Why it stopped

No-paper closure: the local proxy supports the mechanism but synthetic hand-extracted traces are insufficient for a paper-positive claim.

## Recommended next action

Run a bounded follow-up on real or benchmark agent traces with tokenizer-level budgets, learned or LLM-based extraction, extraction-error analysis, and downstream QA/retrieval comparison against raw-memory baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Semantic Memory Compression With Token Budgets
- Success threshold: At <=5% of raw token budget, semantic records achieve at least 90% of full-raw QA accuracy and beat the best equal-budget raw or template baseline by at least 15 absolute accuracy points on two trace domains.
- Stop condition: Stop as negative if extraction errors reduce semantic-record QA below the best equal-budget raw baseline on both domains or if compression requires more than 20% of raw tokens to match raw-recent accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-semantic-compression-for-memory-efficiency-91ededb4dc90`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
