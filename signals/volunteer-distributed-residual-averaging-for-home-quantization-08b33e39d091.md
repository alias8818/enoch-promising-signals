# Volunteer-Distributed Residual Averaging for Home Quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `volunteer-distributed-residual-averaging-for-home-quantization-08b33e39d091`
Run ID: `volunteer-distributed-residual-averaging-for-home-quantization-08b33e39d091-20260609T003145154175+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ca8959169993

## What looked useful

Across 72 same-budget comparisons, volunteer/residual methods had zero wins versus direct quantization. Deterministic residual additive was the closest method but was still at least 1.575x worse in relative MSE and 1.577x worse in output relative MSE; stochastic volunteer averaging was at least 15.183x worse in relative MSE.

## Boundaries and scale limits

Proxy-only CPU experiment; no real transformer weights, perplexity/task evaluation, activation-aware calibration, quantization-aware finetuning, metadata/storage packing accounting, network/worker failure model, or adversarial volunteer setting.

## Claim scope

Synthetic 1024x1024 tensor quantization probe across Gaussian, Laplace, outlier-mixture, and low-rank-plus-noise tensors found no same-value-bit-budget reconstruction or random-linear-output win for stochastic volunteer averaging or additive residual coding over direct blockwise symmetric quantization.

## Why it stopped

Early proxy falsification: bounded synthetic evidence consistently failed to beat the direct same-value-bit-budget quantization baseline, so the idea is not paper-ready and should close as no-paper useful negative signal.

## Recommended next action

Stop this simple residual-averaging quantization route; only reopen if a real-model same-storage protocol with explicit metadata accounting is proposed.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-distributed-residual-averaging-for-home-quantization-08b33e39d091`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
