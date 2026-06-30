# Layered Memory vs Flat Retrieval on Repeated Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-vs-flat-retrieval-on-repeated-tasks-d91108853ecd`
Run ID: `layered-memory-vs-flat-retrieval-on-repeated-tasks-d91108853ecd-20260628T200902426572+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a3c7fc187826

## What looked useful

Primary run over 4320 queries: layered memory accuracy 1.000, flat retrieval 0.378, transcript search 0.764. Layered-minus-flat mean accuracy delta was +0.621759 with 95% bootstrap CI [0.607407, 0.636111]. Sensitivity sweep across 0-8 distractors per session preserved a +0.546 to +0.643 layered-minus-flat delta.

## Boundaries and scale limits

No LLM calls, no embedding model, no human-authored task corpus, and no production persistence path were evaluated; the layered strategy has access to generator labels.

## Claim scope

In a deterministic synthetic repeated-session replay benchmark with structured stable/task/stale labels, layered memory avoided stale and noisy facts better than flat retrieval.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic retrieval-policy evidence, not direct LLM-agent validation.

## Recommended next action

Run a bounded direct replay with an actual LLM agent and embedding retriever on the same stale/noisy repeated-task cases before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM-agent replay of stale/noisy repeated-task memory policies
- Success threshold: Layered memory improves exact-answer accuracy by at least 15 percentage points over flat retrieval with no more than 5 percentage points latency overhead on the bounded replay.
- Stop condition: Stop if the layered advantage falls below 5 percentage points or if failures are dominated by generation errors unrelated to memory retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-vs-flat-retrieval-on-repeated-tasks-d91108853ecd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
