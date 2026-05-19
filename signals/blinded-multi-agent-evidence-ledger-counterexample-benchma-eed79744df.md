# Blinded Multi-Agent Evidence Ledger Counterexample Benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `blinded-multi-agent-evidence-ledger-counterexample-benchma-eed79744df`
Run ID: `blinded-multi-agent-evidence-ledger-counterexample-benchma-eed79744df-20260517T134149557885+0000`

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

- Internal Enoch project: Blinded Multi-Agent Evidence Ledger Counterexample Benchmark: internal_generated:blinded-multi-agent-evidence-ledger-counterexample-benchma-eed79744df

## What looked useful

Tier 2 fixed-seed run covered 1200 tasks per method. Blinded evidence ledger reached 96.00% success versus 94.25% for the strong single-generalist baseline, 86.92% for unblinded multi-agent, and 80.67% for random search. Paired comparison versus the single-generalist baseline gave 54 ledger-only wins, 33 baseline-only wins, delta +1.75 percentage points, exact McNemar p=0.0314. The largest gain was on sparse-needle tasks: 83.0% versus 65.5% for the single-generalist baseline and 26.0% for unblinded multi-agent.

## Boundaries and scale limits

The run used generated integer-domain tasks and heuristic agents rather than real LLM agents, theorem-proving workloads, code-verification tasks, or human-audited evidence ledgers. The advantage over the strongest single-agent baseline was small and not uniform across task families.

## Claim scope

In a deterministic synthetic universal-claim counterexample benchmark with heuristic agents, fixed seeds, equal 120-query budgets, and checked evidence, a blinded role-diverse evidence ledger improves overall counterexample discovery over random search, unblinded multi-agent controls, same-policy blinded ablation, and a strong single-generalist baseline by a small margin.

## Why it stopped

Useful mechanism support but no paper-grade result: the evidence is synthetic/heuristic, the improvement over the strongest real baseline is small, and there is a task-family regression on boundary_low.

## Recommended next action

Stop paper escalation for this run; run one bounded deepen follow-up with actual local/open LLM or code-testing agents on natural-language counterexample tasks before making any broader claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-Agent Natural-Language Evidence Ledger Counterexample Benchmark
- Success threshold: Blinded evidence ledger improves checked counterexample discovery by at least 5 percentage points over the strong single-agent total-budget baseline, with paired p < 0.01 or bootstrap 95% CI excluding zero, and no major task family loses more than 2 percentage points.
- Stop condition: Stop as negative/no-paper if the ledger fails to beat the strong single-agent baseline by 5 percentage points, if gains are concentrated in one narrow family with regressions elsewhere, or if evidence checking cannot be made deterministic.

## Evidence references

- Artifact root: `<local-path>/projects/blinded-multi-agent-evidence-ledger-counterexample-benchma-eed79744df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
