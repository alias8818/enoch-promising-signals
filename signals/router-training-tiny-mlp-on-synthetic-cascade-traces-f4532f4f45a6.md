# Router training: tiny MLP on synthetic cascade traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `router-training-tiny-mlp-on-synthetic-cascade-traces-f4532f4f45a6`
Run ID: `router-training-tiny-mlp-on-synthetic-cascade-traces-f4532f4f45a6-20260611T143600045645+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d6ec3c49fcf5

## What looked useful

Across five seeds, the tiny MLP reached 0.8745 in-distribution route accuracy versus 0.5717 for a linear router, reduced mean direct cost by 41.7% versus executing the cascade, and had only -0.0012 mean success-probability delta versus the cascade. On the shifted synthetic split it reached 0.8805 accuracy, 40.5% cost savings, and +0.0005 success delta.

## Boundaries and scale limits

Evidence is limited to generated 12-dimensional synthetic traces, simulated expert success probabilities, simulated costs, five random seeds, and one modest OOD shift. It does not validate real LLM/tool cascades, production latency, real answer quality, or calibration drift.

## Claim scope

On a synthetic four-expert cheap-to-expensive cascade with nonlinear route structure, a tiny 2-hidden-layer MLP trained from cascade-accepted labels can directly route queries with much higher imitation accuracy than a linear router while preserving the cascade's mean synthetic success probability and reducing expected direct-route cost.

## Why it stopped

Synthetic-only proxy evidence supports the mechanism but is not direct/full validation and is not publication-grade.

## Recommended next action

Stop this run as no-paper useful synthetic evidence; next run should replay the same router comparison on bounded real or semi-real small-model cascade traces with measured task quality and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny MLP router on bounded real small-model cascade traces
- Success threshold: Tiny MLP direct router reduces measured mean route cost or latency by at least 25% versus executing the cascade while keeping measured task quality within 1 percentage point of the cascade and outperforming the linear router by at least 5 percentage points of route accuracy or an equivalent quality-cost frontier improvement.
- Stop condition: Stop if the tiny MLP loses more than 3 percentage points of measured task quality versus the cascade, fails to beat the linear router on the quality-cost frontier, or cannot obtain reproducible real/semi-real traces within the bounded local run.

## Evidence references

- Artifact root: `<local-path>/projects/router-training-tiny-mlp-on-synthetic-cascade-traces-f4532f4f45a6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
