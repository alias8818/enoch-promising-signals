# Real Trace Malformed Tool-Call Router Replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-trace-malformed-tool-call-router-replay-29f84610a7`
Run ID: `real-trace-malformed-tool-call-router-replay-29f84610a7-20260527T044504345810+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-Trace Validation of Tool-Call Validator Router: enoch://control-plane/projects/real-trace-validation-of-tool-call-validator-router-c48fccdb0d/runs/real-trace-validation-of-tool-call-validator-router-c48fccdb0d-20260526T152101262702+0000
- Parent run decision: Held-Out Natural Malformed Tool-Call Router Replay: enoch://control-plane/projects/held-out-natural-malformed-tool-call-router-replay-dba2469a9e/runs/held-out-natural-malformed-tool-call-router-replay-dba2469a9e-20260526T220739682908+0000

## What looked useful

Schema-guided embedded-argument recovery improved executable accuracy over no-schema repair by 12.5 points (97.5% vs 85.0%), strongly outperformed strict JSON parsing (0.0%) and no-repair routing (27.5%), and preserved zero false accepts.

## Boundaries and scale limits

The payloads and tool/argument labels are real recorded traces, but the malformed envelopes are deterministic corruptions rather than naturally occurring malformed model emissions; the source is one local integration trace family with four simple tools and no live serving or human annotation.

## Claim scope

On 20,000 controlled malformed tool-call strings generated from 5,000 real signed/unsigned local integration trace events across five fixed seeds, a schema-guided replay router recovered 100.0% of routes and 97.5% of executable calls with zero false accepts on 2,500 negative texts.

## Why it stopped

No-paper closure: bounded full local replay supports the mechanism on real payloads, but controlled malformation generation is not sufficient for publication-grade real malformed trace evidence.

## Recommended next action

Run one final depth-4 deepen test only if naturally occurring malformed tool-call traces with human-labeled intended routes and arguments are available; otherwise stop at this no-paper useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Naturally Occurring Malformed Tool-Call Router Replay
- Success threshold: Replay router executable accuracy is at least 5 percentage points above no-schema repair, route accuracy is at least 95%, and false accept rate is at most 1% on the naturally malformed held-out trace set.
- Stop condition: Stop if executable-recovery lift over no-schema repair is under 2 percentage points, route accuracy is below 90%, false accepts exceed 2%, or human labels show repaired arguments introduce unsafe substitutions.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-malformed-tool-call-router-replay-29f84610a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
