# Anchor-Gated KV Eviction for CPU Long-Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-gated-kv-eviction-for-cpu-long-context-db26a473560f`
Run ID: `anchor-gated-kv-eviction-for-cpu-long-context-db26a473560f-20260602T142053596487+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a991488e6086

## What looked useful

Anchor-gated reserve improves anchor-linked fact retention by 2.1-11.7 percentage points in the 70% anchor-linked sweep, but it reduces distractor retention by 5.0-30.0 percentage points and keeps total retrieval accuracy flat or slightly worse with about 13-24% Python runtime overhead.

## Boundaries and scale limits

No real LLM KV tensors, no transformer attention computation, no perplexity or QA benchmark, no comparison to H2O/SinkKV beyond recency-only, and no production CPU serving telemetry.

## Claim scope

Deterministic synthetic CPU cache-retention simulation with 200k-token traces, 20k facts, 1,024-entry KV budget, paired seeds, reserve sweep, and anchor-prevalence sensitivity.

## Why it stopped

Bounded synthetic evidence supports the anchor-retention mechanism but not a broad quality or CPU-efficiency win; this is proxy evidence, not full validation.

## Recommended next action

Stop this run as no-paper useful signal; only pursue a bounded direct LLM follow-up if the target workload values anchor-prioritized recall enough to tolerate or mitigate non-anchor degradation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM KV-cache anchor-gating on long-context retrieval
- Success threshold: Anchor-target accuracy improves by at least 5 percentage points while total task accuracy drops by no more than 1 percentage point and CPU latency overhead stays below 15% versus the best baseline at equal KV budget.
- Stop condition: Stop if direct LLM tests reproduce non-anchor degradation above 3 percentage points, fail to beat recency on anchor-target accuracy by 3 percentage points, or exceed 25% CPU latency overhead.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-kv-eviction-for-cpu-long-context-db26a473560f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
