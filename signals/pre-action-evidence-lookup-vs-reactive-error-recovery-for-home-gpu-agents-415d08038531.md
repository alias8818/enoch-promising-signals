# Pre-Action Evidence Lookup vs Reactive Error Recovery for Home GPU Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pre-action-evidence-lookup-vs-reactive-error-recovery-for-home-gpu-agents-415d08038531`
Run ID: `pre-action-evidence-lookup-vs-reactive-error-recovery-for-home-gpu-agents-415d08038531-20260630T120314887734+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6535d1d4d6f9

## What looked useful

Across 72 controlled scenarios with 10,000 tasks per policy per scenario, pre-action lookup was faster in 48 scenarios overall and 40 of 48 scenarios with hazard_rate >= 0.10, but only 8 of 24 low-hazard scenarios. Mean reactive-minus-pre time was +2.896 relative units and mean reactive-minus-pre failures was +2.733.

## Boundaries and scale limits

Proxy-only simulation; no real home-GPU agent traces, live documentation lookups, model recovery behavior, or repository workload distribution were measured.

## Claim scope

In a deterministic synthetic benchmark of local-agent tool hazards, pre-action evidence lookup beats reactive recovery in most medium/high hazard regimes but loses when hazards are rare or lookup evidence is weak or stale.

## Why it stopped

Synthetic proxy supports a conditional mechanism but is not direct/full validation of real home-GPU agents.

## Recommended next action

Stop this run as proxy useful-signal evidence; next run should collect trace-backed metrics from real local coding-agent tasks with selective lookup versus reactive recovery.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-backed selective lookup benchmark for local coding agents
- Success threshold: Selective lookup achieves at least 15% lower median wall-clock time or at least 30% fewer failed actions than reactive-only without lowering task success rate.
- Stop condition: Stop if selective lookup does not improve either median wall-clock time or failed-action count after the labeled task set, or if instrumentation cannot distinguish lookup-caused stale errors from ordinary failures.

## Evidence references

- Artifact root: `<local-path>/projects/pre-action-evidence-lookup-vs-reactive-error-recovery-for-home-gpu-agents-415d08038531`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
