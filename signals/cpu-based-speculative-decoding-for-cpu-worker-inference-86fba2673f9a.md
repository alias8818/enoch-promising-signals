# CPU-based Speculative Decoding for CPU Worker Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-based-speculative-decoding-for-cpu-worker-inference-86fba2673f9a`
Run ID: `cpu-based-speculative-decoding-for-cpu-worker-inference-86fba2673f9a-20260609T101842998682+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/befa06f93b7e

## What looked useful

Speculative decoding helped only in a narrow high-acceptance cheap-draft regime. Best reduced-grid case was 2.03x at one thread with draft_dim 64, gamma 8, and 0.95 acceptance; repeat one-thread high-acceptance cases stayed positive at 1.16-1.53x. Four-thread high-acceptance was near break-even at 0.96-1.05x, while 0.7 acceptance was consistently slower at both one and four threads.

## Boundaries and scale limits

Proxy-only evidence. No trained language model, real draft logits, KV cache, tokenizer, sampling stack, request concurrency, or long serving run was tested. Runs used 64-256 emitted tokens per condition.

## Claim scope

NumPy/OpenBLAS CPU microbenchmark of speculative decoding kernel economics on a CPU worker: synthetic target and draft dense matrices, controlled acceptance probabilities, target_dim 2048, vocab 8192, draft_dim 64-256, gamma 2-8, OpenBLAS threads 1 and 4.

## Why it stopped

No-paper closure: bounded proxy evidence is useful and reproducible but mostly negative outside a narrow high-acceptance regime, and it does not directly validate real CPU worker inference.

## Recommended next action

Run a bounded direct CPU inference follow-up with an actual small language model and real draft model, requiring measured acceptance, end-to-end tokens/s, latency, CPU utilization, and memory before considering deployment or paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU speculative decoding benchmark with real small language models
- Success threshold: Speculative decoding achieves at least 1.2x end-to-end tokens/s improvement with no p95 latency regression above 10% in the high-acceptance prompt class, while low-acceptance cases are correctly identified as non-profitable.
- Stop condition: Stop if measured real-model acceptance is below 0.85 or if speculative throughput is below 1.05x baseline after thread-count and gamma calibration.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-based-speculative-decoding-for-cpu-worker-inference-86fba2673f9a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
