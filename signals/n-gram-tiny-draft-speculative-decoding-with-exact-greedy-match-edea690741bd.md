# N-gram tiny draft speculative decoding with exact greedy match

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-tiny-draft-speculative-decoding-with-exact-greedy-match-edea690741bd`
Run ID: `n-gram-tiny-draft-speculative-decoding-with-exact-greedy-match-edea690741bd-20260601T082920712137+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/14a984222a59

## What looked useful

Exact greedy equality held for all corrected runs. Backoff n-gram drafting improved over fixed-order drafting but remained low-acceptance: best local result accepted 12.79% of proposed tokens, reduced target calls by 12.45%, and measured about 1.17x wall-clock speedup. This is useful as a cheap exact baseline but not enough for a paper-positive claim.

## Boundaries and scale limits

Tested only distilgpt2, WikiText-2, 64 validation prompts, 32 generated tokens per prompt, up to 2000 WikiText-2 training texts for the n-gram table, and a non-production non-KV-cache local harness on one GB10.

## Claim scope

On distilgpt2 with WikiText-2 validation prompts, a backoff token n-gram draft can preserve exact greedy outputs under target verification and provide a small local target-call and wall-clock reduction in a Python/Transformers harness.

## Why it stopped

Local evidence supports exactness and a small mechanism-level speedup, but acceptance and validation breadth are too low for publication-grade support.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should compare backoff n-gram drafting against prompt-lookup and a learned tiny draft in a KV-cache decode harness with a success threshold of at least 1.5x exact-greedy end-to-end speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache benchmark of backoff n-gram draft versus prompt-lookup and learned tiny draft
- Success threshold: At least 1.5x end-to-end wall-clock speedup with exact greedy equality, and no worse than the prompt-lookup or learned tiny-draft baseline on the same prompts.
- Stop condition: Stop if backoff n-gram acceptance stays below 20% or end-to-end speedup stays below 1.25x in the first two KV-cache benchmark settings.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-tiny-draft-speculative-decoding-with-exact-greedy-match-edea690741bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
