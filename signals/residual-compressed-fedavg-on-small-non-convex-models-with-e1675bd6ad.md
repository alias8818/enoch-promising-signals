# Residual Compressed FedAvg on Small Non-Convex Models with Volunteer Availability Traces

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `residual-compressed-fedavg-on-small-non-convex-models-with-e1675bd6ad`
Run ID: `residual-compressed-fedavg-on-small-non-convex-models-with-e1675bd6ad-20260528T171421021710+0000`

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

- Parent run decision: Federated Residual Averaging for Home Volunteer Training: enoch://control-plane/projects/federated-residual-averaging-for-home-volunteer-training-9ec50d8c7bfd/runs/federated-residual-averaging-for-home-volunteer-training-9ec50d8c7bfd-20260528T142303842731+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9eafc81d5e7c

## What looked useful

At 10% top-k, dense FedAvg reached 0.8695 mean accuracy, top-k without residual reached 0.8689, and top-k with residual reached 0.8603. At 2% top-k, top-k without residual reached 0.8820 while residual top-k fell to 0.8360. Residual buffers accumulated larger late-round residual norms, suggesting stale residuals can hurt when clients intermittently disappear and rejoin.

## Boundaries and scale limits

Synthetic two-moons data, synthetic availability traces, 20 clients, 80 rounds, 5 seeds at 10% top-k and 3 seeds at 2% top-k. This does not cover measured volunteer traces, real FL benchmarks, larger models, residual decay/reset policies, secure aggregation constraints, or production network behavior.

## Claim scope

Controlled Tier 1 direct test on a small two-hidden-layer non-convex MLP trained with FedAvg over 20 non-IID synthetic clients and Markov volunteer-style availability traces. Naive client-side residual/error-feedback top-k compression did not improve over non-residual top-k at 10% or 2% transmitted update values.

## Why it stopped

The direct small controlled test failed the predeclared mechanism threshold: residual top-k did not beat non-residual top-k by 0.03 accuracy and was consistently worse, including a larger negative gap under 2% compression. This is not a full-scale validation, but it is direct early falsification for the naive residual-compressed FedAvg variant in the tested setting.

## Recommended next action

Stop this paper path; a bounded follow-up should test residual aging/decay/reset policies against non-residual top-k on the same intermittent traces before considering real-trace or benchmark scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual Aging Policies for Compressed FedAvg Under Intermittent Availability
- Success threshold: Across at least 5 seeds, an age-aware residual policy improves final accuracy over no-residual top-k by at least 0.02 at one compression level, remains within 0.02 of dense FedAvg, and does not increase transmitted values by more than 5%.
- Stop condition: Stop if all age-aware residual policies remain at or below no-residual top-k mean accuracy across 2%, 5%, and 10% top-k, or if residual norms still grow without accuracy gains.

## Evidence references

- Artifact root: `<local-path>/projects/residual-compressed-fedavg-on-small-non-convex-models-with-e1675bd6ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
