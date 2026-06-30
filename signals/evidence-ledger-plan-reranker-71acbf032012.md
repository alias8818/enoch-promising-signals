# Evidence Ledger Plan Reranker

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-plan-reranker-71acbf032012`
Run ID: `evidence-ledger-plan-reranker-71acbf032012-20260603T171013878929+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/788c4883ed21

## What looked useful

On 3,250 held-out synthetic test cases, ledger reranking reached 0.8997 top-1 accuracy versus 0.1440 for score-only; bootstrap delta CI was [0.7403, 0.7698]. A 15-run robustness sweep across score-noise settings and seeds had mean delta 0.7509, min delta 0.6600, and all bootstrap lower bounds positive.

## Boundaries and scale limits

Synthetic benchmark only; no real LLM-generated plans, no natural-language entailment extraction, no human labels, no open-domain retrieval noise, and no end-to-end agent task success measurement.

## Claim scope

A structured evidence-ledger reranker improved held-out top-1 selection accuracy over noisy score-only ranking on a synthetic plan-selection benchmark with explicit evidence IDs and injected evidence failure modes.

## Why it stopped

No-paper closure because the result is a proxy/synthetic validation of the mechanism, not direct publication-grade evidence on real planner traces.

## Recommended next action

Stop this run as useful synthetic evidence; next run should test the reranker on real LLM-generated candidate plans with manually auditable evidence labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-candidate evidence ledger reranking benchmark
- Success threshold: At least +10 percentage points top-1 valid-plan selection over the strongest non-ledger baseline on held-out real candidates, with bootstrap lower bound above zero and false rejection of valid plans below 10%.
- Stop condition: Stop if ledger reranking does not beat the strongest non-ledger baseline on held-out real candidates, if extraction noise dominates gains, or if latency/cost makes the method impractical for the target agent loop.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-plan-reranker-71acbf032012`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
