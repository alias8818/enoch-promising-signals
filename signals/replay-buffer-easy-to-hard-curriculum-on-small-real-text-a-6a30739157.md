# Replay-buffer easy-to-hard curriculum on small real text at fixed tokens

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `replay-buffer-easy-to-hard-curriculum-on-small-real-text-a-6a30739157`
Run ID: `replay-buffer-easy-to-hard-curriculum-on-small-real-text-a-6a30739157-20260619T115843243940+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Easy-to-hard data curriculum for tiny pretraining: does ordering matter at fixed tokens on GB10: enoch://control-plane/projects/easy-to-hard-data-curriculum-for-tiny-pretraining-does-ordering-matter-at-fixed-tokens-on-gb10-0f4623c4c3ee/runs/easy-to-hard-data-curriculum-for-tiny-pretraining-does-ordering-matter-at-fixed-tokens-on-gb10-0f4623c4c3ee-20260619T113821959212+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b8e093e8ed29

## What looked useful

Replay curriculum was worse than uniform by 1.98% mean validation NLL at 600 steps and 4.53% worse at 1800 steps; hard-quartile NLL also regressed at both budgets.

## Boundaries and scale limits

One-layer character GRU, character tokens, Tiny Shakespeare, 3 seeds, 4.9M and 14.7M train tokens per policy/seed. Does not cover subword LMs, GPT-2-small-class transformers, larger corpora, longer training, teacher-loss difficulty, or tuned replay schedules.

## Claim scope

In a controlled small real-text character-language-model test on Tiny Shakespeare at fixed consumed training tokens, the tested easy-to-hard replay curriculum did not improve validation NLL over uniform sampling.

## Why it stopped

Controlled small real-text fixed-token tests directly falsified the pre-registered success threshold for this implementation: replay did not achieve at least 1% validation NLL improvement and worsened hard-quartile NLL.

## Recommended next action

Stop this follow-up as a small direct negative; only revisit with a distinct medium transformer experiment that changes the difficulty estimator or curriculum schedule and keeps fixed-token uniform controls.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/replay-buffer-easy-to-hard-curriculum-on-small-real-text-a-6a30739157`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
