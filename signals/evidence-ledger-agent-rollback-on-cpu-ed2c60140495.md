# Evidence-ledger agent rollback on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-rollback-on-cpu-ed2c60140495`
Run ID: `evidence-ledger-agent-rollback-on-cpu-ed2c60140495-20260524T194945257712+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5cef9dde20c1

## What looked useful

Rollback achieved 100% success at 5%, 10%, 20%, 30%, and 50% injected claim corruption and 97% success at 70%, while no-rollback reached 19%, 6%, then 0% from 5% upward in main/stress conditions; full restart exhausted the 8x action budget at moderate/high corruption and fell to 0% success from 20% upward.

## Boundaries and scale limits

Synthetic proxy only: no real LLM calls, no real external tool side effects, 64-fact tasks, 100-200 seeds per condition, single-process CPU execution, controlled independent corruption rather than realistic model/tool error distributions.

## Claim scope

In a deterministic synthetic fact-gathering harness on CPU, per-step evidence validation plus single-step rollback recovered from injected corrupted intermediate claims more reliably than no rollback and more efficiently than full restart under a fixed action budget.

## Why it stopped

Synthetic proxy evidence supports the mechanism but is insufficient for publication-grade claims about real agents or production rollback.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should embed the same ledger/rollback policy in a real tool-using LLM agent harness with induced tool/model errors and selective-retry baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger rollback in a real tool-using LLM agent harness
- Success threshold: At least 15 percentage-point absolute task-success improvement over the best non-rollback baseline, or at least 25% lower token/tool cost at matched success, across two or more task families with no unresolved side-effect corruption.
- Stop condition: Stop if rollback does not beat the best baseline on either task success or cost in the first two task families, or if side effects cannot be reliably checkpointed and restored.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-rollback-on-cpu-ed2c60140495`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
