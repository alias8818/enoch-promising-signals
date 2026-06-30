# Hierarchical Anchor Compression for CPU Long-Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `hierarchical-anchor-compression-for-cpu-long-context-014d30c73f30`
Run ID: `hierarchical-anchor-compression-for-cpu-long-context-014d30c73f30-20260529T144713425007+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/18d97d379b2d

## What looked useful

Hierarchical mean-anchor routing fails mainly at the coarse group gate: at 262k topic-aligned tokens, the best hierarchical route recovered 0.0703 recall while the flat block-anchor baseline recovered 0.9258 recall at the same 0.78125% candidate-token fraction. Sparse off-topic needles also remained near-random for compressed mean-anchor methods.

## Boundaries and scale limits

Synthetic embeddings only; no trained transformer, no real corpus, no learned anchors, no KV-cache integration, and no full long-context LLM evaluation. Runtime was a local CPU sweep under 10 seconds, so this is mechanism evidence rather than full-scale validation.

## Claim scope

In a bounded synthetic CPU retrieval benchmark over 16k to 262k normalized token embeddings, a two-level hierarchy of mean block/group anchors does not preserve enough recall to justify paper-ready long-context compression claims; flat block mean anchors are the stronger baseline for topic-aligned retrieval.

## Why it stopped

Proxy/local early falsification: the tested two-level mean-anchor hierarchy loses too much recall versus a flat block-anchor control, especially as context length grows. This is not a full validation of LLM long-context behavior and does not rule out learned or multi-prototype anchors.

## Recommended next action

Stop this naive mean-hierarchy line as no-paper evidence; if continuing, test multi-prototype or learned group anchors against the flat block-anchor baseline on the same benchmark before any model-scale work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Prototype Group Anchors for CPU Long-Context Routing
- Success threshold: At 262k topic_aligned tokens, achieve at least 0.85 recall@1 at no more than 1% candidate-token fraction and at least 1.5x lower total ms/query than exact full scan, while not underperforming flat block anchors by more than 0.05 recall at matched candidate fraction.
- Stop condition: Stop if multi-prototype group anchors cannot exceed 0.50 recall@1 at 262k topic_aligned tokens under 1% candidate fraction or if they are slower than the flat block-anchor baseline at matched recall.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-anchor-compression-for-cpu-long-context-014d30c73f30`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
