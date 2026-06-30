# Suffix-Array Drafting for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-drafting-for-speculative-decoding-d8f243d5f2c1`
Run ID: `suffix-array-drafting-for-speculative-decoding-d8f243d5f2c1-20260602T221021664117+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2be831567512

## What looked useful

Suffix retrieval showed 85.35% draft coverage, 0.095 expected accepted tokens per position, and 14.06% greedy first-token accept rate versus 0.00824 and 1.37% for random continuations; it slightly exceeded the count n-gram fallback at 0.079 expected accepted tokens and 10.74% greedy first-token accept rate. Absolute acceptance remained too low for a paper-ready speculative decoding claim.

## Boundaries and scale limits

No integrated speculative decoding loop, no KV-cache scheduler, no throughput measurement, one corpus, one GPT-2-class target model, deterministic proposal acceptance proxy only, and no comparison to a learned draft model.

## Claim scope

On a bounded WikiText-2/GPT-2 proxy with an 80k-token suffix-prefix index and 512 held-out positions, suffix-array-style retrieval produces deterministic 4-token drafts with higher target-LM acceptance proxy metrics than random corpus continuations and a modest edge over a simple count n-gram fallback.

## Why it stopped

No-paper closure: the local evidence is a proxy useful signal, not direct throughput validation, and absolute accepted-token rates were low.

## Recommended next action

Run a bounded integrated decode benchmark on a repetition-heavy real corpus, comparing suffix-array drafting against greedy decoding, count n-gram retrieval, prompt lookup, and a small learned drafter.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated suffix-array speculative decoding on repetition-heavy text
- Success threshold: At least 1.2x wall-clock decode throughput over greedy decoding and at least 0.5 accepted draft tokens per verification step while matching target output distribution constraints in the bounded benchmark.
- Stop condition: Stop if suffix-array drafting fails to beat count n-gram or prompt-lookup retrieval by at least 10% throughput, or if accepted draft tokens remain below 0.25 per verification step after tuning context length and draft length.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-drafting-for-speculative-decoding-d8f243d5f2c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
