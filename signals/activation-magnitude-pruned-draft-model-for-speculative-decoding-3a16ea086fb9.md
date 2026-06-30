# Activation-Magnitude Pruned Draft Model for Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `activation-magnitude-pruned-draft-model-for-speculative-decoding-3a16ea086fb9`
Run ID: `activation-magnitude-pruned-draft-model-for-speculative-decoding-3a16ea086fb9-20260524T235226035010+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/95c5fb3a129e

## What looked useful

Activation-magnitude pruning beat random pruning at both 50% and 25% MLP keep on KL, total variation, draft NLL, and sampled speculative acceptance; at 25% keep it also beat weight-magnitude pruning on all reported draft-distribution and speculative acceptance metrics.

## Boundaries and scale limits

Evidence is synthetic and small-scale: 1.82M parameter target, one seed, MLP-only compaction, no natural-language corpus, no pretrained GPT-2-small-class target, no dense small-draft baseline, and no optimized end-to-end serving speed measurement.

## Claim scope

On a toy synthetic causal language-model task, activation-magnitude MLP neuron pruning can create a compact draft that preserves the trained target distribution better than matched random pruning and improves sampled speculative acceptance, especially at stronger 25% MLP keep compression.

## Why it stopped

Closed as no-paper useful-signal evidence because the current result is synthetic/toy-scale and does not directly validate natural-language quality or production speculative decoding speedup.

## Recommended next action

Run a bounded pretrained GPT-2-small-class follow-up on real text with matched dense small-draft and weight-pruned controls, reporting end-to-end speculative decoding tokens/sec and acceptance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2 activation-pruned draft benchmark for speculative decoding
- Success threshold: Activation-pruned draft improves end-to-end speculative decoding throughput by at least 10% over the best matched pruning control without increasing validation NLL by more than 5% relative to that control, and the result holds for at least two gamma values.
- Stop condition: Stop if activation pruning fails to beat random pruning on both KL and sampled speculative acceptance at two sparsity levels, or if end-to-end throughput is not better than the dense small-draft baseline.

## Evidence references

- Artifact root: `<local-path>/projects/activation-magnitude-pruned-draft-model-for-speculative-decoding-3a16ea086fb9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
