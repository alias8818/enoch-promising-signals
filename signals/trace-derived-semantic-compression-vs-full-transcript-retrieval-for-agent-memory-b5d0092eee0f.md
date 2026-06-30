# Trace-Derived Semantic Compression vs Full-Transcript Retrieval for Agent Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-derived-semantic-compression-vs-full-transcript-retrieval-for-agent-memory-b5d0092eee0f`
Run ID: `trace-derived-semantic-compression-vs-full-transcript-retrieval-for-agent-memory-b5d0092eee0f-20260621T232822240696+0000`

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

- Provider-backed Research Facility batch: z-ai/glm-5.2: enoch://research-facility/provider/z-ai/glm-5.2/25a0052b910a

## What looked useful

Across 2,000 deterministic synthetic tasks and five seeds, semantic compression answered 2000/2000 correctly while transcript search answered 127/2000 correctly under an 8-line budget; semantic facts reduced the token proxy by 99.7233%.

## Boundaries and scale limits

Proxy-only synthetic workload; no real agent transcript corpus, non-oracle fact extractor, embedding/BM25 retriever, LLM answerer, or long-horizon production trace replay was tested.

## Claim scope

Synthetic trace-derived committed facts outperformed budget-limited lexical transcript retrieval on repeated-agent memory questions with stale distractor snippets.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only, not a full validation of agent memory on real transcripts.

## Recommended next action

Run a bounded direct replay on real repeated-agent traces with a non-oracle trace-to-fact extractor and matched BM25 or embedding transcript retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace bounded replay of semantic fact memory versus transcript retrieval
- Success threshold: Semantic fact memory improves answer accuracy by at least 10 percentage points over the strongest transcript retrieval baseline while reducing retrieved token budget by at least 50%.
- Stop condition: Stop if semantic memory fails to beat the strongest transcript retrieval baseline by 5 percentage points on at least 200 labeled real-trace questions or if durable labels cannot be constructed.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-semantic-compression-vs-full-transcript-retrieval-for-agent-memory-b5d0092eee0f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
