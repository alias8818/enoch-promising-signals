# Ternary KV-Momentum for Long Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `ternary-kv-momentum-for-long-context-f8c8defe6401`
Run ID: `ternary-kv-momentum-for-long-context-f8c8defe6401-20260530T055320927283+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/dc7e51af54d2

## What looked useful

Plain per-token ternary KV was the best compressed variant in all tested synthetic conditions. Cross-token momentum residuals consistently increased output distortion and reduced target retrieval in hard 64-dimensional long-context cases, suggesting residual contamination across unrelated tokens.

## Boundaries and scale limits

No trained language model, no real long-context benchmark, no GPU/kernel serving benchmark, and no validation on trained KV distributions. The result is a mechanism-level proxy, not a full long-context model validation.

## Claim scope

Synthetic random-cache attention retrieval at sequence lengths 512, 2048, and 8192 with dimensions 64 and 128: naive streaming momentum/error-feedback ternary KV quantization is worse than plain per-token ternary KV on attention output fidelity and, under hard noisy queries, retrieval accuracy.

## Why it stopped

Proxy early falsification: the directly tested synthetic attention mechanism showed momentum underperforming plain ternary, but this is not a full trained-model validation.

## Recommended next action

Stop this exact mechanism as no-paper evidence; if continuing, test a grouped or block-reset residual design against plain ternary on a tiny trained transformer before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-reset ternary KV residuals on a tiny trained transformer
- Success threshold: Grouped or block-reset residual ternary KV must improve task accuracy or perplexity versus plain ternary by at least 2 percent relative while not worsening attention-output error, at matched cache memory, across at least three seeds.
- Stop condition: Stop if grouped or block-reset residuals fail to beat plain ternary on both task metric and attention-output fidelity, or if benefits appear only in synthetic retrieval without transfer to the trained tiny model.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-kv-momentum-for-long-context-f8c8defe6401`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
