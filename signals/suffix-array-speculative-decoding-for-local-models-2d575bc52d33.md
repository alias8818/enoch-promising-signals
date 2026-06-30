# Suffix-Array Speculative Decoding for Local Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-for-local-models-2d575bc52d33`
Run ID: `suffix-array-speculative-decoding-for-local-models-2d575bc52d33-20260524T202015062703+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b5ed284b6fb1

## What looked useful

Copy-heavy prompts reached 3.24x ideal target-call speedup with 36.6% proposed-token acceptance using max_match=24, while natural held-out prompts reached only 1.12x with 1.7% acceptance and 0% full-draft acceptance. A max_match=1 ablation matched natural-text behavior and improved copy-heavy speedup to 5.34x, weakening the suffix-array-specific novelty claim.

## Boundaries and scale limits

Small model, 16 prompts per suite, 48 generated target tokens per prompt, idealized target-call simulation rather than end-to-end speculative decoding latency; natural text limited to Tiny Shakespeare held-out paragraphs and copy-heavy workload is synthetic.

## Claim scope

On a bounded distilgpt2 greedy-decoding proxy, suffix-index/copy proposals produce useful idealized target-call reductions on synthetic copy-heavy boilerplate/code prompts but not on held-out natural-text prompts.

## Why it stopped

Bounded local evidence is an early/proxy falsification for general natural-text use and does not support the specific suffix-array speculative-decoding claim beyond repetitive copy-heavy cases; this is not a full large-model validation.

## Recommended next action

Stop this project as no-paper useful signal; a separate bounded deepen follow-up should test real code/autocomplete traces with wall-clock speculative decoding and n-gram/cache baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Wall-clock suffix/cache speculative decoding on real code traces
- Success threshold: At least 20% median wall-clock latency reduction versus no speculation on real code/autocomplete traces, with suffix/cache draft outperforming simpler n-gram cache baselines and no quality regression under greedy decoding.
- Stop condition: Stop if real trace acceptance remains below 10% proposed-token acceptance or median wall-clock latency improvement is below 10% after accounting for index and verification overhead.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-for-local-models-2d575bc52d33`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
