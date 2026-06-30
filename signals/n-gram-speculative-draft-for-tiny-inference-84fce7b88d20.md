# N-gram speculative draft for tiny inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-draft-for-tiny-inference-84fce7b88d20`
Run ID: `n-gram-speculative-draft-for-tiny-inference-84fce7b88d20-20260607T171138273482+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a5e63a14f587

## What looked useful

Corpus n-gram drafting reached exact_match_rate 1.0, mean acceptance 0.723, mean forward reduction 0.585, and mean 2.85x local throughput speedup. Prompt-lookup drafting reached exact_match_rate 1.0, mean acceptance 0.872, mean forward reduction 0.702, and mean 3.28x local throughput speedup.

## Boundaries and scale limits

One tiny GPT-2-family model, one Shakespeare-style corpus, 12 held-out prompts per main condition, 64 generated tokens per prompt, greedy decoding only, and a prototype full-context verifier rather than production KV-cache serving.

## Claim scope

In a bounded distilgpt2 + Tiny Shakespeare greedy-decoding probe, order-4 n-gram drafting preserved exact target-model output and reduced target verifier forward calls for short repetitive prompts.

## Why it stopped

This run produced a useful small-model mechanism signal, but it is prototype-bound and not publication-grade or production-serving evidence.

## Recommended next action

Run a cache-aware verifier benchmark on a broader prompt suite with repetitive/code/log and non-repetitive controls before making any serving-speed claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware n-gram speculative decoding for tiny-model serving
- Success threshold: Exact match rate 1.0, median latency speedup above 1.15x on repetition-rich prompt classes, and no more than 5% median slowdown on non-repetitive controls.
- Stop condition: Stop as negative if cache-aware prompt lookup fails exact parity, has median latency speedup at or below 1.05x on repetition-rich prompts, or imposes more than 10% median slowdown on non-repetitive controls.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-tiny-inference-84fce7b88d20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
