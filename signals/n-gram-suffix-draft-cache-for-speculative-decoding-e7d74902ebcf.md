# N-gram Suffix Draft Cache for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-draft-cache-for-speculative-decoding-e7d74902ebcf`
Run ID: `n-gram-suffix-draft-cache-for-speculative-decoding-e7d74902ebcf-20260523T184222924072+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/613e7ca7ee3d

## What looked useful

The cache mechanism works on deterministic repetition and can yield small optimistic wins for two-token drafts on natural text, but raw suffix hits are mostly first-token failures for longer speculative blocks. At gamma=8, Tiny Shakespeare estimated speedup was 0.990 at draft cost 0.02 and Alice was 1.105, with 87.9% and 81.3% zero-accept drafts respectively. Best ablation settings used gamma=2, with estimated speedups of 1.112-1.213 online and 1.062-1.194 static train/test.

## Boundaries and scale limits

No transformer target model was run; word/punctuation tokenization was used instead of production LLM tokenization; speedups are call-count estimates rather than measured GPU serving latency; natural-text evidence covers two small public traces only.

## Claim scope

Trace-level evaluation of an online n-gram suffix draft cache on Tiny Shakespeare, Alice in Wonderland, and a synthetic repeated-token positive control using exact future-token prefix acceptance.

## Why it stopped

Bounded proxy evidence supports only short-horizon opportunistic drafting, not a standalone n-gram suffix cache for robust speculative decoding.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded deepen test should use real model-token traces and measured target verification overhead before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-token suffix draft cache with measured verification overhead
- Success threshold: On at least two non-synthetic generation workloads, gamma>=4 cache drafts achieve measured end-to-end speedup above 1.10 with zero-accept rate below 60% and no quality change relative to the target model samples.
- Stop condition: Stop if gamma>=4 measured speedup is below 1.05 or zero-accept rate stays above 75% after adding a reasonable confidence/support filter.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-draft-cache-for-speculative-decoding-e7d74902ebcf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
