# CPU-Offloaded Low-Rank Optimizer States for Tiny-RAM Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-offloaded-low-rank-optimizer-states-for-tiny-ram-training-abde1a582ca1`
Run ID: `cpu-offloaded-low-rank-optimizer-states-for-tiny-ram-training-abde1a582ca1-20260525T013621067022+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/dc70f9f6e915

## What looked useful

Best primary low-rank run used 4096 optimizer-state bytes versus Adam's 524288 bytes, a 99.21875% state saving, but final loss was 0.00418151403 versus Adam's 3.34303962e-08 and SGD's 0.00213510031. The low-rank optimizer was about 125081x worse than Adam and 1.96x worse than SGD by final loss.

## Boundaries and scale limits

CPU-only synthetic convex regression; no GPU/UMA offload kernels, no transformer training, no token-budget evaluation, no transfer-overlap accounting, and no long-horizon hyperparameter robustness study.

## Claim scope

On deterministic CPU matrix-regression benchmarks up to 256x256 weights, a naive CPU-offloadable low-rank Adam proxy with rank-1 to rank-16 first-moment factors and row/column factored second moments saves optimizer-state memory but does not preserve Adam-like convergence.

## Why it stopped

Proxy/local early falsification: the tested low-rank optimizer-state design achieved large memory savings but failed the practical convergence threshold of matching or beating SGD, and it remained far from full Adam.

## Recommended next action

Stop this mechanism as no-paper evidence; if continuing locally, test whether removing the low-rank first moment and using CPU-offloaded factored/full moments preserves Adam quality under the same memory accounting.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: CPU-offloaded factored optimizer states without low-rank first-moment projection
- Success threshold: A local follow-up is useful only if the best compressed/offloaded variant reaches final loss within 2x Adam and beats SGD while using at most 25% of Adam's accelerator-resident optimizer-state bytes on both regression and one neural benchmark.
- Stop condition: Stop if the best compressed/offloaded variant is worse than SGD on either benchmark after a small LR/rank sweep, or if its runtime exceeds Adam by more than 2x without a corresponding memory-capability benefit.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-low-rank-optimizer-states-for-tiny-ram-training-abde1a582ca1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
