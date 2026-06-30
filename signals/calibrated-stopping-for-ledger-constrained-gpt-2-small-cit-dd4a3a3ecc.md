# Calibrated stopping for ledger-constrained GPT-2-small citation selection

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `calibrated-stopping-for-ledger-constrained-gpt-2-small-cit-dd4a3a3ecc`
Run ID: `calibrated-stopping-for-ledger-constrained-gpt-2-small-cit-dd4a3a3ecc-20260528T161754013823+0000`

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

- Parent run decision: Citation-only ledger constraints for GPT-2-small evidence agents: enoch://control-plane/projects/citation-only-ledger-constraints-for-gpt-2-small-evidence-b1dda55212/runs/citation-only-ledger-constraints-for-gpt-2-small-evidence-b1dda55212-20260528T130513255801+0000
- Parent run decision: Evidence-Ledger Constrained Tool Agent on GPT-2-Small: enoch://control-plane/projects/evidence-ledger-constrained-tool-agent-on-gpt-2-small-f5daa35ce757/runs/evidence-ledger-constrained-tool-agent-on-gpt-2-small-f5daa35ce757-20260528T085623358380+0000

## What looked useful

Across seeds 11, 23, and 37, calibrated GPT-2 stopping averaged macro F1 0.0128 and hit rate 0.0222 at 2.48 citations/query; fixed top-3 GPT-2 averaged macro F1 0.0159 and hit rate 0.0333; BM25 top-3 averaged macro F1 0.3527 and hit rate 0.7000.

## Boundaries and scale limits

Tested on 300 SciFact judged queries and 5,183 candidate abstracts with three fixed calibration/test seeds. This does not cover fine-tuned GPT-2 rankers, prompted/generative citation selection, larger transformer retrievers, or production-scale ledgers.

## Claim scope

On BEIR SciFact with a frozen GPT-2-small hidden-state embedding scorer and an average three-citation ledger, calibrated stopping does not improve held-out citation selection over fixed top-3 GPT-2 and is far below a BM25 top-3 baseline.

## Why it stopped

Tier-2 held-out evidence directly falsifies the calibrated stopping hypothesis for this frozen GPT-2-small scorer: the ranking signal is too weak, calibrated stopping underperforms fixed GPT-2 top-3 on average, and both are far below BM25.

## Recommended next action

Stop this line as a no-paper negative for frozen GPT-2-small embedding citation selection; only revisit if a stronger GPT-2-small first-stage citation scorer is specified and benchmarked against BM25 first.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-stopping-for-ledger-constrained-gpt-2-small-cit-dd4a3a3ecc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
