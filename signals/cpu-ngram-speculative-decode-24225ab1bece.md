# CPU-NGram Speculative Decode

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-ngram-speculative-decode-24225ab1bece`
Run ID: `cpu-ngram-speculative-decode-24225ab1bece-20260528T150415392032+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5b66d5fcf0a5

## What looked useful

CPU n-gram speculation is viable when local repetition gives enough accepted draft tokens, but the optimized prompt-lookup path needs stopping/length validation before it can be treated as an exact drop-in replacement. Low-acceptance regimes lose in simulation; small-model direct tests show speedups but not paper-grade breadth.

## Boundaries and scale limits

Only distilgpt2 and sshleifer/tiny-gpt2 were tested, with two local prompts and up to 96 requested new tokens. No 1B-7B class model, broad prompt suite, production serving stack, quality evaluation, or long-context robustness test was run.

## Claim scope

On two short prompts with a GPU-backed distilgpt2 target in Transformers 4.57.6, CPU prompt-lookup/n-gram assisted generation reduced median greedy decoding wall time by 1.36x-3.13x while preserving the greedy common prefix; exact full-length agreement held for four of six prompt/draft settings and the two failures were max_new_tokens overshoots rather than token-prefix divergence.

## Why it stopped

Bounded local evidence supports the mechanism but is too narrow for a paper and exposed a length-control caveat in some faster settings.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should benchmark a hardened length-trimmed prompt-lookup implementation on a 1B-7B model across at least 100 prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length-safe CPU n-gram speculative decode on a 1B-7B target
- Success threshold: Median latency speedup >= 1.25x on the repetition-heavy split, no median slowdown worse than 5% on the natural split, 100% exact greedy output after length enforcement, and peak memory increase <= 10%.
- Stop condition: Stop if exact greedy output cannot be preserved after length enforcement or if median speedup is below 1.10x on the repetition-heavy split.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-ngram-speculative-decode-24225ab1bece`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
