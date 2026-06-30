# 1-Bit Gradients with Residual Momentum for Local DDP

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `1-bit-gradients-with-residual-momentum-for-local-ddp-1f3ca545acf2`
Run ID: `1-bit-gradients-with-residual-momentum-for-local-ddp-1f3ca545acf2-20260603T202044275546+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/156664998da4

## What looked useful

Plain 1-bit sign synchronization matched dense final accuracy in the bounded confirmation and stress runs at about 31.6x lower communicated bits, but residual-momentum 1-bit synchronization did not improve accuracy/loss and consistently worsened dense-update fidelity. At residual momentum 0.9, relative update MSE versus dense rose from 1.50 for plain sign to 13.21 in the confirmation run and from 1.65 to 21.35 in the higher-non-IID stress run.

## Boundaries and scale limits

No real multi-process DDP all-reduce, no NCCL/Gloo latency measurement, no large language model or real dataset, and no datacenter-scale multi-node validation. Communication benefit is estimated from synchronized bit count only.

## Claim scope

Bounded PyTorch local-DDP proxy on a synthetic non-IID multiclass classification task with a small MLP, 4 workers, local parameter-delta synchronization, and 3-4 seeds per confirmation/stress condition.

## Why it stopped

Proxy/local evidence does not support the residual-momentum improvement claim; residual momentum matched accuracy only because the toy task tolerated noisy updates, while mechanism diagnostics were worse than plain sign compression.

## Recommended next action

Stop this no-paper worker run; before any real DDP scale-up, test a bounded variant with conventional error feedback or per-layer clipping to see whether it avoids the residual-momentum update-MSE explosion on the same harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Clipped Error Feedback for 1-Bit Local-DDP Delta Synchronization
- Success threshold: On both confirmation and stress settings, clipped error feedback must match or exceed plain-sign final accuracy and reduce relative update MSE by at least 25% versus plain sign at the same estimated communication budget.
- Stop condition: Stop if clipped error feedback fails to beat plain sign on relative update MSE or causes any final accuracy drop larger than 0.5 percentage points in either setting.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-gradients-with-residual-momentum-for-local-ddp-1f3ca545acf2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
