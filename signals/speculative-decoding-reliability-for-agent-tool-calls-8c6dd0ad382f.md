# Speculative Decoding Reliability for Agent Tool Calls

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-reliability-for-agent-tool-calls-8c6dd0ad382f`
Run ID: `speculative-decoding-reliability-for-agent-tool-calls-8c6dd0ad382f-20260614T031529668861+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/34cc0b7659b0

## What looked useful

Exact speculative decoding is not intrinsically a tool-call reliability risk in this proxy; the observed risk comes from non-exact acceptance shortcuts that use schema validity as a substitute for target probability correction. Grammar masks eliminate structural invalidity but do not guarantee correct tool or argument semantics.

## Boundaries and scale limits

Synthetic fixed-schema simulator only; no real LLM logits, tokenizer behavior, KV-cache implementation, wall-clock model latency, production tool parser, multi-turn agent state, or tool side effects were tested.

## Claim scope

In a finite synthetic tool-call simulator, exact speculative decoding with target-model rejection sampling preserved target decoder structural validity and semantic tool-call correctness within Monte Carlo error, while schema-only speculative acceptance preserved syntax but reduced semantic correctness when the draft distribution was weaker or stale.

## Why it stopped

Closed as no-paper useful signal because the evidence is proxy/synthetic; it identifies a concrete mechanism and follow-up but is not direct publication-grade validation.

## Recommended next action

Run a bounded direct LLM follow-up comparing serial target decoding, exact speculative decoding, and schema-only/speculative shortcut acceptance on open-weight tool-calling prompts with JSON schemas, measuring wall-clock latency, structural validity, tool selection, argument exact match, and task success.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM validation of exact versus schema-only speculative tool-call decoding
- Success threshold: Exact speculative decoding remains within 1 percentage point of serial target semantic accuracy while achieving at least 1.5x wall-clock or target-forward speedup; schema-only/draft-biased acceptance shows a reproducible semantic degradation of at least 3 percentage points at matched schema validity.
- Stop condition: Stop if exact speculative decoding cannot be instrumented locally or if the serial and speculative paths cannot be made comparable by prompt, schema, model, and sampling settings after a bounded setup attempt.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-reliability-for-agent-tool-calls-8c6dd0ad382f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
