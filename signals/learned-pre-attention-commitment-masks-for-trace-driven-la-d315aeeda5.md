# Learned Pre-Attention Commitment Masks for Trace-Driven Lazy Workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `learned-pre-attention-commitment-masks-for-trace-driven-la-d315aeeda5`
Run ID: `learned-pre-attention-commitment-masks-for-trace-driven-la-d315aeeda5-20260518T074512627904+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Learned Pre-Attention Commitment Masks for Trace-Driven Lazy Workers: internal_generated:learned-pre-attention-commitment-masks-for-trace-driven-la-d315aeeda5

## What looked useful

Predictive masking is feasible in the controlled trace setting: seq-len 128 validation across five seeds reached recall 0.9505 +/- 0.0003, F1 0.8797 +/- 0.0136, AUROC 0.9906 +/- 0.0026, and skipped 0.7972 +/- 0.0311 of attention queries. However, the token MLP control was close and measured sparse runtime was only 0.1569x dense, so the practical speedup claim is unsupported.

## Boundaries and scale limits

Evidence is synthetic-only and local. It does not use real production traces, an end-to-end downstream task, GPT-2-class model training, or a production-quality block-sparse/custom attention kernel. The tested naive selected-query attention path is slower than dense attention.

## Claim scope

On synthetic trace-driven lazy-worker commitments, learned pre-attention masks can hit about 0.95 commitment recall while skipping about 72-80% of worker-token attention queries, substantially outperforming static and cheap heuristic baselines on prediction metrics.

## Why it stopped

Synthetic mechanism support did not translate to measured runtime benefit: the naive selected-query attention path was slower than dense attention despite large query-count reductions, and the evidence is not real-trace or end-to-end task evidence.

## Recommended next action

Stop as no-paper evidence unless a bounded follow-up implements block-aligned or custom sparse attention and tests whether the same learned masks produce real wall-clock speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-Aligned Learned Commitment Masks for Real Sparse Attention Speedup
- Success threshold: At least 0.95 commitment recall, at least 50% query or block reduction, and greater than 1.2x measured end-to-end attention speedup versus dense execution across at least three fixed seeds.
- Stop condition: Terminate as negative if block-aligned sparse execution cannot beat dense attention at the required recall, or if block constraints reduce skip rate below 50%.

## Evidence references

- Artifact root: `<local-path>/projects/learned-pre-attention-commitment-masks-for-trace-driven-la-d315aeeda5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
