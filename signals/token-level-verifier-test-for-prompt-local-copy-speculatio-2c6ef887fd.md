# Token-level verifier test for prompt-local copy speculation

Status: `useful_signal`
Project ID: `token-level-verifier-test-for-prompt-local-copy-speculatio-2c6ef887fd`
Run ID: `token-level-verifier-test-for-prompt-local-copy-speculatio-2c6ef887fd-20260518T183234221794+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6dcd20e5834b

## What looked useful

Prompt-local copy speculation has a strong token-level mechanism signal on controlled copy prompts: exact/distractor copy gold-hit rate was 100%, GPT-2-class top-5 verifier support was about 99.7-100%, and simple controls stayed near 0-8% top-5 support.

## Boundaries and scale limits

Only 24 examples per dataset, synthetic records, teacher-forced continuations, GPT-2-class verifiers, and rank/probability support metrics; no end-to-end speculative decoding, latency, natural corpus, long-context, or 7B+ validation.

## Claim scope

In controlled synthetic copy prompts, a longest-suffix prompt-local copy proposer recovers copied next tokens and receives high top-5 verifier support from distilgpt2 and gpt2, far above recent-token and random-seen controls.

## Why it stopped

Tier 1 mechanism threshold was met, but the evidence is synthetic and token-level only, so it is useful no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded end-to-end speculative decoding test on natural extractive/copy-heavy prompts, measuring accepted copied tokens per verifier pass and wall-clock latency versus no-speculation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end prompt-local copy speculative decoding on extractive prompts
- Success threshold: At least 1.5 accepted copied tokens per verifier pass and at least 10% wall-clock latency reduction on copy-heavy prompts, with no statistically meaningful degradation on no-copy controls.
- Stop condition: Stop if accepted copied tokens per verifier pass are below 1.2 or latency is not improved after accounting for proposer overhead.

## Evidence references

- Artifact root: `<local-path>/projects/token-level-verifier-test-for-prompt-local-copy-speculatio-2c6ef887fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
