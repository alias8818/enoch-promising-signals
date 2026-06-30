# CPU Text Router Cascade With Real Local Runtime

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-text-router-cascade-with-real-local-runtime-05e1e63b48`
Run ID: `cpu-text-router-cascade-with-real-local-runtime-05e1e63b48-20260604T114731250975+0000`

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

- Parent run decision: Tiny Router Cascade for Local CPU Inference: enoch://control-plane/projects/tiny-router-cascade-for-local-cpu-inference-eab320b675c4/runs/tiny-router-cascade-for-local-cpu-inference-eab320b675c4-20260604T073219408888+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4f69b55a54be

## What looked useful

Held-out test after validation threshold selection: always-heavy accuracy 0.982975 at 3.9568 ms mean latency; cascade accuracy 0.993728 at 0.1518 ms mean latency, routing 2.78% of examples and achieving 26.07x mean-latency speedup versus always-heavy.

## Boundaries and scale limits

Single small binary short-message dataset; one deterministic split; one fast model and one deliberately heavy CPU kNN model; no representative local LLM, batching, concurrency, drift, or multi-domain validation.

## Claim scope

On the UCI SMS Spam Collection with a validation-selected confidence threshold, a local CPU cascade using word Naive Bayes as router and hashed character kNN as the heavier classifier improved held-out accuracy versus both baselines while reducing mean latency versus always-heavy inference.

## Why it stopped

Tier 1 controlled small direct test passed and produced useful mechanism evidence, but the single-dataset kNN-heavy setup is not broad or representative enough for paper-positive closure.

## Recommended next action

Run a bounded deepen follow-up across at least three real text datasets with a representative stronger local heavy model and the same validation-selected threshold protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-dataset CPU text router cascade with representative local heavy model
- Success threshold: On at least two of three datasets, cascade accuracy is no worse than always-heavy accuracy minus 0.005 and mean latency is at least 3x faster than always-heavy; no dataset may show more than a 0.01 accuracy drop.
- Stop condition: Stop as negative if two datasets fail the accuracy retention threshold or if representative heavy-model runtime makes the cascade less than 2x faster on all tested datasets.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-text-router-cascade-with-real-local-runtime-05e1e63b48`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
