# Harder Direct Neural Loss-Gap Test for Current-Only TopK AdamW

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `harder-direct-neural-loss-gap-test-for-current-only-topk-a-65c3145573`
Run ID: `harder-direct-neural-loss-gap-test-for-current-only-topk-a-65c3145573-20260520T103357937469+0000`

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

- Parent run decision: Direct Neural Benchmark for Current-Only Sparse-TopK-AdamW: enoch://control-plane/projects/direct-neural-benchmark-for-current-only-sparse-topk-adamw-2acf29f184/runs/direct-neural-benchmark-for-current-only-sparse-topk-adamw-2acf29f184-20260520T102857777219+0000
- Parent run decision: Sparse-TopK-AdamW for Tiny-VRAM Training: enoch://control-plane/projects/sparse-topk-adamw-for-tiny-vram-training-2602f7a3594f/runs/sparse-topk-adamw-for-tiny-vram-training-2602f7a3594f-20260520T101922612223+0000

## What looked useful

Current-only TopK AdamW preserved dense AdamW validation loss at moderate 5-10% sparsity on a real neural classification task, while 1% sparsity degraded accuracy. Error feedback did not materially improve 10% TopK in this setting; random-k had lower validation loss but a weaker accuracy profile, so the mechanism signal is useful but not decisive.

## Boundaries and scale limits

Evidence is limited to a 784-256-256-10 ReLU MLP on MNIST. It does not validate CNNs, transformers, GPT-2-small-class language models, larger datasets, production sparse kernels, wall-clock speedups, or broad optimizer robustness.

## Claim scope

On a direct MNIST NumPy MLP target with 20k train / 5k validation examples, 15 epochs, and five fixed seeds, current-only per-tensor TopK AdamW matched dense AdamW validation loss/accuracy at 10% and 5% active coordinates under the predeclared loss-gap threshold, but failed the accuracy-gap threshold at 1%.

## Why it stopped

Tier-2 direct MNIST MLP evidence supports a bounded mechanism at 5-10% sparsity but is not broad or publication-grade; 1% sparsity is negative under the predeclared accuracy threshold.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to repeat the same fixed-seed AdamW/TopK/random-k/error-feedback matrix on a small CNN or language-model task before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Current-Only TopK AdamW Loss-Gap Test on CNN or Small Language Model
- Success threshold: At 10% and 5% active coordinates, current-only TopK AdamW must be within +0.05 validation loss and within -0.5 percentage points accuracy, or within +2% relative perplexity for a language model, of dense AdamW on at least 4/5 seeds; 1% may fail but must define the sparsity floor.
- Stop condition: Stop as negative if 5% or 10% misses the threshold on two or more seeds, or if random-k matches TopK on all direct metrics and mechanism diagnostics show no top-|g| advantage.

## Evidence references

- Artifact root: `<local-path>/projects/harder-direct-neural-loss-gap-test-for-current-only-topk-a-65c3145573`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
