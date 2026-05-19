# Calibrated logprob routing with a stronger Qwen2.5-Coder fallback

Status: `useful_signal`
Project ID: `calibrated-logprob-routing-with-a-stronger-qwen2-5-coder-f-cf6506eb83`
Run ID: `calibrated-logprob-routing-with-a-stronger-qwen2-5-coder-f-cf6506eb83-20260516T231058096148+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Calibrated logprob routing with a stronger Qwen2.5-Coder fallback: internal_generated:calibrated-logprob-routing-with-a-stronger-qwen2-5-coder-f-cf6506eb83

## What looked useful

The 7B fallback is much stronger than the 1.5B model, but mean-logprob routing underperforms random and length same-budget controls. Full-set weak pass rate was 41.46% and strong pass rate was 82.32%; low mean logprob had failure-detection AUC 0.411, while length had AUC 0.568. Across 10 robust splits, confidence routing lagged random by 1.9 to 5.8 percentage points depending on fallback budget.

## Boundaries and scale limits

One benchmark family, one deterministic decoding setting, one weak/strong Qwen2.5-Coder pair, and one logprob aggregation rule. Larger benchmark suites and richer learned calibrators were not tested.

## Claim scope

On cached HumanEval with greedy Qwen/Qwen2.5-Coder-1.5B-Instruct outputs routed to Qwen/Qwen2.5-Coder-7B-Instruct, weak generated-token mean logprob is not an effective fallback routing score at fixed fallback budgets.

## Why it stopped

Direct HumanEval replication with a stronger Qwen2.5-Coder fallback falsified the specific mean-logprob routing mechanism against real same-budget controls; this is not a full rejection of all learned or multi-feature confidence routers.

## Recommended next action

Stop this depth-4 follow-up as a no-paper negative result; do not recommend another deepen/retry follow-up because the controller lineage is already at the depth cap.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-logprob-routing-with-a-stronger-qwen2-5-coder-f-cf6506eb83`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
