# 2-bit KV Cache with Residual Attention Anchors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `2-bit-kv-cache-with-residual-attention-anchors-e136963a2949`
Run ID: `2-bit-kv-cache-with-residual-attention-anchors-e136963a2949-20260528T022613333519+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d16359ce1dba

## What looked useful

Corrected medium run: baseline 2-bit output MSE was 4.8297. Key-norm anchors reduced MSE by 15.5% at 0.25% anchors, 31.3% at 0.5%, 64.2% at 1%, and approximately 100% at 2% once all injected special tokens were covered. Recent and uniform 5% anchors recovered only 6.1% and 12.4%, respectively, showing that anchor placement matters.

## Boundaries and scale limits

Evidence is limited to synthetic attention tensors on one GB10 GPU, sequence length 4096, 8 heads, dimension 128, batch 2, 64 query tokens, and 8 random seeds. It does not measure real language-model perplexity, generation quality, production KV-cache latency, fused-kernel behavior, long-context prompt distributions, or learned/adaptive anchor selection.

## Claim scope

In a synthetic multi-head attention proxy with injected high-salience retrieval tokens, retaining a small full-precision residual set of key/value cache rows can recover most or all output error introduced by 2-bit KV quantization when the retained rows cover the high-salience tokens. A key-norm selector matched an oracle selector in this constructed high-norm-anchor setting.

## Why it stopped

No-paper closure: the current evidence is a synthetic mechanism signal, not direct language-model or serving evidence.

## Recommended next action

Run a bounded real-model follow-up on a small GPT-2-class transformer: quantize actual autoregressive KV cache to 2 bits, retain key-norm or attention-statistic anchors, and measure loss delta plus generated-token agreement against fp16 KV.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model 2-bit KV anchors on GPT-2-small-class inference
- Success threshold: At 1-2% fp16 anchors, a practical non-oracle selector recovers at least 50% of the degradation from plain 2-bit KV on loss or next-token KL, and outperforms recent/uniform anchors at matched memory.
- Stop condition: Stop if practical non-oracle anchors recover less than 25% of the plain 2-bit KV degradation or do not beat recent/uniform anchors at matched memory.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-residual-attention-anchors-e136963a2949`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
