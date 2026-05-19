# Token-level GPT-2 latency test for suffix-copy speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `token-level-gpt-2-latency-test-for-suffix-copy-speculative-4980023e0f`
Run ID: `token-level-gpt-2-latency-test-for-suffix-copy-speculative-4980023e0f-20260516T135052988449+0000`

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

- Internal Enoch project: Token-level GPT-2 latency test for suffix-copy speculative decoding: internal_generated:token-level-gpt-2-latency-test-for-suffix-copy-speculative-4980023e0f

## What looked useful

Suffix-copy speculation gave exact greedy-equivalent outputs and improved latency when copied drafts were accepted; random history drafts were consistently slower and the no-draft control matched the autoregressive baseline, supporting the mechanism but not broad paper readiness.

## Boundaries and scale limits

Synthetic prompts only; no natural corpus or production trace distribution; GPT-2-small only; single-request Python/Hugging Face implementation; no batching, larger models, or fused serving decoder.

## Claim scope

On an NVIDIA GB10 using Hugging Face GPT-2-small greedy decoding, exact suffix-copy speculative verification reduced token latency on fixed-seed synthetic repeated-context prompts, with mean speedups of 2.87x for repeated clauses and 2.10x for interleaved repeated clauses at draft length 8, while preserving exact greedy outputs.

## Why it stopped

Tier 2 local evidence supports the mechanism in synthetic repeated-context settings, but the claim is not broad or natural enough for publication-grade closure.

## Recommended next action

Run the same exactness-preserving benchmark on a bounded natural text/code prompt corpus with measured suffix recurrence before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-corpus suffix-copy speculative decoding latency for GPT-2-class models
- Success threshold: At least 1.15x mean speedup over autoregressive greedy decoding on natural recurrent-prompt subsets, no significant slowdown on non-recurrent subsets after gating, and 100% exact greedy equivalence.
- Stop condition: Stop if suffix-copy mean speedup is below 1.05x on recurrent natural subsets, if exactness fails, or if random/no-draft controls explain the apparent gain.

## Evidence references

- Artifact root: `<local-path>/projects/token-level-gpt-2-latency-test-for-suffix-copy-speculative-4980023e0f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
