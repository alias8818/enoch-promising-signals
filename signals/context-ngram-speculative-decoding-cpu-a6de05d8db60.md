# Context-Ngram Speculative Decoding CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `context-ngram-speculative-decoding-cpu-a6de05d8db60`
Run ID: `context-ngram-speculative-decoding-cpu-a6de05d8db60-20260523T144434496393+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f4aa93715e73

## What looked useful

Context-copy n-gram drafting has a real repeated-context acceptance signal, especially for byte-like token streams, but coarse tokenization and no-proposal calls limit broad CPU acceleration claims without real decoder integration.

## Boundaries and scale limits

Trace/proxy result only; bounded to Tiny Shakespeare, PEP 8, and CPython README with at most 100k train tokens and 50k eval tokens per corpus/tokenizer/config. No real LLM verifier, KV-cache, batching, sampling, quality, or end-to-end CPU serving latency was measured.

## Claim scope

On three small public text traces using exact future-token replay, a recent context n-gram drafter produced 1.883x-2.108x best verifier-call proxy speedup for byte tokenization and 1.118x-1.334x for word/punctuation tokenization, beating random-copy controls and one-token majority baselines in the byte setting.

## Why it stopped

Useful proxy evidence was obtained, but the run lacks direct model-serving evidence required for a paper-positive decision.

## Recommended next action

Run a bounded deepen follow-up integrating the same drafter into a real CPU decoder and compare wall-clock tokens/sec, verifier calls, and output quality against no speculation and a learned draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Decoder Validation for Context-Ngram Drafting
- Success threshold: At least 20% wall-clock tokens/sec improvement over no speculation on a fixed prompt suite, with verifier-call reduction matching trace expectations and no obvious quality regressions.
- Stop condition: Stop if integration overhead erases speedup, acceptance falls below 0.2 accepted tokens per verifier call on target prompts, or quality/regression checks fail.

## Evidence references

- Artifact root: `<local-path>/projects/context-ngram-speculative-decoding-cpu-a6de05d8db60`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
