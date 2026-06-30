# Real CPU transformer anchor-aware KV eviction test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-cpu-transformer-anchor-aware-kv-eviction-test-e464bd9546`
Run ID: `real-cpu-transformer-anchor-aware-kv-eviction-test-e464bd9546-20260629T050112413780+0000`

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

- Parent run decision: CPU inference integration test for anchor-aware KV eviction: enoch://control-plane/projects/cpu-inference-integration-test-for-anchor-aware-kv-evictio-2a96ab7139/runs/cpu-inference-integration-test-for-anchor-aware-kv-evictio-2a96ab7139-20260629T035012180393+0000
- Parent run decision: Anchor-Aware KV Eviction for CPU Long-Context Inference: enoch://control-plane/projects/anchor-aware-kv-eviction-for-cpu-long-context-inference-23c31c04429b/runs/anchor-aware-kv-eviction-for-cpu-long-context-inference-23c31c04429b-20260629T032951997781+0000

## What looked useful

Primary corrected run: anchor-aware accuracy 0.785 vs FIFO 0.042 and false-anchor control 0.042 at budget 96. Budget sweep showed anchor-aware accuracy 0.507, 0.672, 0.946, 0.932, and 0.795 for budgets 24, 32, 48, 64, and 96, while FIFO stayed near 0.04.

## Boundaries and scale limits

Synthetic single-process CPU probe only; no trained transformer, natural-language task, tokenizer effects, multi-layer KV interactions, serving throughput, or imperfect learned anchor detection was tested.

## Claim scope

In a deterministic NumPy CPU scaled-dot-product attention probe with synthetic anchored facts, anchor-aware KV eviction preserved fact retrieval substantially better than FIFO, random, score-only eviction without pre-query access, and random false-anchor controls across tested cache budgets.

## Why it stopped

No-paper closure: the run produced a useful synthetic mechanism signal, but it is not direct trained-model or production-serving evidence.

## Recommended next action

Run one bounded direct-evidence follow-up using a CPU-runnable trained small transformer or inference stack with KV eviction hooks on a natural-language long-context retrieval task, including false-anchor and FIFO controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU small-transformer anchor-aware KV eviction on natural-language retrieval
- Success threshold: Anchor-aware policy improves retrieval accuracy by at least 10 absolute percentage points over FIFO/LRU and false-anchor controls at two or more KV budgets, while adding less than 20 percent CPU wall-clock overhead in the tested setup.
- Stop condition: Stop if anchor-aware improves less than 5 absolute percentage points over controls at all tested budgets, or if CPU overhead exceeds 50 percent before accuracy gains are demonstrated.

## Evidence references

- Artifact root: `<local-path>/projects/real-cpu-transformer-anchor-aware-kv-eviction-test-e464bd9546`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
