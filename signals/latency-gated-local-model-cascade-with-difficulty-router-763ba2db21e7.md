# Latency-Gated Local Model Cascade with Difficulty Router

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `latency-gated-local-model-cascade-with-difficulty-router-763ba2db21e7`
Run ID: `latency-gated-local-model-cascade-with-difficulty-router-763ba2db21e7-20260525T232631245457+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/74ed5f3bb060

## What looked useful

Across five seeds and seven thresholds, every dataset had at least one viable threshold. Accuracy-matching cascade points achieved 7.66x speedup on breast_cancer with 11.9% routing, 2.31x on digits with 40.9% routing, and 6.28x on wine with 14.6% routing.

## Boundaries and scale limits

Classical-ML proxy only; no LLMs, token generation, GPU scheduling, batching, KV-cache behavior, production serving overhead, or broad prompt distributions were tested.

## Claim scope

On three small scikit-learn built-in datasets, a cheap classifier confidence gate can route a minority of single-query requests to a heavier local classifier and preserve expensive-only accuracy within 1 percentage point while reducing measured mean CPU inference latency.

## Why it stopped

Proxy evidence supports the mechanism but does not directly validate local LLM cascade serving, so paper-positive closure is not warranted.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same router on a bounded real local LLM cascade with cheap-only and expensive-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded Real Local LLM Difficulty-Router Cascade
- Success threshold: At least 1.5x mean end-to-end latency speedup versus larger-model-only with quality within 2 percentage points on a held-out prompt split and no worse than 10% p95 latency regression.
- Stop condition: Stop if the router cannot beat larger-model-only latency by 1.25x at any threshold that keeps quality within 2 percentage points, or if cheap-model confidence is uncorrelated with larger-model rescue benefit.

## Evidence references

- Artifact root: `<local-path>/projects/latency-gated-local-model-cascade-with-difficulty-router-763ba2db21e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
