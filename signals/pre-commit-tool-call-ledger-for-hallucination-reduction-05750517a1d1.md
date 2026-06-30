# Pre-Commit Tool Call Ledger for Hallucination Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pre-commit-tool-call-ledger-for-hallucination-reduction-05750517a1d1`
Run ID: `pre-commit-tool-call-ledger-for-hallucination-reduction-05750517a1d1-20260525T023711101454+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8993b96b9aa6

## What looked useful

On 600 synthetic examples with 500 unsafe and 100 safe answers, the strict ledger guard achieved precision 1.000, recall 1.000, specificity 1.000, and F1 1.000. Citation-only checking achieved recall 0.400 and F1 0.571, missing wrong-value, irrelevant-citation, and ledger-omission failures.

## Boundaries and scale limits

No live LLM generations, no human adjudication, no natural messy tool traces, and no direct measurement of user-visible hallucination reduction; the benchmark uses structured synthetic claims and exact evidence matching.

## Claim scope

In a deterministic synthetic proxy benchmark, a strict pre-commit ledger that cross-checks parsed final-answer claims against ledger entries and exact tool observations detects unsupported answer claims better than accept-all, tool-presence, and citation-only controls.

## Why it stopped

Stopped after a bounded synthetic proxy result: the mechanism is supported, but direct hallucination-reduction evidence from live model generations is still missing, so this is not paper-ready.

## Recommended next action

Run a 100-200 task live LLM A/B evaluation with and without the pre-commit ledger, adjudicating unsupported tool-grounded final-answer claims and measuring over-refusal/incomplete-answer cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM A/B Test of Pre-Commit Tool Call Ledgers
- Success threshold: At least 25% relative reduction in unsupported final-answer claims with no more than 10% absolute increase in over-refusal or incomplete answers.
- Stop condition: Stop if the ledger arm fails to reduce unsupported claims by at least 10% relative on the first 50 adjudicated tasks or if parsing/ledger compliance fails on more than 20% of tasks.

## Evidence references

- Artifact root: `<local-path>/projects/pre-commit-tool-call-ledger-for-hallucination-reduction-05750517a1d1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
