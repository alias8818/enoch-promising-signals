# KV Cache Compression via Adaptive Eviction on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-via-adaptive-eviction-on-gb10-e2dcb20d9792`
Run ID: `kv-cache-compression-via-adaptive-eviction-on-gb10-e2dcb20d9792-20260605T190815202372+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5599534680ce

## What looked useful

Adaptive eviction is promising only when older token utility is stable and repeatedly reinforced; a simple sink+recent baseline is strong and beats the adaptive policy in 5 of 10 scenario/budget pairs. Future tests must include sink+recent controls and real model decode metrics.

## Boundaries and scale limits

No real LLM perplexity, task accuracy, production decode kernel, or long-context serving benchmark was run. The evidence is synthetic/proxy and should not be treated as full validation of KV cache compression in deployed LLM inference.

## Claim scope

On controlled synthetic GPU attention traces at seq_len 768, heads 8, dim 64, a sink-aware adaptive EMA eviction policy improves full-attention output approximation for stable sink-heavy traces and one medium-budget periodic retrieval trace, but does not robustly beat a sink+recent baseline across recency, phase-shift, diffuse, and low-budget retrieval traces.

## Why it stopped

No-paper closure: bounded synthetic evidence is mixed and proxy-only; it supports a mechanism in narrow conditions but does not justify a paper or broad deployment claim.

## Recommended next action

Run a bounded real-model follow-up using GPT-2-small-class or small Llama-class decode traces, comparing adaptive sink EMA against sink+recent and sliding-window baselines on perplexity/task accuracy and tokens/sec at matched KV budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV eviction comparison against sink+recent baseline
- Success threshold: Adaptive sink EMA must beat sink+recent by at least 5% relative reduction in perplexity increase or task accuracy loss at one budget without reducing decode throughput by more than 10%.
- Stop condition: Stop if adaptive sink EMA fails to beat sink+recent on two real-model long-context tasks or incurs more than 10% throughput loss after basic implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-via-adaptive-eviction-on-gb10-e2dcb20d9792`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
