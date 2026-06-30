# Pretrained GPT-2-small residual-source KV cache byte-match test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pretrained-gpt-2-small-residual-source-kv-cache-byte-match-bb0a985e6e`
Run ID: `pretrained-gpt-2-small-residual-source-kv-cache-byte-match-bb0a985e6e-20260607T215055540855+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Extreme INT4 Quantization with Residual Channel Preservation for KV Compression: enoch://control-plane/projects/extreme-int4-quantization-with-residual-channel-preservation-for-kv-compression-cc43f6e4ec9b/runs/extreme-int4-quantization-with-residual-channel-preservation-for-kv-compression-cc43f6e4ec9b-20260607T135205940058+0000
- Parent run decision: End-to-end byte-matched residual-channel KV cache decoding test: enoch://control-plane/projects/end-to-end-byte-matched-residual-channel-kv-cache-decoding-ee9fd709a3/runs/end-to-end-byte-matched-residual-channel-kv-cache-decoding-ee9fd709a3-20260607T182035125797+0000

## What looked useful

Residual-source reconstruction matched 120/120 medium cases for K/V byte equality and exact continuation logits. The post-block wrong-source control matched 0/120 cases and exact logits in 0/120 cases. The lossy fp16 round-trip control failed byte equality and exact logits in all float32 cases while matching only when the model/source was already float16.

## Boundaries and scale limits

No batch sizes above 1, no prefixes above 64 tokens, no GPT-2-medium/large or non-GPT-2 models, no quantized cache storage beyond a lossy fp16 control for float32, no fused/custom attention kernels, no serving throughput or memory benchmark, and no training-time validation.

## Claim scope

For pretrained Hugging Face GPT-2-small in eval inference, batch size 1, prefixes up to 64 tokens, CPU float32/CUDA float32/CUDA float16, and fixed text/random-token inputs, the per-layer prefix K/V cache can be reconstructed byte-exactly from each transformer's residual-source block input by replaying that block's ln_1 and attention c_attn projection.

## Why it stopped

Medium direct validation supports the mechanism in a narrow implementation scope, but does not establish broader novelty, performance value, or paper-positive robustness.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded deepen follow-up should test batch size >1, longer prefixes, and GPT-2 family variants with the same exact byte-match/logit criteria and controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batched and long-prefix GPT-2 residual-source KV reconstruction
- Success threshold: Residual-source reconstruction must produce 100% K/V byte-match and exact continuation logits across all tested batched/long-prefix cases, with wrong-source controls producing 0% byte-match and float32 lossy-source controls producing 0% byte-match.
- Stop condition: Stop on the first reproducible residual-source byte mismatch or exact-logit mismatch after ruling out nondeterminism/API misuse, or after completing the matrix and reporting all metrics.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-gpt-2-small-residual-source-kv-cache-byte-match-bb0a985e6e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
