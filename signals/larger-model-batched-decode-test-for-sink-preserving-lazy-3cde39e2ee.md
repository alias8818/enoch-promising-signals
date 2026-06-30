# Larger-model batched decode test for sink-preserving lazy KV compaction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `larger-model-batched-decode-test-for-sink-preserving-lazy-3cde39e2ee`
Run ID: `larger-model-batched-decode-test-for-sink-preserving-lazy-3cde39e2ee-20260610T091723821442+0000`

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

- Parent run decision: Lazy KV-Cache with Dynamic Memory Budget Allocation: enoch://control-plane/projects/lazy-kv-cache-with-dynamic-memory-budget-allocation-cea80f6b5c46/runs/lazy-kv-cache-with-dynamic-memory-budget-allocation-cea80f6b5c46-20260610T003601833102+0000
- Parent run decision: Real Decode Evaluation of Lazy KV Budget Policies: enoch://control-plane/projects/real-decode-evaluation-of-lazy-kv-budget-policies-524f0b50f8/runs/real-decode-evaluation-of-lazy-kv-budget-policies-524f0b50f8-20260610T051937188062+0000

## What looked useful

Lazy compaction amortized physical cache movement from 128 eager compactions to 4 compactions per 128-token continuation and improved throughput by 12.6% at batch 1, 28.7% at batch 4, and 46.9% at batch 8 while reducing average cache positions from 576.5 to 160.5. However, NLL rose from about 2.20-2.24 under full KV to about 5.97-6.02, mean KL versus full was about 3.96-3.98, and top-1 agreement with full was only about 24%-26%. A matched-cache no-sink ablation was worse, so sink preservation helps but is insufficient at this aggressive window.

## Boundaries and scale limits

The run did not test 7B+ models, production paged-attention kernels, RoPE/ALiBi long-context architectures, natural retrieval workloads, or generated-output human/task quality. The conclusion is limited to the tested gpt2-medium decode setup and cache budgets.

## Claim scope

On gpt2-medium fp16 teacher-forced GPU batched decode with 512-token prompts, 128-token continuations, batch sizes 1/4/8, fixed seeds 11/23/37, and a 16 sink plus 128 recent token target cache, lazy sink-preserving KV compaction reduces average cached positions by about 72% and improves throughput versus full KV at larger batches, but it substantially degrades next-token distributions versus full KV.

## Why it stopped

No-paper useful signal: the Tier 2 direct validation found a real throughput/cache benefit and a real sink-token benefit, but the tested lazy sink-preserving policy is too lossy relative to full KV logits to support a paper or deployment claim.

## Recommended next action

Run a bounded gpt2-medium sweep over larger recent windows and lazy intervals, with a predeclared quality threshold such as top-1 agreement at least 0.80 or mean KL at most 0.5 versus full KV, to identify whether there is a usable quality-speed knee before scaling models or kernels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quality-speed knee sweep for sink-preserving lazy KV compaction
- Success threshold: Find at least one lazy sink-preserving setting with average cached positions at least 25% below full KV, throughput at least 10% above full KV at batch 8, and top-1 agreement at least 0.80 or mean KL at most 0.5 versus full KV.
- Stop condition: Stop if no swept setting up to window 512 meets the quality threshold, or if the only passing settings erase the throughput/cache advantage versus full KV.

## Evidence references

- Artifact root: `<local-path>/projects/larger-model-batched-decode-test-for-sink-preserving-lazy-3cde39e2ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
