# Anchor-Preserved KV Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-preserved-kv-compression-14c188d15639`
Run ID: `anchor-preserved-kv-compression-14c188d15639-20260602T190740690116+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/bbe37b6af998

## What looked useful

Anchor-preserved KV compression has a clear mechanism-level benefit when queries target known old anchors, with anchor-query cosine improvements of +0.892 to +0.990 across tested budgets, but it spends cache budget that slightly hurts old non-anchor queries by about -0.008 to -0.012 cosine.

## Boundaries and scale limits

CPU-only numpy benchmark; random synthetic K/V vectors; oracle anchor identities; no learned anchor detector, real transformer KV traces, language task accuracy, or latency measurement.

## Claim scope

In a synthetic retrieval-shaped attention benchmark with oracle anchor labels, preserving old anchor KVs exactly at a fixed 128-512 slot budget restores anchor-query output fidelity to full attention, while modestly reducing fidelity for old non-anchor queries.

## Why it stopped

No-paper closure: the current result is a synthetic oracle mechanism test, useful for prioritizing the next experiment but not direct/full validation of anchor-preserved KV compression in real LLM inference.

## Recommended next action

Run a bounded real-transformer trace follow-up using heuristic or attention-derived anchor selection, and stop unless it improves a retrieval/task metric at equal KV memory while keeping non-anchor degradation below a preset threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Anchor-Preserved KV Compression Replay
- Success threshold: At equal KV budget, improve anchor-target fidelity or task accuracy by at least 10 percentage points over the best baseline while keeping non-anchor degradation under 3 percentage points and reporting overhead.
- Stop condition: Stop if non-oracle anchors fail to beat the best baseline on anchor-target metrics or if non-anchor degradation exceeds 3 percentage points at the tested memory budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserved-kv-compression-14c188d15639`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
