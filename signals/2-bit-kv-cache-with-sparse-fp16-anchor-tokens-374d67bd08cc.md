# 2-bit KV Cache with Sparse FP16 Anchor Tokens

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-sparse-fp16-anchor-tokens-374d67bd08cc`
Run ID: `2-bit-kv-cache-with-sparse-fp16-anchor-tokens-374d67bd08cc-20260628T174706029696+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ca36c73b2e4f

## What looked useful

Sparse FP16 anchors strongly reduce 2-bit KV attention-output error only when anchor selection captures salient/outlier tokens. Norm-based policies improved relative L2 by about 90-97% on synthetic outlier/copy profiles at 12.5% anchors, but only 9.1% on normal KV. Periodic/recent anchors were generally weak. The useful mechanism signal is that online anchor selection is the central problem, not merely storing sparse FP16 anchors.

## Boundaries and scale limits

No end-to-end language-model perplexity or generation test; no GPT-2-small-class baseline; no packed 2-bit cache kernel; metadata and packing overhead excluded from memory ratio; oracle anchor policy is an upper bound that uses future attention and is not deployable.

## Claim scope

Synthetic scaled-dot-product attention probe with seq_len=4096, 8 heads, dim=128, 32 queries, five seeds, and four KV profiles. 2-bit per-token quantized K/V plus sparse FP16 anchors was compared against plain 2-bit K/V and FP16 reference attention outputs.

## Why it stopped

No-paper useful signal from a synthetic/proxy attention experiment; evidence is not direct enough for a publication claim and naive deployable anchor policies were weak on unstructured KV.

## Recommended next action

Run a bounded direct validation on a GPT-2-small-class model: collect real per-layer KV caches, compare perplexity/generation degradation for plain 2-bit, 2-bit plus norm/recent anchors, and at least one practical KV quantization baseline with metadata-aware memory accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small direct validation for 2-bit KV anchors
- Success threshold: At matched or lower total KV memory than a practical 4-bit baseline, 2-bit plus deployable anchors should recover at least half of the plain-2-bit perplexity degradation and show no more than 10% decode-throughput regression in the prototype path.
- Stop condition: Stop if deployable anchor policies recover less than 25% of the plain-2-bit perplexity degradation or if metadata/packing overhead removes the claimed memory advantage versus 4-bit KV.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-sparse-fp16-anchor-tokens-374d67bd08cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
