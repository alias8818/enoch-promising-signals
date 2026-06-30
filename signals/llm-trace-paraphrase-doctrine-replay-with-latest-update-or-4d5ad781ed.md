# LLM-trace paraphrase doctrine replay with latest-update oracle

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `llm-trace-paraphrase-doctrine-replay-with-latest-update-or-4d5ad781ed`
Run ID: `llm-trace-paraphrase-doctrine-replay-with-latest-update-or-4d5ad781ed-20260629T033816913540+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Paraphrase-robust doctrine update semantics replay: enoch://control-plane/projects/paraphrase-robust-doctrine-update-semantics-replay-b418d1902e/runs/paraphrase-robust-doctrine-update-semantics-replay-b418d1902e-20260629T032209213579+0000
- Parent run decision: Natural-language doctrine memory replay with inferred update semantics: enoch://control-plane/projects/natural-language-doctrine-memory-replay-with-inferred-upda-94da3d695d/runs/natural-language-doctrine-memory-replay-with-inferred-upda-94da3d695d-20260629T014616125618+0000

## What looked useful

The latest-update oracle produced 10/10 accuracy with zero stale errors, versus transcript_search at 8/10 with 2 stale errors and flat_retrieval at 9/10 with 1 stale error. This supports the mechanism but not a paper-ready claim.

## Boundaries and scale limits

Synthetic small corpus; rule-labeled answers; deterministic evaluator; no live LLM inference; no real production traces; no large paraphrase distribution; flat baseline is lexical and not a learned retriever.

## Claim scope

On a 10-case synthetic deterministic replay corpus, a slot-normalized doctrine memory layer with newest-timestamp conflict resolution avoided stale paraphrased-update errors that affected lexical transcript and flat retrieval baselines.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic and rule-based; it supports a mechanism but does not directly validate real LLM trace replay.

## Recommended next action

Run a bounded deepen test on at least 100 independently generated paraphrase/update cases and include a stronger recency-aware retrieval baseline before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Larger paraphrase doctrine replay with recency-aware retrieval baseline
- Success threshold: Layered doctrine memory improves stale-error count by at least 50% over the best non-layered baseline while maintaining at least 95% answer accuracy.
- Stop condition: Stop if the layered approach does not beat the best non-layered baseline on stale-error count or if generated tasks cannot be made independent of evaluator heuristics.

## Evidence references

- Artifact root: `<local-path>/projects/llm-trace-paraphrase-doctrine-replay-with-latest-update-or-4d5ad781ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
