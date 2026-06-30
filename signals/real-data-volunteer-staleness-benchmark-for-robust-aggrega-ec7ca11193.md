# Real-data volunteer staleness benchmark for robust aggregation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-data-volunteer-staleness-benchmark-for-robust-aggrega-ec7ca11193`
Run ID: `real-data-volunteer-staleness-benchmark-for-robust-aggrega-ec7ca11193-20260628T061946869775+0000`

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

- Parent run decision: Byzantine-Robust Aggregation on Simulated Volunteer Cluster: enoch://control-plane/projects/byzantine-robust-aggregation-on-simulated-volunteer-cluster-42f8a9402ba0/runs/byzantine-robust-aggregation-on-simulated-volunteer-cluster-42f8a9402ba0-20260628T055947486429+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/befc816e0544

## What looked useful

The harness produced reproducible evidence that coordinate-wise median and plain staleness decay are weak in this setting; trimmed/staleness-aware methods slightly improved average loss in the normal condition and improved average loss by about 0.012-0.014 under the stress condition, but seed-wise wins were inconsistent.

## Boundaries and scale limits

One small tabular dataset, logistic model, simulated volunteer delays/faults, five seeds per condition, no real volunteer trace, no large neural model, and no multi-dataset validation.

## Claim scope

A small direct real-data benchmark on UCI Wine Quality red with simulated non-IID stale volunteers shows robust/staleness-aware aggregation is viable to test and can reduce average loss under harsher stale faulty-volunteer stress, but the effect is inconsistent across seeds and not paper-ready.

## Why it stopped

Tier 1 direct evidence is mixed: robust/staleness-aware aggregation has a useful stress-condition signal but does not consistently beat plain mean across seeds, so this is no-paper evidence rather than a paper-positive result.

## Recommended next action

Run a bounded deepen test on two additional real datasets or a real volunteer trace with a pre-registered threshold of at least 0.01 mean loss reduction and at least 4/5 paired seed wins over mean aggregation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-dataset paired benchmark for stale robust volunteer aggregation
- Success threshold: At least 0.01 mean test-loss reduction versus plain mean and at least 4/5 paired seed wins on each added dataset or trace.
- Stop condition: Stop if robust/staleness-aware methods fail the threshold on either added dataset/trace or if gains are dominated by a single seed/outlier condition.

## Evidence references

- Artifact root: `<local-path>/projects/real-data-volunteer-staleness-benchmark-for-robust-aggrega-ec7ca11193`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
