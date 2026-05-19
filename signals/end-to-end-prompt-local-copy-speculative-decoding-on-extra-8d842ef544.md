# End-to-end prompt-local copy speculative decoding on extractive prompts

Status: `useful_signal`
Project ID: `end-to-end-prompt-local-copy-speculative-decoding-on-extra-8d842ef544`
Run ID: `end-to-end-prompt-local-copy-speculative-decoding-on-extra-8d842ef544-20260518T183734580343+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: End-to-end prompt-local copy speculative decoding on extractive prompts: internal_generated:end-to-end-prompt-local-copy-speculative-decoding-on-extra-8d842ef544

## What looked useful

Prompt-local copy drafting shows a reproducible end-to-end speed signal with exact FP32 greedy equivalence and fixed-seed controls, but benefits are modest and partly task/prompt-structure dependent.

## Boundaries and scale limits

Single 0.5B instruct model, greedy decoding only, 48-token cap, SQuAD-derived sentence-copy task, simple lexical drafter, conservative cache rebuild on partial accept, no production serving kernel, no larger-model or broad benchmark validation.

## Claim scope

On 192 SQuAD-derived sentence-copy prompts with Qwen2.5-0.5B-Instruct in FP32 greedy decoding, a lexical prompt-local copy drafter preserved exact target outputs and reduced target calls by 18.18% and wall time by 15.42% versus a KV-cache target-only baseline; a random prompt-span control saved 6.26% calls and 4.56% wall time.

## Why it stopped

Tier 2 local evidence supports a useful mechanism signal but is not broad or robust enough for a paper; BF16 sensitivity and shuffled-context savings limit the claim.

## Recommended next action

Run a bounded deepen follow-up using production-style KV cache slicing and a stronger target model on a broader extractive benchmark, with exact greedy equivalence and at least 25% wall-time reduction versus optimized target-only decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-cache prompt-local copy speculative decoding on broader extractive QA
- Success threshold: Across at least 500 examples, lexical prompt-local copy speculative decoding must maintain 100% exact greedy match and reduce wall time by at least 25% versus optimized target-only decoding, while beating random-span control by at least 10 percentage points in paired wall-time saving.
- Stop condition: Stop if exact greedy match drops below 100%, lexical copy fails to beat random-span control by 10 percentage points in paired wall-time saving, or production-style cache handling removes the observed speed advantage.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-prompt-local-copy-speculative-decoding-on-extra-8d842ef544`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
