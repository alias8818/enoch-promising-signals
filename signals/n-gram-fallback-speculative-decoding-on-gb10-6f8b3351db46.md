# N-Gram Fallback Speculative Decoding on gb10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-fallback-speculative-decoding-on-gb10-6f8b3351db46`
Run ID: `n-gram-fallback-speculative-decoding-on-gb10-6f8b3351db46-20260628T073113843009+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b49dbf04196f

## What looked useful

N-gram fallback speculative decoding is viable as a cheap exact greedy draft path when generated text has local repetition, but cache mutation must be handled carefully; an intermediate run produced incorrect output until failed-verification cache rebuilds were added.

## Boundaries and scale limits

Only 128-token greedy continuations were tested, with handcrafted prompts and GPT-2-class models. No sampling, batching, production serving engine, real corpus, long-context, or 1B/7B+ model validation was performed.

## Claim scope

On GB10, for batch-1 exact greedy decoding with GPT-2-class Hugging Face models (`distilgpt2` and `gpt2`) and short locally repetitive prompts, a cache-correct prompt/history n-gram fallback draft preserved exact greedy output and improved wall throughput by 1.10x-2.36x while reducing target forward calls to 0.26x-0.58x of baseline.

## Why it stopped

Useful local mechanism signal, but not paper-ready because evidence is limited to short handcrafted greedy GPT-2-class benchmarks.

## Recommended next action

Run a bounded deepen follow-up on a real prompt corpus with a 1B-3B model on GB10, keeping exact-output assertions and reporting p50/p95 speedup, acceptance, and forward-call ratio by prompt class.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-Level N-Gram Fallback Speculative Decoding on 1B-3B Models
- Success threshold: Exact-output mismatch rate is zero and p50 wall speedup is at least 1.15x on one realistic repetitive/code subset without more than 5% slowdown on low-repetition controls.
- Stop condition: Stop if exact-output mismatches recur after cache rebuild safeguards, or if p50 speedup is below 1.0x across realistic prompt classes despite acceptance above 0.5.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-fallback-speculative-decoding-on-gb10-6f8b3351db46`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
