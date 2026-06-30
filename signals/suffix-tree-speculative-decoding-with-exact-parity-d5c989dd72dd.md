# Suffix-Tree Speculative Decoding with Exact Parity

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-tree-speculative-decoding-with-exact-parity-d5c989dd72dd`
Run ID: `suffix-tree-speculative-decoding-with-exact-parity-d5c989dd72dd-20260628T022703921166+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/795ee7683651

## What looked useful

Two 100k-sample parity checks against exact sequence distributions passed with chi-square p=0.637 and p=0.708. In 128-token sweeps over 1,000 prompts, suffix speculation reduced target calls by 52.9% on repetitive targets, 56.4% on structured targets, and 12.6% on flat targets; acceptance matched the target probability of proposed suffix tokens.

## Boundaries and scale limits

Evidence is limited to CPU synthetic Markov targets, exact enumeration over 4-token continuations, and target-call proxy metrics; it does not measure real transformer latency, GPU batching, KV-cache behavior, tokenizer effects, or suffix-tree memory costs.

## Claim scope

A deterministic suffix-context proposer can be corrected to exact target sampling parity on small Markov target language models, and it reduces target calls when suffix proposals have high target probability.

## Why it stopped

No-paper useful signal: this run provides toy direct parity evidence and proxy target-call evidence, not direct publication-grade LLM serving validation.

## Recommended next action

Run a bounded transformer follow-up using GPT-2-small-class inference to measure exact-parity sampling, latency, and suffix-table memory against no-speculation and n-gram/cache baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer latency validation for exact-parity suffix speculative decoding
- Success threshold: At least 20% median latency reduction on a repetitive-prompt benchmark with parity test p>0.05 across multiple seeds and suffix-table memory below 2x prompt token storage.
- Stop condition: Stop if parity fails, median latency improves by less than 10% versus no speculation, or suffix-table memory exceeds 4x prompt token storage on the benchmark corpus.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-with-exact-parity-d5c989dd72dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
