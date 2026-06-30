# Mandatory Evidence-Ledger Agent on Local Multi-Step Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `mandatory-evidence-ledger-agent-on-local-multi-step-tasks-ca4212a93153`
Run ID: `mandatory-evidence-ledger-agent-on-local-multi-step-tasks-ca4212a93153-20260611T110701531659+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e59f60beba17

## What looked useful

Mandatory current-evidence checks reduced stale-write rate from 75% for a plan-once baseline to 0% on controlled inventory, orders, and policy drift variants, with about 0.079 ms mean overhead per tiny task.

## Boundaries and scale limits

Tested only 200 generated local tasks with hand-coded deterministic agents; no LLM agent, real repository workflow, human review burden, adversarial evidence fabrication, or long-horizon task behavior was measured.

## Claim scope

In a synthetic deterministic local file-task harness with controlled source drift, a mandatory evidence-ledger agent that validates current file hashes before writing eliminated stale-evidence writes made by a plan-once baseline.

## Why it stopped

Synthetic/proxy mechanism probe completed successfully, but it is not direct publication-grade evidence for LLM agents or real multi-step local workflows.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test the same protocol with an actual LLM file/coding agent on hidden-drift local tasks and include a reverify-only ablation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM File-Agent Evidence Ledger on Hidden-Drift Local Tasks
- Success threshold: Ledger agent reduces stale/unsupported writes by at least 50% relative to both baselines without reducing no-drift task success by more than 10 percentage points.
- Stop condition: Stop if the ledger agent fails to improve stale/unsupported-write rate on a 30-task smoke set or if overhead/refusal rate makes no-drift task success fall more than 10 percentage points below baseline.

## Evidence references

- Artifact root: `<local-path>/projects/mandatory-evidence-ledger-agent-on-local-multi-step-tasks-ca4212a93153`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
