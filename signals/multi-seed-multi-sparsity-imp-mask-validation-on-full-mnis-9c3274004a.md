# Multi-seed Multi-sparsity IMP Mask Validation on Full MNIST/Fashion-MNIST CNNs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-seed-multi-sparsity-imp-mask-validation-on-full-mnis-9c3274004a`
Run ID: `multi-seed-multi-sparsity-imp-mask-validation-on-full-mnis-9c3274004a-20260527T002143278828+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Lottery Ticket Sparse Mask Validator: enoch://control-plane/projects/lottery-ticket-sparse-mask-validator-cb9cd555f0d4/runs/lottery-ticket-sparse-mask-validator-cb9cd555f0d4-20260525T183150978755+0000
- Parent run decision: Iterative Lottery-Ticket Mask Validator on Full MNIST/Fashion-MNIST CNNs: enoch://control-plane/projects/iterative-lottery-ticket-mask-validator-on-full-mnist-fash-130243072e/runs/iterative-lottery-ticket-mask-validator-on-full-mnist-fash-130243072e-20260525T200320957594+0000

## What looked useful

IMP exceeded random controls in all 8 dataset/seed/sparsity cells. Mean IMP-random gaps were +11.20 pp and +23.86 pp on MNIST at 80% and 90% sparsity, and +2.93 pp and +12.62 pp on Fashion-MNIST. Mean IMP/dense retention was 98.71% to 101.31% across cells.

## Boundaries and scale limits

CPU-only worker; compact CNN rather than standard LeNet-5-scale or modern CNN; two seeds only; 80% and 90% sparsity only; one-shot magnitude pruning rather than multi-round iterative pruning; short training schedule with some Fashion-MNIST dense instability.

## Claim scope

On full MNIST and Fashion-MNIST with a compact NumPy CNN, two fixed seeds, 80% and 90% sparsity, one dense mask-discovery epoch, and two retraining epochs, one-shot magnitude IMP masks rewound to initialization consistently outperform matched random masks and retain dense-level accuracy.

## Why it stopped

Completed the requested Tier 2-style bounded CPU validation; evidence supports the scoped mechanism but is not publication-grade due to compact model, two seeds, short training, and one-shot rather than full iterative pruning.

## Recommended next action

Run a bounded deepen validation with a standard LeNet-5-scale CNN, at least three seeds, 80/90/95% sparsity, true iterative pruning rounds, and a tuned dense training schedule before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standard LeNet Multi-round IMP Validation on Full MNIST/Fashion-MNIST
- Success threshold: IMP retains >=95% of same-seed dense accuracy and beats random masks by >=2 percentage points in at least 10 of 12 dataset/seed/sparsity cells, with positive mean gaps on both datasets.
- Stop condition: Stop as unsupported if IMP fails the retention threshold on either dataset or fails to beat random masks by >=2 percentage points in a majority of cells at 90% or 95% sparsity.

## Evidence references

- Artifact root: `<local-path>/projects/multi-seed-multi-sparsity-imp-mask-validation-on-full-mnis-9c3274004a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
