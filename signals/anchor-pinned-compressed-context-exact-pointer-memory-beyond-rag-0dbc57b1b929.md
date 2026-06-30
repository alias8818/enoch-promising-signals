# Anchor-Pinned Compressed Context: Exact-Pointer Memory Beyond RAG

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-pinned-compressed-context-exact-pointer-memory-beyond-rag-0dbc57b1b929`
Run ID: `anchor-pinned-compressed-context-exact-pointer-memory-beyond-rag-0dbc57b1b929-20260630T002705157983+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/889938e71ba1

## What looked useful

At 50k records, compressed-summary BM25 answered 0/5,000 exact payload queries because the payload was absent; anchor-pointer exact lookup answered 5,000/5,000; raw BM25 over uncompressed records answered 4,998/5,000. Compressed summaries plus pointer table used 7.2 MB versus 25.7 MB raw text bytes.

## Boundaries and scale limits

Tested with deterministic synthetic data up to 50,000 records and 5,000 exact-anchor queries on one CPU process. Did not test real LLM summarization, embedding RAG, long-context models, natural queries, noisy anchors beyond a simple corrupted-anchor control, or multi-hop pointer chains.

## Claim scope

Synthetic anchored-record benchmark: when compression preserves exact anchors but omits nonce-like payloads, an exact anchor-to-payload pointer table recovers payloads that retrieval over compressed summaries cannot.

## Why it stopped

Bounded synthetic mechanism evidence is positive but proxy-only; it is insufficient for a paper or broad claim beyond compressed-summary retrieval.

## Recommended next action

Stop this run as no-paper useful signal; next, test the same anchored-memory protocol with an actual LLM compressor and a small model-facing retrieval pipeline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-compressed anchor-pointer memory on naturalistic anchored facts
- Success threshold: On at least 1,000 held-out exact-anchor queries, pointer-augmented compressed memory should improve exact-match recall by at least 30 percentage points over compressed-summary RAG while using less than 40% of raw text bytes.
- Stop condition: Stop if the LLM compressor usually retains payloads in summaries, fails to preserve anchors, or pointer lookup improves recall by less than 10 percentage points over compressed-summary RAG.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-pinned-compressed-context-exact-pointer-memory-beyond-rag-0dbc57b1b929`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
