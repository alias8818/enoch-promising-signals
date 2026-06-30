# Speculative Decoding on CPU: N-gram Draft vs Suffix-Tree vs No-Spec Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-on-cpu-n-gram-draft-vs-suffix-tree-vs-no-spec-baseline-ae8f692ab7c1`
Run ID: `speculative-decoding-on-cpu-n-gram-draft-vs-suffix-tree-vs-no-spec-baseline-ae8f692ab7c1-20260611T133202036974+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d4e7aaefaf4c

## What looked useful

Suffix-copy drafting gave a modeled 1.876x speedup on highly repetitive traces by reducing target calls 82.2%, but the best medium-repetition configuration was slower than no-spec at 0.965x and low-repetition traces were clearly worse at 0.720x.

## Boundaries and scale limits

No real LLM, tokenizer, KV cache, production CPU inference engine, or real workload trace was benchmarked; results should not be generalized to deployed CPU serving without direct engine validation.

## Claim scope

Synthetic CPU-trace speculative decoding with exact target continuations, n-gram and suffix-copy draft predictors, and a measured NumPy CPU target-verification cost surrogate.

## Why it stopped

Proxy evidence is mixed and insufficient for paper-positive claims: suffix-copy helps only in the high-repetition synthetic regime, while medium and low repetition fail to beat no-spec under measured CPU verification costs.

## Recommended next action

Stop this proxy run as no-paper useful signal; run a bounded direct CPU inference follow-up with a real small LLM/KV-cache engine and repetition-bucketed real traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM validation of suffix-copy speculative decoding by repetition bucket
- Success threshold: For high-repetition real traces, suffix-copy achieves at least 1.20x wall-clock tokens/sec over no-spec with exact matching outputs, while medium/low-repetition buckets are reported honestly even if slower.
- Stop condition: Stop if high-repetition real traces do not exceed 1.05x wall-clock speedup, or if engine integration cannot verify draft blocks exactly within a bounded local CPU run.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-on-cpu-n-gram-draft-vs-suffix-tree-vs-no-spec-baseline-ae8f692ab7c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
