# Sparse/paged execution for exact segment-aware content-anchor KV replay

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `sparse-paged-execution-for-exact-segment-aware-content-anc-8669d434c6`
Run ID: `sparse-paged-execution-for-exact-segment-aware-content-anc-8669d434c6-20260516T065123394117+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Sparse/paged execution for exact segment-aware content-anchor KV replay: internal_generated:sparse-paged-execution-for-exact-segment-aware-content-anc-8669d434c6

## What looked useful

Exact segment replay must key on context/position-equivalent prefix state, not content alone. Content-only page reuse produced consistent next-token logit errors despite reducing computed tokens.

## Boundaries and scale limits

Synthetic workloads, randomly initialized tiny transformer, no production paged-attention kernel, no pretrained LLM, no real serving traces, and no end-to-end scheduler throughput validation.

## Claim scope

A deterministic small RoPE causal transformer benchmark shows exact KV replay is correct for identical prefix/page states, but content-only page anchors are not exact when causal context or position changes.

## Why it stopped

No-paper useful signal: exact prefix replay is supported, but content-anchor replay is not exact under changed context/position; Tier 4 paper readiness is not met.

## Recommended next action

Stop this follow-up lineage: the useful mechanism is narrowed to exact prefix/tree replay, the broader content-anchor exactness claim is falsified in direct small-model tests, and follow-up depth is already 4.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/sparse-paged-execution-for-exact-segment-aware-content-anc-8669d434c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
