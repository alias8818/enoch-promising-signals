# Entropy-based KV eviction for long-context CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-based-kv-eviction-for-long-context-cpu-inference-6c6c0e628dc5`
Run ID: `entropy-based-kv-eviction-for-long-context-cpu-inference-6c6c0e628dc5-20260525T161950965178+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a571a18fae2a

## What looked useful

Entropy alone failed important cases, especially sink/local retention. Entropy-weighted scoring matched mass-based retention closely but produced zero error wins across 12 scenario-budget cases, while mass and max-attention remained better controls. Future work should only test entropy as part of a hybrid with attention mass and recency safeguards.

## Boundaries and scale limits

No real LM perplexity, token accuracy, CPU decode latency, allocator behavior, multi-head/layer interactions, or production serving trace was measured. T=2048, D=64 synthetic single-head attention with 8 trials per scenario.

## Claim scope

Bounded synthetic KV-cache proxy: entropy-only eviction is not reliable across needle, sink, topic-reuse, and local attention patterns; mass/max-attention baselines and recency controls are stronger or necessary. Entropy-weighted scoring is competitive but did not beat mass-only or max-attention controls.

## Why it stopped

Proxy evidence is useful but no-paper: entropy-only was falsified in controlled attention workloads, and entropy-weighted did not outperform simpler attention-statistic baselines.

## Recommended next action

Run a bounded real-LM deepen test on a small CPU-friendly transformer, comparing mass-only, max-attention, recency/sink+recent, and entropy+mass+recency hybrid policies on perplexity and decode latency under equal KV budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM CPU KV eviction test for entropy-mass-recency hybrids
- Success threshold: Hybrid entropy+mass+recency reduces perplexity/NLL degradation by at least 10% versus the best non-oracle baseline at the same KV budget while preserving or improving CPU decode throughput and memory use.
- Stop condition: Stop if the hybrid fails to beat mass-only or sink+recent on both quality and latency/memory at two KV budgets, or if implementation overhead eliminates CPU throughput gains.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-based-kv-eviction-for-long-context-cpu-inference-6c6c0e628dc5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
