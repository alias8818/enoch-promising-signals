# Evidence-ledger truncation test for multi-step CPU agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-truncation-test-for-multi-step-cpu-agents-b3111217f148`
Run ID: `evidence-ledger-truncation-test-for-multi-step-cpu-agents-b3111217f148-20260531T095618625702+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8408ff0055b8

## What looked useful

Across 2,000 trials for each horizon/position condition, full ledger and oracle structured retention reached 1.0000 accuracy. Tail truncation reached 0.2708 overall accuracy, exactly matching required case-fact visibility, and head+tail reached 0.4150 with predictable blind spots for quarter/middle evidence.

## Boundaries and scale limits

Synthetic CPU-only proxy; no real LLM, natural-language parser, learned retriever, summarizer, or autonomous agent loop was tested. The structured_index condition is oracle-assisted and should not be treated as an implemented policy.

## Claim scope

In a deterministic synthetic multi-step lookup benchmark, naive tail truncation of an append-only evidence ledger fails when required older evidence is outside the retained tail; failures align with missing required evidence, while an oracle compact index retaining the two required facts preserves accuracy at much lower token cost.

## Why it stopped

Proxy useful-signal closure rather than full validation: the truncation mechanism was directly tested, but real agent behavior and non-oracle retention were not.

## Recommended next action

Stop this run as a bounded proxy result; next evidence should implement a non-oracle CPU agent retrieval/summarization policy on the same benchmark and require at least 0.90 accuracy at 128 token units across all target positions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle CPU agent evidence-ledger retention benchmark
- Success threshold: Non-oracle retention achieves at least 0.90 accuracy at 128 token units for every target position and horizon while tail and head_tail retain their observed failure modes.
- Stop condition: Stop if non-oracle retention cannot exceed 0.70 accuracy at 128 token units on horizon 256 middle-position tasks or if failures no longer correlate with required-fact visibility.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-truncation-test-for-multi-step-cpu-agents-b3111217f148`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
