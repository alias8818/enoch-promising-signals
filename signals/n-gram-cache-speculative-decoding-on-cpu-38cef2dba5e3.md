# N-Gram Cache Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cache-speculative-decoding-on-cpu-38cef2dba5e3`
Run ID: `n-gram-cache-speculative-decoding-on-cpu-38cef2dba5e3-20260607T055409472096+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4d064f2d90ca

## What looked useful

On repeated and mutated-repeated traces, n-gram speculative decoding achieved high acceptance and 6.38x to 13.0x target-batch reduction in best conservative rows, yielding 2.43x to 3.25x speedup under a 25% extra-token batched-target cost model. Under no batching, benefits disappear or regress, so CPU viability depends on real batched verification efficiency and adaptive fallback.

## Boundaries and scale limits

No real transformer or production CPU serving backend was tested. Target cost is proxy-modeled from a NumPy kernel plus conservative cost models. Tokenization, KV-cache behavior, sampling, quality, multi-request serving, and latency tails remain unvalidated.

## Claim scope

Trace-level byte-token evidence shows that an online n-gram cache drafter can exactly preserve target outputs and materially reduce target verification batches on repetitive traces; conservative CPU cost models predict speedup only when batched verification is cheaper than separate single-token target calls.

## Why it stopped

No-paper closure: the current result is a trace/proxy useful signal, not direct end-to-end transformer serving evidence.

## Recommended next action

Run a bounded direct CPU backend test in llama.cpp or an equivalent small transformer runtime, comparing tokens/sec and latency with and without adaptive n-gram speculative decoding on repetitive/code-like and low-repetition prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU Backend Test for Adaptive N-Gram Speculative Decoding
- Success threshold: At least 1.15x end-to-end generated tokens/sec on repetitive/code-like prompts with exact output preservation and less than 5% regression on low-repetition prompts.
- Stop condition: Stop if direct backend speedup is below 1.05x on repetitive prompts or if low-repetition prompts regress by 5% or more after adaptive fallback tuning.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cache-speculative-decoding-on-cpu-38cef2dba5e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
