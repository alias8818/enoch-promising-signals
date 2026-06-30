# Tiered Verification Cascade for Local Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiered-verification-cascade-for-local-agent-reliability-f680fcc16f76`
Run ID: `tiered-verification-cascade-for-local-agent-reliability-f680fcc16f76-20260605T214316012868+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1fd369b1bf6e

## What looked useful

Across five 5,000-task seeds, cascade accuracy averaged 0.9043 at 8.8255 relative cost units and invoked the expensive verifier on 46.56% of tasks; no verification averaged 0.5878 accuracy at 1.0 cost, and always-oracle averaged 0.9978 accuracy at 16.2 cost.

## Boundaries and scale limits

Proxy-only evidence from a surrogate agent; no real LLM traces, no measured token/wall-clock verifier cost, and exact generated-task ground truth is available to the expensive verifier.

## Claim scope

In a reproducible synthetic local-agent proxy with arithmetic, string, and JSON tasks, a tiered verifier cascade improves accuracy/cost tradeoff over no verification, cheap-only checks, and self-consistency-only, while using substantially less expensive verification than always-oracle.

## Why it stopped

Closed as proxy useful signal, not full validation; evidence supports the mechanism only in a surrogate benchmark and is insufficient for a paper-positive local-agent reliability claim.

## Recommended next action

Run a bounded real-agent deepen test on 200-500 deterministic tasks using a local open model, measured verifier wall-clock/token cost, and the same baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real local-model tiered verification cascade on deterministic tasks
- Success threshold: Cascade retains at least 70% of always-expensive accuracy gain over no verification and reduces expensive-verifier calls by at least 40%, with no task family showing a statistically clear regression versus no verification.
- Stop condition: Stop if cascade accuracy gain is below 50% of always-expensive gain, expensive-verifier reduction is below 25%, or one task family regresses versus no verification after 200 evaluated tasks.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-verification-cascade-for-local-agent-reliability-f680fcc16f76`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
