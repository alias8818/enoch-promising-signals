# Real-trace replay of evidence-saturation termination for labeled agent tasks

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-trace-replay-of-evidence-saturation-termination-for-l-a6f74a99e0`
Run ID: `real-trace-replay-of-evidence-saturation-termination-for-l-a6f74a99e0-20260527T004303332048+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence Saturation Thresholds for Agent Loop Termination: enoch://control-plane/projects/evidence-saturation-thresholds-for-agent-loop-termination-2a6daa435a69/runs/evidence-saturation-thresholds-for-agent-loop-termination-2a6daa435a69-20260525T173101108804+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/12cd6f3c96f9

## What looked useful

Evidence-saturation thresholds over new-token yield preserved full-trace predictions only by stopping at the end of the median trace: best saturation median savings 0.000 with 0.9979 early/full agreement and 0.6392 accuracy. Fixed 75% replay saved only 0.241 median events and still lost 4.2 percentage points of accuracy.

## Boundaries and scale limits

Single local corpus; lexical token novelty rather than semantic evidence novelty; labels are Enoch decision labels, not human task-success labels; no external trace corpus tested.

## Claim scope

On 474 real local Enoch/Codex traces labeled by final hypothesis_status, a masked lexical evidence-saturation stop rule did not achieve early termination while preserving endpoint labels.

## Why it stopped

Controlled real-trace replay directly failed the pre-set threshold: no saturation grid point reached 25% median event savings while preserving endpoint labels.

## Recommended next action

Stop this saturation-threshold line as a no-paper negative result; a different phase-aware or semantic learned stop rule would need a new bounded mechanism test before escalation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-replay-of-evidence-saturation-termination-for-l-a6f74a99e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
