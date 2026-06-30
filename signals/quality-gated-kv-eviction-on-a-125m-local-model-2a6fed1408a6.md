# Quality-Gated KV Eviction on a 125M Local Model

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-gated-kv-eviction-on-a-125m-local-model-2a6fed1408a6`
Run ID: `quality-gated-kv-eviction-on-a-125m-local-model-2a6fed1408a6-20260620T214422260688+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/737af98364f9

## What looked useful

Quality-gated KV eviction won 9/9 budget-slice comparisons against recency and random. Mean NLL improvement versus recency was -4.5759 at budget 64, -3.7874 at budget 128, and -2.6759 at budget 256; at budget 256 it was only +0.2081 NLL from full cache while recency was +2.8840.

## Boundaries and scale limits

Single 125M model, one dataset, three contiguous token slices, one hand-coded attention heuristic, teacher-forced NLL only, no learned gate, no multi-model validation, no generation-quality evaluation, and no production latency or memory-pressure benchmark.

## Claim scope

On GPT-2 small (124,439,808 parameters) evaluated teacher-forced on three 768-token WikiText-2 validation slices, a cumulative attention-received quality gate with a 16-token protected recent tail outperformed recency-only and random older-token KV eviction at budgets 64, 128, and 256.

## Why it stopped

Useful bounded local evidence was produced, but the run is not paper-ready because breadth, ablations, generation-quality metrics, and serving-cost measurements are missing.

## Recommended next action

Run a bounded deepen follow-up across more WikiText-2 slices plus at least one additional dataset and compare against stronger published-style heavy-hitter eviction baselines before considering paper framing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robustness and Baseline Deepen for Attention-Quality KV Eviction
- Success threshold: Quality-gated eviction beats recency-only and the stronger heavy-hitter baseline by at least 0.1 mean NLL at budget 256 with confidence intervals excluding zero, while staying within 0.3 NLL of full cache.
- Stop condition: Stop if the quality gate fails to beat either recency-only or the stronger baseline on at least half of evaluated slices, or if its advantage is smaller than 0.05 NLL at budget 256.

## Evidence references

- Artifact root: `<local-path>/projects/quality-gated-kv-eviction-on-a-125m-local-model-2a6fed1408a6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
