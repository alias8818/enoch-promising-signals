# Cross-architecture and serialized exact-anchor KV snapshot validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cross-architecture-and-serialized-exact-anchor-kv-snapshot-7920c2d940`
Run ID: `cross-architecture-and-serialized-exact-anchor-kv-snapshot-7920c2d940-20260531T185643639286+0000`

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

- Parent run decision: Real-model exact-anchor KV snapshot validation: enoch://control-plane/projects/real-model-exact-anchor-kv-snapshot-validation-5c92405e0b/runs/real-model-exact-anchor-kv-snapshot-validation-5c92405e0b-20260530T023001018797+0000
- Parent run decision: Exact-Anchor KV Snapshots for Long Context: enoch://control-plane/projects/exact-anchor-kv-snapshots-for-long-context-15cb0f71abbe/runs/exact-anchor-kv-snapshots-for-long-context-15cb0f71abbe-20260529T223423529558+0000

## What looked useful

Across 30 medium cases, serialized cache roundtrips were bit-exact, serialized continuation matched full-prefix baseline with max absolute logit error <= 4.44e-16 and top-1 match rate 1.0, and final cache matched full-prefix cache with max absolute error <= 5.00e-16. Wrong-position ablation produced nonzero logit drift in every case, showing anchor position metadata is required.

## Boundaries and scale limits

Tested only self-contained toy decoders on a CPU worker: 3 layers, d_model 48, 4 heads, anchor length 48, suffix length 16, 5 seeds, 2 serialization formats. Not tested on pretrained models, Hugging Face/vLLM/llama.cpp/TensorRT-LLM cache APIs, different CPU ISA/endianness, GPU runtimes, quantized/paged/batched KV caches, long context, or production snapshot manifests.

## Claim scope

In a deterministic NumPy toy decoder, exact KV anchor snapshots serialized with npz or pickle can be restored and used for incremental continuation with logits and final cache matching a full-prefix recompute baseline to floating-point noise across absolute-position, RoPE, and ALiBI-like attention variants.

## Why it stopped

No-paper useful signal: medium fixed-seed toy evidence supports the mechanism, but the run does not validate real model/framework cache formats or true cross-architecture portability.

## Recommended next action

Run a bounded direct framework validation on small pretrained models using real Hugging Face DynamicCache/static cache serialization plus one independent runtime or hardware target, with byte-exact cache roundtrip checks and full-prefix baseline logits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Framework-level exact-anchor KV snapshot validation on small pretrained decoders
- Success threshold: Across at least 2 architectures, 3 seeds/prompts, 2 anchor lengths, and 2 serialization/runtime targets, serialized-anchor continuation has max logit error <= 1e-5 for fp32 or <= 1e-2 for fp16/bf16, top-1 match rate >= 0.99, cache roundtrip exactness where dtype permits, and both ablations show at least 100x larger logit error or reduced top-1 match.
- Stop condition: Stop as unsupported if any architecture with correct metadata repeatedly exceeds the dtype tolerance, if a real framework cache cannot be faithfully serialized/restored without private state not captured in the snapshot manifest, or if ablations do not distinguish correct from incorrect anchors.

## Evidence references

- Artifact root: `<local-path>/projects/cross-architecture-and-serialized-exact-anchor-kv-snapshot-7920c2d940`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
