# Retrieval Provenance Ledger for Small RAG Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `retrieval-provenance-ledger-for-small-rag-agents-c5ac4525dbf6`
Run ID: `retrieval-provenance-ledger-for-small-rag-agents-c5ac4525dbf6-20260608T030805254623+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/644b992a27af

## What looked useful

The ledger mechanism is useful against stale lexical cache failures, but the benchmark also shows recency metadata alone can explain the measured gain in this setup.

## Boundaries and scale limits

Synthetic structured facts only; no real embeddings, LLM generation, noisy parsing, adversarial metadata, production retrieval stack, or real user feedback. Full run was CPU-only and single-process.

## Claim scope

In a deterministic synthetic stale-cache RAG benchmark with 1,200 queries and 6,000 structured documents, a source/date/claim provenance ledger eliminated stale document selections and improved answer accuracy over plain lexical overlap, but did not outperform a simple recency reranker.

## Why it stopped

Moderate synthetic evidence supports the mechanism against plain overlap, but the tested ledger ties a simpler recency reranker, so this is not publication-grade evidence for a distinct ledger advantage.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up on a realistic small-agent RAG harness with noisy claim extraction and a recency-only baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic Small-Agent Provenance Ledger Versus Recency Reranking
- Success threshold: Ledger improves answer or citation correctness by at least 5 percentage points over recency-only reranking with a paired 95% confidence interval excluding zero, while adding less than 10% median per-query latency.
- Stop condition: Stop if the ledger ties or loses to recency-only reranking on two independent realistic splits, or if noisy claim extraction prevents reliable ledger updates without manual labels.

## Evidence references

- Artifact root: `<local-path>/projects/retrieval-provenance-ledger-for-small-rag-agents-c5ac4525dbf6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
