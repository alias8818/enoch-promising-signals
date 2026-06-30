# Redundancy-Adversarial Filtering for Tiny Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `redundancy-adversarial-filtering-for-tiny-models-fc0ae652c99d`
Run ID: `redundancy-adversarial-filtering-for-tiny-models-fc0ae652c99d-20260526T090521015089+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/026a37900b96

## What looked useful

Redundancy-aware filtering is useful compared with random matched removal under duplicate adversarial pollution, but the adversarial warmup-loss component did not improve over simple dedupe and global loss-only filtering was harmful.

## Boundaries and scale limits

No real language model, no real text corpus, no GPT-2-small-class baseline, no semantic near-duplicate detector, and no datacenter-scale validation. Runs were 8-seed synthetic probes with one-hidden-layer MLPs.

## Claim scope

Synthetic CPU-only bag-of-words tiny-model benchmark with redundant mislabeled duplicate clusters. RAF reduces adversarial duplicate retention and beats random matched downsampling, but does not beat full-data training and is slightly worse than dedupe-only filtering.

## Why it stopped

Proxy synthetic evidence is mixed and does not support RAF over simpler full-data or dedupe controls; this is an early no-paper falsification, not a full real-LM validation.

## Recommended next action

Stop this RAF claim as no-paper based on synthetic evidence; a bounded next test should compare dedupe-only versus RAF on a real small text task before any larger LM run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Dedupe-only versus RAF on a real small noisy text benchmark
- Success threshold: RAF improves OOD or clean held-out accuracy by at least 2 percentage points over both full-data and dedupe-only baselines on mean across seeds, without more than 1 point IID degradation.
- Stop condition: Stop if RAF fails to beat dedupe-only by at least 1 point mean accuracy after 5 seeds or if loss-only/adversarial scoring remains harmful.

## Evidence references

- Artifact root: `<local-path>/projects/redundancy-adversarial-filtering-for-tiny-models-fc0ae652c99d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
