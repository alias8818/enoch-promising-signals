# Tool-use evidence ledger reduces hallucination in small agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tool-use-evidence-ledger-reduces-hallucination-in-small-agents-fc9156fbc29a`
Run ID: `tool-use-evidence-ledger-reduces-hallucination-in-small-agents-fc9156fbc29a-20260527T145613316766+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d359c38564ef

## What looked useful

Across three 90-example seeds, unsupported answers fell from 91/270 (33.7%) to 78/270 (28.9%). Paired comparison had 13 baseline-unsupported cases corrected by the ledger and 0 regressions; exact two-sided sign-test p=0.000244. Missing-evidence hallucination remained high at 78/90 under the ledger.

## Boundaries and scale limits

Static snippets rather than live tool calls; synthetic benchmark; one small model; prompt-only intervention; no human judge labels; no broad task or model-family validation.

## Claim scope

For google/flan-t5-small on a synthetic static tool-output QA benchmark, an explicit evidence-ledger prompt modestly reduced unsupported answers, mainly by improving abstention on missing-evidence questions.

## Why it stopped

Useful local signal but not paper-ready: the ledger effect is modest, synthetic, and still leaves a high unsupported-answer rate on missing-evidence cases.

## Recommended next action

Run a bounded real tool-calling follow-up with multiple small models, naturalistic retrieval traces, and judge-verified support labels; do not write a paper from this synthetic prompt-only result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger in real small-model tool-calling loops
- Success threshold: At least 10 percentage point absolute reduction in unsupported final answers with no more than 3 percentage point accuracy loss, replicated across at least two small models.
- Stop condition: Stop if the ledger fails to reduce unsupported answers by at least 5 percentage points in a 100-example smoke run or causes more than 10 percentage point accuracy loss.

## Evidence references

- Artifact root: `<local-path>/projects/tool-use-evidence-ledger-reduces-hallucination-in-small-agents-fc9156fbc29a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
