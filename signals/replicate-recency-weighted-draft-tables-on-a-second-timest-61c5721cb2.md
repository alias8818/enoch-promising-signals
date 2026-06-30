# Replicate recency-weighted draft tables on a second timestamped corpus with BPE tokens

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `replicate-recency-weighted-draft-tables-on-a-second-timest-61c5721cb2`
Run ID: `replicate-recency-weighted-draft-tables-on-a-second-timest-61c5721cb2-20260522T185607581123+0000`

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

- Parent run decision: Recency-Weighted Co-occurrence Draft Table: enoch://control-plane/projects/recency-weighted-co-occurrence-draft-table-7a05b2129535/runs/recency-weighted-co-occurrence-draft-table-7a05b2129535-20260522T175004441374+0000
- Parent run decision: Recency-weighted co-occurrence draft table on chronological real text: enoch://control-plane/projects/recency-weighted-co-occurrence-draft-table-on-chronologica-3b30bec50a/runs/recency-weighted-co-occurrence-draft-table-on-chronologica-3b30bec50a-20260522T184042825828+0000

## What looked useful

Direct BPE draft-table metrics on a second timestamped corpus were negative: order-3 unweighted global baseline averaged top1_acc 0.213178, top5_acc 0.288188, and mean_greedy_span 0.261603; decay_hl30 was lower on all metrics, and decay_hl90 only tied top-1 within a CI crossing zero while losing top-5. Order-2 robustness also left decay_hl90 slightly below baseline and stronger recency variants clearly below baseline.

## Boundaries and scale limits

The run used titles/domains rather than long documents, three future monthly evaluation periods, one public timestamped corpus, small local BPE/n-gram tables, and table-level draft coverage metrics rather than end-to-end speculative decoding with a neural base model.

## Claim scope

On a 6,000-record 2024 HN story-title/domain timestamped corpus with locally trained byte-level BPE tokens, month-wise future evaluation, and n-gram draft tables, exponential recency weighting and a 30-day window do not improve direct next-token draft coverage over a cumulative unweighted n-gram table baseline.

## Why it stopped

Tier 2 direct local validation with fixed seed, real baseline, ablations, shuffled timestamp control, and order robustness did not support the recency-weighted draft-table hypothesis on the second timestamped BPE corpus.

## Recommended next action

Stop this branch as a no-paper useful negative signal; only revisit with a materially larger timestamped corpus containing full text and an end-to-end speculative-decoding acceptance metric.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/replicate-recency-weighted-draft-tables-on-a-second-timest-61c5721cb2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
