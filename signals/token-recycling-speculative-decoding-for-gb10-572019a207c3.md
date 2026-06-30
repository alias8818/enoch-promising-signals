# Token recycling speculative decoding for gb10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `token-recycling-speculative-decoding-for-gb10-572019a207c3`
Run ID: `token-recycling-speculative-decoding-for-gb10-572019a207c3-20260614T092244005843+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/9845a53f1d57

## What looked useful

Naive recycling is harmless only in the IID control where stale tokens are not meaningfully prefix-dependent. In contextual cases, recycling raised target passes/token by 5.8% to 50.5%, reduced accepted draft tokens/pass by 1.5% to 37.9%, and raised bigram TV by 2.0x to 4.8x versus standard exact speculative decoding.

## Boundaries and scale limits

This was a controlled simulator with known p/q distributions, vocab 64, gamma 5, 4096 sequences x 512 tokens per case. It did not run a transformer target/draft pair or an end-to-end serving stack, so the result is an early algorithmic falsification rather than full transformer-scale validation.

## Claim scope

Naive token recycling that reuses rejected speculative suffix tokens as later draft proposals was tested in an exact Markov language-model simulator on GB10 CUDA. In context-dependent target/draft distributions, it reduced accepted draft tokens per target pass, increased target passes per generated token, and introduced measurable distributional bias relative to standard exact speculative decoding.

## Why it stopped

Proxy/early falsification: the direct algorithmic simulator showed stale recycled tokens break exactness and usually worsen target-pass efficiency in context-dependent generation.

## Recommended next action

Stop this naive-recycling line as no-paper evidence; if continuing, first test a corrected or context-similarity-gated recycling rule for exactness in the same simulator before any transformer-serving benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exactness-preserving gated token recycling for speculative decoding
- Success threshold: Pass simulator exactness within 1.2x standard bigram TV and reduce target passes/token by at least 5% in a contextual case; otherwise stop before transformer benchmarking.
- Stop condition: Stop if the corrected/gated rule cannot preserve exactness in the simulator or if its target-pass improvement is below 5% in all contextual cases.

## Evidence references

- Artifact root: `<local-path>/projects/token-recycling-speculative-decoding-for-gb10-572019a207c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
