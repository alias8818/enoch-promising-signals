# Exact-Anchor Hierarchical KV Compression for Long Documents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-hierarchical-kv-compression-for-long-documents-178676c900d2`
Run ID: `exact-anchor-hierarchical-kv-compression-for-long-documents-178676c900d2-20260603T184432140492+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/45d77e07dfa2

## What looked useful

The useful component is exact sparse anchor preservation with log-count-corrected summaries for non-anchor tokens. At length 8192 and 3% retained-entry budget, exact_anchor_flat reached mean relative L2 0.139 overall and 0.000 on anchor queries versus uniform_summary 0.984 overall. Hierarchical variants were consistently worse than flat, e.g. routed hierarchy had 0.771 overall relative L2 at the same setting.

## Boundaries and scale limits

No trained transformer, learned anchor detector, natural long-document corpus, end-to-end perplexity/QA metric, latency benchmark, or GPU serving measurement was tested. Results use synthetic Gaussian K/V tensors with 1% oracle anchors and up to length 8192.

## Claim scope

Synthetic KV-level attention reconstruction with oracle anchor positions: exact anchor retention plus count-corrected flat summaries preserves anchor-targeted attention outputs and beats uniform/recent/evenly-spaced controls at 8x-33x compression, but tested hierarchical variants do not beat the flat exact-anchor control.

## Why it stopped

Bounded synthetic evidence supports exact anchors but does not support the hierarchical component; the result is not a direct/full validation and is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replace oracle anchors with a detector in a small real transformer and compare exact-anchor flat against stronger KV compression baselines before revisiting hierarchy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle exact-anchor KV compression in a small transformer
- Success threshold: At 4x or greater KV compression, non-oracle exact-anchor flat should retain at least 90% of full-KV retrieval accuracy or keep perplexity degradation under 5%, while beating uniform summaries and recent-window retention by at least 20% relative error on the primary task metric.
- Stop condition: Stop if non-oracle anchor detection fails to recover at least half of the oracle benefit or if exact-anchor flat no longer beats simple summaries under matched KV budgets.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-hierarchical-kv-compression-for-long-documents-178676c900d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
