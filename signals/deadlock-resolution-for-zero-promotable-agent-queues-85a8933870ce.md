# Deadlock Resolution for Zero-Promotable Agent Queues

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deadlock-resolution-for-zero-promotable-agent-queues-85a8933870ce`
Run ID: `deadlock-resolution-for-zero-promotable-agent-queues-85a8933870ce-20260602T171023468081+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/77930d8ad634

## What looked useful

A resolver should classify blockers before promotion. SCC-targeted soft unblocking reduces relaxations in all-soft cases but cannot improve success when a hard dependency cycle remains. Completing all-hard queues requires hard-edge violations in the invalid control.

## Boundaries and scale limits

Tested on synthetic queues of 12, 32, and 96 nodes with 200 trials per configuration. This is not production LangGraph/Enoch trace replay and does not validate real operator recovery behavior.

## Claim scope

Synthetic wait-for queues with explicit hard and soft blockers: valid zero-promotable deadlock resolution succeeds only when cyclic blockers include relaxable soft edges; all-hard cycles require invariant violation or external graph-changing intervention.

## Why it stopped

Synthetic mechanism evidence supports the invariant boundary but is not direct production evidence or paper-ready validation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded step is replaying real zero-promotable queue traces with hard/soft blocker classification and SCC-targeted soft unblocking.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace Replay for Hard-vs-Soft Zero-Promotable Queue Recovery
- Success threshold: At least 20 real or replayed zero-promotable incidents; zero hard-invariant violations; SCC-targeted recovery matches or exceeds random valid completion rate and reduces median interventions by at least 25%.
- Stop condition: Stop if blocker labels cannot be reconstructed, if fewer than 10 usable zero-promotable incidents are available, or if any SCC-targeted recovery requires a hard-invariant violation.

## Evidence references

- Artifact root: `<local-path>/projects/deadlock-resolution-for-zero-promotable-agent-queues-85a8933870ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
