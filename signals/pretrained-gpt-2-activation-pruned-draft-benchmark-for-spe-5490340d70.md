# Pretrained GPT-2 activation-pruned draft benchmark for speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pretrained-gpt-2-activation-pruned-draft-benchmark-for-spe-5490340d70`
Run ID: `pretrained-gpt-2-activation-pruned-draft-benchmark-for-spe-5490340d70-20260525T014631675133+0000`

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

- Parent run decision: Activation-Magnitude Pruned Draft Model for Speculative Decoding: enoch://control-plane/projects/activation-magnitude-pruned-draft-model-for-speculative-decoding-3a16ea086fb9/runs/activation-magnitude-pruned-draft-model-for-speculative-decoding-3a16ea086fb9-20260524T235226035010+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/95c5fb3a129e

## What looked useful

Top-k keep 75% reached 0.925 expected one-step acceptance and 0.915 top-1 agreement; top-k keep 50% reached 0.759 expected acceptance and 0.704 top-1 agreement, while random 50% keep fell to 0.172 acceptance and 0.031 top-1 agreement. All pruned variants were slower than dense GPT-2 in the hook-based dense implementation.

## Boundaries and scale limits

This run did not test custom sparse kernels, full speculative decoding wall-clock, large held-out corpora, temperature sampling, or larger target/draft model pairs. Metrics are one-step distribution overlap/top-1/NLL plus dense forward timing on GPT-2-small.

## Claim scope

On a 32-prompt Tier 1 CUDA benchmark with pretrained GPT-2-small as both target and activation-pruned draft, magnitude top-k activation pruning preserves next-token behavior much better than random masking, but 50% keep misses the preset expected-acceptance threshold and dense PyTorch activation masking does not speed up the draft.

## Why it stopped

Tier 1 direct benchmark produced mixed mechanism support but failed the practical draft threshold: 50% top-k acceptance was below 0.80 and dense activation pruning was slower than the unmodified target, so this is not paper-positive evidence.

## Recommended next action

Stop this branch as no-paper useful signal; next bounded work should test a compute-saving structured or sparse implementation rather than more dense activation masks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Structured compute-saving GPT-2 activation-pruned draft benchmark
- Success threshold: A structured or sparse activation-pruned draft is at least 10% faster than dense GPT-2-small forward while maintaining expected one-step acceptance >=0.90 and top-1 agreement >=0.85 on a held-out prompt set.
- Stop condition: Stop if no compute-saving variant beats dense GPT-2 latency or if all variants below dense latency have expected acceptance below 0.85.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-gpt-2-activation-pruned-draft-benchmark-for-spe-5490340d70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
