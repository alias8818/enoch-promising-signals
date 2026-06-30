# Ledger-Grounded Tool Call Verification for Sub-1B Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `ledger-grounded-tool-call-verification-for-sub-1b-agents-996e467b7837`
Run ID: `ledger-grounded-tool-call-verification-for-sub-1b-agents-996e467b7837-20260525T071131635483+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/111b44975757

## What looked useful

Across 30,000 synthetic cases from six 5,000-case runs, ledger-grounded verification achieved 1.000 invalid recall and 1.000 valid specificity, while shallow transcript checks averaged 0.430 invalid recall and last-result checks averaged 0.181 invalid recall.

## Boundaries and scale limits

No real sub-1B LLM was evaluated; final answers were structured JSON claims; tools were deterministic local functions; the benchmark did not test natural-language claim extraction, nondeterministic APIs, messy production logs, or adaptive adversarial outputs.

## Claim scope

On deterministic synthetic purchase-quote traces with structured JSON ledgers and replayable tool semantics, a ledger-grounded verifier catches injected tool-call and final-answer inconsistencies that shallow transcript checks miss.

## Why it stopped

Closed as a useful synthetic mechanism result, not a full validation or paper-positive result, because the run did not evaluate real sub-1B agents or unstructured model outputs.

## Recommended next action

Run a bounded direct sub-1B-model evaluation with actual generated tool-use traces, comparing no-ledger, transcript-only, and ledger-grounded verification on false accept and false reject rates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Sub-1B Ledger Verification on Generated Tool-Use Traces
- Success threshold: Ledger-grounded verification cuts false accepts by at least 50% relative to transcript-only checking and keeps false rejects below 10% on at least 500 real model-generated traces.
- Stop condition: Stop if model outputs cannot be generated locally, if the ledger verifier fails to improve false accept rate by at least 20% in a 100-trace smoke test, or if false rejects exceed 20% after straightforward schema/claim extraction fixes.

## Evidence references

- Artifact root: `<local-path>/projects/ledger-grounded-tool-call-verification-for-sub-1b-agents-996e467b7837`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
