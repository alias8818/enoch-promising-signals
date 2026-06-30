# Falsifiable Memory Ledger for Long-Context CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `falsifiable-memory-ledger-for-long-context-cpu-agents-7b7d543c25bf`
Run ID: `falsifiable-memory-ledger-for-long-context-cpu-agents-7b7d543c25bf-20260528T001723246961+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/eb1767320215

## What looked useful

Across 20 seeds with 12,000 events each, the ledger achieved 1.000 mean accuracy, citation recall, and conflict-link recall. Rolling summaries at capacities 256/512/1024/2048 reached 0.090/0.178/0.350/0.666 mean accuracy and 0.098/0.197/0.383/0.717 conflict-link recall with stale_prob=0.12. With stale_prob=0 and capacity 4096, rolling summary matched the ledger, narrowing the claim to bounded or lossy compression regimes.

## Boundaries and scale limits

No LLM, no real agent loop, no natural-language retrieval, no production trace data, and no storage/latency penalty beyond a single-process Python proxy. The ledger baseline is unbounded while rolling-summary baselines are bounded; an unlimited perfect rolling memory matched the ledger in the no-stale ablation.

## Claim scope

In a deterministic synthetic long-event memory proxy with entity-attribute updates and explicit contradiction links, an append-only falsifiable ledger preserved current answers, exact evidence citations, and contradiction links under bounded/lossy memory conditions where rolling summaries lost or staled facts.

## Why it stopped

Proxy-only useful signal; not a full validation of long-context CPU agents or a paper-ready result.

## Recommended next action

Run a bounded direct agent-trace follow-up: insert the ledger into a small CPU agent harness, compare against LLM-generated rolling summaries on semi-real tool traces, and measure evidence-cited answer accuracy plus latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Agent-Trace Validation of Falsifiable Memory Ledger
- Success threshold: Ledger improves evidence-cited current-state accuracy by >=30 percentage points and contradiction-link recall by >=25 percentage points versus the LLM-summary baseline, with p50 answer latency <=2x baseline and no increase in stale/wrong answer rate.
- Stop condition: Stop if the ledger improvement is <10 percentage points on evidence-cited accuracy, if latency exceeds 3x baseline after straightforward indexing, or if trace construction cannot provide hidden ground truth without human/private evidence.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-memory-ledger-for-long-context-cpu-agents-7b7d543c25bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
