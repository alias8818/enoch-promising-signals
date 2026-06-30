# Direct LLM Counterexample Ledger Evaluation on Generated Coding Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-llm-counterexample-ledger-evaluation-on-generated-c-57f5e9cb2e`
Run ID: `direct-llm-counterexample-ledger-evaluation-on-generated-c-57f5e9cb2e-20260525T143821536071+0000`

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

- Parent run decision: Counterexample-Guided Agent Self-Correction Ledger: enoch://control-plane/projects/counterexample-guided-agent-self-correction-ledger-c93f61e99312/runs/counterexample-guided-agent-self-correction-ledger-c93f61e99312-20260525T073141445729+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a3a61c76de48

## What looked useful

Counterexample ledgers can repair at least one small-model false-valid judgment without harming specificity, but the predeclared Tier 1 threshold of at least +0.25 invalid-recall lift was not met. Stronger small-model code inspection saturated the no-ledger baseline, leaving no measurable room for ledger lift.

## Boundaries and scale limits

Small generated single-function Python tasks only; concise ground-truth ledgers only; no noisy/adversarial ledger ablations; no real contest or multi-file tasks; two OpenAI small models; first malformed-prompt artifacts invalidated and excluded.

## Claim scope

On a corrected 10-family generated Python coding-task benchmark, direct LLM judging with concise counterexample ledgers produced +0.10 invalid-recall lift for gpt-4o-mini and 0.00 lift for gpt-4.1-mini, with valid specificity 1.00 in both fixed-prompt ledger runs.

## Why it stopped

No-paper useful signal: fixed-prompt direct evidence did not meet the stated +0.25 invalid-recall lift threshold, although it showed a small mechanism signal on gpt-4o-mini.

## Recommended next action

Run a harder bounded deepen test with 50-100 generated task families selected to keep no-ledger invalid recall below ceiling, plus true/irrelevant/wrong-ledger ablations and a paired significance test.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder Counterexample Ledger Lift Test with Ceiling-Controlled Generated Coding Tasks
- Success threshold: Across at least two small/medium LLM judges, true ledgers improve invalid recall by at least +0.25 absolute over no-ledger and irrelevant-ledger controls, with valid specificity >= 0.80 and parseability >= 0.90.
- Stop condition: Stop if a 20-task calibration subset shows no-ledger invalid recall remains above 0.90 for all candidate models or true-ledger lift is below +0.10 while specificity falls below 0.80.

## Evidence references

- Artifact root: `<local-path>/projects/direct-llm-counterexample-ledger-evaluation-on-generated-c-57f5e9cb2e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
