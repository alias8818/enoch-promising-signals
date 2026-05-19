# Held-out sub-1B generation test for evidence-ledger validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `held-out-sub-1b-generation-test-for-evidence-ledger-valida-be30b56387`
Run ID: `held-out-sub-1b-generation-test-for-evidence-ledger-valida-be30b56387-20260516T095742915043+0000`

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

- Internal Enoch project: Held-out sub-1B generation test for evidence-ledger validation: internal_generated:held-out-sub-1b-generation-test-for-evidence-ledger-valida-be30b56387

## What looked useful

Ledger-valid rate averaged 0.801 for true contexts versus 0.001 for shuffled contexts, with acceptance precision 0.828 and recall 0.984 versus F1>=0.5 correctness. Plain prompting slightly outperformed ledger prompting on F1, and DistilBERT extractive QA remained stronger.

## Boundaries and scale limits

Single 77M-parameter generator, SQuAD extractive QA only, 900 held-out examples total across fixed seeds, deterministic validator fallback used because the model did not reliably emit evidence quotes; no broader open-ended generation or larger sub-1B replication.

## Claim scope

On three fixed 300-example SQuAD validation samples with google/flan-t5-small, a deterministic evidence-ledger validator can attach context-sentence evidence to many supported sub-1B generated answers and nearly eliminates true ledger validity under shuffled evidence, but the ledger prompt does not improve generation over a plain prompt.

## Why it stopped

Medium fixed-seed evidence supports a narrow validator mechanism but falsifies the stronger claim that the current sub-1B ledger prompt improves generation or yields reliable model-authored evidence ledgers.

## Recommended next action

Stop this run as no-paper evidence; a bounded follow-up should test constrained model-authored evidence ledgers with a more instruction-following sub-1B model and no deterministic quote fallback.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained model-authored evidence ledgers for sub-1B QA generation
- Success threshold: Model-authored quote-found rate >=0.90, ledger-valid rate >=0.70, ledger F1 no worse than plain F1 by more than 0.02, and shuffled-context ledger-valid rate <=0.05 across all fixed seeds.
- Stop condition: Stop negative if the model-authored quote-found rate remains below 0.75 or ledger F1 is more than 0.05 below plain F1 on two fixed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-sub-1b-generation-test-for-evidence-ledger-valida-be30b56387`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
