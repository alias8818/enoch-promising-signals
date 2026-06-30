# Spec-Decoding with N-gram Fallback

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `spec-decoding-with-n-gram-fallback-6bfdcae87d4c`
Run ID: `spec-decoding-with-n-gram-fallback-6bfdcae87d4c-20260607T230436323963+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fec5ab3734c4

## What looked useful

The corrected exact verifier matched greedy output on all tested prompts and all ablation settings. Main GPT-2 setting max_n=4, gamma=4 reduced target passes by 55.6% on average with 2.45 generated tokens per target pass and 49.8% draft acceptance; gamma=8 reached 60.2% reduction with lower acceptance.

## Boundaries and scale limits

Only GPT-2 small, nine fixed prompts, 64 generated tokens per prompt, greedy decoding, and a prototype full-context verifier were tested. No production KV-cache serving stack, large modern target model, corpus benchmark, neural-draft comparison, or stochastic sampling correction was tested.

## Claim scope

Bounded mechanism probe: for exact greedy decoding with GPT-2 small on nine fixed prompts, a local n-gram fallback draft preserved exact target output and reduced target verification passes.

## Why it stopped

No-paper useful signal: bounded local evidence supports the mechanism, but the prompt set and implementation are too narrow for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on real text and code corpora with an optimized KV-cache verifier and compare n-gram fallback against no-draft and neural-draft baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus benchmark for n-gram fallback speculative decoding
- Success threshold: N-gram fallback preserves exact greedy outputs and achieves at least 20% target-pass reduction or latency improvement over no-draft on one real corpus slice without losing badly to neural draft on all slices.
- Stop condition: Stop if exactness fails, if target-pass reduction is below 10% on both real text and code slices, or if optimized latency is worse than no-draft despite fewer target passes.

## Evidence references

- Artifact root: `<local-path>/projects/spec-decoding-with-n-gram-fallback-6bfdcae87d4c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
