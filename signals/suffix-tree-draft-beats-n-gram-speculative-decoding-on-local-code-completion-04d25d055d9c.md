# Suffix-Tree Draft Beats N-gram Speculative Decoding on Local Code Completion

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-tree-draft-beats-n-gram-speculative-decoding-on-local-code-completion-04d25d055d9c`
Run ID: `suffix-tree-draft-beats-n-gram-speculative-decoding-on-local-code-completion-04d25d055d9c-20260613T024228473994+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/db5f0839bd52

## What looked useful

Suffix-history averaged 1.847 accepted tokens per cursor versus 1.318 for the best fixed n-gram per seed, a 1.405x mean ratio with 1.356x minimum seed-level ratio.

## Boundaries and scale limits

No target LLM verifier, BPE tokenizer, IDE trace, wall-clock speculative decoding latency, multi-language repository mix, or index update-cost integration was tested. Corpus was 80 Python stdlib files with 909 total sampled cursors across three seeds.

## Claim scope

On a bounded offline benchmark over Python standard-library code, a prefix-only variable-order suffix-history draft policy produced more exact accepted lexical draft tokens per cursor than the best fixed-order n-gram baseline across three random cursor seeds.

## Why it stopped

Bounded offline draft-acceptance evidence supports the mechanism but is proxy-only rather than direct publication-grade speculative decoding evidence.

## Recommended next action

Stop this run as no-paper useful-signal evidence; deepen with the same policies inside a real speculative decoding harness using the target model tokenizer and verifier latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier-backed suffix-history speculative decoding on local code completion
- Success threshold: Suffix-history beats the best fixed n-gram by at least 20% accepted target tokens per cursor or at least 10% median latency reduction without increasing p95 latency, on at least 1000 held-out cursor positions.
- Stop condition: Stop if suffix-history fails to beat the best fixed n-gram by 10% accepted target tokens per cursor after 1000 held-out positions or if index/draft overhead removes any verifier-token gain.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-draft-beats-n-gram-speculative-decoding-on-local-code-completion-04d25d055d9c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
