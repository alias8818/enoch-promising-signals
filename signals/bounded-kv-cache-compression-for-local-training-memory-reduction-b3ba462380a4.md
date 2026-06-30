# Bounded KV Cache Compression for Local Training Memory Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-kv-cache-compression-for-local-training-memory-reduction-b3ba462380a4`
Run ID: `bounded-kv-cache-compression-for-local-training-memory-reduction-b3ba462380a4-20260608T090055265583+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/19c7a26103ad

## What looked useful

The mechanism is viable but narrow KV-only compression is too small a share of total full-attention training memory to justify a paper from this evidence. The result is useful as a no-paper bounded signal: optimize or fuse the backward path before expecting material local-training memory reduction.

## Boundaries and scale limits

Tested only synthetic data, 2-4 layer small transformers, sequence lengths 128-1024, PyTorch saved_tensors_hooks, and ordinary unfused attention backward. Not tested on real corpora, GPT-2-small-class or larger models, FlashAttention/custom fused kernels, activation checkpointing combinations, or long-run convergence.

## Claim scope

On a small GPT-style BF16 causal transformer trained on synthetic next-token batches on GB10, int8 compression of KV-shaped saved tensors reduced the packed KV payload to about 52% and reduced end-to-end CUDA peak allocation by only about 1.6-2.1%, with one-step global gradient relative L2 error around 0.001 and no short-run loss delta at BF16 reporting precision.

## Why it stopped

Proxy/local experiment produced a useful but non-paper result: KV-shaped payload compression worked, but actual CUDA peak memory fell only about 1.6-2.1% in the tested setup.

## Recommended next action

Run a bounded fused/FlashAttention-compatible compressed-backward test and require at least 10-15% end-to-end peak memory reduction at matched loss before considering paper development.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused KV Saved-Activation Compression for Attention Backward
- Success threshold: At least 10-15% lower end-to-end CUDA peak allocation at sequence length 1024 or higher, less than 10% throughput overhead, and validation loss within 1% of baseline over a bounded GPT-2-small-class run.
- Stop condition: Stop as negative if the fused path saves less than 10% peak memory, exceeds 10% throughput overhead at matched memory, or shows persistent validation-loss degradation above 1%.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-kv-cache-compression-for-local-training-memory-reduction-b3ba462380a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
