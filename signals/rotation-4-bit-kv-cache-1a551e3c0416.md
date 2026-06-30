# Rotation 4-bit KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rotation-4-bit-kv-cache-1a551e3c0416`
Run ID: `rotation-4-bit-kv-cache-1a551e3c0416-20260604T211817646610+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/28b2f05902ed

## What looked useful

Rotation/direct 4-bit output relative-MSE ratios were 0.995 on normal activations, 0.363 on Student-t(3) activations, and 0.249 on sparse-outlier activations. Attention top-1 agreement improved from 0.872 to 0.926 on Student-t(3), and from 0.881 to 0.938 on sparse outliers.

## Boundaries and scale limits

No pretrained model was evaluated; no perplexity, generation quality, serving latency, or quantized-kernel throughput was measured. Evidence is synthetic mechanism evidence only.

## Claim scope

On synthetic RoPE attention tensors with head_dim 128, 8 heads, seq_len 2048, group_size 32, and paired seeds, Hadamard feature rotation before 4-bit KV quantization reduces attention-output error for heavy-tailed or sparse-outlier activations at the same 4x KV-cache compression; it gives no meaningful benefit for normal activations.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic and mechanism-level, not direct real-model validation.

## Recommended next action

Run a bounded GPT-2-small-class pretrained-model perplexity/decode test comparing FP16 KV, direct 8-bit KV, direct 4-bit KV, and rotated 4-bit KV on the same prompts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small rotated 4-bit KV-cache validation
- Success threshold: Rotated 4-bit KV should reduce direct 4-bit perplexity delta or logit KL by at least 30% while preserving the same nominal 4x KV-cache compression and without more than 10% decode throughput loss in the prototype.
- Stop condition: Stop if real KV activations are not heavy-tailed/outlier-prone or if rotated 4-bit improves synthetic-like diagnostics but fails to improve paired real-model perplexity/logit metrics by at least 10%.

## Evidence references

- Artifact root: `<local-path>/projects/rotation-4-bit-kv-cache-1a551e3c0416`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
