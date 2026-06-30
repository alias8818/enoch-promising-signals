# Speculative Decoding: Small Draft Model Acceleration

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-small-draft-model-acceleration-8f76a11801c1`
Run ID: `speculative-decoding-small-draft-model-acceleration-8f76a11801c1-20260613T112942182072+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/3aa1f9434937

## What looked useful

A deterministic 60-condition simulator found 1.288-2.734 generated tokens per target call. Break-even held for 60/60 conditions at draft_cost <= 0.05, 49/60 at draft_cost 0.10, and 28/60 at draft_cost 0.20. Distribution TV matched target-only sampling-noise controls.

## Boundaries and scale limits

No real LLM weights, GPU wall-clock timing, KV-cache effects, batching overhead, tokenizer effects, or concrete target/draft model pair were tested. Evidence is mechanism-level and proxy-only.

## Claim scope

Synthetic Markov-model speculative decoding supports conditional acceleration: target-equivalent cost improves when the draft distribution is sufficiently close and draft-token cost is low enough; best modeled speedups ranged from 1.459x at draft_cost=0.20 to 2.531x at draft_cost=0.01.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct full validation of real small-draft model acceleration.

## Recommended next action

Stop this run as proxy-only useful signal; next run should benchmark one real target/draft model pair on GPU with measured wall-clock tokens/sec and acceptance diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model speculative decoding wall-clock benchmark
- Success threshold: At least 1.3x median wall-clock tokens/sec improvement over target-only decoding across a bounded prompt set, with no material quality or distribution regression and reproducible logs/metrics.
- Stop condition: Stop as negative if measured speedup is below 1.1x, acceptance is too low to amortize draft cost, or GPU/KV-cache overhead erases modeled gains.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-small-draft-model-acceleration-8f76a11801c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
