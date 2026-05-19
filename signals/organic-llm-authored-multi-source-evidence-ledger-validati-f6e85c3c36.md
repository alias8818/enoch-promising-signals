# Organic LLM-authored multi-source evidence-ledger validation

Status: `useful_signal`
Project ID: `organic-llm-authored-multi-source-evidence-ledger-validati-f6e85c3c36`
Run ID: `organic-llm-authored-multi-source-evidence-ledger-validati-f6e85c3c36-20260518T150332896292+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Organic LLM-authored multi-source evidence-ledger validation: internal_generated:organic-llm-authored-multi-source-evidence-ledger-validati-f6e85c3c36

## What looked useful

The ledger variants failed to beat real baselines: full-evidence MNLI accuracy 0.5638 versus sentence-ledger logistic 0.5345 on 4,000 HoVer test examples; serialized ledger TF-IDF 0.5200; Qwen ledger prompt chance-level on 300 examples.

## Boundaries and scale limits

Main direct run used HoVer only, a tiny MNLI scorer, extractive sentence-ledger rows, and one 300-example Qwen2.5-0.5B organic ledger-prompt subset; no frontier LLM, human-authored ledger, or multi-dataset replication was run.

## Claim scope

On Dzeniks/HoVer binary claim verification, sentence-level evidence-ledger aggregation and a bounded Qwen-authored ledger prompt did not improve validation over whole-evidence NLI or artifact controls.

## Why it stopped

Direct HoVer validation produced a negative/no-paper result: tested ledger methods underperformed or matched baselines and controls, and the bounded organic LLM-ledger subset was chance-level.

## Recommended next action

Stop this depth-4 follow-up and do not claim paper-readiness; any future revisit should be a separate project with stronger LLM ledger authors, multi-dataset replication, and significant gains over whole-evidence baselines.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/organic-llm-authored-multi-source-evidence-ledger-validati-f6e85c3c36`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
