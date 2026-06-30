# Semi-real multi-source trace replay against a production provenance baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `semi-real-multi-source-trace-replay-against-a-production-p-8eb0904115`
Run ID: `semi-real-multi-source-trace-replay-against-a-production-p-8eb0904115-20260528T055713305048+0000`

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

- Parent run decision: Heterogeneous Trace Corpus Replay for Provenance Evidence Ledgers: enoch://control-plane/projects/heterogeneous-trace-corpus-replay-for-provenance-evidence-5fa4ee778c/runs/heterogeneous-trace-corpus-replay-for-provenance-evidence-5fa4ee778c-20260528T031313349541+0000
- Parent run decision: Replay Realistic Agent Tool Traces Through a Provenance Evidence Ledger: enoch://control-plane/projects/replay-realistic-agent-tool-traces-through-a-provenance-ev-fa3579e0d8/runs/replay-realistic-agent-tool-traces-through-a-provenance-ev-fa3579e0d8-20260527T233341468950+0000

## What looked useful

Corrected primary run: fused replay mean F1 0.739 versus span-parent-only 0.419 and single-source lineage 0.543; removing queue events reduced F1 to 0.599. However the full production-style baseline is F1 1.000, fused precision falls with noise, and the no-skew-correction ablation outperformed fixed skew correction.

## Boundaries and scale limits

Primary validation used generated semi-real traces, not private or real production traces; 48 fixed-seed conditions, 43.1M events, and 39.7M truth edges ran locally in 5:49 wall-clock. Real exporter behavior, schema drift, collector storage, production noise, and independently captured provenance were proxied.

## Claim scope

In a corrected no-oracle semi-real replay benchmark with OpenTelemetry-like spans, lineage logs, queue events, DB audit events, and object-store events, multi-source fusion substantially improves edge-level provenance reconstruction over span-parent-only and single-source controls, but remains well below a complete OpenLineage-style production baseline.

## Why it stopped

Corrected bounded validation supports the multi-source mechanism but not the stronger production-baseline claim; mean F1 remains 0.739 against the complete baseline and the timestamp skew ablation is adverse.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded test should replay actual OpenTelemetry/OpenLineage exporter traces from a local production-like stack and replace fixed skew offsets with measured or learned clock alignment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: No-oracle replay on real OpenTelemetry/OpenLineage exporter traces with learned clock alignment
- Success threshold: Full fusion reaches mean F1 >= 0.85, beats single-source lineage by >= 0.15 F1, queue ablation remains positive by >= 0.05 F1, and learned/measured skew alignment is non-negative versus no-skew replay.
- Stop condition: Stop negative if full fusion is below 0.80 mean F1, if learned/measured clock alignment remains worse than no-skew replay, or if real exporter traces cannot provide an independent baseline without private/manual evidence.

## Evidence references

- Artifact root: `<local-path>/projects/semi-real-multi-source-trace-replay-against-a-production-p-8eb0904115`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
