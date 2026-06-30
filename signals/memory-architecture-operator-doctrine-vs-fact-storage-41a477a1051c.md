# Memory Architecture: Operator Doctrine vs Fact Storage

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-architecture-operator-doctrine-vs-fact-storage-41a477a1051c`
Run ID: `memory-architecture-operator-doctrine-vs-fact-storage-41a477a1051c-20260613T073430512362+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6db3840ff63f

## What looked useful

Across 16 conditions with 600 queries each, split_operator_fact accuracy stayed at 1.000. Unified retrieval ranged from 1.000 with no distractors and top_k >= 16 to 0.000 in all 100- and 300-doctrine-distractor conditions, with failures dominated by missing fact retrieval.

## Boundaries and scale limits

Synthetic records and doctrine only; BM25-style lexical retrieval; deterministic answerer; no LLM, neural retriever, real operator corpus, user traffic, or long-run system integration was tested.

## Claim scope

A deterministic synthetic benchmark showed that a unified lexical text memory can lose relevant fact records when operator-doctrine-like chunks compete for retrieval slots, while a split doctrine-as-policy plus structured fact-store architecture preserved correctness on the tested current-authorized-value task.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic and proxy-based; it supports the retrieval-interference mechanism but does not validate a real memory architecture in an LLM/RAG system.

## Recommended next action

Run a bounded deepen follow-up using a small local LLM or neural retriever on natural-language doctrine/fact snippets, measuring answer accuracy and retrieval recall against the same split policy/fact baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural RAG Doctrine-Fact Interference Probe
- Success threshold: Split or explicitly routed memory improves answer accuracy by at least 10 percentage points over unified neural RAG at matched or lower latency in at least two doctrine-distractor levels, with failures attributable to retrieval-slot competition.
- Stop condition: Stop if unified neural RAG reaches at least 98% answer accuracy and at least 98% fact recall@k across all distractor levels with no material latency or memory penalty, or if local model/runtime dependencies prevent a valid comparison.

## Evidence references

- Artifact root: `<local-path>/projects/memory-architecture-operator-doctrine-vs-fact-storage-41a477a1051c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
