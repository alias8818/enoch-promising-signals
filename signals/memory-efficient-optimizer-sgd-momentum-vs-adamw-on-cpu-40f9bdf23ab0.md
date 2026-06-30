# Memory-Efficient Optimizer: SGD+Momentum vs AdamW on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-efficient-optimizer-sgd-momentum-vs-adamw-on-cpu-40f9bdf23ab0`
Run ID: `memory-efficient-optimizer-sgd-momentum-vs-adamw-on-cpu-40f9bdf23ab0-20260610T125851804780+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/28c16a361d95

## What looked useful

SGD+momentum is a plausible CPU memory-saving optimizer when state memory matters: it directly halves optimizer-state bytes relative to AdamW and was faster in standalone update kernels, but it needs learning-rate tuning and high learning rates diverged in the synthetic task.

## Boundaries and scale limits

Evidence is limited to NumPy float32 vector updates and synthetic linear regression. It does not validate PyTorch framework behavior, real datasets, neural network training, mixed precision, checkpointing, or large-model end-to-end time-to-quality.

## Claim scope

On this CPU-only NumPy benchmark, SGD+momentum used one float32 optimizer buffer versus AdamW's two buffers, reducing explicit optimizer state from 8 to 4 bytes per parameter; for vectors up to 20M parameters AdamW updates were 2.84x to 5.62x slower, and tuned SGD+momentum matched or slightly beat AdamW on a small synthetic regression task over three seeds.

## Why it stopped

Proxy/local evidence supports the mechanism but is not direct enough for publication-grade validation of SGD+momentum as a practical AdamW replacement.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded PyTorch CPU follow-up on a real small model/dataset measuring peak RSS, optimizer state, time-to-target validation quality, and hyperparameter sensitivity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch CPU Time-to-Quality Memory Benchmark for SGD+Momentum vs AdamW
- Success threshold: SGD+momentum reaches the AdamW target validation metric with at least 40% lower optimizer-state memory and no more than 10% worse wall-clock time-to-target on the selected PyTorch CPU task.
- Stop condition: Stop if SGD+momentum cannot reach the AdamW target metric under the bounded LR grid or if optimizer-state savings do not translate into lower measured peak RSS.

## Evidence references

- Artifact root: `<local-path>/projects/memory-efficient-optimizer-sgd-momentum-vs-adamw-on-cpu-40f9bdf23ab0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
