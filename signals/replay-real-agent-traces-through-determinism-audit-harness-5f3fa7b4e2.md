# Replay real agent traces through determinism-audit harness

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `replay-real-agent-traces-through-determinism-audit-harness-5f3fa7b4e2`
Run ID: `replay-real-agent-traces-through-determinism-audit-harness-5f3fa7b4e2-20260620T173039803137+0000`

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

- Parent run decision: Determinism-Audit Repro Harness for Agent Reliability: enoch://control-plane/projects/determinism-audit-repro-harness-for-agent-reliability-c9b79c01d66c/runs/determinism-audit-repro-harness-for-agent-reliability-c9b79c01d66c-20260620T171327304002+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e42eb863dd25

## What looked useful

The harness mechanics work on bounded trace fixtures: exact replay stability, volatile-field invariance, and semantic drift detection each reached 1.0 pass rate with zero failed traces.

## Boundaries and scale limits

No real private or production agent trace corpus was present in the workspace. Evidence is limited to small in-project fixtures and does not establish robustness across real traces, longer sessions, tool diversity, or noisy historical logs.

## Claim scope

A local Tier 1 determinism-audit harness replayed 3 in-project agent-like trace fixtures with 16 total events and 7 repetitions per trace, achieving stable exact hashes, volatile-field invariance, and semantic mutation detection.

## Why it stopped

Tier 1 mechanism test passed, but the original real-agent-trace claim was not directly validated because no real trace corpus was available in the worker workspace.

## Recommended next action

Stop this run as no-paper useful signal; deepen only if an anonymized small real trace corpus can be added and replayed through the same audit with manual spot checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay anonymized real agent traces through the determinism-audit harness
- Success threshold: At least 0.95 exact replay stability, 0.95 volatile-field invariance, and 0.95 semantic mutation detection on the anonymized real trace corpus, with no severe manual spot-check failures.
- Stop condition: Stop if no real trace corpus is available, if redaction removes semantic fields needed for audit, or if any core rate falls below 0.90 after one documented canonicalization adjustment.

## Evidence references

- Artifact root: `<local-path>/projects/replay-real-agent-traces-through-determinism-audit-harness-5f3fa7b4e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
