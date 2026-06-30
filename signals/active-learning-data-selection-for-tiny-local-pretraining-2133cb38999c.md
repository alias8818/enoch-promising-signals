# Active Learning Data Selection for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `active-learning-data-selection-for-tiny-local-pretraining-2133cb38999c`
Run ID: `active-learning-data-selection-for-tiny-local-pretraining-2133cb38999c-20260608T171903583668+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c9a4a95ae464

## What looked useful

High proxy-loss selection collapsed to 100% noise and was far worse than random. Low-loss selection selected 100% target examples but still underperformed random, suggesting easy/redundant examples. A label-aware target oracle beat random, so the failure is specific to proxy-loss-only acquisition rather than lack of selectable signal.

## Boundaries and scale limits

Three synthetic seeds, 3000 candidates per seed, 480 selected sequences, 120 proxy steps, 260 fresh-model training steps per selected subset; not natural language, not GPT-2-small-class, and not a long-schedule validation.

## Claim scope

Toy synthetic tiny causal-LM pretraining with mixed target, near-target, and noise candidates: proxy-loss-only active selection did not improve held-out target validation loss over random sampling at equal selected-sequence budget.

## Why it stopped

Proxy-scale early falsification, not full validation: the tested proxy-loss-only active selection strategies all underperformed random on direct tiny-LM target validation loss, while the oracle control showed subset choice can matter.

## Recommended next action

Stop this run as a proxy-scale early falsification of proxy-loss-only selection; a bounded follow-up should test quality-filtered diversity-aware acquisition on a semi-natural corpus before any larger pretraining run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quality-filtered diversity-aware acquisition for tiny pretraining
- Success threshold: Diversity-aware quality-filtered acquisition reduces mean target validation loss by at least 5% relative to both random and quality-filtered random with non-overlapping 95% bootstrap confidence intervals.
- Stop condition: Stop if the method fails to beat quality-filtered random by 2% mean validation loss after the planned seeds or if selection diagnostics show collapse to redundant/easy examples.

## Evidence references

- Artifact root: `<local-path>/projects/active-learning-data-selection-for-tiny-local-pretraining-2133cb38999c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
