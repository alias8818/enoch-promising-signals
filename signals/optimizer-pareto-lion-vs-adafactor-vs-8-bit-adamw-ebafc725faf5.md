# Optimizer Pareto: Lion vs Adafactor vs 8-bit AdamW

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `optimizer-pareto-lion-vs-adafactor-vs-8-bit-adamw-ebafc725faf5`
Run ID: `optimizer-pareto-lion-vs-adafactor-vs-8-bit-adamw-ebafc725faf5-20260613T093401148991+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/90ea5e0df42f

## What looked useful

Adafactor provided the strongest optimizer-state memory Pareto point at 0.093 MB state, Lion provided the best loss/throughput point at 2.101 final loss and 334k tokens/sec, and the local 8-bit AdamW proxy was not competitive at 2.881 final loss, 243k tokens/sec, and 3.665 MB state.

## Boundaries and scale limits

Synthetic data, tiny model, 300 training steps, three seeds, short single-seed learning-rate sweep, local unfused optimizer implementations, and an 8-bit AdamW proxy rather than production bitsandbytes or fused kernels.

## Claim scope

On a 1.829M-parameter synthetic causal-transformer early-training task on GB10, tuned Lion reached the lowest mean final loss and highest throughput, Adafactor used vastly less optimizer state with modestly worse and more variable loss, and the local blockwise 8-bit AdamW proxy was dominated by Adafactor.

## Why it stopped

Bounded synthetic/proxy evidence only; useful for pruning and follow-up design but not a full optimizer validation or paper-ready result.

## Recommended next action

Stop this run as no-paper useful signal; next run should repeat the comparison on a real corpus with official/fused optimizer implementations, especially production 8-bit AdamW.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus fused-optimizer Pareto check for Lion, Adafactor, and 8-bit AdamW
- Success threshold: A non-dominated Pareto point must improve at least one of validation loss, time-to-target, tokens/sec, peak memory, or optimizer-state memory without regressing all other measured axes by more than 10% against the nearest competitor.
- Stop condition: Stop if production 8-bit AdamW is unavailable on the target stack after documented install attempts, or if after the bounded sweep one optimizer is clearly dominated on validation loss, throughput, and memory.

## Evidence references

- Artifact root: `<local-path>/projects/optimizer-pareto-lion-vs-adafactor-vs-8-bit-adamw-ebafc725faf5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
