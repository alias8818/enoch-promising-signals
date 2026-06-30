# Real-trace validation of safety-first cascade refusal routing

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `real-trace-validation-of-safety-first-cascade-refusal-rout-edbabae9e3`
Run ID: `real-trace-validation-of-safety-first-cascade-refusal-rout-edbabae9e3-20260522T074804214482+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Safety-First Cascade Router for Local Agent Refusal: enoch://control-plane/projects/safety-first-cascade-router-for-local-agent-refusal-7217e459d233/runs/safety-first-cascade-router-for-local-agent-refusal-7217e459d233-20260522T011259285938+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d176ef2f214d

## What looked useful

The cascade reduced unsafe false-allow / missed stop rate from 0.2967 to 0.0860, a 71.0% relative reduction, and used 22.8% of always-review cost with 20.0% defer rate. It failed the parent success threshold because safe false-refusal rose from 0.0836 to 0.5175, a +43.4 point increase, tripping the >+10 point stop condition.

## Boundaries and scale limits

Controller decisions are adjacent stop/refusal labels rather than independent human safety labels; Enoch project traces are not production local-agent traffic; the fallback reviewer is a lightweight local text model rather than a large instruction model or human reviewer; cost is relative model-call cost, not measured serving latency.

## Claim scope

On 204 locally mined real Enoch/OMX stop-versus-continue traces with six held-out task-family folds, a lexical plus cheap text classifier plus trained stronger local reviewer cascade reduced missed stop/refusal decisions versus a cheap direct classifier at low relative review cost, but severely over-refused continue traces.

## Why it stopped

Direct Tier 1 real-trace validation failed the stated utility threshold: despite safety and cost gains, the cascade increased safe false-refusal by +43.4 absolute percentage points versus the cheap direct classifier, exceeding the +10 point stop condition.

## Recommended next action

Stop this follow-up as no-paper mixed evidence; do not scale the current safety-first cascade without first adding an explicit over-refusal calibration/control mechanism and validating it on independent human-labeled local-agent safety traces.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-validation-of-safety-first-cascade-refusal-rout-edbabae9e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
