# Parameter-Matched Sparse Mixture-of-Depths vs Dense Baseline

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `parameter-matched-sparse-mixture-of-depths-vs-dense-baseline-763586b73b9b`
Run ID: `parameter-matched-sparse-mixture-of-depths-vs-dense-baseline-763586b73b9b-20260525T081220947606+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8a852442b9b4

## What looked useful

At equal 146,564 trainable parameters, dense validation loss averaged 3.5796 versus 4.0069 for MoD, dense validation accuracy averaged 0.1786 versus 0.0697 for MoD, and MoD train throughput averaged 0.900x dense despite routing only half the token positions.

## Boundaries and scale limits

Test used 4-layer 146,564-parameter toy transformers, synthetic modular recurrence data, 3 seeds, 200 optimization steps, CPU PyTorch implementation, and one routing capacity of 0.5. It does not cover GPT-2-small-class models, natural-language corpora, optimized GPU sparse kernels, auxiliary router losses, longer training, or capacity schedules.

## Claim scope

In a small CPU-bound synthetic autoregressive language-modeling benchmark, a learned-router sparse Mixture-of-Depths variant routing 50% of token positions per block did not match a dense transformer baseline with exactly equal trainable parameter count.

## Why it stopped

Proxy-scale but direct controlled evidence falsified the naive 50% learned-router sparse-depth variant: it was substantially worse in validation loss and accuracy and slower on average than the equal-parameter dense baseline.

## Recommended next action

Stop this run as an early bounded negative; only revisit with a parameter-matched GPT-2-small-class real-corpus test using optimized sparse kernels and an explicit router/load-balancing design.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched learned-router MoD with capacity sweep and auxiliary router loss
- Success threshold: A MoD configuration must recover within 0.05 validation loss of dense while achieving at least 1.15x train-token throughput or a clearly lower measured compute proxy across all seeds.
- Stop condition: Stop if all capacities remain more than 0.10 validation loss worse than dense or fail to exceed dense throughput by at least 10%.

## Evidence references

- Artifact root: `<local-path>/projects/parameter-matched-sparse-mixture-of-depths-vs-dense-baseline-763586b73b9b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
