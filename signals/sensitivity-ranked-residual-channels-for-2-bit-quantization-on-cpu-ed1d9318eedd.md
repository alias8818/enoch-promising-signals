# Sensitivity-Ranked Residual Channels for 2-bit Quantization on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sensitivity-ranked-residual-channels-for-2-bit-quantization-on-cpu-ed1d9318eedd`
Run ID: `sensitivity-ranked-residual-channels-for-2-bit-quantization-on-cpu-ed1d9318eedd-20260601T004231718906+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/03d2b34b4c60

## What looked useful

Sensitivity-ranked residual channels reduced holdout output MSE by 0.3198 on average across 24 scenario-budget cells versus 0.0461 for random selection, had 0.9779 mean top-k overlap with the holdout oracle, and won 18/24 non-oracle cells. The advantage over diagonal sensitivity was small at 0.0016 absolute average MSE-reduction.

## Boundaries and scale limits

No real model weights, no real task data, no end-to-end perplexity or accuracy, and no packed int2 CPU kernel throughput were tested. Evidence is layer-level and synthetic, though held out across seeds and activation regimes.

## Claim scope

In a CPU-only NumPy proxy over synthetic 512x512 linear layers, restoring 1-10% of output channels after 2-bit per-channel weight quantization is useful, and calibration output-error sensitivity nearly matches a holdout oracle for choosing residual channels.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a synthetic layer-level proxy rather than direct real-model CPU quantization validation.

## Recommended next action

Run a bounded real-model CPU follow-up using a small transformer or MLP with calibration data, comparing sensitivity-ranked residual channels against diagonal sensitivity, quant-error norm, random selection, and no residuals on task quality plus low-bit CPU latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU validation of sensitivity-ranked residual channels for 2-bit quantization
- Success threshold: Sensitivity-ranked residual channels recover at least 50% of the quality loss from plain 2-bit quantization and beat the best cheap non-oracle baseline by at least 5% relative quality-loss recovery at no more than 10% residual-channel budget.
- Stop condition: Stop if sensitivity ranking fails to beat diagonal sensitivity or quant-error norm on the real-model metric at two or more residual budgets, or if residual-channel CPU overhead removes the practical benefit.

## Evidence references

- Artifact root: `<local-path>/projects/sensitivity-ranked-residual-channels-for-2-bit-quantization-on-cpu-ed1d9318eedd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
