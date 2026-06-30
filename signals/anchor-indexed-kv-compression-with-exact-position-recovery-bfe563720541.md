# Anchor-Indexed KV Compression with Exact Position Recovery

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-kv-compression-with-exact-position-recovery-bfe563720541`
Run ID: `anchor-indexed-kv-compression-with-exact-position-recovery-bfe563720541-20260621T230804772937+0000`

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

- Provider-backed Research Facility batch: z-ai/glm-5.2: enoch://research-facility/provider/z-ai/glm-5.2/25a0052b910a

## What looked useful

Anchor indexing solved the position-recovery failure introduced by compaction: 0/9,216 sweep lookup errors for anchors versus 75.0% to 91.67% errors for a stride-only compacted-index control. Metadata was 1.63% to 1.92% of compressed bytes in the sweep.

## Boundaries and scale limits

CPU-only synthetic arrays; no real transformer decoding, no RoPE integration in model runtime, no long-context serving trace, no GPU/kernel throughput measurement, and no exact KV-value recovery because the payload used lossy int8 quantization.

## Claim scope

In deterministic synthetic compacted KV-cache simulations up to 8,192 tokens, per-block anchor metadata recovered exact original absolute positions for all sampled lookups, while a simple uint8 payload gave roughly 3.9x memory reduction versus kept fp32 KV with low synthetic attention-output error.

## Why it stopped

No-paper closure: this run provides bounded synthetic mechanism evidence, not direct model-quality or serving-performance validation.

## Recommended next action

Run a bounded real-model follow-up that inserts anchor-indexed KV retrieval into a small transformer decoding path and compares perplexity/position-sensitive generation against dense KV and a non-anchor compaction baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer anchor-indexed KV decoding validation
- Success threshold: Zero position-recovery errors, less than 1% relative perplexity degradation versus dense KV on the fixed slice, at least 2x KV memory reduction, and non-anchor control showing measurable position-related failure under compaction.
- Stop condition: Stop if any position-recovery error occurs, if perplexity degrades by 1% or more versus dense KV, if memory reduction is below 2x, or if integration cannot run within a bounded local small-model experiment.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-kv-compression-with-exact-position-recovery-bfe563720541`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
