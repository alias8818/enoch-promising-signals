# Medium transformer shard fingerprint confirmation with marker-background controls

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-transformer-shard-fingerprint-confirmation-with-mar-c9a29bc6f4`
Run ID: `medium-transformer-shard-fingerprint-confirmation-with-mar-c9a29bc6f4-20260621T015332295313+0000`

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

- Parent run decision: Statistical Fingerprinting of Volunteer Training Shards: enoch://control-plane/projects/statistical-fingerprinting-of-volunteer-training-shards-f9e573fc6ebb/runs/statistical-fingerprinting-of-volunteer-training-shards-f9e573fc6ebb-20260621T011752544847+0000
- Parent run decision: Neural LM shard fingerprint probe with marker-background controls: enoch://control-plane/projects/neural-lm-shard-fingerprint-probe-with-marker-background-c-cd85e7a28a/runs/neural-lm-shard-fingerprint-probe-with-marker-background-c-cd85e7a28a-20260621T013716093924+0000

## What looked useful

Transformer shard-ID accuracy was 1.000 for marker-plus-background, 0.998 for marker-only, 1.000 for background-only, and 0.235 for the null control versus 0.25 chance across seeds 11/17/23. The unigram baseline matched positive-condition accuracy, showing the detected fingerprint is largely lexical rather than transformer-specific.

## Boundaries and scale limits

CPU-only small Transformer LMs on synthetic corpora; no natural text, pretrained GPT-2-small-class model, large-scale training, or unigram-matched real-data shard validation.

## Claim scope

Synthetic 4-shard language-model provenance test with fixed seeds, marker/background ablations, null shared-distribution control, and a per-shard unigram baseline. Shard identity is recoverable from held-out sequence losses when marker or background token distributions differ.

## Why it stopped

Medium confirmation found reproducible synthetic shard fingerprints, but the real unigram baseline solved the same task, so the stronger transformer-specific fingerprint claim is not supported.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use unigram-matched or marker-stripped shards and require the Transformer to beat lexical baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Unigram-matched transformer shard fingerprint test on controlled text shards
- Success threshold: Transformer shard-ID accuracy at least 0.40 with chance 0.25 and at least 0.05 absolute accuracy above unigram and other lexical baselines across all fixed seeds, with positive mean best-other-minus-true NLL margin.
- Stop condition: Stop as negative if unigram-matched marker-free shards stay at or below 0.30 accuracy or fail to beat lexical baselines by 0.05 absolute accuracy across fixed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/medium-transformer-shard-fingerprint-confirmation-with-mar-c9a29bc6f4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
