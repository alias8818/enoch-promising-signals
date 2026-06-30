# 2-Bit Asymmetric KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-asymmetric-kv-cache-b69d58aa2f4a`
Run ID: `2-bit-asymmetric-kv-cache-b69d58aa2f4a-20260607T074316001510+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/74310f1de90c

## What looked useful

Full-head asym2 K/V raised loss from 4.2244 to 5.7813 (+1.5570 nats) and perplexity from 68.33 to 324.20, worse than signed 2-bit at 5.5273 loss. Asym2 group size 8 reduced the loss to 4.4436 (+0.2192 nats) but would require substantial min/max metadata, making it not a clean 2-bit cache.

## Boundaries and scale limits

12,288 tokens per mode on GPT-2-small, sequence length 128, CUDA fp16 eager attention. Did not test packed cache storage, decode-time cache updates, long contexts, residual windows, larger LLMs, task accuracy, or custom kernels.

## Claim scope

On GPT-2-small with WikiText-2 evaluation, direct full-head 2-bit asymmetric quantization/dequantization of K and V before attention substantially degrades language-model loss and is worse than a signed 2-bit baseline; finer asymmetric groups reduce the loss hit but introduce metadata overhead that weakens the clean 2-bit-cache claim.

## Why it stopped

Early bounded falsification of the simple full-head 2-bit asymmetric KV-cache mechanism; the only positive signal requires finer groups with metadata overhead and is not publication-grade direct evidence.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test metadata-aware group-8 asymmetric K/V with actual packed decode cache and compare effective bits/value plus loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Metadata-aware group-8 asymmetric KV cache with packed decode storage
- Success threshold: Loss delta versus fp16 is at most 0.2 nats while effective K/V cache footprint is at most 3 bits per value including metadata, with no throughput regression larger than 25% versus fp16 eager decode.
- Stop condition: Stop if metadata-inclusive footprint exceeds 3 bits/value or validation loss delta exceeds 0.4 nats after tuning group size and a small residual window.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-asymmetric-kv-cache-b69d58aa2f4a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
