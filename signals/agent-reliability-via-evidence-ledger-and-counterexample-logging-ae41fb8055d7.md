# Agent reliability via evidence ledger and counterexample logging

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-reliability-via-evidence-ledger-and-counterexample-logging-ae41fb8055d7`
Run ID: `agent-reliability-via-evidence-ledger-and-counterexample-logging-ae41fb8055d7-20260605T134308662334+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/4be1fc6fa736

## What looked useful

Across 10 seeds and 50,000 cases per variant, ledger+counterexample reduced mean wrong decision rate from 0.02942 to 0.00008 and mean faulty rule acceptance from 0.41686 to 0.18760; ledger-only detected unsupported fabricated claims but did not improve decision accuracy.

## Boundaries and scale limits

The evidence is synthetic, CPU-only, deterministic, and does not use real LLM outputs, retrieval, long-context reasoning, production agent traces, or human-judged task outcomes.

## Claim scope

In a synthetic rule-grounded eligibility benchmark, evidence-ledger validation plus finite-space counterexample logging reduces accepted faulty rules and wrong final decisions compared with a first-answer baseline and ledger-only validation.

## Why it stopped

Synthetic proxy supports the mechanism but is not direct/full validation of real agent reliability.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same ledger and counterexample protocol on frozen real model outputs from bounded rule-grounded tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model evidence-ledger and counterexample reliability probe
- Success threshold: Ledger-plus-counterexample reduces wrong-answer acceptance by at least 30% versus baseline without more than doubling false-positive rejections compared with ledger-only.
- Stop condition: Stop if real model traces show no reduction in wrong-answer acceptance or if counterexample logging mostly rejects correct answers.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-via-evidence-ledger-and-counterexample-logging-ae41fb8055d7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
