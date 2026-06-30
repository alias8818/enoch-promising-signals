# Speculative Drafting with Anchor Verification for Long Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `speculative-drafting-with-anchor-verification-for-long-context-fc5d952ad3a6`
Run ID: `speculative-drafting-with-anchor-verification-for-long-context-fc5d952ad3a6-20260525T101421551315+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3646626a8185

## What looked useful

In a 100,000-trial-per-condition Monte Carlo grid, sparse anchor verification frequently accepted corrupted long-context draft blocks. At length 256 with stride 32, false accepts among accepted blocks were 22.11% at 0.1% draft token error, 70.94% at 0.5%, 91.66% at 1.0%, and 99.34% at 2.0%, while using only 3.5% of full verifier token checks.

## Boundaries and scale limits

Synthetic/proxy evidence only: no real LLM serving stack, no natural long-context prompt corpus, no measured model latency, and no quality evaluation. The result directly tests the anchor-only correctness mechanism, not all possible anchor-like verifiers.

## Claim scope

Sparse token-anchor verification is not a correctness-preserving replacement for full per-token speculative verification on deterministic long-context copy spans with independent draft token errors.

## Why it stopped

Proxy early falsification: the tested sparse-token anchor mechanism accepts many unchecked interior errors on long-context copy spans, so the current idea is not paper-ready and should not be scaled as a correctness-preserving speculative decoder without a stronger verifier.

## Recommended next action

Stop the anchor-only variant as a correctness-preserving verifier; if continuing locally, test an exact block-checksum or contiguous micro-span verifier against the same false-accept threshold before any real-model latency work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-plus-block verifier for long-context speculative drafting
- Success threshold: False accept rate among accepted blocks below 1% for block lengths 128 and 256 at 1% draft token error, with target verification work fraction at or below 0.33.
- Stop condition: Stop if false accepts remain above 1% at 1% draft token error or if verifier work exceeds one third of full per-token verification.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-drafting-with-anchor-verification-for-long-context-fc5d952ad3a6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
