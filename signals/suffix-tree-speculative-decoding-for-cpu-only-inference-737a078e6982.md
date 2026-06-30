# Suffix-Tree Speculative Decoding for CPU-Only Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-for-cpu-only-inference-737a078e6982`
Run ID: `suffix-tree-speculative-decoding-for-cpu-only-inference-737a078e6982-20260620T075802135032+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bf455e7e63d3

## What looked useful

K=4 and K=6 suffix-longest-context drafting cleared the proxy break-even threshold on repeated/template/local text at verify_token_cost=0.65, but failed badly on low-repeat Markov text and became mostly negative when verification cost approached greedy decoding.

## Boundaries and scale limits

No real transformer, tokenizer, KV cache, or CPU serving stack was benchmarked. Corpora were synthetic/local traces. Results do not establish broad CPU-only inference acceleration or publication-grade performance.

## Claim scope

Bounded trace-level evidence: suffix-history speculative decoding can produce enough exact accepted draft tokens on repetitive/template token streams to beat a conservative proxy cost model when target verification is materially cheaper than greedy decoding.

## Why it stopped

Trace-only proxy evidence is useful for mechanism triage but insufficient for a paper or an end-to-end CPU inference claim.

## Recommended next action

Run one bounded direct CPU serving benchmark with a small local model and real tokenizer/KV path, comparing greedy decoding against suffix-history drafting on repeated and low-repeat prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU model benchmark for suffix-history speculative decoding
- Success threshold: At least 1.10x tokens/sec over greedy on repetitive prompts and no worse than 0.95x on low-repeat prompts in a bounded CPU-only benchmark.
- Stop condition: Stop if verifier cost is within 10% of greedy per token and K=4 acceptance is below 2 accepted tokens per speculative step on repetitive prompts.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-for-cpu-only-inference-737a078e6982`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
