# Adaptive local cascade router with latency-quality Pareto on 10GB

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-local-cascade-router-with-latency-quality-pareto-on-10gb-e2746720b30b`
Run ID: `adaptive-local-cascade-router-with-latency-quality-pareto-on-10gb-e2746720b30b-20260527T214150993850+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/df2fb53c6ff9

## What looked useful

Confidence routing had a real selection signal, reaching 85.68% accuracy at threshold 0.79 versus 84.06% for random same-fraction routing. However, batched GB10 inference made the larger model faster than the smaller model, so all cascades were slower than all-large in batched mode. Batch-1 routing could approach large-model accuracy with small speedups, but the best near-large point was only 1.1% faster than all-large.

## Boundaries and scale limits

Tested one dataset, one model family, one 30k/5k split, and offline latency estimates from measured component inference. Not validated on LLM generation, persistent serving, concurrent traffic, tokenizer overhead, or production-quality routing calibration.

## Claim scope

On a bounded Fashion-MNIST GB10 benchmark with two local PyTorch MLP classifiers, confidence-based escalation improves accuracy more than random same-fraction escalation, but it does not provide a robust latency-quality Pareto win across serving modes.

## Why it stopped

Bounded local evidence is mixed: confidence routing works as a selector, but the main latency-quality Pareto claim is not robust because batched GPU latency favored the larger model and batch-1 gains were marginal.

## Recommended next action

Stop this run as no-paper useful signal; next test should use a persistent local serving harness with latency-calibrated model pairs before making any cascade Pareto claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent-serving latency calibration for local cascade routers
- Success threshold: Adaptive cascade must match at least 99% of all-large quality while reducing p50 and p90 end-to-end latency by at least 15% versus all-large, and must beat random same-fraction routing by at least 1 percentage point quality at matched route fraction.
- Stop condition: Stop if measured cheap-model plus router overhead is not at least 20% lower than all-large latency in the target serving mode, or if confidence routing fails to beat random same-fraction routing on held-out examples.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-local-cascade-router-with-latency-quality-pareto-on-10gb-e2746720b30b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
