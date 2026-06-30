# Rotating sparse optimizer updates for 75% optimizer memory reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rotating-sparse-optimizer-updates-for-75-optimizer-memory-reduction-4be87d1fd71f`
Run ID: `rotating-sparse-optimizer-updates-for-75-optimizer-memory-reduction-4be87d1fd71f-20260531T204902211295+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e8771661c28c

## What looked useful

The mechanism is feasible as optimizer-state accounting: active_fraction=0.25 used 67,592-72,984 bytes of Adam moments versus 270,360-291,920 bytes dense, a 74.998%-74.999% reduction, with each coordinate updated 96 times versus 384 dense updates. At the same 1e-3 learning rate it lagged dense AdamW on spiral loss (0.0306 vs 0.0012 mean validation loss) despite high accuracy; at 4e-3 it matched dense spiral accuracy and loss closely on these toy tasks. Gaussian10 was saturated for all configs.

## Boundaries and scale limits

Tested only MLPs with about 34k-36k parameters, synthetic/local datasets, 12 epochs, 3 seeds, and logical optimizer-state accounting. The implementation uses flattened parameter copies for measurement simplicity, so it does not demonstrate production peak-memory savings, distributed behavior, embedding-heavy models, transformer pretraining, or long-horizon stability.

## Claim scope

On two small deterministic classification tasks, a rotating sparse AdamW variant that keeps moments only for the active 25% parameter block achieved the intended ~75% logical Adam moment-state reduction and preserved final validation accuracy when the learning rate was compensated, but this is not full end-to-end memory or large-model evidence.

## Why it stopped

Bounded local evidence supports the optimizer-state mechanism but does not validate the original broad 75% optimizer memory reduction claim under realistic training memory, transformer dynamics, or long-horizon convergence.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded test should replace flattened-copy optimizer code with a production-style shard/state implementation and run a small transformer or GPT-2-small-class comparison with real peak-memory telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-style rotating AdamW state on a small transformer
- Success threshold: Measured optimizer-state peak memory is at least 70% lower than dense AdamW and final validation loss is within 5% of dense AdamW at matched token/step budget.
- Stop condition: Stop if production telemetry shows less than 50% optimizer-state peak-memory reduction, or if compensated rotating updates exceed dense validation loss by more than 15% after the planned budget.

## Evidence references

- Artifact root: `<local-path>/projects/rotating-sparse-optimizer-updates-for-75-optimizer-memory-reduction-4be87d1fd71f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
