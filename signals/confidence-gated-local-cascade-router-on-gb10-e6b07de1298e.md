# Confidence-gated local cascade router on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `confidence-gated-local-cascade-router-on-gb10-e6b07de1298e`
Run ID: `confidence-gated-local-cascade-router-on-gb10-e6b07de1298e-20260610T031823461824+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8a2ca7664871

## What looked useful

The confidence scores enriched routed sets for hard examples and low escalation rates were cheaper than running the large model on every example, but the cascade premise failed: the routed-to model was slower and lower accuracy across primary and rescue runs. Future cascade tests should first prove the expert is stronger on the routed distribution before optimizing the router.

## Boundaries and scale limits

This was not an LLM-serving benchmark and did not test production prompts, tokenizer effects, KV-cache behavior, human preference quality, or calibrated uncertainty beyond raw softmax confidence. The result falsifies this bounded local setup, not all cascade routing.

## Claim scope

On two deterministic GB10-local synthetic classification cascades using a 5k-parameter cheap MLP, a 484k-parameter larger MLP, raw softmax confidence routing, and same-budget random controls, confidence-gated routing did not improve the accuracy-cost tradeoff because the larger local model was consistently less accurate than the cheap model.

## Why it stopped

Proxy/early falsification: in the tested GB10-local synthetic cascades, routing to the larger local model reduced accuracy because the larger model underperformed the cheap model even after longer-training rescue runs.

## Recommended next action

Stop this run as a bounded negative; a next bounded test should use an actually stronger local model pair and require the expert to beat the cheap model on the routed subset before evaluating cascade thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Expert-valid confidence cascade with a demonstrably stronger local model pair
- Success threshold: Across at least 5 seeds or benchmark shards, the expert must beat the cheap model on the routed subset, and the best validation-selected confidence threshold must improve held-out accuracy by at least 1 percentage point over cheap-only and 0.5 percentage points over same-budget random while costing less than 70% of expert-only inference.
- Stop condition: Stop negative if the expert is not stronger on the low-confidence subset or if confidence routing fails to beat same-budget random on held-out data.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-local-cascade-router-on-gb10-e6b07de1298e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
