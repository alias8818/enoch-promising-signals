# Queue-Driven Curriculum Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-driven-curriculum-data-selection-for-tiny-pretraining-870f5470bf65`
Run ID: `queue-driven-curriculum-data-selection-for-tiny-pretraining-870f5470bf65-20260608T081823442969+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/19c7a26103ad

## What looked useful

Queue-driven deficit sampling reallocated training toward rare/hard buckets and reduced rare_hard_macro cross-entropy by 6.8% versus static curriculum and 8.8% versus imbalanced corpus-random sampling, but worsened macro loss by 6.4% versus static curriculum because common easy-bucket loss degraded.

## Boundaries and scale limits

Synthetic generated tasks, tiny character-level model, 600 training steps, 3 seeds, no natural language corpus, no downstream transfer, and no GPT-2-small-class or larger validation.

## Claim scope

In a 3-seed synthetic character-level tiny Transformer proxy with five heterogeneous pretraining buckets and a fixed 600-step budget, validation-deficit queue sampling improved rare/hard bucket validation loss but did not improve all-bucket macro validation loss over the best static-curriculum baseline.

## Why it stopped

Bounded proxy produced mixed evidence: the mechanism improves rare/hard buckets but fails the primary macro-improvement criterion, so this is not a full validation or paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded medium follow-up that tests replay-constrained validation queues on a real small pretraining corpus with static and corpus-random baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay-Constrained Queue Curriculum on Real Tiny Pretraining Buckets
- Success threshold: Replay-constrained queue improves rare/hard subgroup loss by at least 3% relative while matching or improving all-bucket macro validation loss versus the best baseline across at least 3 seeds.
- Stop condition: Stop if macro validation loss is worse than the best baseline by more than 1% after preserving rare/hard gains, or if rare/hard gains disappear under replay constraints.

## Evidence references

- Artifact root: `<local-path>/projects/queue-driven-curriculum-data-selection-for-tiny-pretraining-870f5470bf65`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
