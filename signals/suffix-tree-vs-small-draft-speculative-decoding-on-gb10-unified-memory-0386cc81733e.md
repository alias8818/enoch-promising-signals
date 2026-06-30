# Suffix-tree vs small-draft speculative decoding on GB10 unified memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-vs-small-draft-speculative-decoding-on-gb10-unified-memory-0386cc81733e`
Run ID: `suffix-tree-vs-small-draft-speculative-decoding-on-gb10-unified-memory-0386cc81733e-20260620T005136567877+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/970da9f66e8b

## What looked useful

Across three calibrated seeds, suffix lookup was extremely cheap and accepted 4.74 tokens/position on copied-span traces, while the tiny GRU draft accepted 5.61 tokens/position but spent about 16.4 s proposing over 3,992 positions. On IID Zipf traces suffix lookup made zero proposals, while the draft accepted only about 0.024 tokens/position with the same proposal overhead. This supports suffix lookup as a cheap repeat-span proposer or hybrid gate, not as a universal replacement for a learned draft.

## Boundaries and scale limits

No real target model verification, no natural-language/code corpus, no optimized draft KV-cache or batching, and no large UMA stress test. Results should not be treated as full end-to-end decoding throughput validation.

## Claim scope

Bounded synthetic/proxy speculative-decoding proposer comparison on GB10: online suffix-context lookup versus a small CUDA GRU draft on repeated and low-repetition token traces, scored by exact held-out-token acceptance.

## Why it stopped

Synthetic proxy evidence is useful but insufficient for paper-positive claims; it does not validate end-to-end target-model decoding throughput.

## Recommended next action

Stop this run as no-paper useful signal; next run should perform real target-model speculative verification on natural-language/code traces with no-speculation, suffix-only, draft-only, and suffix-first/draft-fallback baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-target suffix-first versus draft-only speculative decoding
- Success threshold: Suffix-first/draft-fallback must improve end-to-end tokens/s by at least 10% over the better of suffix-only and draft-only on repeated-span workloads without regressing more than 3% on low-repetition workloads.
- Stop condition: Stop if suffix matching contributes less than 5% accepted tokens on real traces or if proposal/index overhead eliminates throughput gains versus the best single-method baseline.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-vs-small-draft-speculative-decoding-on-gb10-unified-memory-0386cc81733e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
