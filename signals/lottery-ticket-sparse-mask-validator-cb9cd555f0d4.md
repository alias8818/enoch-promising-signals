# Lottery Ticket Sparse Mask Validator

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lottery-ticket-sparse-mask-validator-cb9cd555f0d4`
Run ID: `lottery-ticket-sparse-mask-validator-cb9cd555f0d4-20260525T183150978755+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01c5be3baed4

## What looked useful

The validator detected task-relevant sparse-mask structure: IMP rewind exceeded random rewind by +4.8, +12.32, and +36.84 accuracy points at 80%, 90%, and 95% sparsity, and exceeded shuffled IMP by +5.18, +12.46, and +30.04 points.

## Boundaries and scale limits

Small MNIST subset only; one-hidden-layer MLP only; one-shot pruning only; 5 seeds; no full MNIST, iterative pruning, CNN, transformer, GPT-2-small-class, or large-scale validation.

## Claim scope

On a pure NumPy one-hidden-layer MNIST MLP using 2,000 training examples, 1,000 test examples, 5 seeds, one-shot global magnitude pruning, and rewound sparse retraining, IMP masks retained substantially higher accuracy than same-sparsity random and shuffled controls at 80%, 90%, and 95% sparsity.

## Why it stopped

Bounded CPU experiment completed with useful no-paper signal; evidence is limited to a small MLP/MNIST proxy and does not justify publication-grade lottery-ticket claims.

## Recommended next action

Run a bounded deepening study with iterative pruning on full MNIST or Fashion-MNIST using a CNN baseline, at least 10 seeds, and paired statistical tests; stop here for this run because current evidence is useful but not paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Iterative Lottery-Ticket Mask Validator on Full MNIST/Fashion-MNIST CNNs
- Success threshold: IMP rewind mean test accuracy exceeds both random and shuffled controls by at least 2 percentage points at 90% sparsity with paired-test p < 0.05 or non-overlapping 95% confidence intervals.
- Stop condition: Stop as negative/no-paper if IMP fails to beat either control by 2 percentage points at 90% sparsity or if the effect disappears under iterative pruning with paired seeds.

## Evidence references

- Artifact root: `<local-path>/projects/lottery-ticket-sparse-mask-validator-cb9cd555f0d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
