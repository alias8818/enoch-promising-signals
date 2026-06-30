# Easy-to-Hard Curriculum vs Random Ordering for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `easy-to-hard-curriculum-vs-random-ordering-for-tiny-local-pretraining-e935926b6f50`
Run ID: `easy-to-hard-curriculum-vs-random-ordering-for-tiny-local-pretraining-e935926b6f50-20260619T093316287614+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fc6676296d4e

## What looked useful

Naive repeated easy-to-hard ordering was consistently worse than random ordering on validation loss and hard-bin loss in this tiny local pretraining proxy, suggesting non-iid ordering can harm rather than help.

## Boundaries and scale limits

Synthetic arithmetic corpus only; tiny transformer only; 5 paired seeds at 800 steps plus 3 paired seeds at 1600 steps; not natural-language, code, GPT-2-small-class, or web-scale pretraining evidence.

## Claim scope

In a controlled generated arithmetic next-token language-modeling proxy with a 4-layer 128-wide tiny transformer, repeated easy-to-hard example ordering underperformed random ordering at matched steps and data.

## Why it stopped

Proxy/early falsification rather than full validation: easy-to-hard ordering was worse than random in every paired seed across the bounded runs.

## Recommended next action

Stop this exact naive-curriculum line as a paper claim; if continuing locally, test a mixed or annealed curriculum that preserves hard-example exposure throughout training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mixed-difficulty annealed curriculum for tiny local pretraining
- Success threshold: Mixed annealed curriculum beats random by at least 0.03 nats/token mean validation loss and does not worsen hard-bin loss across at least 4 of 5 paired seeds.
- Stop condition: Stop if mixed annealing fails to beat random on mean validation loss or worsens hard-bin loss in 3 or more paired seeds.

## Evidence references

- Artifact root: `<local-path>/projects/easy-to-hard-curriculum-vs-random-ordering-for-tiny-local-pretraining-e935926b6f50`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
