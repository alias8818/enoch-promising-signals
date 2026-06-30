# Evidence Ledger for Tiny CPU Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-tiny-cpu-agent-reliability-e63a222e3265`
Run ID: `evidence-ledger-for-tiny-cpu-agent-reliability-e63a222e3265-20260604T113721280367+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4f69b55a54be

## What looked useful

Across 600,000 trials per agent, the evidence ledger reduced aggregate false commit rate from 0.0531 for the strongest baseline, abstaining weighted vote, to 0.0142, a 73.3% relative reduction, while lowering coverage from 84.8% to 58.9%.

## Boundaries and scale limits

Synthetic categorical facts only; no real LLM, no real tool APIs, no long-horizon planning, no learned source calibration, and fixed thresholds. The result supports a bounded mechanism, not broad tiny CPU agent reliability.

## Claim scope

In a deterministic synthetic noisy-observation fact-recovery benchmark, a provenance-aware evidence ledger with source-diversity caps and contradiction-margin abstention reduced false commitments for a tiny CPU decision agent compared with latest-wins, majority, weighted-vote, and abstaining weighted-vote baselines.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and shows a reliability/coverage tradeoff rather than publication-grade validation of real tiny CPU agent reliability.

## Recommended next action

Run a bounded real-agent harness with a CPU-runnable tiny model or scripted ReAct agent on multi-step tool tasks with injected noisy/stale observations, equalized observation budgets, and reliability/coverage frontier metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Tiny-Agent Evidence Ledger Harness Under Injected Tool Noise
- Success threshold: At least 40% relative false-final-answer reduction versus the best calibrated abstaining baseline at no less than 50% coverage across three or more nonzero noise settings.
- Stop condition: Stop if ledger advantage disappears after calibration, coverage falls below 50% at useful noise levels, or task success does not improve at any comparable false-answer rate.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tiny-cpu-agent-reliability-e63a222e3265`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
