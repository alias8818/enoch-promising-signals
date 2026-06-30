# Suffix-Tree Speculative Draft for Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-draft-for-local-serving-8c0b3501bc39`
Run ID: `suffix-tree-speculative-draft-for-local-serving-8c0b3501bc39-20260607T190408257137+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f3795769f29a

## What looked useful

The mechanism is worth a bounded direct-serving follow-up: suffix-tree drafting produced stable idealized target-call reductions on repeated support/code/low-entropy traces and stayed neutral on random entropy controls.

## Boundaries and scale limits

No real LLM, tokenizer, GPU target pass, KV-cache, batching, or wall-clock serving latency was measured. Results are synthetic/proxy only and should not be interpreted as end-to-end local-serving speedup.

## Claim scope

In deterministic synthetic/proxy traces that emulate repeated local-serving outputs, an online suffix-index drafter using only past emitted tokens can reduce idealized target verification calls by 2.7x-4.7x on structured or low-entropy traces while showing no meaningful benefit on random high-entropy traces.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a synthetic/proxy mechanism test, not a real local LLM serving validation.

## Recommended next action

Run a direct local-serving benchmark around a small llama.cpp or vLLM model with real tokenization, repeated prompts, no-draft baseline, wall-clock tokens/sec, target forward calls, acceptance, and memory overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Local-Serving Benchmark for Online Suffix-Index Drafting
- Success threshold: At least 1.2x end-to-end tokens/sec or latency improvement on repeated/mixed local-serving traces, no meaningful regression on random controls, and less than 10% additional memory overhead.
- Stop condition: Stop if acceptance falls below 0.1 accepted draft tokens per target call on realistic repeated prompts, or if lookup/update overhead eliminates measured wall-clock gains.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-draft-for-local-serving-8c0b3501bc39`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
