# Context-Suffix Speculative Decoding Without Any Draft Model

Status: `useful_signal`
Project ID: `context-suffix-speculative-decoding-without-any-draft-model-cb96b6c2ff11`
Run ID: `context-suffix-speculative-decoding-without-any-draft-model-cb96b6c2ff11-20260519T053100620435+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a66c1f900995

## What looked useful

Suffix lookup proposals are useful on repetitive/self-similar contexts and useless on random traces; exact full-context verification reduced target calls from 64 to about 24-26 on gpt2 fp32 and from 128 to about 41-44 on distilgpt2. Practical KV-cache serving remains unresolved because the GPT-2 cached verifier diverged from cached greedy in this prototype.

## Boundaries and scale limits

Tested only Hugging Face eager inference on GB10 with hand-written prompts, max 128 generated tokens, tiny/distilgpt2/gpt2-class models, and a prototype cache implementation. No standard corpus, large modern LM, sampling, batching, paged KV-cache, or production serving kernel validation.

## Claim scope

Local small-model evidence shows that context-suffix prompt lookup can act as a no-draft speculative proposal source and preserve greedy decoding under full-context verification on distilgpt2 and gpt2; one distilgpt2 KV-cache run was also exact and faster than cached greedy.

## Why it stopped

Moderate local evidence supports the mechanism, but the result is not paper-positive and GPT-2 cached verification exactness failed in the prototype.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to harden an exact KV-cache verifier and rerun on a standard text corpus before considering any serving-speed claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact KV-Cache Context-Suffix Verification on Standard Text Prompts
- Success threshold: Zero exactness failures and at least 1.25x mean tokens/sec over cached greedy on the repetitive/high-self-similarity subset, without more than 5% regression on low-repetition prompts.
- Stop condition: Stop as negative if any exactness failure remains after cache-position fixes or if speedup over cached greedy is below 1.10x on the high-repetition subset.

## Evidence references

- Artifact root: `<local-path>/projects/context-suffix-speculative-decoding-without-any-draft-model-cb96b6c2ff11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
