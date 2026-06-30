# Learned Task-Complexity Router for Local Cascade

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `learned-task-complexity-router-for-local-cascade-5cc4a7f7f200`
Run ID: `learned-task-complexity-router-for-local-cascade-5cc4a7f7f200-20260610T113441810110+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dc32965b9de5

## What looked useful

The mechanism is worth a direct LLM-cascade follow-up: after correcting the cascade to have a real cheap/strong capacity gap, learned routing beat confidence routing by +0.0042 to +0.0160 mean accuracy and +0.0034 to +0.0072 accuracy-per-cost across budgets, and beat confidence on cheap-error ROC AUC for all three datasets.

## Boundaries and scale limits

Proxy-only evidence: no local LLMs, prompts, answer quality judgments, token costs, serving latency, or production traffic were evaluated. Datasets are small built-in sklearn tasks; the cost model is normalized rather than measured serving cost.

## Claim scope

On three small sklearn tabular classification tasks with a shallow decision-tree cheap model and ExtraTrees strong model, a learned router using cheap-model telemetry and simple input statistics improved cascade accuracy and cost-normalized accuracy over confidence-threshold and random routing at 5%, 10%, 20%, and 35% escalation budgets across 30 stratified splits per dataset.

## Why it stopped

Closed as no-paper useful proxy signal: evidence supports the mechanism in a classifier cascade but does not directly validate a local LLM task-complexity router.

## Recommended next action

Run a bounded direct local LLM cascade follow-up using cheap and strong local models, real prompt tasks, measured latency/token cost, and the same learned-router versus confidence-threshold controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Local LLM Learned Router Benchmark
- Success threshold: At three or more escalation budgets, learned routing improves task quality over confidence-threshold routing by at least 1 percentage point or an equivalent judged-quality margin while preserving or improving quality-per-latency/cost.
- Stop condition: Stop if the learned router fails to beat confidence-threshold routing on both quality and quality-per-cost at most budgets, or if cheap-model telemetry is unavailable/reliably uninformative on the selected local LLM stack.

## Evidence references

- Artifact root: `<local-path>/projects/learned-task-complexity-router-for-local-cascade-5cc4a7f7f200`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
