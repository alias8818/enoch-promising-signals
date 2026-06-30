# Bounded KV Compression with Exact Anchor Preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-kv-compression-with-exact-anchor-preservation-4de96951b1d1`
Run ID: `bounded-kv-compression-with-exact-anchor-preservation-4de96951b1d1-20260613T072812023422+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6db3840ff63f

## What looked useful

Across 18 medium synthetic cases, anchor K/V max absolute error was 0.0. Clustered compression averaged relative L2 0.1565 on clustered KV and 0.2212 on anchor-heavy KV, versus 0.4692 and 0.7683 for uniform selection. High-entropy random KV remained materially worse at 0.5652 relative L2, showing the mechanism is conditional rather than universally lossless.

## Boundaries and scale limits

No trained transformer, real KV cache, multi-layer decode, perplexity, generation-quality, latency, or production-kernel evidence was produced. Results are synthetic and depend on non-anchor KV redundancy/clusterability.

## Claim scope

Synthetic single-attention probes show that exact anchor KV preservation plus bounded clustered non-anchor summaries can approximate full attention substantially better than anchors-only or uniform non-anchor selection at 12.8x-51.2x compression, while preserving anchor K/V rows exactly.

## Why it stopped

Synthetic tensor evidence is useful but not paper-grade direct evidence for real transformer KV-cache compression.

## Recommended next action

Run a bounded direct-model follow-up on a GPT-2-small-class model that applies exact-anchor clustered KV compression during evaluation and reports perplexity, generation drift, cache memory, and decode latency against full KV and matched-budget selection baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2-small KV-cache evaluation of exact-anchor clustered compression
- Success threshold: At least 8x KV slot reduction, anchor K/V max absolute error 0.0, less than 5% perplexity degradation versus full KV, and lower loss/perplexity degradation than matched-budget uniform selection.
- Stop condition: Stop if real-model perplexity degradation exceeds 15% at 8x compression or if clustered compression does not outperform matched-budget uniform selection in two independent validation slices.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-kv-compression-with-exact-anchor-preservation-4de96951b1d1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
