# N-gram CPU draft for speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cpu-draft-for-speculative-decoding-3d5717657fb1`
Run ID: `n-gram-cpu-draft-for-speculative-decoding-3d5717657fb1-20260523T173904443479+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ba0aaaf3c26

## What looked useful

The mechanism is plausible only for repeated or stereotyped contexts: prompt-adaptive order-4 gamma-4 reached 17.58% first-token exact match and 0.38% full-draft match, while shuffled order-4 gamma-4 reached 2.68% and 0.00%. High-dominance repeated 4-token contexts were rare but stronger, with 31.06% first-token and 3.42% full gamma-4 exact match.

## Boundaries and scale limits

This run used a text exact-match proxy, not an LLM verifier; it did not measure real speculative-decoding wall-clock speedup, tokenizer effects, KV-cache behavior, or serving integration overhead. Evidence is small/local and should not be generalized to 7B+ model serving without direct verifier measurements.

## Claim scope

On a 361k-token public-domain text benchmark with 5,000 held-out sampled positions, a CPU n-gram drafter is very cheap and beats a shuffled control, but generic exact continuation acceptance is low: about 16-18% first-token match and about 0.20-0.23 average accepted draft tokens for gamma up to 8.

## Why it stopped

Proxy evidence supports cheap drafting and a repeat-context mechanism, but acceptance is too low and too indirect for a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test is to integrate the n-gram drafter with a small open LLM verifier and measure actual tokens/s on generic versus repetition-heavy prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LLM verifier test for prompt-adaptive n-gram speculative decoding
- Success threshold: At least 1.15x wall-clock tokens/s over no-draft on repetition-heavy prompts with no regression larger than 5% on generic prompts, measured across at least 100 prompts or continuations.
- Stop condition: Stop if end-to-end wall-clock speedup is below 1.05x on repetition-heavy prompts or if drafter/indexing overhead erases the target-pass reduction.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cpu-draft-for-speculative-decoding-3d5717657fb1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
