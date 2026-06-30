# Cascade Agent: Escalate on Tool-Call Failure or Low Confidence

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cascade-agent-escalate-on-tool-call-failure-or-low-confidence-51b0052d5191`
Run ID: `cascade-agent-escalate-on-tool-call-failure-or-low-confidence-51b0052d5191-20260614T081152045672+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e6034c628f0

## What looked useful

Low-confidence escalation is promising as a calibrated, budget-aware cascade trigger, but the run found a concrete boundary condition: with uninformative confidence and high escalation cost, tool-failure-only escalation slightly wins.

## Boundaries and scale limits

Synthetic traces only; no real LLM confidence, real tool failures, real user tasks, LangGraph integration, or production latency/cost measurements were tested. Thresholds were selected on the same synthetic population, so deployment claims require held-out trace validation.

## Claim scope

In a deterministic synthetic cascade-agent simulation with 100,000 tasks per scenario, escalating after tool-call failure or low primary confidence improved success/cost utility over tool-failure-only escalation when confidence was calibrated or partially informative; the benefit narrowed or reversed when confidence was uninformative and escalation was expensive.

## Why it stopped

No-paper closure because the evidence is synthetic/proxy-only and threshold-optimized, not direct publication-grade validation.

## Recommended next action

Stop this run as a synthetic useful signal; next run should replay the same policies on real or scripted agent traces with held-out threshold selection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay confidence-and-tool-failure cascade policies on real agent traces
- Success threshold: Held-out low-confidence escalation improves utility over tool-failure-only by at least 0.02 absolute with bootstrap p05 delta above 0 in at least two realistic trace categories, without more than 3x average cost.
- Stop condition: Stop as unsupported if held-out utility delta is non-positive, if gains require test-set threshold tuning, or if average cost exceeds 3x tool-failure-only for less than 0.02 utility gain.

## Evidence references

- Artifact root: `<local-path>/projects/cascade-agent-escalate-on-tool-call-failure-or-low-confidence-51b0052d5191`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
