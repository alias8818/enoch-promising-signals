# Local-Complexity Curriculum for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `local-complexity-curriculum-for-tiny-pretraining-cb25e652d6fb`
Run ID: `local-complexity-curriculum-for-tiny-pretraining-cb25e652d6fb-20260525T120601547376+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8cd4bb28951f

## What looked useful

Easy-to-hard local-complexity ordering was an early negative: medium confirmation val loss was 2.5174 for sequential easy-to-hard and 2.4387 for paced easy-to-hard versus 2.4078 for random. The hard-bucket regressions were +0.2366 and +0.0565 loss. A paced hard-to-easy schedule produced a small opposite-direction signal, 2.4010 val loss and -0.0178 hard-bucket loss versus random.

## Boundaries and scale limits

Single corpus, character-level tokenization, small transformer, 600-step medium confirmation, three seeds, no GPT-2-small-class baseline, no large-corpus pretraining, no downstream transfer, and no long-horizon scaling law check.

## Claim scope

In a tiny character-level transformer pretraining proxy on Tiny Shakespeare, easy-to-hard local-complexity curricula did not improve validation loss over shuffled sampling at matched optimizer steps and token budget; both sequential and paced easy-to-hard schedules were worse, especially on high-complexity validation windows.

## Why it stopped

The original easy-to-hard local-complexity curriculum was falsified in a bounded proxy rather than validated; evidence is useful but too small and too proxy-scoped for publication.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing, run one bounded token-level deepen test of paced hard-to-easy versus shuffled on a small GPT-style model and at least two corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-Level Hard-to-Easy Local-Complexity Curriculum Check
- Success threshold: Paced hard-to-easy must beat shuffled by at least 0.02 validation loss on hard buckets and not be worse overall by more than 0.005 on both corpora.
- Stop condition: Stop if hard-to-easy fails to beat shuffled on hard-bucket validation in either corpus or if the effect disappears when exposure is matched.

## Evidence references

- Artifact root: `<local-path>/projects/local-complexity-curriculum-for-tiny-pretraining-cb25e652d6fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
