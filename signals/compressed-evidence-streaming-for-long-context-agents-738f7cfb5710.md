# Compressed Evidence Streaming for Long-Context Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-evidence-streaming-for-long-context-agents-738f7cfb5710`
Run ID: `compressed-evidence-streaming-for-long-context-agents-738f7cfb5710-20260526T045121568327+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7cc8b96039e4

## What looked useful

Compressed evidence storage can make the query-relevant context nearly constant-size in a synthetic long-stream task, but a strict online policy that discards currently unreachable facts fails on about half of random-order streams.

## Boundaries and scale limits

Synthetic templates only; oracle extraction; no real LLM agent answering; no public natural-language corpus; simple baselines rather than tuned production retrievers or graph-RAG systems.

## Claim scope

In controlled synthetic two-hop evidence streams, a compressed fact-store context packer with oracle extraction preserves both answer-supporting facts at 32-512 token context budgets far better than simple raw FIFO, recency, lexical top-k, and one-step expanded retrieval baselines.

## Why it stopped

Evidence is synthetic mechanism evidence only, not direct validation of compressed evidence streaming for real long-context agents.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replace oracle extraction with a real extractor or small LLM summarizer on a public multi-hop QA corpus and compare fixed-budget answer accuracy against tuned retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Extractor CES on Public Multi-Hop QA
- Success threshold: At least 10 percentage-point absolute improvement in citation-supported answer accuracy over the best tuned retrieval baseline at <=25% of the raw context budget, across at least 500 examples.
- Stop condition: Stop if extractor/summarizer errors reduce citation-supported answer accuracy to within 3 percentage points of the best retrieval baseline at all tested budgets.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-evidence-streaming-for-long-context-agents-738f7cfb5710`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
