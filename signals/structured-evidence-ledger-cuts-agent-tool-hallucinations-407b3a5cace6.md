# Structured evidence ledger cuts agent tool hallucinations

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `structured-evidence-ledger-cuts-agent-tool-hallucinations-407b3a5cace6`
Run ID: `structured-evidence-ledger-cuts-agent-tool-hallucinations-407b3a5cace6-20260529T011800503637+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0856d70663e7

## What looked useful

The ledger scaffold produced seven baseline-only fixes and zero ledger-only primary hallucination regressions, but still failed in 13/20 decoy cases and 20/20 unsupported-action cases, including false provenance where wrong values were attributed to an observation ID.

## Boundaries and scale limits

Single small local instruction model, deterministic decoding, simulated tool outputs, templated tasks, regex scoring, no real multi-turn tool dispatch, no human grading, and no larger-model or production-agent validation.

## Claim scope

In an 80-case synthetic paired benchmark using Qwen/Qwen2.5-0.5B-Instruct with simulated tool observations, a structured evidence-ledger prompt reduced primary unsupported value/action claims from 50.0% to 41.25%, with improvement concentrated in user-decoy value-copying cases.

## Why it stopped

Bounded local evidence supports only a category-specific mechanism, not a broad or paper-ready claim that structured evidence ledgers cut agent tool hallucinations generally.

## Recommended next action

Stop this run as no-paper useful signal; next run should test parser-enforced ledgers on real or richer tool traces with at least two stronger instruction models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parser-enforced evidence ledgers on richer tool traces
- Success threshold: At least 30% relative reduction in unsupported-claim rate versus baseline on each major error category, with no more than 10% absolute increase in omissions and false-provenance rate below 5%.
- Stop condition: Stop if parser-enforced ledgers fail to improve unsupported-action traces or if false provenance remains above 10% after validation.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-cuts-agent-tool-hallucinations-407b3a5cace6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
