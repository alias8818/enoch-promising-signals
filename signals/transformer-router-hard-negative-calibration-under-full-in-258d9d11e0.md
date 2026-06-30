# Transformer-router hard-negative calibration under full int8/int4 quantization

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `transformer-router-hard-negative-calibration-under-full-in-258d9d11e0`
Run ID: `transformer-router-hard-negative-calibration-under-full-in-258d9d11e0-20260522T100754380040+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Quantized Tool Router for Safer Small Agents: enoch://control-plane/projects/quantized-tool-router-for-safer-small-agents-e12bce903e45/runs/quantized-tool-router-for-safer-small-agents-e12bce903e45-20260522T012314896937+0000
- Parent run decision: Hard-Negative OOD Calibration for Quantized Tool Routers: enoch://control-plane/projects/hard-negative-ood-calibration-for-quantized-tool-routers-3d470a58c2/runs/hard-negative-ood-calibration-for-quantized-tool-routers-3d470a58c2-20260522T072710255512+0000

## What looked useful

Hard-negative calibration produced an error-shaping effect under int4, reducing hard-negative error share by 5.9 percentage points versus CE, but it lowered int4 accuracy by 0.68 percentage points and worsened NLL/Brier/ECE. Label smoothing was the strongest baseline for int4 accuracy and NLL, and adding the hard-negative margin to label smoothing did not beat label smoothing.

## Boundaries and scale limits

Small synthetic benchmark only: 64 experts, compact 2-layer Transformer router, 3 fixed seeds, fake quantized inference rather than backend integer kernels or quantization-aware training, no real MoE language-model downstream loss or production traffic.

## Claim scope

On a controlled synthetic Transformer-router expert-selection benchmark with explicit same-group hard negatives and full learned-router-path fake quantized inference, hard-negative margin calibration reduced same-group hard-negative error share but did not improve int8/int4 top-1 accuracy, NLL, Brier, or ECE versus CE and label-smoothing baselines.

## Why it stopped

Tier 2 fixed-seed evidence with a real CE baseline, label-smoothing control, and HN+label-smoothing ablation found a mixed mechanism but negative primary robustness result, not paper-positive support.

## Recommended next action

Stop this follow-up as no-paper useful evidence; only revisit if running a real MoE/GPT-2-small-class quantization-aware router study with downstream loss and routing metrics.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/transformer-router-hard-negative-calibration-under-full-in-258d9d11e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
