# Anchor-Delta KV Compression for Long-Context on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-delta-kv-compression-for-long-context-on-gb10-de93d0c1a77c`
Run ID: `anchor-delta-kv-compression-for-long-context-on-gb10-de93d0c1a77c-20260610T104401931340+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b3efcd0e635c

## What looked useful

At T=32768 and rho=0.995, 4-bit anchor-delta block-16 reduced attention-output relative RMSE from 0.01105 for direct 4-bit to 0.00266 at 3.05x fp16 memory compression; at rho=0.8 it worsened error from 0.06492 to 0.07533. Block-64 gives better memory compression (3.56x) but higher error. 8-bit anchor-delta was accurate but slightly less memory-efficient and not meaningfully better than direct 8-bit overall. All prototype compressed paths added about 250-378% overhead versus fp16 attention, so practical viability requires fused/incremental decode kernels.

## Boundaries and scale limits

Synthetic traces only; no real pretrained LLM KV cache, perplexity, generation quality, paged-attention integration, fused kernel, or 7B+ serving benchmark was tested. Timing is a PyTorch prototype decompression+attention path, not an optimized kernel implementation.

## Claim scope

On GPU-resident synthetic long-context KV traces up to T=32768, H=8, D=64, Q=64, anchor-delta low-bit compression improves attention-output error over direct 4-bit quantization only when KV traces are temporally smooth and anchor blocks are short; it is not a general replacement for direct quantization and this prototype is slower than fp16 attention because reconstruction is unfused.

## Why it stopped

Closed as no-paper useful signal: the bounded synthetic evidence supports a narrow mechanism but also shows clear failure modes and unoptimized decode overhead; it is not direct/full LLM validation.

## Recommended next action

Run a bounded real-model follow-up that captures KV caches from a GPT-2-small-class or similarly small pretrained decoder over 2k-8k tokens, measures actual KV temporal smoothness by layer/head, and applies only the promising block-16/block-64 anchor-delta settings against direct 4-bit/8-bit baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model KV Smoothness Gate for Anchor-Delta Compression
- Success threshold: For at least one nontrivial set of layers/heads, anchor-delta 4-bit must reduce attention-output or logit relative error by at least 2x versus direct 4-bit while keeping fp16 KV compression >=3.0x and not exceeding direct quantization overhead by more than 50% in the prototype timing.
- Stop condition: Stop if real KV smoothness is below the synthetic rho=0.95 equivalent for most layers/heads or if anchor-delta fails to beat direct 4-bit by at least 25% error on real traces.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-delta-kv-compression-for-long-context-on-gb10-de93d0c1a77c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
