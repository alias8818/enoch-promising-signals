# Anchor-ngram speculative decoding on long code context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-ngram-speculative-decoding-on-long-code-context-ba1a9fc19268`
Run ID: `anchor-ngram-speculative-decoding-on-long-code-context-ba1a9fc19268-20260610T040903986006+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43b997fa0ab8

## What looked useful

Anchor scoring improved exact accepted draft tokens by 1.33% to 5.10% relative across n-gram lengths 2-4, with the largest gain at 2-gram prefixes and diminishing gains for longer prefixes. Most decisions tied, so the practical effect may be limited unless model-level acceptance confirms it.

## Boundaries and scale limits

No target LLM, tokenizer-level speculative decoding loop, latency measurement, GPU inference, non-Python corpus, or production serving workload was tested. The largest run used 45,000 sampled positions across a 9-point parameter grid.

## Claim scope

On a CPU-only offline exact-continuation proxy over 20 Python stdlib files with 8K-token context windows, a def/class anchor-scored n-gram selector produced small but consistent mean accepted-token gains over a recency-only n-gram selector.

## Why it stopped

Closed as no-paper useful signal because the evidence is an offline exact-continuation proxy, not full model acceptance or serving-speed validation.

## Recommended next action

Stop this worker run; next run should test tokenizer-level anchor n-gram drafting inside a real code LLM speculative decoding loop and require both higher accepted tokens and net tokens/sec improvement after drafter overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-level anchor n-gram speculative decoding in a real code LLM loop
- Success threshold: At least 5% net tokens/sec improvement over recency-only n-gram speculative decoding with no degradation in exact output quality on a held-out long-code benchmark.
- Stop condition: Stop if anchor scoring adds less than 2% accepted-token improvement or any accepted-token gain is erased by drafter overhead in end-to-end tokens/sec.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-ngram-speculative-decoding-on-long-code-context-ba1a9fc19268`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
