# N-Gram Draft Head for Local Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-head-for-local-speculative-decoding-42ffe363d782`
Run ID: `n-gram-draft-head-for-local-speculative-decoding-42ffe363d782-20260605T024051044088+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/47a251bb1026

## What looked useful

The mechanism is repetition-sensitive: best proxy speedup was 3.85x on degenerate greedy distilgpt2, 1.83x on sampled distilgpt2, but only 1.09x on WikiText-2 with a 3.7% accepted-token fraction. This argues against broad paper claims for simple exact n-gram drafting, while preserving a narrow engineering follow-up for repetitive/local-cache workloads.

## Boundaries and scale limits

No trained draft head, no GPT-2-small-class parameter-matched baseline, no integrated speculative decoding runtime, no wall-clock serving benchmark, no sampling-distribution correctness test, and only small local prompt/corpus budgets.

## Claim scope

A prefix-only n-gram draft proposer was tested on small local probes against greedy distilgpt2 continuations, sampled distilgpt2 continuations, and WikiText-2 natural token streams. It produced strong proxy target-call reductions only on repetitive model-generated text, moderate proxy gains on sampled model text, and weak gains on natural text.

## Why it stopped

Bounded proxy and corpus evidence is mixed: the idea works mainly when the target stream repeats, and the natural text control is too weak for a paper-ready or broad viability claim.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, implement a real wall-clock speculative decoder and require at least 1.15x end-to-end decode throughput on non-degenerate prompts before investing further.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Wall-clock n-gram speculative decoder on non-degenerate local prompts
- Success threshold: At least 1.15x end-to-end decode tokens/s versus no-draft baseline on non-degenerate prompts, with accepted-token fraction above 10% and no correctness regression.
- Stop condition: Stop if integrated throughput is at or below 1.05x, accepted-token fraction stays below 10% on non-degenerate prompts, or draft lookup overhead consumes the proxy target-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-head-for-local-speculative-decoding-42ffe363d782`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
