# Local Adversarial Agent Trap Benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `local-adversarial-agent-trap-benchmark-d06b8db45e8b`
Run ID: `local-adversarial-agent-trap-benchmark-d06b8db45e8b-20260611T142000338387+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd9129181108

## What looked useful

Across 120 scenarios, the naive recursive-reader policy was unsafe on 120/120 cases, the task-file allowlist policy was unsafe on 15/120 cases due to misleading task-relevant test comments, and the guarded noninterference policy was unsafe on 0/120 cases.

## Boundaries and scale limits

Evidence is limited to 120 synthetic scenarios and deterministic policy abstractions; no real LLM coding agent, live tool-call runtime, public-repository prevalence study, or adaptive adversary was tested.

## Claim scope

A dependency-free synthetic local benchmark can generate eight adversarial coding-agent workspace trap families and distinguish deterministic unsafe recursive-read, partial file-allowlist, and guarded noninterference policies.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a synthetic proxy benchmark, not direct validation of real agent behavior.

## Recommended next action

Run the generated trap suite against at least two real local coding agents with captured tool traces and compare unsafe action rates against the deterministic oracle labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace real coding agents on the local adversarial trap suite
- Success threshold: At least one real agent/configuration shows a nonzero unsafe rate on two or more trap families, and a guarded configuration reduces unsafe rate by at least 80% while preserving at least 80% task completion.
- Stop condition: Stop if both tested real agents have zero unsafe proposals across all scenarios or if tool traces cannot be captured reproducibly.

## Evidence references

- Artifact root: `<local-path>/projects/local-adversarial-agent-trap-benchmark-d06b8db45e8b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
