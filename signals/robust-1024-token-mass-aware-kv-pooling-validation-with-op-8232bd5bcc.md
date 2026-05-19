# Robust 1024-token mass-aware KV pooling validation with optimized compression

Status: `useful_signal`
Project ID: `robust-1024-token-mass-aware-kv-pooling-validation-with-op-8232bd5bcc`
Run ID: `robust-1024-token-mass-aware-kv-pooling-validation-with-op-8232bd5bcc-20260519T090103893127+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Robust 1024-token mass-aware KV pooling validation with optimized compression: internal_generated:robust-1024-token-mass-aware-kv-pooling-validation-with-op-8232bd5bcc

## What looked useful

Mass-aware pooling/selection is substantially better than naive uniform pooling, recent-only, and norm selection controls. However, distilgpt2 favors simple stride at all budgets, while GPT-2 small favors mass-aware selection/pooling at 256 and 512 token budgets, making the central robustness claim mixed rather than paper-ready.

## Boundaries and scale limits

Single-node GB10 local inference validation only; no 7B+ models, no non-GPT-2 architectures, no long autoregressive generation evaluation, no optimized serving kernels, and no multi-corpus robustness suite.

## Claim scope

1024-token next-token KV-cache compression evaluation on WikiText-2 using distilgpt2 and GPT-2 small. Mass-aware methods show a useful mechanism signal on GPT-2 small and against weak pooling controls, but mass-aware pooling is not robustly better than stride across models.

## Why it stopped

Tier 4 robustness threshold failed: direct 1024-token evidence is mixed across distilgpt2 and GPT-2 small, and mass-aware pooling does not robustly beat the simple stride baseline.

## Recommended next action

Stop this depth-4 follow-up as no-paper mixed evidence; do not spawn another deepen/retry follow-up under the controller cap.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/robust-1024-token-mass-aware-kv-pooling-validation-with-op-8232bd5bcc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
