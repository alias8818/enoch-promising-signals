# Suffix-Array Speculative Drafting for CPU Inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `suffix-array-speculative-drafting-for-cpu-inference-fb94b90dd665`
Run ID: `suffix-array-speculative-drafting-for-cpu-inference-fb94b90dd665-20260608T104414003959+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8b444109bef9

## What looked useful

Exact suffix retrieval was coverage-limited at 4-token contexts and too noisy at 2-token contexts. Across Shakespeare, Frankenstein, and Sherlock traces, non-oracle suffix-array mean accepted tokens/query was 0.004-0.040 with min_ctx=4 and 0.057-0.159 with min_ctx=2; full 8-token acceptance was zero. A suffix-array oracle scanning up to 512 candidates only reached 0.158-0.367 mean accepted tokens/query with near-zero full draft acceptance, while n-gram hash lookup was typically 10-15x faster.

## Boundaries and scale limits

This was a bounded CPU-only trace proxy, not real target-LM speculative decoding. It used simple word/punctuation tokens, static train/test corpus splits, Python implementations, and public-domain prose/drama corpora rather than modern subword LLM corpora, code traces, document-local prompt history, or end-to-end inference.

## Claim scope

On three public-domain word/punctuation token traces up to 120k tokens, a static suffix-array retrieval drafter over an earlier corpus slice produced very low exact held-out continuation yield for 8-token drafts and did not beat a direct n-gram hash baseline on accepted tokens per millisecond.

## Why it stopped

Bounded trace-level proxy evidence provides an early falsification rather than a full validation: retrieval continuations rarely match held-out futures, oracle candidate selection remains weak, and suffix-array lookup is slower than a direct hash baseline in the tested regime.

## Recommended next action

Stop this suffix-array-as-static-retriever direction for general CPU inference unless a bounded document-local or small-LM acceptance follow-up first shows at least 1 accepted token per query and better accepted tokens per millisecond than a hash/trie baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Document-local retrieval drafting with real small-LM acceptance
- Success threshold: At least 1.0 accepted tokens/query and at least 20% higher end-to-end tokens/second than both no-draft and hash/trie retrieval baselines on a bounded repetition-heavy workload, without a regression on ordinary prose controls.
- Stop condition: Stop if suffix retrieval remains below 0.5 accepted tokens/query, fails to beat hash/trie accepted tokens per millisecond, or increases end-to-end CPU inference latency.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-drafting-for-cpu-inference-fb94b90dd665`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
