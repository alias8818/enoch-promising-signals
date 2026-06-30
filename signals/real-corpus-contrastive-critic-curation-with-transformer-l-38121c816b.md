# Real-corpus contrastive critic curation with transformer LM validation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-corpus-contrastive-critic-curation-with-transformer-l-38121c816b`
Run ID: `real-corpus-contrastive-critic-curation-with-transformer-l-38121c816b-20260528T115451111255+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Tiny contrastive critic for local pretraining data curation: enoch://control-plane/projects/tiny-contrastive-critic-for-local-pretraining-data-curation-522d5c92e966/runs/tiny-contrastive-critic-for-local-pretraining-data-curation-522d5c92e966-20260528T080903376555+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1290e91868e3

## What looked useful

A stronger contrastive critic produced a score spread and bottom-scored chunks trained a worse LM than random, but top-scored curation did not improve held-out LM loss versus random and missed the +2% success threshold.

## Boundaries and scale limits

One real corpus, one seed, byte-level 2-layer transformer models, 1536 selected training windows, 384 validation windows, and a weak-to-modest critic; not a GPT-2-scale or multi-corpus validation.

## Claim scope

Small direct WikiText-2 byte-level transformer LM test of contrastive critic top-score curation versus random and bottom-score controls.

## Why it stopped

Controlled small direct real-corpus transformer LM validation failed the stated threshold: top-score curation was -0.023% worse than random in the stronger-critic run, not >=2% better.

## Recommended next action

Stop this branch as no-paper evidence; only revisit with a materially stronger critic objective and repeated multi-seed LM validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out contrastive critic with multi-seed subword LM curation validation
- Success threshold: Mean top-score curated LM validation loss >=2% lower than random with top beating bottom in all or nearly all seeds.
- Stop condition: Stop if held-out critic accuracy remains below 60% or if the mean top-score LM improvement is below 1% after three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-contrastive-critic-curation-with-transformer-l-38121c816b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
