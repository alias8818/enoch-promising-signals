# Real small-LLM tool-agent validation of multi-entry evidence ledgers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `real-small-llm-tool-agent-validation-of-multi-entry-eviden-c3b3b9a608`
Run ID: `real-small-llm-tool-agent-validation-of-multi-entry-eviden-c3b3b9a608-20260609T142755203380+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence-ledger wrapper for local small LLM tool agents: enoch://control-plane/projects/evidence-ledger-wrapper-for-local-small-llm-tool-agents-3113ecb421/runs/evidence-ledger-wrapper-for-local-small-llm-tool-agents-3113ecb421-20260609T033216769015+0000
- Parent run decision: Multi-entry evidence-ledger validation for local small tool agents: enoch://control-plane/projects/multi-entry-evidence-ledger-validation-for-local-small-too-468b930b29/runs/multi-entry-evidence-ledger-validation-for-local-small-too-468b930b29-20260609T070307330643+0000

## What looked useful

Across 5 seeds, 480 tasks per condition, the multi-entry ledger reached 0.3417 mean accuracy and 0.8500 citation recall. Plain transcript reached 0.3771 accuracy and single summary reached 0.4083 accuracy. Ledger accuracy deltas were -0.0354 versus transcript and -0.0667 versus summary, while citation recall improved sharply only when source IDs were explicitly shown.

## Boundaries and scale limits

Synthetic deterministic tools; final evidence-use step only; one fully validated non-degenerate small instruction model; Qwen2.5-0.5B-Instruct smoke tests were answer-collapsed; no live external tools or multi-model robustness sweep.

## Claim scope

On deterministic claim-matching tool-evidence tasks with SmolLM2-1.7B-Instruct, explicit multi-entry evidence ledgers improve source-id citation recall but do not improve final answer accuracy versus plain transcript or single-summary baselines.

## Why it stopped

Bounded direct validation found a useful auditability mechanism but falsified the stronger answer-accuracy claim against evidence-present baselines.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded adjacent test should remove answer-position bias and test whether ledger citation gains persist with semantic answer labels or forced option comparison.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Position-bias-controlled evidence ledger validation with semantic answer labels
- Success threshold: Ledger condition must improve answer accuracy by at least 3 percentage points over both transcript and single-summary baselines while maintaining citation recall above 0.75 and unsupported citation rate below 0.05.
- Stop condition: Stop if a smoke run over 50 tasks per condition shows prediction mass above 80% on one answer label for every tested small model, or if the full run again shows ledger accuracy below either evidence-present baseline.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-llm-tool-agent-validation-of-multi-entry-eviden-c3b3b9a608`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
