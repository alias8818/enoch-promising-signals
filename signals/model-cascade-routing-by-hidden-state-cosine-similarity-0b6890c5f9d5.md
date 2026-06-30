# Model Cascade Routing by Hidden-State Cosine Similarity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `model-cascade-routing-by-hidden-state-cosine-similarity-0b6890c5f9d5`
Run ID: `model-cascade-routing-by-hidden-state-cosine-similarity-0b6890c5f9d5-20260608T220412620627+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7b7a88ab66bb

## What looked useful

Hidden-state cosine kNN reached AUROC 0.671 on distilgpt2 and 0.674 on GPT-2, above random, but confidence reached 0.772 and 0.814 respectively and gave substantially higher accepted cheap accuracy at 10-20% coverage. Adding hidden cosine to confidence/margin/entropy did not improve the router.

## Boundaries and scale limits

2048 fixed-length validation windows per main run; GPT-2-class autoregressive models only; oracle deferral proxy instead of an actual stronger-model cascade; no production latency, batching, or cost measurement; no layer sweep or learned metric projection.

## Claim scope

On WikiText-2 next-token routing with distilgpt2 and GPT-2 small, last-token hidden-state cosine routers carry above-random correctness signal but are not competitive with confidence, margin, or entropy baselines for accepting cheap-model predictions.

## Why it stopped

Proxy/local evidence supports a weak hidden-cosine mechanism but early-falsifies the practical standalone routing claim against simple logit-derived controls; this is not a full large-scale cascade validation.

## Recommended next action

Stop this run as a bounded no-paper useful signal; any follow-up should first test whether layer-wise or learned hidden-state metrics add incremental value over confidence controls in an actual two-model cascade.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layer-wise learned hidden-state routing versus confidence in an actual small-to-medium LM cascade
- Success threshold: Hidden-state features improve test AUROC by at least 0.03 over the best logit-only baseline and improve realized cascade accuracy or cost-adjusted utility at 10-30% cheap acceptance on both datasets.
- Stop condition: Stop if hidden-state features fail to beat the best logit-only baseline by 0.01 AUROC on the first held-out dataset or do not improve realized cascade utility at any tested coverage.

## Evidence references

- Artifact root: `<local-path>/projects/model-cascade-routing-by-hidden-state-cosine-similarity-0b6890c5f9d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
