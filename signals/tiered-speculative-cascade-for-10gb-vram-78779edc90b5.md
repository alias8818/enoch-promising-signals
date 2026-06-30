# Tiered Speculative Cascade for 10GB VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-speculative-cascade-for-10gb-vram-78779edc90b5`
Run ID: `tiered-speculative-cascade-for-10gb-vram-78779edc90b5-20260529T151756900501+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f20cb0e4924a

## What looked useful

Tiered speculative cascades are not generally better than a single medium draft under a 10 GB budget. In the 400-scenario grid, only 2.0% met the full threshold of <=10 GB, >2% speedup over single-draft, and >5% speedup over target-only. Wins require a very cheap small tier and small-medium agreement around 0.85-0.95.

## Boundaries and scale limits

No real model logits or serving stack were benchmarked; acceptance rates, per-token costs, and 10 GB residency are modeled. GB10 UMA does not expose discrete VRAM capacity through nvidia-smi, so memory feasibility is a budget model rather than measured concurrent model residency.

## Claim scope

Closed-form expected-cost feasibility probe for a small-to-medium-to-target speculative decoding cascade under an explicit 10 GB modeled memory budget, anchored by GB10 CUDA smoke/calibration measurements.

## Why it stopped

No-paper useful signal: this run is a modeled/proxy feasibility result, not direct full validation, and the mechanism only works in a narrow parameter region.

## Recommended next action

Run a bounded real-model trace with three concurrently loaded small/quantized models under a 10 GB cap, measuring acceptance length, latency, and peak memory against target-only and single-draft baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model acceptance trace for 10 GB tiered speculative cascade
- Success threshold: Tiered cascade achieves at least 10% tokens/second improvement over single-draft speculative decoding and at least 5% over target-only, with no exactness regression and peak residency <=10 GB.
- Stop condition: Stop if measured small-medium agreement is below 0.85, the small tier costs more than 3% of target per generated token, or concurrent residency exceeds 10 GB before showing speedup.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-speculative-cascade-for-10gb-vram-78779edc90b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
