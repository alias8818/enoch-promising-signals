# Speculative decoding with KV-cache draft tokens without extra VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `speculative-decoding-with-kv-cache-draft-tokens-without-extra-vram-a9f5522620d9`
Run ID: `speculative-decoding-with-kv-cache-draft-tokens-without-extra-vram-a9f5522620d9-20260605T160905465527+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/7be7d2f361d0

## What looked useful

Target-side draft/proposal KV does not inherently require an extra gamma-sized target KV buffer if the serving engine can write proposals into unused positions of the normal preallocated cache and treat rejection as logical rollback. The tradeoff is extra target verification work when acceptance is low.

## Boundaries and scale limits

The run used a small random transformer, batch size 1, short sequences, eager PyTorch, and synthetic proposal tokens. It did not test a pretrained large model, production paged KV cache, CUDA graphs, batching, draft-model runtime, draft-model weights, or draft-model KV memory. fp16 exactness failed in one benchmark setting and needs direct follow-up.

## Claim scope

A toy CUDA causal-transformer verifier showed that target-model speculative proposal KV entries can be written into the already preallocated target KV cache, committed by advancing logical length, and rejected by rolling logical length back, with exact fp32 greedy-output equivalence across gamma and accept-rate sweeps.

## Why it stopped

Bounded CUDA toy evidence supports the target-KV overlay mechanism but is not full end-to-end speculative-decoding validation, and the fp16 mismatch prevents claiming production-ready correctness.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should test fp16/bf16 numerical equivalence and allocator behavior in a small real-model paged-KV implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Low-precision and paged-cache validation for overlay speculative target KV
- Success threshold: Exact output match or a justified distribution-level acceptance rule with zero unexplained greedy mismatches across at least 1,000 generated tokens, plus allocator evidence showing zero incremental target KV pages for proposal windows.
- Stop condition: Stop if low-precision overlay verification produces persistent unexplained mismatches above 0.1% of generated tokens or if the paged-cache allocator necessarily reserves separate gamma-sized target KV pages.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-kv-cache-draft-tokens-without-extra-vram-a9f5522620d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
