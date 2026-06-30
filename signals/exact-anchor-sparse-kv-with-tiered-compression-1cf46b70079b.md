# Exact-anchor sparse KV with tiered compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-sparse-kv-with-tiered-compression-1cf46b70079b`
Run ID: `exact-anchor-sparse-kv-with-tiered-compression-1cf46b70079b-20260529T062723382268+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/05ed41879930

## What looked useful

Exact anchors are conditionally helpful but not a general correctness mechanism; fixed-anchor sparse KV needs content/salience-aware retention to avoid catastrophic loss on important non-anchor tokens.

## Boundaries and scale limits

No real transformer, training, perplexity, production quantization, offload, GPU kernel, or serving-latency validation was run. Compression is approximated by grouped mean K/V entries with fractional memory cost.

## Claim scope

Synthetic NumPy attention-cache proxy at sequence length 4096 and dimension 64: fixed exact anchors plus recent tokens and grouped compressed middle KV preserve dense attention on anchor-aligned and recency-aligned traces at roughly 8-16% effective KV memory, but fail on non-recent/non-anchor high-mass tokens.

## Why it stopped

Proxy evidence is mixed and falsifies the broad fixed-anchor claim without full model validation; it is useful for steering follow-up work but not paper-ready.

## Recommended next action

Stop this run as a proxy useful-signal negative; next bounded test should replace fixed anchors with salience-aware anchor admission and compare against dense attention on real transformer KV traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Salience-aware exact anchors for sparse KV retention
- Success threshold: Mean relative attention-output L2 <= 0.10 and mean cosine >= 0.99 at <= 0.15 effective KV memory on anchor-friendly, recency-friendly, and non-anchor high-mass cases; real-trace degradation must remain small versus dense baseline.
- Stop condition: Stop if salience-aware anchors still exceed 0.25 mean relative L2 or cosine remains below 0.95 on non-anchor high-mass cases at >=0.15 effective KV memory.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-sparse-kv-with-tiered-compression-1cf46b70079b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
