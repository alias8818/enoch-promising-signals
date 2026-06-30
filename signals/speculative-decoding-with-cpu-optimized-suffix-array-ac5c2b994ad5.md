# Speculative Decoding with CPU-Optimized Suffix Array

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-cpu-optimized-suffix-array-ac5c2b994ad5`
Run ID: `speculative-decoding-with-cpu-optimized-suffix-array-ac5c2b994ad5-20260529T072443740203+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/78abe1b60d0e

## What looked useful

The suffix-array mechanism is correct for exact-copy reuse, but ordinary held-out prose has too little exact continuation reuse to support useful speculative drafts; a hash n-gram baseline matches acceptance while being roughly 68-72x faster per query in this benchmark.

## Boundaries and scale limits

Proxy benchmark only: no neural target model, no production tokenizer, one small public-domain-style prose corpus, single-process Python implementation, and no end-to-end speculative decoding latency measurement.

## Claim scope

On Tiny Shakespeare exact regex token splits, CPU suffix-array drafting can recover perfect drafts for exact repeated spans but provides only about 0.18-0.20 accepted tokens per query on real next-split held-out prose and does not improve acceptance over a simpler hash n-gram baseline.

## Why it stopped

Proxy early falsification: real-holdout exact-token acceptance was negligible and suffix-array lookup did not beat a simpler hash n-gram control, though exact-repeat positive controls validated the mechanism.

## Recommended next action

Stop this run as a proxy early falsification for general prose; only deepen on copy-heavy code/RAG/prompt-cache workloads with a real tokenizer and target-model acceptance loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Suffix-array drafting on copy-heavy code or RAG workloads with real tokenizer acceptance
- Success threshold: At least 1.0 accepted target-model tokens per query and at least 10% end-to-end latency reduction over the stronger hash n-gram or prompt-lookup baseline on the same workload.
- Stop condition: Stop if accepted tokens per query remain below 0.5 or end-to-end latency fails to beat the hash n-gram baseline on the bounded copy-heavy workload.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-cpu-optimized-suffix-array-ac5c2b994ad5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
