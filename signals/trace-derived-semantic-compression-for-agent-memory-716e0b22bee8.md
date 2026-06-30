# Trace-Derived Semantic Compression for Agent Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-derived-semantic-compression-for-agent-memory-716e0b22bee8`
Run ID: `trace-derived-semantic-compression-for-agent-memory-716e0b22bee8-20260628T053147270662+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/bd7acb8f5843

## What looked useful

Semantic causal memories built from execution traces achieved 1.000 mean accuracy and coverage at a 0.014 memory/raw token ratio, while the strongest raw signal baseline reached 0.550 accuracy at a 0.139 ratio and random/recent raw retention stayed below 0.307 accuracy even at 0.20 ratio.

## Boundaries and scale limits

Proxy-only synthetic traces; no real LLM agent logs, no learned extractor, no embedding/vector retrieval, no multi-session staleness handling, no adversarial ambiguity, and no full-scale serving or model-in-the-loop validation.

## Claim scope

On a deterministic synthetic benchmark where noisy agent traces include stable extractable success/failure event lines, trace-derived semantic aggregation preserved future action-selection accuracy at 1.4% of raw trace tokens and outperformed raw trace retention baselines across 30 seeds.

## Why it stopped

The mechanism is supported only in a schema-bound synthetic proxy, so it is useful for follow-up design but not a direct/full validation of agent memory compression.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded evidence should replace synthetic TRACE_SIGNAL parsing with real or semi-real agent traces and an extractor baseline under the same memory budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate trace-derived semantic compression on real agent logs with extractor controls
- Success threshold: At least 15 percentage points higher downstream accuracy than the best non-semantic baseline at equal or lower memory token budget, with extractor precision and recall both at or above 0.85 on audited events.
- Stop condition: Stop if semantic extraction precision or recall falls below 0.70 or if downstream accuracy is within 5 percentage points of a cheaper raw/query-aware retrieval baseline across two independent trace sets.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-semantic-compression-for-agent-memory-716e0b22bee8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
