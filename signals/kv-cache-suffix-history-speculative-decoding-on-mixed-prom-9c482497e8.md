# KV-cache suffix-history speculative decoding on mixed prompt strata

Status: `useful_signal`
Project ID: `kv-cache-suffix-history-speculative-decoding-on-mixed-prom-9c482497e8`
Run ID: `kv-cache-suffix-history-speculative-decoding-on-mixed-prom-9c482497e8-20260519T093634597322+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: KV-cache suffix-history speculative decoding on mixed prompt strata: internal_generated:kv-cache-suffix-history-speculative-decoding-on-mixed-prom-9c482497e8

## What looked useful

Suffix-history achieved 0.6863 target calls/token, a 31.37% reduction versus greedy and draft_spec, with 79.93% cache accept rate and zero mismatches. Shuffled-history reached 0.8125 target calls/token and 19.15% cache accept rate, supporting that matched suffix history provides a real mechanism signal beyond generic cached continuations.

## Boundaries and scale limits

Synthetic prompt stream; small target/draft models; greedy decoding only; no production paged KV-cache or persistent past_key_values serving backend; wall-clock tokens/s did not beat greedy in this Python/HF harness.

## Claim scope

On a local GB10/PyTorch exact greedy speculative-decoding harness with distilgpt2 target, sshleifer/tiny-gpt2 draft, 96 synthetic mixed-strata prompts per seed, five fixed seeds, gamma=4, and 24 generated tokens per prompt, an online suffix-history proposal cache reduced target verification calls/token versus greedy, draft-speculative, and shuffled-history controls while preserving exact greedy outputs.

## Why it stopped

Medium local confirmation supports the suffix-history proposal mechanism but does not establish a production KV-cache speedup or paper-ready result; wall-clock speed in this harness remained below greedy.

## Recommended next action

Deepen with a real KV-cache or paged-attention serving implementation using a competent draft baseline and real prompt traces; require both exactness and end-to-end latency or throughput improvement before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Suffix-history speculative decoding in a real KV-cache serving path
- Success threshold: Matched suffix-history must have zero exactness regressions, at least a 10% target calls/token reduction versus the best non-history speculative baseline, at least a 5% p50 or throughput improvement end-to-end, and must beat shuffled-history by at least 5 percentage points in target-call reduction.
- Stop condition: Stop if matched suffix-history fails to beat shuffled-history or the best standard speculative baseline on target calls/token, or if target-call reductions do not translate into any end-to-end latency/throughput improvement in the real KV-cache backend.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-suffix-history-speculative-decoding-on-mixed-prom-9c482497e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
