# Cascade Context Compression via Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cascade-context-compression-via-routing-0a1195d1b747`
Run ID: `cascade-context-compression-via-routing-0a1195d1b747-20260526T004741034379+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8aaed54ce305

## What looked useful

Coarse cascade routing beat recency in 19/24 condition/capacity cells with mean accuracy delta +0.00850. Fine topic/entity routing produced large skewed tail-topic gains up to +0.26990 but lost heavily on skewed head-topic and oldest-key controls, exposing equal-partition brittleness.

## Boundaries and scale limits

No trained language model, learned router, tokenizer, attention kernel, downstream QA, or end-to-end generation benchmark was run. Full validation would require model-level experiments and adaptive routing controls.

## Claim scope

Synthetic key-value stream benchmark only: deterministic routed context compression can modestly improve exact recall over same-budget recency in most tested cells, while route shape strongly controls whether gains hold under skew.

## Why it stopped

Synthetic/proxy evidence supports a mechanism and failure mode but does not validate model-level cascade context compression.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen experiment comparing fixed routed memory with adaptive per-route capacity on the same synthetic suite plus a small retrieval-LM task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Capacity for Routed Context Compression
- Success threshold: Adaptive routing improves mean accuracy over recency by at least 0.02, beats fixed cascade on at least 18/24 synthetic cells, and eliminates losses worse than -0.02 on head-topic and oldest-quartile skew controls.
- Stop condition: Stop if adaptive routing fails to beat fixed cascade on mean synthetic accuracy or still has any skew-control loss worse than -0.05 at two or more capacities.

## Evidence references

- Artifact root: `<local-path>/projects/cascade-context-compression-via-routing-0a1195d1b747`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
