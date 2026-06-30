# BudgetLedger: Constraint-Compliance Evidence for Bounded Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `budgetledger-constraint-compliance-evidence-for-bounded-agents-3ae53dfa1c56`
Run ID: `budgetledger-constraint-compliance-evidence-for-bounded-agents-3ae53dfa1c56-20260609T224808555546+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4c3df127b157

## What looked useful

Across 5,000 primary 28-step episodes, BudgetLedger achieved 93.92% compliance versus 0% for FIFO context, 0% for lossy checklist, and 2.10% for a ledger without cumulative accounting; paired bootstrap improvement over no-accounting ledger was +0.9182 compliance, 95% CI [0.9104, 0.9256].

## Boundaries and scale limits

Evidence is rule-based and synthetic, not from real LLM agents or production tool-use tasks. BudgetLedger drops to 43.5% compliance at 48 steps because the online heuristic under-plans future evidence, while an offline oracle remains at 100%.

## Claim scope

Synthetic bounded-agent task episodes show that a structured BudgetLedger with exact cumulative accounting substantially reduces budget, prohibited-label, and approval violations versus recent-context, lossy-checklist, and no-accounting ledger controls at 12-28 step horizons.

## Why it stopped

Synthetic proxy supports the accounting mechanism but is not direct LLM evidence, and long-horizon 48-step stress exposes a planner-quality failure rather than a closed validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a small real LLM/tool-agent benchmark with context truncation and the same FIFO/checklist/no-accounting controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BudgetLedger on Small LLM Tool-Agent Constraint Tasks
- Success threshold: BudgetLedger compliance exceeds the best non-ledger control by at least 25 percentage points with a 95% bootstrap confidence interval excluding zero, and task success is no more than 10 percentage points worse than the best compliant baseline.
- Stop condition: Stop if BudgetLedger improves compliance by less than 10 percentage points over checklist/no-accounting controls or if task success drops by more than 20 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/budgetledger-constraint-compliance-evidence-for-bounded-agents-3ae53dfa1c56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
