# Lookahead Jacobi Decoding on GB10: Draft-Free Parallel Verification

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `lookahead-jacobi-decoding-on-gb10-draft-free-parallel-verification-0f790db347f7`
Run ID: `lookahead-jacobi-decoding-on-gb10-draft-free-parallel-verification-0f790db347f7-20260628T142358047866+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3a0b5f922d63

## What looked useful

Naive target-model-only Jacobi block verification accepted only 1.00-1.10 tokens per target forward and ran at 0.44-0.57x cached greedy throughput in exact float32 runs. fp16 full-prefix recomputation can also diverge from cached greedy near argmax ties.

## Boundaries and scale limits

Tested GPT-2 124M, five prompts, 64 generated tokens for final float32 sweep, block sizes 4/8/16. Did not test full Lookahead Decoding n-gram pool/cache, optimized serving kernels, batching, long contexts, or 7B+ models.

## Claim scope

On GB10 with Hugging Face GPT-2 and a naive draft-free Jacobi block verifier without the Lookahead Decoding n-gram pool/cache, exact float32 decoding matches greedy but does not speed up generation.

## Why it stopped

Early bounded negative: direct local tests show exact naive Jacobi verification has too little multi-token acceptance and too much full-prefix recompute overhead to beat cached greedy; this is not a full validation or falsification of the complete Lookahead Decoding algorithm.

## Recommended next action

Stop this naive variant; the only bounded follow-up worth running is to implement the full Lookahead Decoding n-gram pool/cache on GB10 and require both exactness and >1.1x cached-greedy tokens/sec before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 Lookahead Decoding with n-gram pool/cache
- Success threshold: Sustained >1.5 accepted tokens per target forward and >1.1x cached-greedy tokens/sec on GPT-2-class models across the prompt suite, with exact greedy equivalence.
- Stop condition: Stop if n-gram pool/cache implementation still stays below 1.2 accepted tokens per forward or below 0.9x cached-greedy tokens/sec after bounded tuning.

## Evidence references

- Artifact root: `<local-path>/projects/lookahead-jacobi-decoding-on-gb10-draft-free-parallel-verification-0f790db347f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
