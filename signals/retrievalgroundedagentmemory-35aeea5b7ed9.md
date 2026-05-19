# RetrievalGroundedAgentMemory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `retrievalgroundedagentmemory-35aeea5b7ed9`
Run ID: `retrievalgroundedagentmemory-35aeea5b7ed9-20260519T120659967060+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fce03dab0611

## What looked useful

Retrieval alone was insufficient under update conflicts: at 5000 events naive BM25 top-1 reached 0.2036 accuracy with 0.7726 stale-error rate, while top-16 retrieval plus latest entity-slot grounding reached 1.0000 accuracy and 0.0000 stale-error rate. Recency-only fell to 0.0210 accuracy due to misses.

## Boundaries and scale limits

Tested only synthetic structured facts up to 5000 events, 10 seeds, 500 queries per seed. No LLM agent, natural conversation traces, learned embeddings, approximate vector database, multi-session persistence, or human evaluation was tested.

## Claim scope

On deterministic synthetic long-horizon memory streams with repeated entity-slot updates and distractors, BM25 retrieval over a top-k candidate set plus latest entity-slot grounding greatly improves current-fact QA accuracy over recency-only memory and naive BM25 top-1 retrieval.

## Why it stopped

No-paper closure: this run produced a synthetic/proxy mechanism signal, not full validation of retrieval-grounded agent memory in real LLM agents.

## Recommended next action

Run a bounded direct follow-up using paraphrased natural-language traces, dense retrieval, and a small local instruction model required to cite retrieved evidence before answering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paraphrased LLM-Agent Memory Grounding Benchmark
- Success threshold: Grounded retrieval improves answer accuracy by at least 20 percentage points over the best baseline and reduces stale-error rate by at least 50% at a retrieval top-k no larger than 16.
- Stop condition: Stop if grounded retrieval fails to beat the best baseline by 10 percentage points on answer accuracy or if stale-error reduction is below 25% after the predefined trace set.

## Evidence references

- Artifact root: `<local-path>/projects/retrievalgroundedagentmemory-35aeea5b7ed9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
