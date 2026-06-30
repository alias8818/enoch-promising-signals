# Live two-stage calibrated cascade on heldout local-agent tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-two-stage-calibrated-cascade-on-heldout-local-agent-t-868a913737`
Run ID: `live-two-stage-calibrated-cascade-on-heldout-local-agent-t-868a913737-20260619T063427889536+0000`

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

- Parent run decision: Calibration-gated cascade on real local-agent task traces: enoch://control-plane/projects/calibration-gated-cascade-on-real-local-agent-task-traces-2a43cbaa2d/runs/calibration-gated-cascade-on-real-local-agent-task-traces-2a43cbaa2d-20260619T053944207478+0000
- Parent run decision: Calibration-Gated Cascade for Local Agents: enoch://control-plane/projects/calibration-gated-cascade-for-local-agents-0d39d3f80c1a/runs/calibration-gated-cascade-for-local-agents-0d39d3f80c1a-20260619T051922104151+0000

## What looked useful

Across five fixed seeds with 1,200 calibration and 5,000 heldout tasks per seed, calibrated confidence ECE improved from 0.3211 to 0.0889, but the calibrated cascade achieved 0.9829 accuracy with only 21.4% cost reduction versus always-strong. The raw-confidence cascade was essentially tied/slightly better at 0.9833 accuracy and 21.3% cost reduction. A loss sweep up to 5 percentage points allowed accuracy loss still reached only 27.2% calibrated cost reduction.

## Boundaries and scale limits

Local executable task benchmark only; cheap and strong agents are deterministic programmatic agents rather than real LLM/tool-use agents; costs are modeled latency units, not measured token or model-serving wall-clock costs.

## Claim scope

On a reproducible heldout benchmark of deterministic arithmetic, string, and JSON local-agent tasks, Platt calibration substantially improved cheap-agent confidence calibration but a two-stage calibrated threshold cascade did not meet the Tier 2 cost/accuracy threshold or beat a raw-confidence cascade.

## Why it stopped

Tier 2 direct heldout validation missed the stated threshold: calibrated routing reduced cost by 21.4%, below the 30% target, and did not outperform raw-confidence routing.

## Recommended next action

Stop this calibration-only thresholding line as no-paper evidence; if continuing locally, test a family-aware learned router that can change ranking rather than only recalibrate confidence magnitudes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Family-aware learned router for heldout local-agent cascades
- Success threshold: At least 30% cost reduction versus always-strong with heldout accuracy no more than 2 percentage points below always-strong, and at least 5 percentage points more cost reduction than both raw-confidence and calibrated-confidence threshold cascades at the same accuracy floor.
- Stop condition: Stop if the learned router cannot beat calibrated-confidence routing by at least 3 percentage points cost reduction at the 2-point accuracy floor or if any task family regresses by more than 2 percentage points versus the calibrated cascade.

## Evidence references

- Artifact root: `<local-path>/projects/live-two-stage-calibrated-cascade-on-heldout-local-agent-t-868a913737`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
