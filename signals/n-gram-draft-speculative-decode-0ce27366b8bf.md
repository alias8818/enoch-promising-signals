# N-gram Draft Speculative Decode

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-draft-speculative-decode-0ce27366b8bf`
Run ID: `n-gram-draft-speculative-decode-0ce27366b8bf-20260604T222103992367+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5938b088e934

## What looked useful

distilgpt2 at 48 tokens/prompt matched greedy outputs for all 8 prompts. With max_draft=8, synthetic prompts had 0.842 acceptance, 30 vs 192 target calls, and 3.13x wall speedup; natural prompts had 1.000 acceptance, 32 vs 192 target calls, and 2.43x wall speedup. A max_draft sweep showed speedups rising from 1.34x to 3.96x on synthetic prompts as target calls fell.

## Boundaries and scale limits

Tested only on sshleifer/tiny-gpt2 and distilgpt2, 4 synthetic/repetitive prompts plus 4 natural prompts, 12-48 generated tokens per prompt. Natural-prompt gains were mostly from distilgpt2 newline repetition. No stochastic sampling, large model, batched serving, real trace, optimized KV-cache verifier, or production kernel was tested.

## Claim scope

In exact greedy decoding with small GPT-2-family models on small handcrafted prompt suites, a history n-gram draft can reproduce the target greedy sequence exactly while reducing target-model calls and improving local wall-clock latency when continuations contain repeated n-grams.

## Why it stopped

Small direct benchmark supports the mechanism but is too narrow and partly driven by greedy repetition loops, so it is not publication-grade validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is an optimized KV-cache verification benchmark on real corpus prompts with GPT-2-small-class and a learned-draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized n-gram speculative decoding on real prompt corpora
- Success threshold: At least 1.25x median latency speedup with exact greedy equivalence on a predeclared repetitive/copy-heavy subset, no regression beyond 5% on non-repetitive prompts, and clear evidence that gains are not only newline or single-token loops.
- Stop condition: Stop if exact equivalence fails, if median speedup is below 1.10x after optimized verification, or if gains appear only on degenerate repeated whitespace/single-token loops.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decode-0ce27366b8bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
