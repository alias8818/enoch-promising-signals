# Tiered KV Cache for >64k Context on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-kv-cache-for-64k-context-on-gb10-3d13cc35ff60`
Run ID: `tiered-kv-cache-for-64k-context-on-gb10-3d13cc35ff60-20260621T232824590176+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/49b19478d320

## What looked useful

Exact host-tiered KV matched full-GPU attention numerically within float16 error and reduced measured CUDA allocation at 131072 tokens from 813.7 MB to 84.2 MB in the one-layer benchmark, but decode latency was 6.37x slower. At 65536 tokens, pageable host KV was 8.39x slower and pinned host KV remained 5.89x slower, making straightforward exact host/UMA tiering no-paper despite the memory-capacity benefit.

## Boundaries and scale limits

Not full model serving, not multi-layer scheduling, not real traffic, not fused paged attention, not quality evaluation. PyTorch explicit chunk copies may overstate latency versus a custom overlapped kernel, but it directly tests the naive exact tiering mechanism.

## Claim scope

Single-token decode microbenchmark on GB10 for exact single-layer attention with synthetic float16 KV tensors, 8 KV heads, head_dim 128, batch 1, sequence lengths up to 131072, comparing full-GPU KV against host-tiered cold KV plus a 4096-token hot CUDA window.

## Why it stopped

Bounded GB10 microbenchmarks produced a mixed useful signal: memory reduction and exactness were supported, but the naive tiered design was 5.89x to 8.39x slower at 64k, so it is not paper-ready or practically efficient as implemented.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded action is a separate deepen experiment with overlapped pinned transfers and a fused/paged attention kernel targeting less than 2x slowdown at 64k while preserving exactness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Overlapped pinned-transfer paged attention for exact 64k KV tiering on GB10
- Success threshold: At 65536 tokens, exact tiered decode median latency is less than 2x full-GPU latency while reducing resident CUDA KV allocation by at least 4x for the tested one-layer shape.
- Stop condition: Stop if the optimized exact tiered path remains above 3x full-GPU median latency at 65536 tokens after pinned double-buffering and chunk-size tuning, or if correctness diverges beyond float16 tolerance.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-cache-for-64k-context-on-gb10-3d13cc35ff60`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
