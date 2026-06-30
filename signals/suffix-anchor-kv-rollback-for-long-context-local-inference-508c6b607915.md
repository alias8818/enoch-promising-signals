# Suffix-Anchor KV Rollback for Long-Context Local Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-anchor-kv-rollback-for-long-context-local-inference-508c6b607915`
Run ID: `suffix-anchor-kv-rollback-for-long-context-local-inference-508c6b607915-20260523T234003472552+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/84a15477df72

## What looked useful

The mechanism works if the cache is explicitly restored after each branch. The first smoke failed because DynamicCache is mutable and naive reuse extends the anchor; adding crop(anchor_len) made rollback numerically match full recompute. Performance is conditional: larger anchors helped, while a 256-token anchor with larger suffixes was slower than full recompute.

## Boundaries and scale limits

Synthetic small-model benchmark only: random weights, batch size 1, anchors up to 2048 tokens, suffixes up to 512 tokens, no trained long-context LLM, no tokenizer-real prompts, no serving scheduler, no paged-attention allocator, no quantized model, and no concurrent sessions.

## Claim scope

On a random 30M GPT-2-style decoder running on GB10 with Hugging Face transformers, suffix-anchor KV rollback by cropping a mutable DynamicCache back to the anchor length preserves suffix logits within floating-point tolerance and improves repeated prefill latency when the stable anchor is large enough, with measured 1.50x-2.87x speedups for 1024-2048 token anchors and 32-512 token suffixes.

## Why it stopped

Evidence is a bounded synthetic mechanism benchmark, not a publication-grade validation on trained long-context models or production serving workloads.

## Recommended next action

Stop this run as no-paper useful signal; next, test the same rollback discipline inside a real paged-attention local serving stack on a trained long-context model with edit/branch workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paged-Attention Suffix-Anchor Rollback on a Trained Local Long-Context Model
- Success threshold: At least 25% lower median prefill or TTFT versus full recompute on stable-anchor edit traces, no semantic/output divergence beyond normal deterministic tolerance, and no more than 10% memory overhead versus the engine's normal prefix-cache baseline.
- Stop condition: Stop if rollback cannot be implemented without copying most of the KV cache per branch, if output equivalence fails under deterministic decoding, or if median latency improvement is below 10% on 4k+ anchor workloads.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-anchor-kv-rollback-for-long-context-local-inference-508c6b607915`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
