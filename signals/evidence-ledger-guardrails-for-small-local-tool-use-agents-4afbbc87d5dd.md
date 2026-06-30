# Evidence-ledger guardrails for small local tool-use agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-guardrails-for-small-local-tool-use-agents-4afbbc87d5dd`
Run ID: `evidence-ledger-guardrails-for-small-local-tool-use-agents-4afbbc87d5dd-20260603T191720320164+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/61f117a7314a

## What looked useful

Evidence-ledger binding of answer fields to matching tool observations is a useful guardrail mechanism in the proxy setting. Block-only validation prevents unsafe accepts but causes false blocks; ledger validation with automatic reread/repair preserved correctness in this benchmark.

## Boundaries and scale limits

Planner behavior was stochastic rather than a real LLM; tools were dictionary reads rather than shell/filesystem/web actions; evidence was exact-match field evidence, not natural-language entailment; results do not validate real deployed local tool-use agents.

## Claim scope

In a deterministic synthetic small-tool benchmark, final-answer evidence ledger validation with one repair pass eliminated unsupported accepted claims across 20 seeded runs and 300,000 mode trials while adding bounded tool-call overhead.

## Why it stopped

Synthetic proxy supports the mechanism but is not direct/full validation of real local LLM tool-use agents.

## Recommended next action

Stop this run as no-paper useful signal; next direct evidence should test the same ledger protocol on a small local LLM agent with real shell/filesystem tasks and independent unsupported-claim grading.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger validation on real local LLM file and shell tasks
- Success threshold: Ledger-retry reduces unsupported accepted claims by >=80% relative to baseline with false blocks <=5% and overhead reported on the same task suite.
- Stop condition: Stop as negative if unsupported accepted claims fall by <50%, false blocks exceed 10%, or the repair loop repeatedly masks missing evidence without producing valid citations.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-guardrails-for-small-local-tool-use-agents-4afbbc87d5dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
