# Residual-channel preservation on real BPE tokenizations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `residual-channel-preservation-on-real-bpe-tokenizations-6d45bd8b4c`
Run ID: `residual-channel-preservation-on-real-bpe-tokenizations-6d45bd8b4c-20260516T204503137868+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Residual-channel preservation on real BPE tokenizations: internal_generated:residual-channel-preservation-on-real-bpe-tokenizations-6d45bd8b4c

## What looked useful

A direct 5-seed GPT-2 BPE perplexity test supports the residual-channel preservation mechanism: grad-act masks beat activation-only and random controls in 5/5 seeds at the main 50% and 75% keep fractions and at all other tested keep fractions.

## Boundaries and scale limits

Single pretrained GPT-2-small model, one GPT-2 BPE tokenizer, one corpus, frozen weights, no pruning-aware recovery or fine-tuning, no larger models, no modern tokenizer families, no efficient runtime kernel validation, and 102400 validation tokens per seed.

## Claim scope

On pretrained GPT-2-small with real GPT-2 BPE tokenization on WikiText-2, gradient-times-activation residual-channel scores preserve next-token perplexity better than activation-only, gradient-only, permuted grad-act, and random masks across five fixed calibration seeds at 25%, 50%, 75%, and 87.5% channel keep fractions; weight-magnitude is stronger only at the harsh 25% keep fraction.

## Why it stopped

No-paper useful signal: the direct GPT-2 BPE mechanism test is positive, but publication-grade evidence would require recovery/fine-tuning persistence and broader model/tokenizer replication.

## Recommended next action

Run one final depth-4 deepen test with short post-mask recovery or fine-tuning on the same GPT-2 BPE setup; stop the chain if grad-act does not beat activation-only after recovery at 50% and 75% keep in at least 4/5 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Post-mask recovery validation for GPT-2 BPE residual-channel preservation
- Success threshold: Grad-act post-recovery validation perplexity ratio is lower than activation-only and random mean in at least 4/5 seeds at both 50% and 75% keep fractions, without being dominated by weight-magnitude at both fractions.
- Stop condition: Stop as no-paper if grad-act fails to beat activation-only after recovery in at least 4/5 seeds at either 50% or 75% keep, or if recovery eliminates the grad-act advantage.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-preservation-on-real-bpe-tokenizations-6d45bd8b4c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
