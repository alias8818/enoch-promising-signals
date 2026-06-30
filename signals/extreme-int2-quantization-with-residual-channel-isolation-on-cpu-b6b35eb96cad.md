# Extreme INT2 Quantization with Residual Channel Isolation on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `extreme-int2-quantization-with-residual-channel-isolation-on-cpu-b6b35eb96cad`
Run ID: `extreme-int2-quantization-with-residual-channel-isolation-on-cpu-b6b35eb96cad-20260609T134715299720+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1ef4e8652a3f

## What looked useful

Residual output-channel isolation repaired concentrated row-outlier INT2 error by 46.8% versus pure INT2 at 3.75 bpw, but the best sub-4-bpw residual configuration was still 2.68x worse than INT4 in the favorable row-outlier scenario and 4.04x to 4.60x worse in mixed-tail and gaussian scenarios.

## Boundaries and scale limits

No real transformer weights, no activation traces, no packed INT2 CPU kernel, no end-to-end perplexity or task accuracy, and no latency or memory-bandwidth benchmark were tested. The result is a bounded mechanism probe, not a full model-serving validation.

## Claim scope

On synthetic 768x768 CPU linear-projection probes, per-output-row affine INT2 plus exact high-precision residual output-channel isolation up to 12.5% isolated rows improved pure INT2 error in outlier-heavy cases but did not approach pure INT4 output relative RMSE under a sub-4-bpw storage budget.

## Why it stopped

Proxy early falsification: the tested synthetic linear-projection mechanism failed the predeclared threshold of INT2 plus residual rows under 4 bpw reaching within 1.25x INT4 output relative RMSE.

## Recommended next action

Stop this as a paper claim; the only justified next bounded test is a real GPT-2-small-layer activation-aware replication to check whether real channel error concentration is much stronger than these synthetic probes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware INT2 residual channel isolation on real GPT-2-small layers
- Success threshold: At <=4.0 bpw including residual rows and metadata, INT2 plus residual isolation reaches within 1.25x pure INT4 layer-output relative RMSE on at least 75% of tested GPT-2-small projection layers and improves pure INT2 RMSE by at least 25%.
- Stop condition: Stop if activation-aware real-layer results remain more than 2x worse than INT4 on most tested layers or improve pure INT2 by less than 25%.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int2-quantization-with-residual-channel-isolation-on-cpu-b6b35eb96cad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
