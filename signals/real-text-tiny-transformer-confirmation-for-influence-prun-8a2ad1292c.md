# Real-text tiny-transformer confirmation for influence-pruned data selection

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-text-tiny-transformer-confirmation-for-influence-prun-8a2ad1292c`
Run ID: `real-text-tiny-transformer-confirmation-for-influence-prun-8a2ad1292c-20260610T122301195406+0000`

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

- Parent run decision: Influence-pruned data selection beats random subsampling for tiny local pretraining: enoch://control-plane/projects/influence-pruned-data-selection-beats-random-subsampling-for-tiny-local-pretraining-b911f7976f63/runs/influence-pruned-data-selection-beats-random-subsampling-for-tiny-local-pretraining-b911f7976f63-20260610T034842769983+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7ed16ef07a68

## What looked useful

Naive influence_top selection failed the predefined success threshold, losing to random in all 3 paired seeds with mean held-out loss difference +0.02005. The ranking still had signal because bottom-ranked blocks were consistently worse, suggesting the failure may be redundancy/overfitting or approximation quality rather than pure noise.

## Boundaries and scale limits

Tiny character-level Transformer, Tiny Shakespeare corpus, 300 final training updates, final-layer/norm gradient scoring approximation; not a broad-corpus or GPT-2-scale validation.

## Claim scope

Tier 1 direct real-text tiny-Transformer test of naive top gradient-alignment subset selection on Tiny Shakespeare: 512 candidate blocks, 128 selected blocks, 3 paired final-training seeds.

## Why it stopped

Corrected Tier 1 direct test did not satisfy the stated threshold: influence_top had higher held-out loss than random in 3/3 paired seeds.

## Recommended next action

Stop this branch as no-paper evidence; the one bounded next test is diversity-capped influence selection using the same real-text paired-seed protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-capped influence pruning on real-text tiny Transformer
- Success threshold: Diversity-capped influence_top beats random in at least 2 of 3 paired seeds with negative mean held-out loss difference, while bottom control remains worse than top.
- Stop condition: Stop if diversity-capped influence_top fails to beat random in at least 2 of 3 paired seeds or if bottom-control separation disappears.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-tiny-transformer-confirmation-for-influence-prun-8a2ad1292c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
