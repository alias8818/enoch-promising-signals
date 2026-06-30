# Longer GPT-2-small AdamW8bit robustness curve across learning rates and corpus slices

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `longer-gpt-2-small-adamw8bit-robustness-curve-across-learn-3d24b6a24a`
Run ID: `longer-gpt-2-small-adamw8bit-robustness-curve-across-learn-3d24b6a24a-20260610T174647516741+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-text GPT-2-small AdamW8bit stability and validation-perplexity check on GB10: enoch://control-plane/projects/real-text-gpt-2-small-adamw8bit-stability-and-validation-p-75ddb1685c/runs/real-text-gpt-2-small-adamw8bit-stability-and-validation-p-75ddb1685c-20260610T163829376389+0000
- Parent run decision: Multi-seed longer GPT-2-small AdamW8bit validation curve check: enoch://control-plane/projects/multi-seed-longer-gpt-2-small-adamw8bit-validation-curve-c-c81c806e82/runs/multi-seed-longer-gpt-2-small-adamw8bit-validation-curve-c-c81c806e82-20260610T170949427859+0000

## What looked useful

AdamW8bit completed all 9 paired GPT-2-small comparisons with zero non-finite steps. Mean eval-loss delta versus AdamW was +0.013679, median delta was -0.000050, max absolute delta was 0.163251. AdamW8bit averaged 1.109x AdamW tokens/sec and reduced mean peak allocation from 2.9918 GB to 2.2539 GB.

## Boundaries and scale limits

Completed evidence is 18 short direct cells, 50 optimizer steps per cell, 204800 tokens per cell, 3.6864M total training tokens. Attempts at 200 and 800 steps per cell were terminated by the attached runner/session before completing the grid, so this does not validate longer convergence, final perplexity parity, checkpoint persistence, or full pretraining behavior.

## Claim scope

On this GB10 host, bitsandbytes AdamW8bit runs successfully for short-horizon GPT-2-small-from-scratch language-model training on WikiText-103 and tracks torch AdamW across a 3 learning-rate x 3 corpus-slice grid for 50 optimizer steps per cell, with zero non-finite steps and lower peak CUDA allocation.

## Why it stopped

The run produced a complete short-horizon direct GPT-2-small optimizer robustness grid, but the requested Tier 3 longer validation was not completed because 200-step and 800-step attached runs were terminated before grid completion.

## Recommended next action

Stop as no-paper useful signal; the next concrete action is a controller-safe rerun of the same 18-cell matrix at 200 to 800 optimizer steps per cell under a non-interactive long-running executor that is not subject to attached-session SIGTERM.

## Follow-up

- Recommended: `true`
- Type: `retry`
- Title: Controller-safe 200-800 step GPT-2-small AdamW8bit robustness rerun
- Success threshold: At 200 or more steps per cell, AdamW8bit has zero non-finite steps, mean eval-loss delta versus AdamW no worse than +0.05, no individual paired eval-loss regression worse than +0.20 without a matching shared-baseline instability, and at least 15% lower peak optimizer/training memory.
- Stop condition: Stop if AdamW8bit has any reproducible non-finite step not seen in AdamW, mean eval-loss regression exceeds +0.05 after 200 steps per cell, or the long-running executor cannot keep jobs alive long enough to complete at least 200 steps per cell.

## Evidence references

- Artifact root: `<local-path>/projects/longer-gpt-2-small-adamw8bit-robustness-curve-across-learn-3d24b6a24a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
