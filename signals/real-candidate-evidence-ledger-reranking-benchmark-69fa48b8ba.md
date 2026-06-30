# Real-candidate evidence ledger reranking benchmark

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-candidate-evidence-ledger-reranking-benchmark-69fa48b8ba`
Run ID: `real-candidate-evidence-ledger-reranking-benchmark-69fa48b8ba-20260603T231013776636+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence Ledger Plan Reranker: enoch://control-plane/projects/evidence-ledger-plan-reranker-71acbf032012/runs/evidence-ledger-plan-reranker-71acbf032012-20260603T171013878929+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/788c4883ed21

## What looked useful

Dev-tuned lexical evidence ledger features overfit: they improved dev metrics but reduced held-out nDCG@10 by a mean -0.00632 and MRR@10 by a mean -0.00659 across five real-candidate SciFact splits. Recall@20 improved by +0.01093, suggesting broader-candidate movement without useful top-10 ranking gains.

## Boundaries and scale limits

Single dataset/domain, BM25 candidate generator only, top-100 candidate pools, coarse linear weight tuning, lexical ledger features only; no neural entailment, cross-encoder, LLM-based ledger, or cross-dataset validation was tested.

## Claim scope

On BEIR SciFact with BM25 top-100 real candidate pools, the tested deterministic lexical evidence-ledger reranker does not improve held-out early ranking quality over BM25; nDCG@10 and MRR@10 were negative on all five deterministic dev/test splits.

## Why it stopped

Controlled small direct test failed the Tier 1 success threshold: all five held-out splits had negative nDCG@10 and MRR@10 deltas versus BM25, with aggregate changed-query nDCG@10 losses exceeding wins.

## Recommended next action

Stop pursuing this lexical evidence-ledger reranker as a paper direction; any future attempt should pre-register richer entailment-aware ledger features and require held-out nDCG@10 and MRR@10 gains on real candidate pools.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-candidate-evidence-ledger-reranking-benchmark-69fa48b8ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
