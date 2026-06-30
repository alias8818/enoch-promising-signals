# Difficulty-ordered curriculum via auxiliary scorer on tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `difficulty-ordered-curriculum-via-auxiliary-scorer-on-tiny-pretraining-517502f93fba`
Run ID: `difficulty-ordered-curriculum-via-auxiliary-scorer-on-tiny-pretraining-517502f93fba-20260629T141717557060+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e50efb8a17e4

## What looked useful

Auxiliary scorer quality was not the bottleneck: score/difficulty correlation averaged 0.942 across seeds, yet easy-to-hard and hard-to-easy curricula were worse than random at every logged checkpoint. Final mean validation loss was 1.26185 for random, 1.37396 for easy-to-hard, and 1.36929 for hard-to-easy.

## Boundaries and scale limits

Three seeds, synthetic corpus only, tiny Transformer target model, 450 target optimizer steps per variant, no natural text or large-scale pretraining validation.

## Claim scope

In a synthetic tiny language-modeling pretraining harness with three latent difficulty families, a small auxiliary Transformer LM reliably ranked examples by difficulty, but naive global score-sorted curricula did not improve equal-token validation loss over random ordering.

## Why it stopped

Proxy toy evidence consistently falsified the naive sorted-ordering hypothesis under equal token budgets; this is not a full natural-language validation.

## Recommended next action

Stop this naive sorted-curriculum line as a paper claim; the bounded next test, if pursued, should evaluate paced or interleaved score-aware sampling that preserves mixed difficulty exposure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paced mixed curriculum from auxiliary scorer instead of global sorting
- Success threshold: Paced mixed curriculum reduces final mean validation loss versus random by at least 0.03 and is not worse on the hardest validation slice across at least five seeds.
- Stop condition: Stop if paced mixed sampling fails to beat random on overall validation loss by step 450 or improves only the easy slice while worsening level 2.

## Evidence references

- Artifact root: `<local-path>/projects/difficulty-ordered-curriculum-via-auxiliary-scorer-on-tiny-pretraining-517502f93fba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
