# Evidence-Ledger Rollback for Safer CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-for-safer-cpu-agents-dd0fef2a67f7`
Run ID: `evidence-ledger-rollback-for-safer-cpu-agents-dd0fef2a67f7-20260525T061031013499+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4f14132308e8

## What looked useful

The mechanism converted corrupted-context and stale-version unsafe commits into evidence rejections or postcheck rollbacks over 240,000 paired synthetic runs, at the cost of lower task-success rate when unsafe baseline commits would have changed the target anyway.

## Boundaries and scale limits

Synthetic single-action benchmark only; no real LLM planner, shell execution, filesystem side effects, multi-step tasks, adversarial evidence poisoning, or partial rollback failure modes were tested.

## Claim scope

In a deterministic synthetic CPU-agent state-mutation proxy with trusted task/state evidence, noisy planner context, and a 0.05 external version race rate, evidence-ledger precondition checks plus snapshot rollback reduced unsafe committed mutations from 0.05225-0.76445 under baseline to 0.0 across tested corruption rates.

## Why it stopped

Current run provides a useful synthetic mechanism signal but not direct real-agent evidence; finalize as no-paper rather than overclaiming.

## Recommended next action

Run a direct file-system agent harness with recorded or LLM-generated shell task traces, evidence poisoning controls, and multi-step rollback persistence checks before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger rollback on real file-system CPU-agent tasks
- Success threshold: Guarded executor reduces unsafe persistent side effects by at least 75% relative to baseline at corruption rates >=0.1 while preserving at least 80% of baseline success on clean-context tasks.
- Stop condition: Stop if guarded execution fails to reduce unsafe side effects by 50% in the first 100 paired direct file-task runs or if rollback frequently corrupts unrelated state.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-for-safer-cpu-agents-dd0fef2a67f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
