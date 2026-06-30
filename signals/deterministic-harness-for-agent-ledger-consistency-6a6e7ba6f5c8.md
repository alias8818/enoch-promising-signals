# Deterministic Harness for Agent Ledger Consistency

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-harness-for-agent-ledger-consistency-6a6e7ba6f5c8`
Run ID: `deterministic-harness-for-agent-ledger-consistency-6a6e7ba6f5c8-20260522T073734083060+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8b8a45c3f053

## What looked useful

The harness produced zero reference failures and detected all three injected ledger defects in 500/500 seeds each, with zero deterministic replay mismatches and median minimized failure length of 2 events.

## Boundaries and scale limits

Evidence is limited to a local synthetic ledger, 500 deterministic seeds, 120 generated events per seed, and three injected defect classes. It does not validate production agent runtimes, distributed persistence, concurrency, crash recovery, or real external tool side effects.

## Claim scope

A dependency-free deterministic Python harness can reproduce and minimize consistency failures for a synthetic multi-agent ledger with transfer, reserve, commit, cancel, duplicate-event, conservation, and reservation invariants.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct production or paper-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is to adapt the harness to a real agent ledger implementation and replay recorded agent/tool traces with concurrency and persistence schedules.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deterministic Replay Adapter for a Real Agent Ledger
- Success threshold: On at least 100 recorded or semi-real traces, reference replay has zero unexplained invariant failures, at least two realistic injected or historical defects are detected reproducibly, and minimized counterexamples replay with zero digest mismatches.
- Stop condition: Stop if no real ledger adapter can be built locally, recorded traces cannot be obtained, or the harness cannot reproduce injected defects after 100 traces.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-harness-for-agent-ledger-consistency-6a6e7ba6f5c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
