# Mass-aware exact-anchor clustered KV cache decoding on GPT-2-small

Status: `useful_signal`
Project ID: `mass-aware-exact-anchor-clustered-kv-cache-decoding-on-gpt-22c14bdcc3`
Run ID: `mass-aware-exact-anchor-clustered-kv-cache-decoding-on-gpt-22c14bdcc3-20260519T073503497929+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Mass-aware exact-anchor clustered KV cache decoding on GPT-2-small: internal_generated:mass-aware-exact-anchor-clustered-kv-cache-decoding-on-gpt-22c14bdcc3

## What looked useful

Mass-aware clustering achieved delta NLL +0.6639 and top-1 match 0.6367 versus full KV at 0.376 mean cache ratio, while uniform clustering was +5.3748 NLL, random representatives +4.9993 NLL, and anchors-only +6.4023 NLL. This supports the mechanism that attention-mass-weighted older-token clusters carry useful information, but the quality gap is too large for a paper-ready cache-compression method.

## Boundaries and scale limits

Completed evidence covers 8 WikiText-2 validation windows, 32 target tokens per window, 3 fixed seeds, GPT-2-small only, fp16 inference, and an unoptimized Python per-step clustering implementation. It does not cover larger models, longer contexts, free-running generation, optimized kernels, or broad corpus robustness.

## Claim scope

On GPT-2-small teacher-forced WikiText-2 validation windows, mass-aware exact-anchor clustered KV compression at a 96-entry cache budget over 256-token prefixes preserves substantially more next-token behavior than uniform clustering, random older representatives, or anchors-only, but it does not preserve full-cache quality.

## Why it stopped

Completed medium direct validation found a real mechanism signal versus controls, but the GPT-2-small quality loss versus full KV cache is too large and the prototype is too slow for a paper-positive result.

## Recommended next action

Run a bounded deepen follow-up with vectorized or periodic compression plus a budget/anchor sweep; stop unless at least one setting reaches delta NLL <= 0.15 at <= 50% mean cache length with top-1 match >= 0.80 on at least 2048 WikiText-2 target tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Vectorized periodic mass-aware KV clustering budget sweep on GPT-2-small
- Success threshold: At least one mass-aware setting has delta NLL <= 0.15 versus full KV, top-1 match >= 0.80, and mean cache length <= 50% of full prefix cache, while outperforming all ablations.
- Stop condition: Stop if all mass-aware settings remain above delta NLL 0.30 or fail to beat the strongest non-mass-aware ablation on the fixed validation windows.

## Evidence references

- Artifact root: `<local-path>/projects/mass-aware-exact-anchor-clustered-kv-cache-decoding-on-gpt-22c14bdcc3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
