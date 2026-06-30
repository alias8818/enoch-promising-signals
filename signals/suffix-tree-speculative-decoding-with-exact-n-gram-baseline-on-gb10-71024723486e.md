# Suffix-Tree Speculative Decoding with Exact N-Gram Baseline on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-with-exact-n-gram-baseline-on-gb10-71024723486e`
Run ID: `suffix-tree-speculative-decoding-with-exact-n-gram-baseline-on-gb10-71024723486e-20260621T221722041604+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cf76d8b746b8

## What looked useful

The suffix-style variable-context drafter accepted 1.26x to 2.21x more tokens per target position than exact fixed n-gram baselines, but lookup throughput was only 0.35x to 0.38x of exact n-gram, build time was 15x to 35x higher, and state count was 16x to 39x higher. The mechanism improves coverage but the naive index is not a clear end-to-end win.

## Boundaries and scale limits

No real transformer verification loop, no real text corpus, no optimized suffix-array/tree memory layout, no GPU retrieval, and no million-token or long-serving cache validation. The result should not be generalized to production speculative decoding throughput without an end-to-end model benchmark.

## Claim scope

Retrieval-only synthetic-token benchmark on GB10 comparing a Python bounded suffix-trie variable-context drafter against exact fixed n-gram drafters at 20k, 60k, and 120k training-token scales with 2,000 held-out decode positions per case.

## Why it stopped

Retrieval-only evidence is mixed: suffix retrieval improves mean accepted length but loses substantial lookup/build/index efficiency versus the exact n-gram baseline, so this is not a paper-positive validation.

## Recommended next action

Stop this run as no-paper useful signal; if pursued, run a bounded end-to-end small-model speculative decoding benchmark with exact n-gram, n-gram-backoff, and compact suffix retrieval under identical prompts and report accepted tokens per second.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-model speculative decoding with compact suffix retrieval versus exact n-gram backoff
- Success threshold: Compact suffix retrieval must improve end-to-end accepted tokens per second or generation tokens per second by at least 10% over the best exact n-gram/backoff baseline while staying within 2x memory and build/update cost.
- Stop condition: Stop if compact suffix retrieval is within +/-5% of the best exact n-gram/backoff baseline, is slower end-to-end, or exceeds 2x memory/build/update cost without a compensating throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-with-exact-n-gram-baseline-on-gb10-71024723486e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
