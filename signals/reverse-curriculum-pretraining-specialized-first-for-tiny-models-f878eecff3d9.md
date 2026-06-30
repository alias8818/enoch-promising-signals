# Reverse-Curriculum Pretraining: Specialized-First for Tiny Models

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `reverse-curriculum-pretraining-specialized-first-for-tiny-models-f878eecff3d9`
Run ID: `reverse-curriculum-pretraining-specialized-first-for-tiny-models-f878eecff3d9-20260610T001501936924+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e1d7582ea778

## What looked useful

Specialized-first learned the specialized stream after phase 1 but forgot it after the later general phase: final specialized loss averaged 7.9818 versus 0.9435 for general-first and 0.9643 for mixed. Mixed training preserved specialized performance while matching specialized-first on general validation.

## Boundaries and scale limits

Synthetic streams only; sub-million-parameter Transformer; 5 seeds; 220 steps per phase; not a GPT-2-small-class or real-corpus validation.

## Claim scope

In a controlled synthetic tiny causal-LM experiment with identical token budgets, the naive specialized-first-then-general curriculum did not improve final specialized validation loss and was strongly worse than both general-first-then-specialized and mixed curricula.

## Why it stopped

Proxy synthetic early falsification of the naive specialized-first schedule: the result is not full validation, but it directly tested equal-token curriculum order and found strong specialized forgetting.

## Recommended next action

Stop naive order-only specialized-first scaling; only run a bounded follow-up if adding replay or retention controls that directly target the observed forgetting mechanism.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Specialized-first with replay retention for tiny models
- Success threshold: special_first_plus_replay final specialized loss within 0.10 nats of mixed while final general loss is no worse than mixed by more than 0.10 nats.
- Stop condition: Stop if replay/retention cannot reduce the special-first final specialized loss gap below 1.0 nat versus mixed across 5 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/reverse-curriculum-pretraining-specialized-first-for-tiny-models-f878eecff3d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
