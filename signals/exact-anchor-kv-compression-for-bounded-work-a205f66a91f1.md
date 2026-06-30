# Exact Anchor KV Compression for Bounded Work

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `exact-anchor-kv-compression-for-bounded-work-a205f66a91f1`
Run ID: `exact-anchor-kv-compression-for-bounded-work-a205f66a91f1-20260605T230427986770+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f9f83ddb00d4

## What looked useful

Finite sampled attention maps had full column rank for 8, 16, 32, 64, and 96 distinct keys. With V=I, subset anchors produced large nonzero L1 error even at 2x compression, while exact duplicate keys compressed 6x with numerical-zero output error.

## Boundaries and scale limits

Evidence is a mathematical/mechanistic NumPy probe up to 96 keys with identity-value witnesses and duplicate-key positive controls. It is not a production KV-cache benchmark, trained LLM perplexity test, learned anchor-policy evaluation, or large-context serving experiment.

## Claim scope

For generic distinct keys and arbitrary values/queries in standard softmax attention, retaining a bounded subset or bounded number of anchor KV entries cannot preserve exact full-context attention outputs as context grows; exact merging is only supported for duplicate/equivalent keys when count and summed values are retained.

## Why it stopped

Proxy/direct mechanistic falsification rather than full validation: the tested exactness conditions fail for generic distinct keys, and larger LLM runs would not make an exact bounded-anchor scheme exact without additional restrictions or state.

## Recommended next action

Stop this exact-anchor claim as an early direct/mechanistic falsification; only revisit if the method narrows the claim to duplicate/equivalent-key merging or to approximate compression with explicit error bounds.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-bounded-work-a205f66a91f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
