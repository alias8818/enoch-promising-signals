# Calibration-gated cascade on real local-agent task traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `calibration-gated-cascade-on-real-local-agent-task-traces-2a43cbaa2d`
Run ID: `calibration-gated-cascade-on-real-local-agent-task-traces-2a43cbaa2d-20260619T053944207478+0000`

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

- Parent run decision: Calibration-Gated Cascade for Local Agents: enoch://control-plane/projects/calibration-gated-cascade-for-local-agents-0d39d3f80c1a/runs/calibration-gated-cascade-for-local-agents-0d39d3f80c1a-20260619T051922104151+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/886dd2a97b95

## What looked useful

The calibration gate passed the pre-registered threshold of at least 95% accepted accuracy and at least 25% accepted coverage on random and project-heldout real local-agent traces. Ten project-heldout seeds gave accepted accuracy mean/min/max 0.9814/0.9800/0.9840 and accepted fraction mean/min/max 0.8758/0.8690/0.8857.

## Boundaries and scale limits

This is Tier 1 trace evidence only. The cheap stage predicts command success/failure from command text, not task completion quality. The strong stage is an oracle simulation from recorded labels, not a live larger local model. Cost reduction is based on an illustrative cheap=0.10 and strong=1.00 model, not measured serving latency or token cost.

## Claim scope

On about 81k real local Enoch/Codex command-execution trace samples, a dependency-free calibrated cheap command-outcome predictor can gate a simulated cascade: on project-heldout splits it accepted about 87.6% of heldout samples with about 98.1% accepted accuracy while escalating the rest to an oracle verifier stage.

## Why it stopped

Tier 1 mechanism support was obtained on real traces, but paper readiness is blocked by the oracle strong-stage proxy and command-outcome target.

## Recommended next action

Run a bounded live two-stage local-agent replay on fixed heldout tasks, comparing cheap-only, strong-only, and calibrated cascade routing with measured latency/cost and task-quality outcomes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live two-stage calibrated cascade on heldout local-agent tasks
- Success threshold: Cascade task success at least 95% of strong-only success with at least 40% fewer strong-model calls and no more than 5% absolute increase in failed tasks.
- Stop condition: Stop if calibrated routing cannot reach 95% of strong-only success at any threshold that reduces strong-model calls by at least 25%, or if live task variance prevents a stable comparison within the bounded task set.

## Evidence references

- Artifact root: `<local-path>/projects/calibration-gated-cascade-on-real-local-agent-task-traces-2a43cbaa2d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
