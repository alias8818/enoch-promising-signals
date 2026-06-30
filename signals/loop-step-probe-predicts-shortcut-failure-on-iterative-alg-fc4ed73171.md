# Loop-Step Probe Predicts Shortcut Failure on Iterative Algorithm Tasks

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `loop-step-probe-predicts-shortcut-failure-on-iterative-alg-fc4ed73171`
Run ID: `loop-step-probe-predicts-shortcut-failure-on-iterative-alg-fc4ed73171-20260531T171846881452+0000`

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

- Parent run decision: Micro-Sharded Gradient Accumulation with On-Device Cheating Probes: enoch://control-plane/projects/micro-sharded-gradient-accumulation-with-on-device-cheating-probes-a0c0499425fd/runs/micro-sharded-gradient-accumulation-with-on-device-cheating-probes-a0c0499425fd-20260530T051240898620+0000
- Parent run decision: Transformer-Loop Cheating Probe Validation: enoch://control-plane/projects/transformer-loop-cheating-probe-validation-ce3ef6df5b/runs/transformer-loop-cheating-probe-validation-ce3ef6df5b-20260531T100901839636+0000

## What looked useful

The result points to a representation-use gap. Linear decodability of loop-step state can be high even when the model's trained output head follows a shortcut and fails OOD, so probe accuracy alone should not be treated as a reliable shortcut-failure predictor.

## Boundaries and scale limits

Synthetic two-state automaton only; five fixed seeds per regime; GB10 local single-process training; not tested on natural-language, arithmetic, graph, program-execution, or large-model iterative reasoning tasks.

## Claim scope

In a controlled small causal-transformer seen-one automaton with a spurious final-token shortcut, linear loop-step and final-state probes did not predict shortcut failure: hidden states encoded the true loop state while the model still failed balanced longer OOD evaluation during early shortcut use.

## Why it stopped

Tier 2 fixed-seed synthetic evidence falsifies the simple predictor claim in this setting rather than supporting publication readiness.

## Recommended next action

Stop this no-paper run; the next bounded test should add causal readout or intervention diagnostics to separate state availability from state use.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Causal Readout Test for Loop-State Availability Versus Use
- Success threshold: Across at least five seeds and two iterative tasks, a causal-use metric predicts OOD accuracy with correlation at least 0.7 and separates biased-failing from balanced/generalizing models by at least 20 OOD accuracy points, while linear probe accuracy alone does not.
- Stop condition: Stop if no task exhibits persistent shortcut failure after convergence or if causal-use metrics do not outperform linear probes on fixed-seed OOD prediction.

## Evidence references

- Artifact root: `<local-path>/projects/loop-step-probe-predicts-shortcut-failure-on-iterative-alg-fc4ed73171`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
