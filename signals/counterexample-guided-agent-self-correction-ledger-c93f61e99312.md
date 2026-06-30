# Counterexample-Guided Agent Self-Correction Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-guided-agent-self-correction-ledger-c93f61e99312`
Run ID: `counterexample-guided-agent-self-correction-ledger-c93f61e99312-20260525T073141445729+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a3a61c76de48

## What looked useful

Across 200 seeds x 100 tasks, the ledger condition improved first-pass success from 0.000 to 0.950 and reduced corrections by 95% while both baseline and ledger reached 1.000 final accuracy after current-task correction.

## Boundaries and scale limits

The result is proxy-only: no LLM agent, natural-language task parsing, noisy template recognition, bad-ledger transfer, tool-use traces, or external coding benchmark was tested.

## Claim scope

In a deterministic symbolic proxy benchmark with five recurring underspecified program-synthesis templates, a template-keyed ledger of generalized counterexample probes reduced repeated correction cycles versus a per-task self-correction baseline.

## Why it stopped

Closed as a no-paper useful signal because the evidence supports the mechanism only in a symbolic proxy benchmark, not in actual LLM agent self-correction.

## Recommended next action

Run a bounded direct LLM-agent follow-up on generated coding tasks with ledger-vs-baseline controls, noisy template mapping, and token/correction metrics; do not write a paper from this proxy result alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM Counterexample Ledger Evaluation on Generated Coding Tasks
- Success threshold: Ledger improves first-pass pass@1 by at least 15 percentage points or reduces correction-token cost by at least 25% with no more than 2 percentage points final pass-rate loss versus baseline.
- Stop condition: Stop if ledger transfer causes more than 5 percentage points final pass-rate loss, if first-pass/cost gains are below threshold after 100 tasks, or if template matching cannot be automated without human labels.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-guided-agent-self-correction-ledger-c93f61e99312`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
