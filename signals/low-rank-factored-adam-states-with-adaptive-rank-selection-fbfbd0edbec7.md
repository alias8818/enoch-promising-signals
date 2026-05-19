# Low-Rank Factored Adam States with Adaptive Rank Selection

Status: `useful_signal`
Project ID: `low-rank-factored-adam-states-with-adaptive-rank-selection-fbfbd0edbec7`
Run ID: `low-rank-factored-adam-states-with-adaptive-rank-selection-fbfbd0edbec7-20260516T065542210038+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6eeb1383b126

## What looked useful

The prototype reduced final stored optimizer-state bytes by large factors, but naive adaptive SVD compression required nonnegative second-moment repair, was tens of times slower than dense AdamW, had high first-moment approximation error, and failed badly on the 256-dimensional task.

## Boundaries and scale limits

No LLM or GPT-2-small-class training was run; results cover dimensions up to 256 for 250 optimizer steps on one GB10, with a prototype that uses full SVDs rather than production kernels.

## Claim scope

Small local PyTorch probes of SVD-compressed adaptive-rank Adam states for matrix parameters on synthetic full-rank linear regression and synthetic gradient-stream moment approximation.

## Why it stopped

Proxy and small direct optimizer tests found a useful early falsification of the naive mechanism rather than a full validation: memory savings were real, but correctness hazards, high moment error, severe runtime overhead, and dim-256 convergence failure make it non-viable as tested.

## Recommended next action

Stop this naive SVD-compressed adaptive-rank Adam-state line as no-paper evidence; only pursue a bounded adjacent variant if it enforces nonnegative second moments and prevents rank collapse.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Diagonal-plus-low-rank nonnegative Adam second moments with rank-floor selection
- Success threshold: On dim 256 for 250 steps, final validation loss within 10x dense AdamW, optimizer-state bytes at least 2x lower than dense AdamW, and throughput no worse than 5x slower than dense AdamW.
- Stop condition: Stop if the variant still collapses to ineffective rank, produces invalid second moments, exceeds 5x dense AdamW runtime on dim 256, or remains more than 10x worse than AdamW validation loss.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-factored-adam-states-with-adaptive-rank-selection-fbfbd0edbec7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
