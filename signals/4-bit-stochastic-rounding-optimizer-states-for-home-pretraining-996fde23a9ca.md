# 4-bit Stochastic Rounding Optimizer States for Home Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `4-bit-stochastic-rounding-optimizer-states-for-home-pretraining-996fde23a9ca`
Run ID: `4-bit-stochastic-rounding-optimizer-states-for-home-pretraining-996fde23a9ca-20260621T103301912218+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/eacd2fdc9cc6

## What looked useful

Standard eps=1e-8 produced a reproducible denominator-collapse failure with 4-bit stochastic state loss +23.03 versus fp32. Stabilized eps=1e-4 avoided collapse but 4-bit stochastic remained +1.56 loss versus fp32, while 4-bit nearest was only +0.25 in the same proxy. Estimated optimizer-state storage was 0.125x fp32 Adam.

## Boundaries and scale limits

Small embedding MLP, synthetic Markov-token data, 3 seeds, CPU-only, no transformer, no real corpus, no packed kernel, and estimated rather than measured optimizer-state memory savings.

## Claim scope

Bounded NumPy synthetic next-token proxy: naive per-tensor 4-bit stochastic-rounded Adam moment states are not viable as-is; they fail under standard Adam epsilon and remain substantially worse than fp32 after simple epsilon stabilization.

## Why it stopped

Early proxy falsification: the local direct optimizer-state test found large reproducible instability under default Adam epsilon and a large remaining quality gap for the stabilized stochastic variant, so full-scale validation of this exact naive design is not justified.

## Recommended next action

Stop this project as a no-paper negative for naive stochastic-rounded 4-bit Adam states; if continuing, test a bounded adjacent design with second-moment floors and finer-grained scales before any larger model run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: 4-bit Adam states with nonzero v floors and fine-grained scales
- Success threshold: Mean final validation-loss delta versus fp32 <= 0.10 with no seed diverging and estimated optimizer-state memory ratio <= 0.167.
- Stop condition: Stop if default or stabilized floored/blockwise 4-bit remains >0.30 validation-loss delta versus fp32 after 300 steps, or if zero-v fraction still causes instability.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-stochastic-rounding-optimizer-states-for-home-pretraining-996fde23a9ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
