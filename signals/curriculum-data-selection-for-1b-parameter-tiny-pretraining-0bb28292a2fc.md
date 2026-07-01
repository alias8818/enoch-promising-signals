# Curriculum Data Selection for 1B Parameter Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `curriculum-data-selection-for-1b-parameter-tiny-pretraining-0bb28292a2fc`
Run ID: `curriculum-data-selection-for-1b-parameter-tiny-pretraining-0bb28292a2fc-20260611T141438200585+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4ab3cbe94cf3

## What looked useful

Simple predictability-based quality selection removed random noise but over-selected near-duplicate boilerplate, producing much worse structured validation loss than random selection. Diversity filtering mitigated the damage but still lagged random.

## Boundaries and scale limits

No real web corpus, no transformer stack, no tokenizer study, no downstream tasks, and no 1B-parameter or GPU pretraining run. Results only test the proxy mechanism and early selection failure mode.

## Claim scope

CPU-only synthetic tiny-LM proxy comparing simple curriculum/data-selection policies under a fixed selected-document and SGD-step budget.

## Why it stopped

Proxy early falsification: naive quality/easy-to-hard selection underperformed random in the controlled tiny-LM setup; this is not full 1B-scale validation.

## Recommended next action

Run a bounded real-corpus small-transformer follow-up that compares random sampling, quality filtering, and duplicate-capped quality-diversity selection at matched sequence-item budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus small-transformer check for duplicate-capped curriculum selection
- Success threshold: Quality plus duplicate/domain caps beats random validation NLL by at least 2% across seeds while naive quality alone does not, with diagnostics showing reduced duplicate concentration.
- Stop condition: Stop if duplicate/domain-capped quality selection fails to beat random by 2% mean validation NLL or if gains are not consistent across at least two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-data-selection-for-1b-parameter-tiny-pretraining-0bb28292a2fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
