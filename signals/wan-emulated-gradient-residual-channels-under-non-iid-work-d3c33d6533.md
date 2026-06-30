# WAN-emulated gradient residual channels under non-IID worker data

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `wan-emulated-gradient-residual-channels-under-non-iid-work-d3c33d6533`
Run ID: `wan-emulated-gradient-residual-channels-under-non-iid-work-d3c33d6533-20260604T141701012620+0000`

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

- Parent run decision: Gradient Residual Channels for Home Distributed Training: enoch://control-plane/projects/gradient-residual-channels-for-home-distributed-training-553cef7e50ae/runs/gradient-residual-channels-for-home-distributed-training-553cef7e50ae-20260604T094419046350+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8f397d98905f

## What looked useful

Easy separable tasks saturated and showed no accuracy benefit. In the harder overlapping-class setting, topk_residual trailed topk_no_residual by 4.743 pp at lr=0.35 and by 2.617 pp at lr=0.15, despite a lower-loss signal in the lr=0.15 check.

## Boundaries and scale limits

Synthetic in-process WAN emulator only; no real multi-host WAN, real network traces, large nonconvex model, foundation-model workload, or production distributed optimizer stack.

## Claim scope

In a controlled small PyTorch softmax-classification benchmark with 8 non-IID label-skewed workers, top-k compressed gradient messages, and emulated WAN delay/drop, naive residual error-feedback channels did not meet the Tier 1 success threshold versus no-residual top-k.

## Why it stopped

The direct small test falsified the stated +3 pp residual-over-no-residual accuracy threshold under the non-saturated overlapping-class condition; this is early controlled evidence, not full-scale validation.

## Recommended next action

Stop this run as a reproducible Tier 1 early negative; the only concrete next action is a bounded mechanism follow-up testing age-aware residual decay or clipping on the same overlapping non-IID WAN-emulated benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Age-aware residual decay for delayed non-IID top-k gradient channels
- Success threshold: Residual decay or clipping beats no-residual top-k by at least 3 percentage points final accuracy, or matches no-residual accuracy within 1 point while reducing delivered gradient values by at least 25%, across 5 seeds.
- Stop condition: Stop if both residual decay and clipping fail to beat no-residual top-k on accuracy or communication efficiency under the fixed overlapping non-IID WAN-emulated benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/wan-emulated-gradient-residual-channels-under-non-iid-work-d3c33d6533`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
