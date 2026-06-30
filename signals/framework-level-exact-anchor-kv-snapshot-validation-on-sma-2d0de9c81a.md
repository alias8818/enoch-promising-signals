# Framework-level exact-anchor KV snapshot validation on small pretrained decoders

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `framework-level-exact-anchor-kv-snapshot-validation-on-sma-2d0de9c81a`
Run ID: `framework-level-exact-anchor-kv-snapshot-validation-on-sma-2d0de9c81a-20260601T040550798138+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-model exact-anchor KV snapshot validation: enoch://control-plane/projects/real-model-exact-anchor-kv-snapshot-validation-5c92405e0b/runs/real-model-exact-anchor-kv-snapshot-validation-5c92405e0b-20260530T023001018797+0000
- Parent run decision: Cross-architecture and serialized exact-anchor KV snapshot validation: enoch://control-plane/projects/cross-architecture-and-serialized-exact-anchor-kv-snapshot-7920c2d940/runs/cross-architecture-and-serialized-exact-anchor-kv-snapshot-7920c2d940-20260531T185643639286+0000

## What looked useful

Across 288 model/prompt/anchor rows, exact-anchor snapshot resume preserved all suffix top-1 logits and all 8-step greedy continuations. Worst resumed suffix-logit max absolute difference was 2.441406e-04 and controls diverged, especially for distilgpt2 and gpt2 wrong-anchor/zero-KV ablations.

## Boundaries and scale limits

Validated on sshleifer/tiny-gpt2, distilgpt2, and gpt2 with 24 deterministic prompts, four anchors per prompt, and 8 greedy continuation steps. Not validated for batched or padded inputs, non-GPT2 architectures, quantized inference, beam search or sampling, cross-device cache transfer, long-context limits, 7B+ models, or serving throughput.

## Claim scope

For unbatched, no-padding CPU float32 inference on GPT-2-family small pretrained decoders in Hugging Face Transformers, serialized exact-token anchor KV snapshots can replay suffix logits and greedy continuations without changing top-1 outputs versus full-prefill decoding.

## Why it stopped

Direct bounded validation succeeded, but the scope is too narrow for publication-grade evidence and broader architecture/batching/serving validation remains untested.

## Recommended next action

Stop as no-paper useful signal; the bounded evidence supports exact-anchor KV snapshot mechanics on GPT-2-family small decoders but not a broad framework paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-anchor KV snapshots under batched padding and non-GPT2 decoder families
- Success threshold: At least two decoder families, including one non-GPT2 family, show 100% suffix top-1 agreement and 100% greedy-token agreement over at least 200 total anchor rows, with wrong-position or wrong-mask controls diverging in logits.
- Stop condition: Stop negative if any supported framework path cannot preserve top-1 suffix logits under correct exact-anchor snapshots after fixing documented attention_mask/cache_position usage, or if only GPT-2-family unbatched cases remain viable.

## Evidence references

- Artifact root: `<local-path>/projects/framework-level-exact-anchor-kv-snapshot-validation-on-sma-2d0de9c81a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
