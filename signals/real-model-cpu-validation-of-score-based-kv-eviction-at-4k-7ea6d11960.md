# Real-model CPU validation of score-based KV eviction at 4k-8k context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-model-cpu-validation-of-score-based-kv-eviction-at-4k-7ea6d11960`
Run ID: `real-model-cpu-validation-of-score-based-kv-eviction-at-4k-7ea6d11960-20260527T061503316352+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Score-based KV eviction for long-context CPU inference: enoch://control-plane/projects/score-based-kv-eviction-for-long-context-cpu-inference-9eb4e2b6fdd1/runs/score-based-kv-eviction-for-long-context-cpu-inference-9eb4e2b6fdd1-20260526T023921141374+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/77620b22bbc3

## What looked useful

Score-based retention was worse than recency by large NLL margins at 4k and near-8k context; recency stayed close to the full-cache reference, while score-based retention was sometimes worse than random near 8k.

## Boundaries and scale limits

Single 135M real model, one synthetic controlled prompt distribution, one seed for random retention, cumulative last-layer mean-attention score only, no real-document benchmark, no multi-model replication, and no serving-system latency measurement.

## Claim scope

In a bounded CPU direct test with HuggingFaceTB/SmolLM2-135M on controlled synthetic text, cumulative last-layer attention-score KV retention underperformed simple recency on continuation NLL at 4096 and 7680 prompt tokens for every tested retained-cache budget.

## Why it stopped

Direct small real-model 4k and near-8k tests falsified the practical threshold that score-based KV retention should beat a recency baseline under the tested policy; this is a bounded negative, not full-scale validation.

## Recommended next action

Stop treating this score-only policy as promising; only revisit with a pre-registered hybrid or task-specific score policy that must beat recency on multi-document 4k-8k NLL or task accuracy.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-model-cpu-validation-of-score-based-kv-eviction-at-4k-7ea6d11960`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
