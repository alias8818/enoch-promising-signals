# Field-aware evidence-ledger gate on realistic local-agent tool traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `field-aware-evidence-ledger-gate-on-realistic-local-agent-2760ab2637`
Run ID: `field-aware-evidence-ledger-gate-on-realistic-local-agent-2760ab2637-20260523T063234605972+0000`

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

- Parent run decision: Evidence-ledger tool-use for 1B local agent reliability: enoch://control-plane/projects/evidence-ledger-tool-use-for-1b-local-agent-reliability-0236f810616f/runs/evidence-ledger-tool-use-for-1b-local-agent-reliability-0236f810616f-20260523T034904869036+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8fdc9667bbfb

## What looked useful

Field binding matters: unsupported claims that reuse real evidence values under the wrong field produced a 100% false-accept rate for a flat value gate and 0% false-accept rate for the field-aware gate in the Tier 1 run, with 0% clean-claim rejection.

## Boundaries and scale limits

Small local trace sample; deterministic claim generation; exact structured fields only; no live LLM claim extraction, paraphrase handling, ambiguous support labels, or deployed agent-runtime intervention.

## Claim scope

In a controlled Tier 1 test on 80 real local Codex JSONL traces, exact field-aware ledger gating rejected harness-generated field-swap claims whose values existed elsewhere in the trace ledger, while flat value-membership gating accepted them.

## Why it stopped

Useful mechanism signal from a controlled small direct test, but not paper-ready because the evaluated claims were harness-generated field swaps rather than natural model-authored claims.

## Recommended next action

Run a bounded deepen test on manually labeled atomic claims extracted from real model-authored local-agent final answers, comparing field-aware, flat, type-aware, and LLM-judge gates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Field-aware gate on manually labeled model-authored local-agent claims
- Success threshold: Field-aware gate unsupported-claim accept rate at least 30 percentage points lower than the best non-field-aware baseline with supported-claim reject rate no higher than 10%.
- Stop condition: Stop if field-aware gating fails to beat the best non-field-aware baseline by 10 percentage points on unsupported-claim acceptance or rejects more than 20% of supported claims.

## Evidence references

- Artifact root: `<local-path>/projects/field-aware-evidence-ledger-gate-on-realistic-local-agent-2760ab2637`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
