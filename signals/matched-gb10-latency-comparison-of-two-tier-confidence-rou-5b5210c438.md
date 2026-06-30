# Matched GB10 Latency Comparison of Two-Tier Confidence Routing Versus Early-Exit Serving

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `matched-gb10-latency-comparison-of-two-tier-confidence-rou-5b5210c438`
Run ID: `matched-gb10-latency-comparison-of-two-tier-confidence-rou-5b5210c438-20260610T140044822464+0000`

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

- Parent run decision: Confidence-Thresholded Two-Tier Local Cascade on gb10: enoch://control-plane/projects/confidence-thresholded-two-tier-local-cascade-on-gb10-776064df95aa/runs/confidence-thresholded-two-tier-local-cascade-on-gb10-776064df95aa-20260610T073430945187+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/01fe695f76d4

## What looked useful

Under matched branch outcomes, two-tier routing failed the latency threshold. It was 14.5% to 32.6% slower by median at 25% and 50% easy mixed workloads, and only 1.4% to 2.1% faster by median at 75% easy while regressing p95 latency by about 32%. Early-exit benefited from reusing early compute on fallback.

## Boundaries and scale limits

Small synthetic models with random weights; confidence outcomes were scheduled by easy_fraction rather than learned; no production inference engine, trained task quality, batching policy, KV-cache, or real traffic trace was tested.

## Claim scope

Controlled small GB10 CUDA latency comparison of two-tier routing versus early-exit serving with matched branch decisions on transformer-like PyTorch inference shapes.

## Why it stopped

Controlled small direct GB10 latency evidence did not support two-tier confidence routing over early-exit serving; this is not a full validation because confidence quality and production serving were not tested.

## Recommended next action

Stop this latency-only branch as an early negative; if continuing the line, run a bounded trained/calibrated quality-matched comparison rather than another synthetic branch-schedule latency test.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quality-matched trained confidence comparison for two-tier routing versus early-exit serving
- Success threshold: At matched task quality and matched request set, two-tier routing must reduce median latency by at least 10% on a mixed workload while keeping p95 latency no worse than early-exit.
- Stop condition: Stop if two-tier routing is not at least 10% faster by median without p95 regression at two or more nontrivial fallback rates, or if task-quality parity cannot be achieved with the small local model.

## Evidence references

- Artifact root: `<local-path>/projects/matched-gb10-latency-comparison-of-two-tier-confidence-rou-5b5210c438`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
