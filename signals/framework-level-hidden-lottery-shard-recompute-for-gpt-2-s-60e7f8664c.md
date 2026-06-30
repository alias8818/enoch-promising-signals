# Framework-level hidden lottery shard recompute for GPT-2-small-class training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `framework-level-hidden-lottery-shard-recompute-for-gpt-2-s-60e7f8664c`
Run ID: `framework-level-hidden-lottery-shard-recompute-for-gpt-2-s-60e7f8664c-20260520T090452729835+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Audited Gradient Lottery With Shard Recompute Challenges: enoch://control-plane/projects/audited-gradient-lottery-with-shard-recompute-challenges-78cd4366a7/runs/audited-gradient-lottery-with-shard-recompute-challenges-78cd4366a7-20260520T085008349351+0000
- Parent run decision: Neural training-loop audit lottery with deterministic shard recompute: enoch://control-plane/projects/neural-training-loop-audit-lottery-with-deterministic-shar-62cfb6401e/runs/neural-training-loop-audit-lottery-with-deterministic-shar-62cfb6401e-20260520T085536567531+0000

## What looked useful

Shard recompute matched dense validation loss in the bounded main run and reduced peak CUDA allocation by 21.1% in the activation-stress setting, but main-setting memory savings were only 1.3%, throughput was only 31.1% of dense, and a frozen random-route control matched the learned router. The practical framework-level implementation is not viable as tested, while the activation-memory lever may justify a fused-kernel follow-up.

## Boundaries and scale limits

The run used byte-level vocabulary, 500-step training horizons for the main comparison, one activation-stress seed, and a PyTorch framework-level shard loop rather than a fused sparse FFN kernel. It did not test canonical GPT-2 BPE embeddings, billions-token pretraining, long-context robustness, or distributed/datacenter training.

## Claim scope

On a GPT-2-small-block-shape byte-level WebText LM with 12 layers, width 768, 12 heads, bf16 CUDA training, and two fixed 500-step seeds, framework-level top-4-of-8 FFN shard recompute preserved short-horizon validation loss but did not meet practical throughput or main-setting memory targets. A larger batch/sequence stress check showed an activation-memory lever but still severe throughput loss.

## Why it stopped

The direct bounded test missed the practical success threshold: learned shard recompute had 1.3% main-setting memory savings versus the 15% target and 31.1% dense throughput versus the 80% target, while the random-route control matched learned routing. This is not a full-scale negative for all possible fused implementations, but it falsifies the framework-level PyTorch shard-recompute claim as tested.

## Recommended next action

Stop this framework-level implementation as no-paper evidence; only pursue a bounded deepen follow-up if replacing the Python shard loop with a fused or vectorized grouped-matmul implementation that can test the same memory target without the current throughput collapse.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused grouped-matmul hidden lottery shard recompute for GPT-2-small blocks
- Success threshold: At batch 8, sequence 512 or a stronger activation-stressed GPT-2-small-block setting, fused shard recompute must preserve validation loss within 3% of dense, reduce peak CUDA allocation by at least 15%, and reach at least 80% of dense throughput; learned routing should outperform random routing by at least 0.5% relative validation loss.
- Stop condition: Stop if the fused/vectorized implementation remains below 70% dense throughput after basic profiling and batching fixes, or if learned routing again fails to beat random routing under matched memory and active-shard budgets.

## Evidence references

- Artifact root: `<local-path>/projects/framework-level-hidden-lottery-shard-recompute-for-gpt-2-s-60e7f8664c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
