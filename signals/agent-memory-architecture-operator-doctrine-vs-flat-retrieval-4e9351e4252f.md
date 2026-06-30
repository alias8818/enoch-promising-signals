# Agent Memory Architecture: Operator Doctrine vs Flat Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-memory-architecture-operator-doctrine-vs-flat-retrieval-4e9351e4252f`
Run ID: `agent-memory-architecture-operator-doctrine-vs-flat-retrieval-4e9351e4252f-20260610T121250884778+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/31c701dfcb0a

## What looked useful

Operator doctrine achieved 1.000 answer accuracy across 38,400 in-schema queries while flat lexical retrieval ranged from 0.111 to 0.127 by distractor density; candidate sets dropped from 320-1280 records to 3.7-15.7 records. A schema-gap probe dropped operator-doctrine accuracy to 0.105, showing the mechanism depends on robust doctrine/parser coverage.

## Boundaries and scale limits

Synthetic memory records only; deterministic schema parser; no dense embedding baseline; no LLM-in-the-loop agent; no real production memory traces; no natural paraphrase coverage beyond the schema-gap probe.

## Claim scope

In a deterministic synthetic agent-memory benchmark with project/fact/date metadata, stale records, authority tiers, revoked records, and lexical distractors, an explicit operator-doctrine filter plus authority/recency ranking substantially improved top-record answer accuracy and reduced candidate set size versus flat lexical retrieval when queries used in-schema fact wording.

## Why it stopped

The result is bounded synthetic evidence with a clear parser-coverage failure mode, not full validation of an agent memory architecture.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should replace the deterministic parser with a semantic or LLM parser and evaluate on human-authored paraphrases plus embedding and metadata-filtered baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Doctrine Retrieval With Semantic Parser and Natural Paraphrase Memory Queries
- Success threshold: On at least 1000 held-out paraphrase queries, semantic doctrine retrieval improves top-record answer accuracy by at least 15 percentage points over the best non-doctrine baseline while keeping parser-induced unrecoverable failures below 10%.
- Stop condition: Stop if parser coverage remains below 90% or if the best non-doctrine metadata/vector hybrid matches doctrine accuracy within 5 percentage points at comparable latency and candidate count.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-architecture-operator-doctrine-vs-flat-retrieval-4e9351e4252f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
