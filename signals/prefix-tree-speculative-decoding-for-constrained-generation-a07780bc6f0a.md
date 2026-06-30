# Prefix-tree speculative decoding for constrained generation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prefix-tree-speculative-decoding-for-constrained-generation-a07780bc6f0a`
Run ID: `prefix-tree-speculative-decoding-for-constrained-generation-a07780bc6f0a-20260609T091235418908+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/93c206f86f51

## What looked useful

Across 72 synthetic rows, speculative decoding averaged 1.70x launch reduction versus unary-skip on template slots, 1.74x on random tries, 1.29x on shared JSON, and 1.0x on flat enumerations. A 50k-sample focused case matched exact target TV about as well as baseline while reducing launches 2.94x versus unary-skip.

## Boundaries and scale limits

No real transformer, KV-cache kernel, GPU/CPU serving latency, production schema dataset, or trained draft model was tested. Launch counts are an algorithmic proxy, not wall-clock model throughput.

## Claim scope

Synthetic finite-trie constrained sampling with exact enumerated target distributions: prefix-tree speculative blocks preserve the constrained distribution within Monte Carlo error and reduce counted target launches beyond a unary-skip baseline only on trie shapes with multiple nearby branch decisions.

## Why it stopped

Synthetic algorithmic evidence is promising but insufficient for a paper-positive claim because real model serving latency and real constrained-generation workloads were not directly tested.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should wrap the same sampler around a small real transformer and constrained benchmark to measure wall-clock latency against strict and unary-skip baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model latency validation for prefix-tree speculative constrained decoding
- Success threshold: At least 1.5x median wall-clock speedup versus unary-skip on repeated-branch workloads, no speedup claim on flat-enum controls, and no statistically meaningful output-distribution drift.
- Stop condition: Stop as negative if draft overhead or block verification makes speedup versus unary-skip less than 1.2x on repeated-branch workloads or if exactness checks show material distribution drift.

## Evidence references

- Artifact root: `<local-path>/projects/prefix-tree-speculative-decoding-for-constrained-generation-a07780bc6f0a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
