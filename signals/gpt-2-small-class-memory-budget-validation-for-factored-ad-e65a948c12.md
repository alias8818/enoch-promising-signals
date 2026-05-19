# GPT-2-small-class memory-budget validation for factored Adam floor sweep

Status: `useful_signal`
Project ID: `gpt-2-small-class-memory-budget-validation-for-factored-ad-e65a948c12`
Run ID: `gpt-2-small-class-memory-budget-validation-for-factored-ad-e65a948c12-20260516T073302908247+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: GPT-2-small-class memory-budget validation for factored Adam floor sweep: internal_generated:gpt-2-small-class-memory-budget-validation-for-factored-ad-e65a948c12

## What looked useful

The floor sweep produced a stable memory map: floors 1-256 factor essentially all GPT-2-small matrix parameters, floor 512 changes little, and floor 1024 factors none. Factored second moment plus full first moment halves fp32 AdamW optimizer state but does not beat PyTorch bf16-state AdamW in this environment. The no-first-moment ablation nearly eliminates optimizer state but is not a drop-in Adam replacement.

## Boundaries and scale limits

The run used 120-step training sweeps, synthetic-token main data with a one-seed WikiText-2 confirmation, and a custom research optimizer. It validates optimizer memory allocation and real forward/backward execution, but not long-horizon convergence, validation perplexity, hyperparameter robustness, or publication-level novelty.

## Claim scope

On a GPT-2-small-class 123.9M-parameter bf16 training harness, factored second-moment state with a full fp32 first moment and floor <=256 reduces optimizer state by about 49.9% versus an explicit fp32-state AdamW baseline; a floor of 1024 disables factorization and returns to dense-state memory.

## Why it stopped

No-paper closure: memory mechanism is supported at GPT-2-small-class scale, but optimizer-quality and convergence evidence are too short and too narrow for a paper.

## Recommended next action

Run at most one depth-4 deepen validation on real text for >=2000 steps with held-out validation loss, comparing fp32 AdamW, bf16 AdamW, factored_m floors 128 and 1024, and factored_nom; otherwise stop as useful no-paper memory evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text convergence validation for GPT-2-small factored Adam floor 128
- Success threshold: factored_m floor 128 retains at least 45% optimizer-state savings versus fp32 AdamW and validation perplexity is within 3% of fp32 AdamW at matched tokens, with floor 1024 returning to dense-state memory.
- Stop condition: Stop if factored_m floor 128 loses the memory advantage, diverges, or exceeds fp32 AdamW validation perplexity by more than 3% after matched-token training.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-memory-budget-validation-for-factored-ad-e65a948c12`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
