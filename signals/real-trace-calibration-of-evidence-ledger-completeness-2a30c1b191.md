# Real Trace Calibration of Evidence Ledger Completeness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-calibration-of-evidence-ledger-completeness-2a30c1b191`
Run ID: `real-trace-calibration-of-evidence-ledger-completeness-2a30c1b191-20260525T120601050819+0000`

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

- Parent run decision: Bounded Agent Task Difficulty Calibration via Evidence Ledger Completeness: enoch://control-plane/projects/bounded-agent-task-difficulty-calibration-via-evidence-ledger-completeness-bc63355516f7/runs/bounded-agent-task-difficulty-calibration-via-evidence-ledger-completeness-bc63355516f7-20260525T102431060892+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/74ba39470e6c

## What looked useful

The harness parsed a real Codex trace and achieved 8/8 correct completeness classifications with zero false passes and zero false fails on one complete bundle plus seven seeded omission cases.

## Boundaries and scale limits

Single project trace, eight controlled cases, local CPU-only harness, no independent held-out traces, no naturally occurring omission corpus, and no adversarial or multi-worker validation.

## Claim scope

Tier 1 controlled direct test on one real Enoch/Codex JSONL trace from this project. The tested claim is that a trace-anchored evidence-ledger checker can classify one complete bundle and seven seeded incomplete bundles covering run notes, native decision, legacy mirror, metrics, command log, decision enum, and trace digest completeness.

## Why it stopped

Tier 1 mechanism support only; the result is useful but not paper-positive because the calibration used one real trace with controlled seeded omissions.

## Recommended next action

Run a blinded multi-trace deepen test with at least 10 independent real Enoch traces and hidden omissions before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded Multi-Trace Evidence Ledger Completeness Calibration
- Success threshold: Zero false passes and at most one explainable false fail across at least 10 independent real traces with hidden omissions.
- Stop condition: Stop if any incomplete evidence bundle falsely passes, or if more than one complete bundle falsely fails without a trace/log corruption explanation.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-calibration-of-evidence-ledger-completeness-2a30c1b191`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
