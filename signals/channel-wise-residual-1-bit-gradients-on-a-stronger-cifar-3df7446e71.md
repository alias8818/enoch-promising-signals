# Channel-wise residual 1-bit gradients on a stronger CIFAR baseline with timing overhead

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `78`
Project ID: `channel-wise-residual-1-bit-gradients-on-a-stronger-cifar-3df7446e71`
Run ID: `channel-wise-residual-1-bit-gradients-on-a-stronger-cifar-3df7446e71-20260522T190623169896+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Channel-wise 1-bit residual gradients on a channel-heterogeneous CIFAR model with scale-overhead accounting: enoch://control-plane/projects/channel-wise-1-bit-residual-gradients-on-a-channel-heterog-06ea71ff32/runs/channel-wise-1-bit-residual-gradients-on-a-channel-heterog-06ea71ff32-20260522T104424331693+0000
- Parent run decision: Real-data comparison of channel-wise versus global 1-bit residual gradients: enoch://control-plane/projects/real-data-comparison-of-channel-wise-versus-global-1-bit-r-66960931c3/runs/real-data-comparison-of-channel-wise-versus-global-1-bit-r-66960931c3-20260522T083424564210+0000

## What looked useful

Residual 1-bit reached 93.305% mean best test accuracy versus 93.38% dense and 92.745% no-residual 1-bit. It used about 1.026 effective gradient bits/parameter and had +3.42% mean epoch wall-time overhead versus dense.

## Boundaries and scale limits

Single local GB10 GPU, CIFAR-10 only, one architecture, two seeds, optimizer-side simulated gradient compression rather than distributed communication or fused-kernel implementation; no ImageNet, transformer, multi-node, or production communication benchmark evidence.

## Claim scope

On full CIFAR-10 with WideResNet-16-4 for 40 epochs and two fixed seeds, channel-wise/row-wise residual 1-bit gradients nearly matched dense-gradient test accuracy while improving over a no-residual 1-bit control and adding about 3.4% mean epoch wall-time overhead in this Python implementation.

## Why it stopped

Direct bounded CIFAR validation supports the residual mechanism but is not broad or deployment-realistic enough for paper-positive evidence.

## Recommended next action

Stop this follow-up as no-paper useful-signal evidence; only open a new project if it will test fused/distributed residual 1-bit communication speedups or a broader dataset/model regime.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/channel-wise-residual-1-bit-gradients-on-a-stronger-cifar-3df7446e71`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
