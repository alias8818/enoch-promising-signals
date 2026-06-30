# Real-dataset DDP hook validation of bandwidth-shaped residual 1-bit gradients

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-dataset-ddp-hook-validation-of-bandwidth-shaped-resid-5f2eabc671`
Run ID: `real-dataset-ddp-hook-validation-of-bandwidth-shaped-resid-5f2eabc671-20260522T165839908583+0000`

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

- Parent run decision: Bandwidth-shaped local DDP validation of residual 1-bit gradients: enoch://control-plane/projects/bandwidth-shaped-local-ddp-validation-of-residual-1-bit-gr-f03d455a1e/runs/bandwidth-shaped-local-ddp-validation-of-residual-1-bit-gr-f03d455a1e-20260522T161304426363+0000
- Parent run decision: Residual-Compensated 1-bit Gradients for Home Distributed Training: enoch://control-plane/projects/residual-compensated-1-bit-gradients-for-home-distributed-training-f1824475b741/runs/residual-compensated-1-bit-gradients-for-home-distributed-training-f1824475b741-20260522T150955082830+0000

## What looked useful

Shaped residual 1-bit DDP hooks are mechanically viable and suppress residual explosion: robust lr=0.04 accuracy was 0.8988 versus 0.1315 for unbounded error feedback and 0.8875 for no-residual sign, with 31.99x estimated payload compression. Stable FP32 reached 0.9585, so the method is not paper-ready.

## Boundaries and scale limits

MNIST only, small CNN only, 2 local CPU DDP ranks only, localhost gloo only. Payload bytes are estimated from actual packed tensors communicated by the hook, but this is not a multi-node network-throughput, NCCL/GPU-overlap, large-model, or full-corpus validation.

## Claim scope

On a 2-rank local PyTorch DDP/gloo MNIST CNN run with fixed seeds, packed 1-bit gradient hooks achieved an estimated 31.99x payload reduction. Residual clipping/decay prevented unbounded error-feedback collapse and modestly improved no-residual sign compression, but remained below a stable FP32 DDP baseline.

## Why it stopped

Tier 2 local evidence supports the residual-shaping mechanism but not a paper-positive training or bandwidth-speedup claim because shaped 1-bit remains about 5.97 percentage points below stable FP32 and bandwidth speedup was not measured on multi-node hardware.

## Recommended next action

Stop this run as no-paper useful signal; a bounded next test should sweep residual clip/decay on the same harness and then repeat the best setting on a harder real dataset before any larger-scale claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual clip and decay sweep for shaped 1-bit DDP hooks
- Success threshold: On MNIST, shaped 1-bit mean accuracy within 3 absolute percentage points of stable FP32 across 3 seeds while keeping at least 30x estimated payload reduction and avoiding residual explosion; if met, repeat on a harder real-data setting.
- Stop condition: Stop if no clip/decay setting beats no-residual sign by at least 1 absolute point or if all settings remain more than 5 absolute points below stable FP32.

## Evidence references

- Artifact root: `<local-path>/projects/real-dataset-ddp-hook-validation-of-bandwidth-shaped-resid-5f2eabc671`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
