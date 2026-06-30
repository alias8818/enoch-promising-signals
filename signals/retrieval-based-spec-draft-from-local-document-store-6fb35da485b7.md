# Retrieval-Based Spec Draft from Local Document Store

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `retrieval-based-spec-draft-from-local-document-store-6fb35da485b7`
Run ID: `retrieval-based-spec-draft-from-local-document-store-6fb35da485b7-20260621T100602031200+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4ee2f99f8a58

## What looked useful

BM25 and hybrid retrieval reached 0.7905 mean coverage with 1.0 citation validity, 0 unsupported requirements, and 0 distractor contamination. Random retrieval averaged 0.2281 coverage over 30 seeds and introduced 0.7000 mean distractor contamination.

## Boundaries and scale limits

Synthetic corpus, extractive drafter, token-overlap evaluator, 5 tasks, no real enterprise document stores, no human ratings, no LLM-only or production RAG comparison.

## Claim scope

In a deterministic synthetic local document store with 12 documents and 5 spec tasks, retrieval-backed extractive drafting improved required-fact coverage over no-retrieval and random-retrieval controls while preserving citation validity.

## Why it stopped

Proxy mechanism supported, but evidence is synthetic/extractive and not sufficient for a paper or production-grade validation.

## Recommended next action

Run a bounded deepen follow-up using real local documents, LLM-generated citation-constrained drafts, and blinded rubric or human evaluation against authored specs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Evaluation of Retrieval-Grounded Spec Drafting
- Success threshold: Retrieval-augmented drafts improve mean requirement coverage by at least 0.15 over LLM-only and random-context controls, keep unsupported requirements below 5 percent, and receive higher blinded usefulness ratings on at least 70 percent of tasks.
- Stop condition: Stop if retrieval-augmented drafts fail to beat LLM-only by 0.10 coverage or if unsupported requirements exceed 10 percent after citation constraints.

## Evidence references

- Artifact root: `<local-path>/projects/retrieval-based-spec-draft-from-local-document-store-6fb35da485b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
