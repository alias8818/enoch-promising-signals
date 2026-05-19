# Constrained span-candidate evidence ledgers for sub-1B QA generation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `28`
Project ID: `constrained-span-candidate-evidence-ledgers-for-sub-1b-qa-41c6554697`
Run ID: `constrained-span-candidate-evidence-ledgers-for-sub-1b-qa-41c6554697-20260516T103732481983+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `28`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Constrained span-candidate evidence ledgers for sub-1B QA generation: internal_generated:constrained-span-candidate-evidence-ledgers-for-sub-1b-qa-41c6554697

## What looked useful

Oracle ledger coverage is high, especially with larger candidate caps, so candidate ledgers can contain correct evidence spans; the negative result comes from the sub-1B likelihood selector failing to choose the right span often enough. The constraint guarantees evidence containment but loses 10-32 EM points versus free generation depending on cap/model.

## Boundaries and scale limits

Evaluation covered 500-example fixed-seed SQuAD subsets, three seeds for FLAN-T5-small, candidate-cap ablations, and one FLAN-T5-base run. It did not cover open-domain retrieval, multi-hop QA, synthetic QA pair training utility, human factuality assessment, or broad multi-dataset paper-scale validation.

## Claim scope

On SQuAD validation with supplied gold contexts, FLAN-T5-small/base sub-1B models, and greedy generation, model-scored constrained span-candidate evidence ledgers enforce in-context answers but substantially underperform free generation on EM and F1.

## Why it stopped

Direct fixed-seed SQuAD validation with real baselines and controls showed robust accuracy regressions for constrained span ledgers despite high oracle coverage; this is not paper-positive.

## Recommended next action

Stop this follow-up campaign at depth 4 and archive the negative useful-signal result; any future work should start only with a new selector mechanism that can close the observed EM/F1 gap against free generation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/constrained-span-candidate-evidence-ledgers-for-sub-1b-qa-41c6554697`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
