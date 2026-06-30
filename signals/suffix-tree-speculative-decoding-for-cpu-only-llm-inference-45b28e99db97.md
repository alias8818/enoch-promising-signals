# Suffix-Tree Speculative Decoding for CPU-Only LLM Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-for-cpu-only-llm-inference-45b28e99db97`
Run ID: `suffix-tree-speculative-decoding-for-cpu-only-llm-inference-45b28e99db97-20260528T162313375272+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3daf641213d4

## What looked useful

Suffix-continuation proposals reduce optimistic target verification calls slightly, but acceptance is low: best confirmation result was 1.181x optimistic call-count speedup in-domain with 5.03% draft-token acceptance; cross-domain speedups were 1.082x and 1.054x with 2.60% and 1.71% acceptance. With even a small per-extra-token verification cost, the best configurations fall below baseline.

## Boundaries and scale limits

No real LLM forward pass, no BPE tokenizer, no llama.cpp or PyTorch CPU latency benchmark, and only 5k-token held-out traces with 20k-token training indexes in the confirmation run.

## Claim scope

CPU-only trace-level proxy evaluation of suffix-continuation speculative decoding on small public-domain text corpora using exact held-out continuation acceptance.

## Why it stopped

Proxy early falsification: ordinary-text suffix continuations did not produce enough accepted draft tokens for a credible general CPU-only speculative decoding speedup, and direct/full evidence would need a real CPU LLM benchmark to overturn this.

## Recommended next action

Stop broad-claim pursuit; if continuing, run a bounded direct benchmark only on copy-heavy workloads where suffix reuse is expected to be high.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM Benchmark for Copy-Heavy Suffix Speculation
- Success threshold: At least 1.2x end-to-end tokens/sec improvement over greedy decoding on two copy-heavy workloads, with no regression worse than 5% on ordinary prose and index memory below 10% of model memory.
- Stop condition: Stop if BPE trace acceptance is below 20% on copy-heavy workloads or if direct CPU target verification cost erases the optimistic call-count speedup.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-for-cpu-only-llm-inference-45b28e99db97`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
