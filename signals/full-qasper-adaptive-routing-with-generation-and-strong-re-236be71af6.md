# Full-Qasper Adaptive Routing With Generation and Strong Retrieval Controls

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `full-qasper-adaptive-routing-with-generation-and-strong-re-236be71af6`
Run ID: `full-qasper-adaptive-routing-with-generation-and-strong-re-236be71af6-20260522T064604418928+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evaluate Adaptive Context Routing on Public Long-Document QA: enoch://control-plane/projects/evaluate-adaptive-context-routing-on-public-long-document-9ca2fb7347/runs/evaluate-adaptive-context-routing-on-public-long-document-9ca2fb7347-20260522T024514460744+0000
- Parent run decision: Context-Length Adaptive Router for Long-Document QA: enoch://control-plane/projects/context-length-adaptive-router-for-long-document-qa-bbb7b2faf727/runs/context-length-adaptive-router-for-long-document-qa-bbb7b2faf727-20260522T010245145307+0000

## What looked useful

The learned adaptive router underperformed section-aware TF-IDF on held-out recall@5 across seeds 13, 42, and 99: mean 0.3103 versus 0.3770, with paired bootstrap deltas strictly negative. Oracle routing reached 0.5037 recall@5, showing complementary candidate retriever successes that question-only routing failed to exploit.

## Boundaries and scale limits

CPU-only lexical retrieval and deterministic extractive generation; no neural generator or dense retriever was evaluated. Evidence mapping is paragraph/caption-level string overlap from Qasper annotations.

## Claim scope

On the cached full Qasper train/validation/test splits, a supervised question-feature adaptive router over BM25, TF-IDF, section-aware TF-IDF, hybrid, first-paragraph, and random retrievers does not improve evidence retrieval or extractive generation over strong single-retriever controls.

## Why it stopped

Direct Tier 2 full-Qasper validation with fixed seeds, ablations, real lexical baselines, retrieval metrics, and extractive generation metrics falsified the deployable adaptive-routing hypothesis.

## Recommended next action

Stop this router design; if continuing locally, test a score-level rank-fusion or reranking follow-up that uses candidate retrieval scores/text instead of question-only method classification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Qasper score-level adaptive rank fusion
- Success threshold: Beat section-aware TF-IDF test recall@5 by at least 0.03 absolute with paired bootstrap 95% CI above 0, while maintaining answer F1 within 0.002 absolute of the best lexical generation control.
- Stop condition: Stop if rank fusion fails to beat section-aware TF-IDF recall@5 by 0.01 absolute on validation or if test bootstrap confidence intervals include zero after validation-selected hyperparameters.

## Evidence references

- Artifact root: `<local-path>/projects/full-qasper-adaptive-routing-with-generation-and-strong-re-236be71af6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
