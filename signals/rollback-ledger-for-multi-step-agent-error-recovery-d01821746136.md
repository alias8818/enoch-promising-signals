# Rollback ledger for multi-step agent error recovery

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `rollback-ledger-for-multi-step-agent-error-recovery-d01821746136`
Run ID: `rollback-ledger-for-multi-step-agent-error-recovery-d01821746136-20260527T144554888264+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d359c38564ef

## What looked useful

The rollback ledger achieved 1.0 success rate in the main synthetic run, matching restart, while reducing mean executed actions from 367.896 to 88.861 and rollback/replay actions from 287.896 to 8.861. Naive local retry left stale dependent state, with 0.199 success rate and 15.192 mean final mismatches.

## Boundaries and scale limits

Tested only in a local CPU-only simulator: 1,000-trial main run with 80-step plans plus nine 500-trial sensitivity settings. No real LLM agents, external tools, irreversible side effects, concurrent execution, noisy detectors, or LangGraph integration were evaluated.

## Claim scope

In deterministic synthetic dependent-state workflows with perfect eventual error detection and reversible writes, a dependency-aware rollback ledger preserved final-state correctness like whole-prefix restart while substantially reducing replay work.

## Why it stopped

Synthetic evidence supports the mechanism but is not direct agent/tool evidence and cannot justify a paper-positive decision.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement the ledger in a small LangGraph-style reversible tool harness with noisy delayed detectors and compare against restart, retry, and checkpoint restore.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rollback ledger in a reversible LangGraph tool-agent harness
- Success threshold: Rollback ledger matches restart task success within 2 percentage points while reducing mean recovery actions by at least 30% and introducing less than 15% normal-path overhead versus no-ledger execution.
- Stop condition: Stop if ledger correctness falls more than 2 percentage points below restart, if dependency uncertainty causes unrecoverable side effects in more than 5% of tasks, or if overhead exceeds replay savings.

## Evidence references

- Artifact root: `<local-path>/projects/rollback-ledger-for-multi-step-agent-error-recovery-d01821746136`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
