# Real-corpus suffix-index drafting with strong retrieval baselines

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-suffix-index-drafting-with-strong-retrieval-ba-7f40914aa9`
Run ID: `real-corpus-suffix-index-drafting-with-strong-retrieval-ba-7f40914aa9-20260524T050803717795+0000`

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

- Parent run decision: Rolling suffix-array context drafting: enoch://control-plane/projects/rolling-suffix-array-context-drafting-c1bed41f798b/runs/rolling-suffix-array-context-drafting-c1bed41f798b-20260524T044733896526+0000
- Parent run decision: LCP-accelerated suffix-index context drafting: enoch://control-plane/projects/lcp-accelerated-suffix-index-context-drafting-99edfb8d11/runs/lcp-accelerated-suffix-index-context-drafting-99edfb8d11-20260524T050011598399+0000

## What looked useful

Suffix replay improved mean accepted tokens from 0.0133 in the shuffled control to 0.1894 at similar coverage, but greedy backoff n-gram reached 0.2631 mean accepted tokens and higher first-token and >=2-token acceptance. Gating suffix matches increased conditional acceptance up to 0.3151 but reduced coverage to 0.2719 and lowered unconditional accepted tokens.

## Boundaries and scale limits

No neural verifier, no end-to-end speculative decoding loop, no large corpus beyond WikiText-2, and no 7B-class model integration. BM25 and n-gram baselines are local Python baselines, not production-optimized systems.

## Claim scope

On WikiText-2 raw v1 with 700k train tokens, 3 fixed seeds, and 3,600 held-out test positions, exact suffix-index continuation replay shows a real context-matching mechanism versus a shuffled-continuation control but does not beat a strong greedy backoff n-gram drafting baseline on direct accepted-token metrics.

## Why it stopped

Tier-2 real-corpus evidence supports the suffix-matching mechanism but falsifies the practical standalone drafting claim against a simple strong n-gram baseline.

## Recommended next action

Stop this paper track; if continuing, run a bounded opportunistic confidence-gated suffix-plus-ngram hybrid test on a larger real corpus with an explicit accepted-tokens-per-cost metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-gated suffix drafting as an opportunistic hybrid drafter
- Success threshold: Hybrid suffix-gated-plus-ngram must improve accepted tokens per millisecond by at least 10% over n-gram-only while preserving or improving mean accepted tokens across all fixed seeds.
- Stop condition: Stop if confidence gating still lowers unconditional mean accepted tokens or accepted tokens per millisecond versus n-gram-only on two consecutive fixed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-suffix-index-drafting-with-strong-retrieval-ba-7f40914aa9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
