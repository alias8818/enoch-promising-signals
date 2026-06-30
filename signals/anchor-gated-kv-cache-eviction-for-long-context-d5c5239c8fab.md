# Anchor-Gated KV Cache Eviction for Long Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-gated-kv-cache-eviction-for-long-context-d5c5239c8fab`
Run ID: `anchor-gated-kv-cache-eviction-for-long-context-d5c5239c8fab-20260529T171148247561+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a781bc0ef3e5

## What looked useful

Anchor-gated eviction won 9/9 compressed-cache cells. Mean accuracy was 0.1667 for anchor-gated, 0.0707 for sliding, 0.0705 for sink-sliding, and 0.1724 for the no-eviction reference; mean anchor loss reduction versus sliding was 3.006 nats.

## Boundaries and scale limits

Synthetic data only; tiny model; explicit oracle/schema anchor protection; no pretrained LLM, natural-language benchmark, learned gate, production serving latency, or robustness to anchor tagging errors.

## Claim scope

In a synthetic anchored associative-recall task with a 318k-parameter toy causal transformer, schema-derived anchor-gated KV retention preserves most of the full-cache recall signal under cache budgets of 32-64 tokens and outperforms sliding and sink-sliding eviction.

## Why it stopped

The result is a bounded toy/proxy mechanism test, not full validation; absolute full-cache accuracy was only about 17%, and no pretrained/natural-language serving evidence was produced.

## Recommended next action

Stop this run as no-paper useful signal; next run should replace the oracle/schema anchor mask with a learned or heuristic anchor detector on a stronger small-model long-context retrieval benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Anchor Detection for KV Eviction on Small Long-Context Retrieval
- Success threshold: Learned/heuristic anchor-gated eviction achieves at least 80% of the oracle anchor-gated accuracy gain over sliding while reducing KV positions by at least 50% versus full cache on held-out contexts.
- Stop condition: Stop if learned/heuristic anchor-gated eviction fails to beat sliding by at least 5 percentage points accuracy or materially increases decode latency at the same cache budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-kv-cache-eviction-for-long-context-d5c5239c8fab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
