# AdamW Gradient-Gated Top-k on a Real Small Model Task

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adamw-gradient-gated-top-k-on-a-real-small-model-task-4da797c021`
Run ID: `adamw-gradient-gated-top-k-on-a-real-small-model-task-4da797c021-20260526T232851382463+0000`

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

- Parent run decision: Gradient-Gated Sparse Optimizer: Train Top-k% Parameters by Gradient Signal: enoch://control-plane/projects/gradient-gated-sparse-optimizer-train-top-k-parameters-by-gradient-signal-7fb674a3e80b/runs/gradient-gated-sparse-optimizer-train-top-k-parameters-by-gradient-signal-7fb674a3e80b-20260526T173311361295+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/31d6205bf9bc

## What looked useful

The 25% gradient-gated top-k variant is an early negative on a real small task because it missed dense AdamW by 3.60 points and did not beat random-k. One-seed sensitivity showed 50% top-k at 0.9245 accuracy versus 0.9335 dense AdamW and 0.9220 random-k, suggesting only a limited less-aggressive follow-up is warranted.

## Boundaries and scale limits

The test used MNIST, a compact 784-256-128-10 MLP, 10,000 train examples, 2,000 validation examples, 8 epochs, and a behavior-focused Python optimizer with dense moment tracking. It does not validate GPT-2-small-class language modeling, larger models, longer schedules, or sparse systems speedups.

## Claim scope

On a direct small-model MNIST MLP task, tensorwise AdamW gradient-gated top-k with 25% selected coordinates trains but fails the preset useful-signal threshold: it is 3.60 accuracy points below dense AdamW and 0.62 points below random-k across three seeds.

## Why it stopped

Direct Tier 1 validation falsified the preset 25% success threshold on a real small-model task; this is not full-scale validation, but it is sufficient no-paper evidence against the tested optimizer setting.

## Recommended next action

Stop this 25% update-fraction claim as a no-paper early negative; if continuing, run a bounded 50% keep-fraction multi-seed deepen test before considering larger models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: AdamW gradient-gated top-k at 50% updates on a small real model task
- Success threshold: Mean 50% top-k validation accuracy is within 0.5 percentage points of dense AdamW and at least 1.0 point above 50% random-k across at least five seeds.
- Stop condition: Stop negative if 50% top-k is more than 0.5 points below dense AdamW or fails to beat random-k by 1.0 point on the multi-seed mean.

## Evidence references

- Artifact root: `<local-path>/projects/adamw-gradient-gated-top-k-on-a-real-small-model-task-4da797c021`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
