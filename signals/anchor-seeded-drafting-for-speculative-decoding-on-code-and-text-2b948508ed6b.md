# Anchor-Seeded Drafting for Speculative Decoding on Code and Text

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-seeded-drafting-for-speculative-decoding-on-code-and-text-2b948508ed6b`
Run ID: `anchor-seeded-drafting-for-speculative-decoding-on-code-and-text-2b948508ed6b-20260610T103258416720+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b3efcd0e635c

## What looked useful

Anchor-seeded retrieval drafting produced high coverage and multi-token exact matches: 2.155 accepted tokens/query on code and 3.643 on text, versus 0.390 and 0.542 for the best fixed n-gram baselines.

## Boundaries and scale limits

Proxy-only offline corpus experiment; no target model logits, no tokenizer-specific model evaluation, no wall-clock speculative decoding speedup, no public benchmark sweep, and no validation above about 220k regex tokens per corpus.

## Claim scope

On local causal token streams from Python code and /usr/share/doc text, anchor-copy drafting from previous suffix matches accepted 5.52x and 6.72x more oracle future tokens per query than the best fixed n-gram majority next-token baseline.

## Why it stopped

Proxy mechanism result is useful but not full validation; stopping before paper claim because actual target-model acceptance and serving speedup were not measured.

## Recommended next action

Run a bounded direct speculative-decoding follow-up with a small open target model, measuring accepted tokens and wall-clock throughput against prompt-lookup and small-drafter baselines on the same code/text prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-Model Speculative Decoding Test for Anchor-Seeded Drafting
- Success threshold: At least 1.25x wall-clock throughput over greedy decoding and at least 10% higher accepted tokens/query than prompt-lookup or n-gram baseline on both code and text subsets.
- Stop condition: Stop if anchor retrieval overhead erases throughput gains or if accepted tokens/query is not better than prompt-lookup/ngram controls on either corpus.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-seeded-drafting-for-speculative-decoding-on-code-and-text-2b948508ed6b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
