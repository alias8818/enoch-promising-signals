# N-gram Draft Model for GPT-2-small Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-model-for-gpt-2-small-speculative-decoding-0d7cfd0a1e6f`
Run ID: `n-gram-draft-model-for-gpt-2-small-speculative-decoding-0d7cfd0a1e6f-20260605T000414232169+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8918b642850a

## What looked useful

The n-gram draft mechanism works but is weak: backoff n-grams proposed many tokens, accepted only 2.6-9.0% of attempted draft tokens depending on draft length, and produced a stable 13.4-13.5% target-call reduction. Larger draft chunks did not improve accepted-token count and mostly increased wasted proposals.

## Boundaries and scale limits

Tested only GPT-2-small, WikiText-2, 24 prompts, 32 generated tokens per prompt, deterministic greedy decoding, and a simple no-cache full-prefix verifier. Not validated for production KV-cache speculative decoding, batched serving, stochastic decoding, broader corpora, or larger models.

## Claim scope

On a bounded GPT-2-small/WikiText-2 exact-greedy harness, a longest-match backoff n-gram draft model preserves exact greedy output and reduces target forward calls by about 13.4-13.5%, with low draft acceptance and about 1.17-1.20x wall-time speedup in a no-cache full-prefix verifier/baseline.

## Why it stopped

Bounded direct evidence supports a small mechanism but not a paper-ready claim; low acceptance makes the simple global n-gram draft model only modestly useful.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should compare prompt-local or retrieval-augmented n-gram drafting against this global WikiText n-gram baseline under the same exact GPT-2-small verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-local n-gram draft table for GPT-2-small exact speculative decoding
- Success threshold: At least 25% target-call reduction with exact output equality on both datasets and no worse than 1.15x wall-time speedup in the no-cache harness.
- Stop condition: Stop if prompt-local or retrieval-augmented n-grams remain below 20% target-call reduction or fail exact output equality.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-model-for-gpt-2-small-speculative-decoding-0d7cfd0a1e6f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
