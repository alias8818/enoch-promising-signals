# Aggressive KV eviction with retrieval-augmented recomputation on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `aggressive-kv-eviction-with-retrieval-augmented-recomputation-on-cpu-ec78f84278cf`
Run ID: `aggressive-kv-eviction-with-retrieval-augmented-recomputation-on-cpu-ec78f84278cf-20260628T052912111398+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d9ddc8cc00d2

## What looked useful

Recomputation is beneficial when retrieval selects the target evicted chunk, but aggressive lossy chunk retrieval is the bottleneck. Default k=4 retrieval_recompute accuracy was 0.184 versus 0.000 for sliding/retrieval-only and 1.000 for full KV; best tested k=16 ablation reached 0.547.

## Boundaries and scale limits

Synthetic single-query proxy only; no real transformer layers, tokenizer, natural-language benchmark, learned retrieval, serving implementation, or end-to-end decode latency measurement. Best ablation still trails full KV by 45.3 accuracy points.

## Claim scope

In a deterministic CPU NumPy attention/KV proxy, retrieval-augmented exact recomputation recovers some old-prefix facts that sliding-window eviction and compressed retrieval-only miss, while retaining about 86.7% fewer persistent token-equivalents than full KV.

## Why it stopped

Proxy evidence is mixed: recomputation improves over eviction baselines but retrieval recall is too low to support a broad viability claim or paper-ready result.

## Recommended next action

Stop this run as no-paper proxy evidence; next bounded action is to implement the policy in a tiny real transformer inference loop and measure long-context loss/accuracy plus peak KV memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer retrieval-recompute KV eviction test
- Success threshold: Retrieval_recompute recovers at least 80% of full-KV task accuracy while reducing persistent KV memory by at least 50% and staying within 2x full-KV CPU decode latency on the bounded benchmark.
- Stop condition: Stop if retrieval_recompute remains below 50% of full-KV accuracy after using a stronger exact/vector retrieval index, or if CPU decode latency exceeds 5x full KV at less than 50% KV memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/aggressive-kv-eviction-with-retrieval-augmented-recomputation-on-cpu-ec78f84278cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
