# Suffix-tree speculative decoding on CPU with exact no-spec baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-on-cpu-with-exact-no-spec-baseline-51527ad0b5f2`
Run ID: `suffix-tree-speculative-decoding-on-cpu-with-exact-no-spec-baseline-51527ad0b5f2-20260621T143002201921+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3f2726222032

## What looked useful

The mechanism is exact and can reduce target-call count on recurrent contexts, but direct CPU speedup is unsupported for a cheap target. The idea is only promising if a real batched verifier has enough per-call overhead to amortize suffix-index drafting.

## Boundaries and scale limits

Synthetic corpora only; deterministic n-gram target only; no real transformer logits, KV-cache behavior, or directly measured batched neural verifier. Simulated target-call overhead is not publication-grade speed evidence.

## Claim scope

In a bounded synthetic CPU benchmark with a deterministic word n-gram target, suffix/context-index speculative decoding preserved exact greedy output and reduced counted target invocations by 71.3% to 74.1%, but the unbatched Python implementation was slower wall-clock than the exact no-spec baseline.

## Why it stopped

Bounded synthetic evidence supports exactness and call reduction but does not directly support wall-clock CPU speedup over the exact no-spec baseline.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a CPU transformer follow-up with exact greedy baseline and batched draft verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU transformer suffix-index speculation with batched exact verification
- Success threshold: At least 1.15x wall-clock speedup over exact greedy no-spec decoding with zero output mismatches on recurrent prompts, and no more than 5% slowdown on non-recurrent prompts.
- Stop condition: Stop if batched verification cannot be implemented exactly on CPU within the local budget, or if measured speedup stays below 1.05x on recurrent prompts after draft-length calibration.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-on-cpu-with-exact-no-spec-baseline-51527ad0b5f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
