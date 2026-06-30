# Exact-Anchor KV Snapshots for Long Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-kv-snapshots-for-long-context-15cb0f71abbe`
Run ID: `exact-anchor-kv-snapshots-for-long-context-15cb0f71abbe-20260529T223423529558+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9cb0c1dbbdea

## What looked useful

Exact-anchor KV snapshots are mechanically viable for suffix equivalence when position and causal-mask accounting are correct, and they can reduce amortized compute when multiple continuations share the same anchor. Single-branch reuse did not amortize the anchor build cost in the local probe.

## Boundaries and scale limits

No pretrained LLM, GPU kernel, RoPE/ALiBi/learned-position production implementation, quantized cache, paged-attention allocator, disk persistence, 7B+ model, 128k real prompt, or serving scheduler was tested. A 7B-like fp16 full KV snapshot at 128k anchor tokens projects to 62.5 GiB per batch item, making storage economics the main unvalidated systems constraint.

## Claim scope

In a deterministic NumPy causal transformer with 4 layers, 4 heads, d_model 64, anchors up to 512 tokens, suffixes of 32 tokens, and up to 8 shared-prefix branches, exact per-layer KV snapshots reproduced full-prefix suffix activations within 3.6e-6 max absolute error and improved amortized CPU proxy runtime for multi-branch reuse.

## Why it stopped

Evidence is a bounded CPU NumPy mechanism/proxy result, not full validation of long-context LLM serving or a publication-grade systems benchmark.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test the same anchor snapshot invariant and cache economics on a real small transformer implementation with native KV APIs and realistic position encoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model exact-anchor KV snapshot validation
- Success threshold: Max logit difference remains within implementation floating point tolerance, and at least one multi-branch shared-prefix setting has end-to-end speedup greater than 1.5x after including anchor build and restore costs.
- Stop condition: Stop if restored-anchor logits diverge beyond tolerance under correct position accounting, or if restore/storage overhead prevents speedup in all tested multi-branch settings.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-snapshots-for-long-context-15cb0f71abbe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
