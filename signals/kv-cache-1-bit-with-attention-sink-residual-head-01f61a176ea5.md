# KV-cache 1-bit with attention-sink residual head

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-1-bit-with-attention-sink-residual-head-01f61a176ea5`
Run ID: `kv-cache-1-bit-with-attention-sink-residual-head-01f61a176ea5-20260619T234440598627+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b77064485f94

## What looked useful

1-bit all-cache reconstruction was highly distorted on GPT-2 seq128 (mean relative MSE 2.2533). Keeping 4 full-precision sink tokens reduced mean relative MSE to 0.4238, while adding one residual head/layer only improved it to 0.4151 at about 17% of fp16 cache bits. More residual heads improved distortion slowly but raised the cache fraction to about 40% for four heads.

## Boundaries and scale limits

Activation-boundary probe only; no patched autoregressive KV-cache decoding, next-token KL/perplexity, throughput, learned quantizer, modern 7B+ model, or long-context benchmark was tested.

## Claim scope

On pretrained GPT-2 small attention activations at 128-256 tokens, preserving early attention-sink K/V states greatly reduces sign-only 1-bit KV-cache attention-output distortion, while preserving one sink-attending residual head per layer adds only a small additional gain.

## Why it stopped

Proxy activation evidence supports sink-token preservation but shows the residual-head addition is weak and the combined approximation remains too distorted for a positive paper gate.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should patch GPT-2 KV-cache decoding and require next-token KL/perplexity improvement at comparable cache fraction before considering larger models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2 KV-cache decoding test for 1-bit sink-token cache
- Success threshold: At 128-512 token contexts on GPT-2-small-class, achieve at least 4x cache-bit reduction versus fp16 with mean next-token KL <= 0.05 and perplexity degradation <= 3%; residual heads must improve KL by at least 10% relative over sink-only at the same or lower cache fraction.
- Stop condition: Stop if sink-only or sink-plus-residual-head exceeds mean next-token KL 0.10 or perplexity degradation 5% at less than 4x cache-bit reduction, or if residual heads do not beat sink-only after cache-fraction matching.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-1-bit-with-attention-sink-residual-head-01f61a176ea5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
