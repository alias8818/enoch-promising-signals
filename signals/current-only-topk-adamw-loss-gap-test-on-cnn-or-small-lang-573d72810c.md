# Current-Only TopK AdamW Loss-Gap Test on CNN or Small Language Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `current-only-topk-adamw-loss-gap-test-on-cnn-or-small-lang-573d72810c`
Run ID: `current-only-topk-adamw-loss-gap-test-on-cnn-or-small-lang-573d72810c-20260520T104424580936+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Harder Direct Neural Loss-Gap Test for Current-Only TopK AdamW: enoch://control-plane/projects/harder-direct-neural-loss-gap-test-for-current-only-topk-a-65c3145573/runs/harder-direct-neural-loss-gap-test-for-current-only-topk-a-65c3145573-20260520T103357937469+0000
- Parent run decision: Direct Neural Benchmark for Current-Only Sparse-TopK-AdamW: enoch://control-plane/projects/direct-neural-benchmark-for-current-only-sparse-topk-adamw-2acf29f184/runs/direct-neural-benchmark-for-current-only-sparse-topk-adamw-2acf29f184-20260520T102857777219+0000

## What looked useful

Magnitude-selected current-only TopK AdamW is better than random-k sparsity and can nearly close the FashionMNIST CNN loss gap at 20-50% density with longer training, but aggressive sparsity has a substantial fixed-budget gap.

## Boundaries and scale limits

Single dataset, single CNN, no validation split, no small language model, no hyperparameter sweep, and best-test-loss selection uses the test set as a diagnostic rather than a paper-grade selection protocol.

## Claim scope

On one small FashionMNIST CNN with fixed seeds 0/1/2, current-gradient magnitude TopK AdamW has a clear 10-epoch loss gap at 5-20% density, but with 30 epochs narrows to a small +0.0096 best-test-loss gap at 20% density and effectively matches dense AdamW at 50% density; random-k 20% remains worse.

## Why it stopped

Bounded local validation produced a useful but mixed no-paper signal; the result supports the mechanism but does not justify a publication-grade claim.

## Recommended next action

Run one final depth-4 bounded deepen test with a validation split and either CIFAR-10 CNN or a small language model, using a predeclared success threshold of <=0.01 validation-selected test-loss gap at <=20% density versus dense AdamW.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validation-Selected TopK AdamW Loss-Gap Test on CIFAR-10 or Small LM
- Success threshold: Mean validation-selected test loss gap <=0.01 versus dense AdamW at <=20% density, and at least 0.015 lower loss than random-k at the same density.
- Stop condition: Stop if <=20% TopK exceeds dense AdamW by >0.03 mean test loss after the tuned fixed budget or fails to beat random-k by at least 0.01.

## Evidence references

- Artifact root: `<local-path>/projects/current-only-topk-adamw-loss-gap-test-on-cnn-or-small-lang-573d72810c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
