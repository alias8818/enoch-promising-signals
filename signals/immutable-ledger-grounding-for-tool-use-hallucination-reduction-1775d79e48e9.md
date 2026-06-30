# Immutable Ledger Grounding for Tool-Use Hallucination Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `immutable-ledger-grounding-for-tool-use-hallucination-reduction-1775d79e48e9`
Run ID: `immutable-ledger-grounding-for-tool-use-hallucination-reduction-1775d79e48e9-20260525T202341494337+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/abf77b336ae1

## What looked useful

The systems mechanism is reproducible and appears useful as a guardrail: mutable scratchpad accuracy dropped to 78.924% in the combined stale/overwrite condition, while ledger accepted error rate remained 0.0% with 1.024% rejection in that same condition. This supports a bounded follow-up with an actual instruction model.

## Boundaries and scale limits

No LLM generated answers in this run; tasks were synthetic numeric state lookups; no real tool APIs, long-context prompt pressure, multi-agent settings, or production latency/token overhead were evaluated.

## Claim scope

In a synthetic tool-observation benchmark with stale mutable memory and adversarial scratchpad overwrites, an append-only hash-chained ledger plus mandatory observation citation validation reduced accepted unsupported numeric tool-result claims to zero across 100,000 evaluated questions, while rejecting about 1% deliberately tampered ledger answers.

## Why it stopped

Closed as a proxy useful signal rather than full validation because the benchmark isolates the ledger/verifier mechanism without LLM-generated tool-use answers.

## Recommended next action

Run a direct small-instruction-model evaluation comparing identical tool-use prompts with mutable scratchpad context versus immutable ledger plus citation verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM Prompt Evaluation of Immutable Tool Ledgers
- Success threshold: At least 30% relative reduction in unsupported claim rate versus mutable scratchpad with no more than 10% absolute increase in non-answer/rejection rate.
- Stop condition: Stop if unsupported claim reduction is below 10% relative or if rejection/non-answer rate rises by more than 20% absolute on the matched task set.

## Evidence references

- Artifact root: `<local-path>/projects/immutable-ledger-grounding-for-tool-use-hallucination-reduction-1775d79e48e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
