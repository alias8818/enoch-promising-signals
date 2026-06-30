# CPU N-gram Speculative Decoding with Exact Suffix Matching

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-with-exact-suffix-matching-749cad8f48a8`
Run ID: `cpu-n-gram-speculative-decoding-with-exact-suffix-matching-749cad8f48a8-20260529T183713444773+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/770071bce95e

## What looked useful

Exact suffix matching produces many short suffix hits, but for GPT-style tokens most hits predict the wrong continuation. Longer suffixes improve precision but are too rare to reduce target steps. Byte-level replay can pass the local threshold, indicating the mechanism works mainly when token units are very small or literal repetition is dense.

## Boundaries and scale limits

No live LLM target verification, no GPU serving stack, no KV-cache timing, no real assisted-generation API, and only four natural-language books plus a 100k-byte-per-book byte sanity run. Results do not cover repetition-heavy code, chat-template, RAG, or long-document editing workloads.

## Claim scope

Causal offline replay over four public-domain natural-language books shows exact suffix replay is not useful as a general GPT-style subword-token speculative decoder: best cl100k_base result saved 2.27% target steps with 1.03% proposal precision. A byte-token proxy exceeded 10% target-step reduction, but byte units are not ordinary LLM decoding tokens.

## Why it stopped

Proxy trace replay with GPT-style tokens failed the 10% target-step reduction threshold by a wide margin, so this is not a paper-positive result or a viable general CPU speculative decoder from the tested evidence.

## Recommended next action

Stop this general natural-language investigation as an early proxy falsification; only pursue a bounded deepen follow-up on repetition-heavy real LLM-token workloads if that domain is the intended target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact suffix speculative replay on repetition-heavy LLM-token workloads
- Success threshold: Mean target forward-pass reduction of at least 10% after CPU overhead on subword-token traces, with no corpus segment relying solely on byte-level or future-leaking matches.
- Stop condition: Stop if subword-token trace replay remains below 10% target-step reduction or if live target verification loses the trace-replay gain after CPU lookup/KV-cache overhead.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-with-exact-suffix-matching-749cad8f48a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
