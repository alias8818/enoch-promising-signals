# Held-out MBPP/HumanEval confirmation for minimum-token-logprob Qwen2.5-Coder cascade routing

Status: `useful_signal`
Project ID: `held-out-mbpp-humaneval-confirmation-for-minimum-token-log-13719bee3c`
Run ID: `held-out-mbpp-humaneval-confirmation-for-minimum-token-log-13719bee3c-20260516T220824175722+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Held-out MBPP/HumanEval confirmation for minimum-token-logprob Qwen2.5-Coder cascade routing: internal_generated:held-out-mbpp-humaneval-confirmation-for-minimum-token-log-13719bee3c

## What looked useful

Minimum token logprob is predictive of failures but not the best cascade score. Combined low-score AUC for small-model failure was 0.708 for min, versus 0.797 for mean and 0.784 for p05. At 50% escalation, min reached 75.83% pass@1 at 91.88% weighted cost versus 80.00% at 85.62% for mean and 80.83% at 87.59% for p05.

## Boundaries and scale limits

Medium subset only; deterministic pass@1 only; parameter-weighted generated-token proxy instead of measured serving cost; no calibration/test threshold split; no EvalPlus or hidden tests.

## Claim scope

On a fixed 120-task held-out local subset, 60 MBPP test tasks plus 60 HumanEval tasks, Qwen2.5-Coder 1.5B-to-7B confidence routing improves over small-only and often over random matched-rate routing, but raw minimum generated-token logprob is weaker than mean or p05 logprob routing ablations.

## Why it stopped

Medium direct evaluation did not confirm minimum-token logprob as the preferred router; stronger ablation scores beat it on pass@1 and AUC at comparable escalation rates.

## Recommended next action

Stop this minimum-token-logprob follow-up as no-paper evidence; branch to a bounded robust-confidence routing test using full local MBPP/HumanEval with calibration/test thresholds.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Robust logprob confidence scores for Qwen2.5-Coder cascade routing
- Success threshold: A robust confidence score improves held-out pass@1 by at least 5 percentage points over random routing and at least 2 points over raw min-logprob at the same parameter-weighted cost on combined MBPP/HumanEval.
- Stop condition: Stop if no robust confidence score beats raw min-logprob by at least 2 pass@1 points at matched weighted cost, or if gains disappear under calibration/test thresholding.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-mbpp-humaneval-confirmation-for-minimum-token-log-13719bee3c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
