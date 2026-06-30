# N-gram Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-on-cpu-b71bd224b872`
Run ID: `n-gram-speculative-decoding-on-cpu-b71bd224b872-20260608T185012866522+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d5119da739e8

## What looked useful

Best synthetic regimes showed 2.00x-8.70x overhead-adjusted estimated speedups from 49.9%-88.5% fewer target iterations; iid random text showed 1.00x and 0% acceptance, confirming strong workload dependence.

## Boundaries and scale limits

No real LLM forward pass, production tokenizer, llama.cpp/transformer integration, real prompt suite, or end-to-end wall-clock decoder benchmark was run. Results should not be read as publication-grade CPU LLM speedups.

## Claim scope

Bounded trace-level evidence on synthetic CPU token streams: prompt-local exact n-gram drafting can reduce target decode iterations on repetition-heavy text, is neutral on iid random text, and has negligible measured Python retrieval overhead under a 20 ms target-step cost assumption.

## Why it stopped

No-paper useful signal: mechanism supported on synthetic trace tests, but direct CPU LLM wall-clock validation is required before any stronger claim.

## Recommended next action

Run one bounded end-to-end CPU decoder follow-up using a small real model/runtime and a real repeated-prompt suite; stop this run because current evidence is trace-level and not paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU LLM validation for prompt-local n-gram speculative decoding
- Success threshold: At least 1.25x median wall-clock speedup on repeated/template prompts, identical generated token sequences versus greedy verification, and no more than 5% median slowdown on low-repetition controls.
- Stop condition: Stop if integration overhead eliminates speedup below 1.10x on repeated prompts or causes more than 5% slowdown on low-repetition controls.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-on-cpu-b71bd224b872`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
